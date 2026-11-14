# Phase II Results and Conclusions

**Project:** How Concrete Mix Design and Curing Affect Compressive Strength  
**Course:** JMU ENGR 315 — Computational Methods in Engineering  
**Team:** Team 33  
**Members:** Dylan Wagner and Mitchell Kim

## Dataset and analysis

The analyses below use **all 1,030 samples** in the [UCI Concrete Compressive Strength dataset](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength). Strength is reported in megapascals (MPa), curing age in days, and mixture ingredient quantities in kg/m³. The data were analyzed using descriptive statistics, Pearson correlation, logarithmic curve fitting, linear regression, and a group comparison.

These results describe relationships across different concrete mixtures. They should not be interpreted as estimates of the causal effect of changing one ingredient or curing time while holding other factors constant.

## Question 1 — How does curing age relate to compressive strength?

**Method:** Group all samples by curing age, calculate mean strength and sample standard deviation for each age, calculate Pearson's correlation coefficient, and fit a logarithmic curve to individual observations.

**Calculated metrics:**

| Metric | Result |
|---|---:|
| Total samples | 1,030 |
| Pearson correlation coefficient, r | 0.3289 |
| Logarithmic model coefficient, a (MPa) | 11.3110 |
| Logarithmic model coefficient, b (MPa) | 7.7423 |
| Coefficient of determination, R² | 0.3049 |

**Fitted relationship:**

```text
Compressive strength (MPa) = 11.3110 + 7.7423 * ln(curing age in days)
```

**Strength grouped by curing age:**

| Age (days) | Number of samples | Mean strength (MPa) | Sample standard deviation (MPa) |
|---:|---:|---:|---:|
| 1 | 2 | 9.46 | 4.50 |
| 3 | 134 | 18.98 | 9.86 |
| 7 | 126 | 26.05 | 14.58 |
| 14 | 62 | 28.75 | 8.64 |
| 28 | 425 | 36.75 | 14.71 |
| 56 | 91 | 51.89 | 14.31 |
| 90 | 54 | 40.48 | 9.82 |
| 91 | 22 | 69.81 | 7.70 |
| 100 | 52 | 47.67 | 8.40 |
| 120 | 3 | 39.65 | 1.10 |
| 180 | 26 | 41.73 | 10.93 |
| 270 | 13 | 51.27 | 10.64 |
| 360 | 6 | 40.70 | 4.17 |
| 365 | 14 | 43.56 | 9.62 |

**Conclusion:** Curing age has a positive association with concrete compressive strength (r = 0.3289). The logarithmic curve captures a general upward trend, but its R² of 0.3049 shows that age alone does not account for most of the observed variation. Average strength is not strictly increasing in every age group because the dataset compares different concrete mixtures rather than repeated measurements of identical mixes.

## Question 2 — How does water-to-cement ratio relate to compressive strength?

**Method:** Divide the water content (kg/m³) by cement content (kg/m³) to calculate a dimensionless water-to-cement ratio for each sample, then apply ordinary least-squares linear regression and calculate Pearson's r and R².

**Calculated metrics:**

| Metric | Result |
|---|---:|
| Total samples | 1,030 |
| Pearson correlation coefficient, r | -0.5007 |
| Linear regression slope (MPa per unit ratio) | -26.6379 |
| Linear regression intercept (MPa) | 55.7502 |
| Coefficient of determination, R² | 0.2507 |

**Fitted relationship:**

```text
Compressive strength (MPa) = 55.7502 - 26.6379 * (water / cement)
```

**Conclusion:** A higher water-to-cement ratio is associated with lower compressive strength. The correlation is moderately negative (r = -0.5007), but the simple linear model explains only about 25.1% of the variation in compressive strength. The analysis does not control for curing age, other cementitious materials, or additives.

## Question 3 — At 28 days, how does strength compare with and without fly ash?

**Method:** Filter the dataset to samples tested at **exactly 28 days**. Split the samples into two groups based on whether fly-ash content is greater than zero. Calculate group sample counts, mean compressive strengths, and sample standard deviations. Compare group means with Welch's independent-samples t-test.

**Group statistics:**

| Metric | With fly ash | Without fly ash |
|---|---:|---:|
| Number of samples | 217 | 208 |
| Mean strength (MPa) | 34.07 | 39.54 |
| Sample standard deviation (MPa) | 13.12 | 15.76 |

**Statistical comparison:**

| Metric | Result |
|---|---:|
| Total 28-day samples | 425 |
| Mean difference: with fly ash minus without (MPa) | -5.47 |
| Welch's t-statistic | -3.8776 |
| Welch–Satterthwaite degrees of freedom | 402.94 |
| Two-sided p-value | 0.0001232 |

**Conclusion:** At 28 days, samples containing fly ash had a mean strength approximately **5.47 MPa lower** than samples without fly ash. The difference between these two groups is statistically significant using Welch's t-test (p ≈ 0.0001232). However, the groups may also differ in cement content, water content, or other material quantities. Therefore, this result does **not** establish that adding fly ash causes a decrease in strength.

## Overall conclusion

The full dataset shows three main relationships: curing age is positively associated with compressive strength, water-to-cement ratio is negatively associated with strength, and at 28 days the fly-ash-containing group has a lower unadjusted mean strength than the no-fly-ash group. These findings support the need to consider both curing conditions and concrete mixture proportions when studying strength. Additional analyses that account for multiple ingredients simultaneously would be useful for drawing more specific conclusions.

## Reproducibility and submission materials

The repository's Python scripts should regenerate metrics with `print()` and save labeled graphs with Matplotlib:

```bash
python -m pip install -r requirements.txt
python run_all.py
```

Run those commands **inside the `ENGR315_Team33_PhaseII` folder**. Then commit the generated full-dataset output files (`results/`), graphs (`plots/`), dataset (`data/concrete.csv`), and the updated project README to GitHub. The numbers in this report are full-dataset results, **not** the preliminary 70-row demonstration included in the initial project files.

## References

1. Yeh, I. (1998). *Concrete Compressive Strength* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5PK67
2. UCI dataset listing: https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength
3. Public CSV mirror: https://github.com/HansenHan/ML_UCI_Concrete_Compressive_Strength/blob/main/Concrete_Data.csv