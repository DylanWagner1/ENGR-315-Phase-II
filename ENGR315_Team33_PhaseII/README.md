# How Concrete Mix Design and Curing Affect Compressive Strength

**ENGR 315 Computational Methods in Engineering — Team 33**  
**Contributors:** Dylan Wagner and Mitchell Kim  
**Phase II: Sub-Task 6 — Python Analysis and Progress Report**

## Objective and Motivation

Concrete compressive strength matters in structural and civil engineering. The goal of this project is to identify relationships between concrete curing time, mix composition, and compressive strength by applying statistics and curve fitting in Python.

## Dataset

**Primary source:** [Concrete Compressive Strength — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength), attributed to I-Cheng Yeh (1998), DOI: [10.24432/C5PK67](https://doi.org/10.24432/C5PK67), available under CC BY 4.0. The complete dataset has **1,030 samples** with ingredient amounts (kg/m³), curing age (days), and compressive strength (MPa). The project scripts download a comma-separated copy of this dataset from [this public GitHub mirror](https://github.com/HansenHan/ML_UCI_Concrete_Compressive_Strength/blob/main/Concrete_Data.csv) when executed online. The `data/concrete.csv` file is the downloaded complete dataset; `data/example_first_70_age_strength.csv` is **not the full dataset**.

## Questions and Methods

| Question | Calculations | Visualization |
| --- | --- | --- |
| 1. How does curing age relate to compressive strength? | Average strength and standard deviation by age; Pearson correlation; logarithmic curve fit and R² | Individual observations, group means ± SD, fitted logarithmic curve |
| 2. How does water-to-cement ratio relate to compressive strength? | Compute water / cement; linear regression; Pearson r; R²; slope and p-value | Scatterplot with regression line |
| 3. How does 28-day strength compare with and without fly ash? | Filter to exactly 28 days; mean, SD, and count by group; Welch's independent-samples t-test | Mean strength by group with SD error bars |

All values are descriptive unless otherwise indicated; other mixture ingredients can affect the relationships observed. A statistical association does not establish causation.

## Implementation Details

- **`prepare_data.py`** downloads the complete public dataset, if it is not already present.
- **`q1_curing_age.py`** loads curing age and strength, groups data by age, computes metrics and a logarithmic least-squares fit, and saves a plot.
- **`q2_water_cement.py`** calculates the water-to-cement ratio and a linear regression, and saves a plot.
- **`q3_fly_ash.py`** filters concrete to exactly 28 days, compares fly-ash groups, and saves a plot.
- **`run_all.py`** downloads data, runs all three analyses, records the printed terminal output to the `results/` directory, and inserts the full results and plots into this README.
- **`update_readme.py`** updates only the results section between the marked lines, preserving other README content.

## How to Run

In a terminal opened in the project folder:

```bash
python -m pip install -r requirements.txt
python run_all.py
```

This writes `results/q1_curing_age_output.txt`, `results/q2_water_cement_output.txt`, `results/q3_fly_ash_output.txt`, and three labeled PNG plots under `plots/`. It also updates the **Results** and **Conclusions** sections of this README with all command-line output and graphs. **Run this on a machine with internet access before committing the final Phase II update.**

To see a preliminary test of Question 1 using only the first 70 authentic rows from the UCI copy, run:

```bash
python q1_curing_age.py --data data/example_first_70_age_strength.csv --plot example_first_70_q1.png
```

This is a **limited test**, not the complete dataset or final project findings.

## Preliminary Progress — Question 1 (70-Row Test Only)

The script was successfully exercised using the first 70 source observations for curing age and strength. For these **70 source rows**, Pearson correlation was **r = 0.4213** and the logarithmic fit had **R² = 0.3785**. Mean compressive strength was **10.53 MPa at 3 days** (4 observations) and **47.99 MPa at 365 days** (10 observations). This limited slice shows a positive age-strength association, but the large spread between mixes means curing age alone does not explain the results. These 70 samples are not a random sample of the full dataset, so these values should **not** be interpreted as the final 1,030-record findings.

**Example terminal output:** [results/example_first_70_q1_output.txt](results/example_first_70_q1_output.txt)

![Preliminary concrete age vs. strength plot](plots/example_first_70_q1.png)

<!-- BEGIN GENERATED RESULTS -->
## Results (Full UCI Dataset)

Pending complete-dataset execution: run `python run_all.py` to calculate and insert actual results, command-line outputs, and plots for all three questions.

## Conclusions (Full UCI Dataset)

Pending the full dataset analysis. No full-dataset numerical conclusions are claimed in this preliminary package.

<!-- END GENERATED RESULTS -->

## Actions That Need to Be Completed

- [x] Define three question/method pairs and prepare Python code for all three.
- [x] Include a checked, limited test for Question 1 and its actual console output and plot.
- [ ] Run `python run_all.py` online to load all 1,030 rows, generate final results, and automatically update the README.
- [ ] Review the plots and conclusions for each question; discuss possible confounding variables.
- [ ] Commit/push the final scripts, README, dataset, console outputs, and plots to Team 33's GitHub repository.
- [ ] Submit **Team 33's own project GitHub repository URL** in Canvas.

## References

1. Yeh, I. (1998). *Concrete Compressive Strength* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5PK67
2. Public CSV mirror of the UCI dataset: https://github.com/HansenHan/ML_UCI_Concrete_Compressive_Strength/blob/main/Concrete_Data.csv
3. JMU ENGR 315 Project Description (attached to assignment).
