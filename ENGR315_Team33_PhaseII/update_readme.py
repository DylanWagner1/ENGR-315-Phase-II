import numpy as np
from scipy import stats
from common import ROOT, RESULT_DIR, load_data

START = "<!-- BEGIN GENERATED RESULTS -->"
END = "<!-- END GENERATED RESULTS -->"


def main():
    readme_path = ROOT / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    blocks = [
        ("Question 1: Curing Age", "q1_curing_age", "q1_curing_age.png"),
        ("Question 2: Water-to-Cement Ratio", "q2_water_cement", "q2_water_cement.png"),
        ("Question 3: Fly Ash at 28 Days", "q3_fly_ash", "q3_fly_ash.png"),
    ]
    lines = [START, "## Results (Full UCI Dataset)", ""]
    for heading, stem, image in blocks:
        output = (RESULT_DIR / f"{stem}_output.txt").read_text(encoding="utf-8").rstrip()
        lines.extend([
            f"### {heading}", "", "Command-line output:", "", "```text", output,
            "```", "", f"![{heading}](plots/{image})", "",
        ])
    df = load_data(columns=["Age", "Concrete compressive strength", "Water", "Cement", "Fly Ash"])
    age = df[df["Age"] > 0]
    r_age = age["Age"].corr(age["Concrete compressive strength"])
    age_direction = "positive" if r_age > 0 else "negative"
    ratio_df = df[df["Cement"] > 0]
    water_ratio = ratio_df["Water"] / ratio_df["Cement"]
    regression = stats.linregress(water_ratio, ratio_df["Concrete compressive strength"])
    ratio_direction = "positive" if regression.slope > 0 else "negative"
    day28 = df[df["Age"] == 28]
    with_ash = day28[day28["Fly Ash"] > 0]["Concrete compressive strength"]
    without_ash = day28[day28["Fly Ash"] == 0]["Concrete compressive strength"]
    difference = with_ash.mean() - without_ash.mean()
    test = stats.ttest_ind(with_ash, without_ash, equal_var=False)
    significance = (
        "shows evidence of different group means (p < 0.05)"
        if test.pvalue < 0.05 else
        "does not show a statistically significant difference (p >= 0.05)"
    )
    lines.extend([
        "## Conclusions (Full UCI Dataset)", "",
        f"1. **Curing age:** Across {len(age)} samples, age and compressive strength have "
        f"a {age_direction} Pearson correlation (r = {r_age:.3f}). The logarithmic trend and "
        "age-specific standard deviations should be considered together; mix compositions also vary.",
        f"2. **Water-to-cement ratio:** The association is {ratio_direction} "
        f"(r = {regression.rvalue:.3f}, R² = {regression.rvalue**2:.3f}). "
        "This is an unadjusted regression, not a prediction controlling for other mixture ingredients.",
        f"3. **Fly ash at 28 days:** The fly-ash group's mean strength is "
        f"{difference:+.2f} MPa relative to the no-fly-ash group. "
        f"The Welch test {significance} (p = {test.pvalue:.4g}). "
        "This group comparison cannot isolate the causal effect of fly ash.",
        "", "**Overall limitation:** The mixes differ in cement, water, curing age, and other ingredients. "
        "These results describe associations in the dataset, not controlled experiments.", "",
        END,
    ])
    replacement = "\n".join(lines)
    if START not in text or END not in text:
        raise ValueError("Could not locate README generated-results markers")
    prefix = text.split(START, 1)[0]
    suffix = text.split(END, 1)[1]
    readme_path.write_text(prefix + replacement + suffix, encoding="utf-8")
    print("README full-data results section updated")


if __name__ == "__main__":
    main()
