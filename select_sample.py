import shutil
from pathlib import Path

src_path = Path("/Users/vicki/Downloads/44k_reconstructions/")
des_path = Path("./samples/")

model_dir_map = {
    "original_44k": "original_44k",
    "original_22k": "original_22k",
    "baseline": "sinc_44k",
    "generated": "nugan_44k",
    "wav2wav": "wav2wav_44k",
}

# Cheryl samples
cheryl_sel_indices = [str(idx) for idx in [0, 1, 2, 3, 4, 5, 6, 7]]
cheryl_src_path = src_path / "cheryl_recons"
cheryl_des_path = des_path / "cheryl_recons"

for key, val in model_dir_map.items():
    (cheryl_des_path / val).mkdir(parents=True, exist_ok=True)
    for i, idx in enumerate(cheryl_sel_indices):
        fname = f"sample_{idx}.wav"
        shutil.copy(
            cheryl_src_path / key / fname, cheryl_des_path / val / f"sample_{i}.wav"
        )


# daps sample
daps_sel_indices = [
    ("m1", 0),
    ("m2", 1),
    ("m3", 2),
    ("m4", 3),
    ("f1", 4),
    ("f2", 5),
    ("f3", 6),
    ("f4", 7),
]
daps_src_path = src_path / "daps_recons"
daps_des_path = des_path / "daps_recons"

for key, val in model_dir_map.items():
    if key == "wav2wav":
        continue
    (daps_des_path / val).mkdir(parents=True, exist_ok=True)
    for i, (spkr, idx) in enumerate(daps_sel_indices):
        fname = f"daps_{spkr}_script5_{idx}.wav"
        shutil.copy(
            daps_src_path / key / fname, daps_des_path / val / f"sample_{i}.wav"
        )
