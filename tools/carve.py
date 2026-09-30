"""Carve DJH3 container files by magic boundaries."""
import os, re
ISO = r'D:\DJ Hero 1+2+3 Redeux\djhero3_x360_proto.iso'
P0SEC, P0SZ, SEC = 27203, 2097152000, 2048
P1SEC = 1061445
EXT = {'FSAR': 'far', 'FSB4': 'fsb', 'FSB5': 'fsb', 'BIK': 'bik', '<?xml': 'xml'}
OUT = r'D:\DJ Hero 1+2+3 Redeux\DJH3'

hits = []
with open(r'C:\Users\Colin\AppData\Local\Temp\opencode\magics.txt', encoding='utf-16') as f:
    for line in f:
        m = re.match(r"(p\d) \+([0-9a-f]+)\s+b'(.+)'", line.strip())
        if m and m.group(3) in EXT:
            part, off, magic = m.group(1), int(m.group(2), 16), m.group(3)
            base = 0 if part == 'p0' else P0SZ
            hits.append((base + off, magic))
hits.sort()
print('carvable:', len(hits))
os.makedirs(OUT, exist_ok=True)
with open(ISO, 'rb') as f:
    for i, (off, magic) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else P0SZ + 1711013888
        size = end - off
        if size <= 0 or size > 600 * 1024 * 1024:
            print('skip weird', hex(off), magic, size)
            continue
        if off < P0SZ:
            f.seek(P0SEC * SEC + off)
        else:
            f.seek(P1SEC * SEC + (off - P0SZ))
        blob = f.read(size).rstrip(b'\x00')
        fn = '%04d_%s.%s' % (i, magic.replace('?', 'q').replace('<', ''), EXT[magic])
        with open(os.path.join(OUT, fn), 'wb') as o:
            o.write(blob)
print('done')
