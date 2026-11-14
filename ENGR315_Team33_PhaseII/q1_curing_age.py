import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import DATA_PATH, load_data, plot_path


def analyze(data_file=DATA_PATH, output_name="q1_curing_age.png"):
    df = load_data(data_file, ["Age", "Concrete compressive strength"])
    df = df[df["Age"] > 0].copy()
    x = df["Age"].to_numpy(dtype=float)
    y = df["Concrete compressive strength"].to_numpy(dtype=float)
    if len(df) < 3 or np.unique(x).size < 2:
        raise ValueError("Need at least three valid samples at two or more curing ages")

    summary = (
        df.groupby("Age")["Concrete compressive strength"]
        .agg(count="count", mean="mean", std="std")
        .reset_index()
        .sort_values("Age")
    )
    r = np.corrcoef(x, y)[0, 1]
    slope, intercept = np.polyfit(np.log(x), y, 1)
    fitted = intercept + slope * np.log(x)
    ss_res = np.sum((y - fitted) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r_squared = 1 - ss_res / ss_tot

    print("QUESTION 1: How does curing age relate to compressive strength?")
    print(f"Number of concrete samples: {len(df)}")
    print(f"Pearson correlation (age vs. strength): r = {r:.4f}")
    print(f"Logarithmic fitted curve (age > 0): strength (MPa) = {intercept:.4f} + {slope:.4f} ln(age in days)")
    print(f"Coefficient of determination for logarithmic fit: R^2 = {r_squared:.4f}")
    print("\nStrength grouped by curing age:")
    print(f"{'Age (days)':>11} {'Count':>8} {'Mean (MPa)':>12} {'Std (MPa)':>12}")
    for item in summary.itertuples(index=False):
        std = f"{item.std:.2f}" if np.isfinite(item.std) else "N/A"
        print(f"{item.Age:11.0f} {item.count:8d} {item.mean:12.2f} {std:>12}")

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.scatter(x, y, s=17, alpha=0.22, label="Individual samples")
    ax.errorbar(
        summary["Age"], summary["mean"],
        yerr=summary["std"].fillna(0), fmt="o", capsize=3,
        markersize=5, label="Mean +/- 1 SD by age"
    )
    fit_x = np.linspace(max(1, float(np.min(x))), float(np.max(x)), 400)
    ax.plot(fit_x, intercept + slope * np.log(fit_x), linewidth=2,
            label=f"Log fit (R^2 = {r_squared:.3f})")
    ax.set(title="Concrete Strength vs. Curing Age",
           xlabel="Curing Age (days)", ylabel="Compressive Strength (MPa)")
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    destination = plot_path(output_name)
    fig.savefig(destination, dpi=170)
    plt.close(fig)
    print(f"\nPlot saved: plots/{destination.name}")
    print("Interpretation: The raw correlation is descriptive; differences in mix design may confound the age relationship.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(DATA_PATH))
    parser.add_argument("--plot", default="q1_curing_age.png")
    args = parser.parse_args()
    analyze(args.data, args.plot)
