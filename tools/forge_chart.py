#!/usr/bin/env python3
"""DJH chart forge: lane flips + density injection for .xmk charts.

Usage:
  forge_chart.py flip <chart.xmk> <out.xmk> <lane-from> <lane-to> <count>
  forge_chart.py inject <base.xmk> <donor.xmk> <out.xmk>
  forge_chart.py info <chart.xmk>

Format (measured): header [ver=2][hash][count][183], header size =
filesize - count*16; events are 16B records, byte0 = ASCII type tag.
B = tap notes (b15 lane: 0/100 standard, 1 hard, 109+ specials).
"""
import struct
import sys


def load(path):
    with open(path, 'rb') as f:
        d = bytearray(f.read())
    n = struct.unpack('>I', d[8:12])[0]
    h = len(d) - n * 16
    assert h > 0, 'bad header math'
    return d, n, h


def events(d, n, h, want=b'B'):
    return [bytes(d[h + i * 16:h + (i + 1) * 16])
            for i in range(n) if d[h + i * 16:h + i * 16 + 1] == want]


def cmd_info(path):
    from collections import Counter
    d, n, h = load(path)
    print('%s: %d bytes, %d events, hdr %d' % (path, len(d), n, h))
    print(Counter(chr(d[h + i * 16]) if 32 <= d[h + i * 16] < 127
                  else d[h + i * 16] for i in range(n)).most_common(10))


def cmd_flip(src, dst, lane_from, lane_to, count):
    d, n, h = load(src)
    done = 0
    for i in range(n):
        o = h + i * 16
        if d[o:o + 1] == b'B' and d[o + 15] == lane_from and done < count:
            d[o + 15] = lane_to
            done += 1
    open(dst, 'wb').write(bytes(d))
    print('flipped %d, events %d' % (done, n))


def cmd_inject(base, donor, dst):
    b, nb, hb = load(base)
    e, ne, he = load(donor)
    bevents = [bytes(b[hb + i * 16:hb + (i + 1) * 16]) for i in range(nb)]
    have = set(r[1:5] for r in bevents if r[:1] == b'B')
    extra = []
    for i in range(ne):
        r = bytes(e[he + i * 16:he + (i + 1) * 16])
        if r[:1] == b'B' and r[1:5] not in have:
            extra.append(r)
    merged = sorted(bevents + extra, key=lambda r: r[1:5])
    out = bytearray(b[:hb])
    for r in merged:
        out += r
    struct.pack_into('>I', out, 8, len(merged))
    open(dst, 'wb').write(bytes(out))
    print('base %d + %d = %d' % (nb, len(extra), len(merged)))


if __name__ == '__main__':
    c = sys.argv[1]
    if c == 'info':
        cmd_info(sys.argv[2])
    elif c == 'flip':
        cmd_flip(sys.argv[2], sys.argv[3], int(sys.argv[4]),
                 int(sys.argv[5]), int(sys.argv[6]))
    elif c == 'inject':
        cmd_inject(sys.argv[2], sys.argv[3], sys.argv[4])
