"""Minimal XDVDFS (Xbox 360 image) lister/extractor. Temp tool, not part of any repo."""
import struct, sys, os

SECTOR = 2048
MAGIC = b"MICROSOFT*XBOX*MEDIA"

def read_table(f, sector, size):
    f.seek(sector * SECTOR)
    return f.read(size)

def parse_entries(table):
    """BST walk of a directory table. Yields (name, sector, size, is_dir)."""
    out = []
    def walk(off):
        if off == 0 and out and off != 0:
            return
        if off + 14 > len(table):
            return
        left, right, sector, size, attr, nlen = struct.unpack_from("<HHIIBB", table, off)
        name = table[off+14:off+14+nlen]
        try:
            s = name.decode("ascii")
        except UnicodeDecodeError:
            s = None
        if s is not None and not (len(out) == 0 and s == ""):
            # skip the self/root entry only if empty name at table start
            if not (off == 0 and s == ""):
                out.append((s, sector, size, bool(attr & 0x10)))
        elif off == 0:
            pass
        if left:
            walk(left * 4)
        if right:
            walk(right * 4)
    walk(0)
    return out

def list_all(f, sector, size, prefix=""):
    table = read_table(f, sector, size)
    entries = parse_entries(table)
    files = []
    for name, sec, sz, is_dir in entries:
        path = prefix + "/" + name if prefix else name
        if is_dir:
            files += list_all(f, sec, sz, path)
        else:
            files.append((path, sec, sz))
    return files

def main():
    img, cmd = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "list"
    with open(img, "rb") as f:
        f.seek(32 * SECTOR)
        vol = f.read(32)
        assert vol[:20] == MAGIC, f"bad magic: {vol[:20]!r}"
        root_sec, root_sz = struct.unpack_from("<II", vol, 20)
        print(f"root sector={root_sec} size={root_sz}")
        files = list_all(f, root_sec, root_sz)
    print(f"files: {len(files)}")
    total = sum(s for _, _, s in files)
    print(f"total bytes: {total}")
    if cmd == "list":
        for p, sec, sz in sorted(files):
            print(f"  {sz:>10}  {p}")
    elif cmd == "extract":
        dest = sys.argv[3]
        with open(img, "rb") as f:
            for p, sec, sz in files:
                out = os.path.join(dest, p.replace("/", os.sep))
                os.makedirs(os.path.dirname(out) or dest, exist_ok=True)
                f.seek(sec * SECTOR)
                with open(out, "wb") as o:
                    o.write(f.read(sz))
        print(f"extracted to {dest}")

if __name__ == "__main__":
    main()
