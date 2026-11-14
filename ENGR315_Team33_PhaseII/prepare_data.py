from urllib.request import urlopen
from common import DATA_PATH

DATA_URL = "https://raw.githubusercontent.com/HansenHan/ML_UCI_Concrete_Compressive_Strength/main/Concrete_Data.csv"


def main():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH.exists():
        print(f"Dataset already exists: {DATA_PATH}")
        return
    try:
        with urlopen(DATA_URL, timeout=30) as response:
            contents = response.read()
    except Exception as error:
        raise RuntimeError(
            "Dataset download failed. Download the UCI Concrete Compressive Strength dataset "
            "and save a CSV named concrete.csv in the data folder. "
            f"Mirror: {DATA_URL}"
        ) from error
    DATA_PATH.write_bytes(contents)
    print(f"Downloaded concrete dataset to: {DATA_PATH}")


if __name__ == "__main__":
    main()
