import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from common import load_data, plot_path


def analyze():
    df = load_data(columns=["Water", "Cement", "Concrete compressive strength"])
    df = df[df["Cement"] > 0].copy()
    df["Water-to-Cement Ratio"] = df["Water"] / df["Cement"]
    x = df["Water-to-Cement Ratio"].to_numpy(dtype=float)
    y = df["Concrete compressive strength"].to_numpy(dtype=float)
    if len(df) < 3 or np.unique(x).size < 2:
        raise ValueError("Need at least three samples with varying water-to-cement ratios")

    result = stats.linregress(x, y)
    print("QUESTION 2: How does water-to-cement ratio relate to compressive strength?")
    print(f"Number of concrete samples with positive cement content: {len(df)}")
    print(f"Mean water-to-cement ratio: {x.mean():.4f} (unitless)")
    print(f"Pearson correlation: r = {result.rvalue:.4f}")
    print(f"Regression line: strength (MPa) = {result.intercept:.4f} + {result.slope:.4f} * water/cement ratio")
    print(f"Coefficient of determination: R^2 = {result.rvalue ** 2:.4f}")
    print(f"Slope: {result.slope:.4f} MPa per 1.0 unit of water/cement ratio")
    print(f"Two-sided slope p-value: {result.pvalue:.3g}")

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.scatter(x, y, s=17, alpha=0.32, label="Individual samples")
    fit_x = np.linspace(x.min(), x.max(), 200)
    ax.plot(fit_x, result.intercept + result.slope * fit_x,
            label=f"Linear fit (R^2 = {result.rvalue ** 2:.3f})", linewidth=2)
    ax.set(title="Concrete Strength vs. Water-to-Cement Ratio",
           xlabel="Water-to-Cement Ratio (unitless)", ylabel="Compressive Strength (MPa)")
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    destination = plot_path("q2_water_cement.png")
    fig.savefig(destination, dpi=170)
    plt.close(fig)
    print(f"\nPlot saved: plots/{destination.name}")
    print("Interpretation: This is a raw association; the cement ratio is not adjusted for supplementary binders or sample age.")


if __name__ == "__main__":
    analyze()
