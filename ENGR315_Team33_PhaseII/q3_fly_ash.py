import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from common import load_data, plot_path


def analyze():
    df = load_data(columns=["Fly Ash", "Age", "Concrete compressive strength"])
    df = df[df["Age"] == 28].copy()
    without = df.loc[df["Fly Ash"] == 0, "Concrete compressive strength"].to_numpy(dtype=float)
    with_ash = df.loc[df["Fly Ash"] > 0, "Concrete compressive strength"].to_numpy(dtype=float)
    if len(without) < 2 or len(with_ash) < 2:
        raise ValueError("Need at least two 28-day samples in each fly-ash group")

    mean_without = without.mean()
    mean_with = with_ash.mean()
    difference = mean_with - mean_without
    welch = stats.ttest_ind(with_ash, without, equal_var=False)
    print("QUESTION 3: How does average 28-day strength compare with and without fly ash?")
    print(f"Total samples cured for exactly 28 days: {len(df)}")
    print(f"Without fly ash: n = {len(without)}, mean = {mean_without:.2f} MPa, SD = {without.std(ddof=1):.2f} MPa")
    print(f"With fly ash:    n = {len(with_ash)}, mean = {mean_with:.2f} MPa, SD = {with_ash.std(ddof=1):.2f} MPa")
    print(f"Mean difference (with - without): {difference:+.2f} MPa")
    print(f"Welch two-sample t-test: t = {welch.statistic:.4f}, p = {welch.pvalue:.4g}")

    fig, ax = plt.subplots(figsize=(7.2, 5.5))
    labels = ["Without Fly Ash", "With Fly Ash"]
    means = [mean_without, mean_with]
    stds = [without.std(ddof=1), with_ash.std(ddof=1)]
    ax.bar(labels, means, yerr=stds, capsize=6, width=0.56, alpha=0.85)
    ax.set(title="28-Day Concrete Strength by Fly-Ash Presence",
           ylabel="Mean Compressive Strength (MPa)", xlabel="Concrete Mix Group")
    ax.grid(axis="y", alpha=0.2)
    ax.set_axisbelow(True)
    ax.text(0, means[0] + stds[0] + 1.3, f"n = {len(without)}", ha="center")
    ax.text(1, means[1] + stds[1] + 1.3, f"n = {len(with_ash)}", ha="center")
    ax.set_ylim(0, max(m + s for m, s in zip(means, stds)) * 1.25)
    fig.tight_layout()
    destination = plot_path("q3_fly_ash.png")
    fig.savefig(destination, dpi=170)
    plt.close(fig)
    print(f"\nPlot saved: plots/{destination.name}")
    print("Interpretation: Differences between groups do not prove the effect of adding fly ash, because mix ingredients also vary.")


if __name__ == "__main__":
    analyze()
