# AutoDL complete project backup

Backup of `AutoDL_SimpleMemVLA_LIBERO-Recover_20261111.zip` dated 2026-11-11.

The complete original ZIP is stored in [19 split release assets](https://github.com/zch6a/simplememvla-recover-backup/releases/tag/backup-20261111).
It is the whole AutoDL data disk `/root/autodl-tmp` for the SimpleMemVLA × LIBERO-Recover test:
source code (`code/`), experiment results and logs (`results/`, `logs/`), the conda environment (`envs/smv`),
model weights (`ckpt/`), and the LIBERO-Recover scenes (`data/`).

- Original ZIP size: 19,692,844,439 bytes
- Part size: 1 GiB, except the final part
- Original ZIP SHA-256: `60abd5546cee614be73eedfad2dd400b9bef420df8304336d0d888a46fefd354`

## Restore

1. Download all `.partNNN` assets from the release into one directory.
2. Save `restore.py` and `archive-manifest.json` in that directory.
3. Run `python restore.py`.

The script verifies every part, merges the original ZIP, and verifies its SHA-256.
Allow enough disk space for both the downloaded parts and the restored ZIP.
The parts are raw byte segments; concatenate them before opening the ZIP.

Unzipping gives an `autodl-tmp/` folder. The conda environment was installed at `/root/autodl-tmp/envs/smv`;
put it back at that path to use it directly.