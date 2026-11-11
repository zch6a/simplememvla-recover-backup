"""Verify the downloaded .partNNN files and merge them back into the original ZIP.

Run in the folder that holds all parts plus archive-manifest.json:
    python restore.py
"""
import hashlib
import json
import os
import sys

CHUNK = 16 * 1024 * 1024


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def main():
    with open("archive-manifest.json", encoding="utf-8") as f:
        manifest = json.load(f)

    bad = []
    for part in manifest["parts"]:
        name = part["name"]
        if not os.path.exists(name):
            bad.append(f"missing: {name}")
        elif os.path.getsize(name) != part["size"]:
            bad.append(f"wrong size: {name}")
        elif sha256_of(name) != part["sha256"]:
            bad.append(f"checksum mismatch: {name}")
        else:
            print(f"ok  {name}")
    if bad:
        print("\n".join(bad))
        sys.exit("Re-download the parts listed above, then run restore.py again.")

    out = manifest["archive"]["name"]
    h = hashlib.sha256()
    with open(out, "wb") as dst:
        for part in manifest["parts"]:
            with open(part["name"], "rb") as src:
                for block in iter(lambda: src.read(CHUNK), b""):
                    dst.write(block)
                    h.update(block)
    if h.hexdigest() != manifest["archive"]["sha256"]:
        sys.exit(f"Merged {out} does not match the original SHA-256.")
    print(f"restored {out} ({os.path.getsize(out):,} bytes), SHA-256 verified")


if __name__ == "__main__":
    main()
