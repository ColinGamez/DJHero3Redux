"""FSG-FILE-SYSTEM extractor (FreeStyleGames container, DJH3 proto).
Usage: fsg_extract.py <part0> <part1> <outdir> [--carve]
Without --carve: parse + stats only."""
import struct, sys, os, binascii

MAGIC = b'FSG-FILE-SYSTEM\x00'

P0SEC, P0SZ = 27203, 2097152000
P1SEC, P1SZ = 1061445, 1711013888
SECTOR = 2048

def view(f, off, size):
    """Read container-relative range (spans part0/part1) straight from ISO."""
    out = bytearray()
    while size > 0:
        if off < P0SZ:
            iso = P0SEC * SECTOR + off
            n = min(size, P0SZ - off)
        else:
            iso = P1SEC * SECTOR + (off - P0SZ)
            n = min(size, P0SZ + P1SZ - off)
        f.seek(iso)
        chunk = f.read(n)
        if not chunk:
            break
        out += chunk
        off += len(chunk)
        size -= len(chunk)
    return bytes(out)

def parse(c0):
    assert c0[:16] == MAGIC, c0[:16]
    hdr = struct.unpack_from('>8I', c0, 20)
    print('header:', [hex(v) for v in hdr])
    count = hdr[4]
    print('record count: %d (0x%x)' % (count, count))
    recs = []
    for i in range(count):
        h, x, o, s = struct.unpack_from('>IIII', c0, 52 + i * 16)
        if h or x or o or s:
            recs.append((h, x, o, s))
    print('nonempty records:', len(recs))
    return recs

def main():
    iso, outdir = sys.argv[1], sys.argv[2]
    with open(iso, 'rb') as f:
        f.seek(P0SEC * SECTOR)
        c0head = f.read(0x44000)
        assert c0head[:16] == MAGIC, c0head[:16]
        hdr = struct.unpack_from('>8I', c0head, 20)
        print('header:', [hex(v) for v in hdr])
        count = hdr[4]
        print('record count: %d (0x%x)' % (count, count))
        recs = []
        for i in range(count):
            h, x, o, s = struct.unpack_from('>IIII', c0head, 52 + i * 16)
            if h or x or o or s:
                recs.append((h, x, o, s))
        print('nonempty records:', len(recs))
        total = sum(s for _, _, _, s in recs)
        print('sum sizes:', total)
        print('sizes: min=%d max=%d' % (min(s for _, _, _, s in recs), max(s for _, _, _, s in recs)))
        bad = [(h, o, s) for h, _, o, s in recs if o + s > P0SZ + P1SZ]
        print('out-of-range:', len(bad))
        for b in bad[:5]:
            print('  %08x off=%x size=%d' % b)
        if '--carve' in sys.argv:
            os.makedirs(outdir, exist_ok=True)
            for i, (h, x, o, s) in enumerate(recs):
                blob = view(f, o, s)
                with open(os.path.join(outdir, '%05d_%08x.bin' % (i, h)), 'wb') as out:
                    out.write(blob)
            print('carved %d files to %s' % (len(recs), outdir))

if __name__ == '__main__':
    main()
