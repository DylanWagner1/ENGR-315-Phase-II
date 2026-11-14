from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "concrete.csv"
PLOT_DIR = ROOT / "plots"
RESULT_DIR = ROOT / "results"


def load_data(path=DATA_PATH, columns=None):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run 'python prepare_data.py' to download the full UCI dataset."
        )
    data = pd.read_csv(path, encoding="utf-8-sig")
    data.columns = data.columns.str.strip()
    required = columns or ["Age", "Concrete compressive strength"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        raise ValueError(f"Dataset missing required columns: {missing}. Found: {list(data.columns)}")
    for col in required:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    original = len(data)
    data = data.dropna(subset=required).copy()
    if len(data) != original:
        print(f"Excluded {original - len(data)} rows with missing/non-numeric values")
    return data


def plot_path(filename):
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    return PLOT_DIR / filename
