from pathlib import Path
import subprocess
import sys
from common import ROOT, RESULT_DIR

SCRIPTS = ["q1_curing_age.py", "q2_water_cement.py", "q3_fly_ash.py"]


def main():
    subprocess.run([sys.executable, str(ROOT / "prepare_data.py")], check=True, cwd=ROOT)
    RESULT_DIR.mkdir(exist_ok=True)
    for script in SCRIPTS:
        result = subprocess.run(
            [sys.executable, str(ROOT / script)], capture_output=True,
            text=True, cwd=ROOT, check=True
        )
        print(result.stdout)
        (RESULT_DIR / (Path(script).stem + "_output.txt")).write_text(result.stdout, encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "update_readme.py")], check=True, cwd=ROOT)
    print("All 3 plots, terminal outputs, and the README results section have been updated.")


if __name__ == "__main__":
    main()
