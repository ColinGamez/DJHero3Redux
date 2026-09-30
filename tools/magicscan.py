"""Stream-scan DJH3 container for embedded file magics."""
MAGICS = [b'FSAR', b'BIKI', b'BIK', b'FSB5', b'FSB4', b'<?xml', b'<DJCon',
          b'#XMB', b'X360', b'.xex']
ISO = r'D:\DJ Hero 1+2+3 Redeux\djhero3_x360_proto.iso'
P0SEC, P0SZ, SEC = 27203, 2097152000, 2048
P1SEC, P1SZ = 1061445, 1711013888
CHUNK = 64 * 1024 * 1024
MaxTail = 64

with open(ISO, 'rb') as f:
    for pname, psec, psz in (('p0', P0SEC, P0SZ), ('p1', P1SEC, P1SZ)):
        base = 0 if pname == 'p0' else P0SZ
        tail = b''
        for pos in range(0, psz, CHUNK):
            f.seek(psec * SEC + pos)
            data = tail + f.read(min(CHUNK, psz - pos))
            for m in MAGICS:
                i = 0
                while True:
                    i = data.find(m, i)
                    if i < 0 or i >= len(data) - MaxTail and pos + len(data) < psz:
                        break
                    # skip tail-edge (may be split); handle by overlap anyway
                    if i > len(data) - MaxTail - 1:
                        break
                    print('%s +%x  %s' % (pname, base + pos + i - len(tail), m))
                    i += 1
            tail = data[-MaxTail:]
print('scan done')
