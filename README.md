# Assessing the Impact of Open Environmental Data on Temperature Predictions Using Regression-Kriging

## Overview

This repository contains the complete modelling workflow for predicting air temperature in Heidelberg (Germany) using **Regression–Kriging (RK)**.

The project integrates:

- High-temporal-resolution air temperature sensor data (2023)
- Elevation, global forest canopy height, and global building height as covariates
- Hourly and monthly RK frameworks
- Spatial autocorrelation diagnostics
- Covariates importance assessment

The resulting high-temporal resolution temperature grids provide spatially continuous climatological datasets and support research on urban heat stress and heat-adaptive routing at a spatial resolution of 30 m.

---

## Primary Research Goals

This study incorporates high-temporal-resolution air temperature data from weather measurement sensors to account for city-scale climatic and environmental variability.

RK is applied to generate spatially continuous air-temperature surfaces across Heidelberg. In addition to air temperature, the following environmental covariates are included:

- Elevation  
- Tree canopy height  
- Building height 

These variables are widely cited as influencing urban thermal conditions and human thermal comfort. The resulting temperature grids complement existing point-based measurements and provide a spatially continuous representation of neighbourhood-scale thermal conditions.

## Research Questions

- **RQ 1:** How accurately can regression–kriging predict spatial patterns of hourly air temperature in an urban environment using a sparse sensor network under different meteorological conditions?
- **RQ 2:** Which environmental and urban covariates explain spatial variability in urban air temperature, and how does their relative explanatory importance vary over the diurnal cycle and across meteorological conditions?
- **RQ 3:** How does temporal aggregation scale affect the performance and outcomes of RK-based temperature interpolation?

---

## Repository Structure

**data/** Input datasets
**plots/** Generated output figures
**python_scripts/** Information on how to derive temp measurements from server
**r_scripts/** RMarkdown with all analysis steps

---

## How to run the analysis
The analysis consists of eight RMarkdown scripts, each covering a specific component of the workflow. They can be grouped into three smaller work packages with the recommended execution order being:

### Work Package 1 – Hourly RK

1. [01_hourly_rk.Rmd](r_scripts/01_hourly_rk.Rmd) Complete RK framework with hourly temporal resolution.
2. [02_hourly_rk_results.Rmd](r_scripts/01_hourly_rk_results.Rmd) Generates plots and visual summaries of the hourly RK results.
3. [03_hourly_rk_model_comparison.Rmd](r_scripts/03_hourly_rk_model_comparison.Rmd) Compares hourly RK predictions with the 2023 Stadtklimaanalyse of the City of Heidelberg.

---

### Work Package 2 – Hourly MLR Analysis

4. [04_hourly_mlr.Rmd](r_scripts/04_hourly_mlr.Rmd) Implements the deterministic component (MLR) of the hourly RK framework.
5. [05_hourly_mlr_results.Rmd](r_scripts/05_hourly_mlr_results.Rmd) Produces evaluation plots and diagnostics for the hourly MLR models.


---

### Work Package 3 – Covariate Analysis, Monthly RK & Gaussian-smoothed canopy height data

6. [06_multicollinearity_covariates.Rmd](r_scripts/06_multicollinearity_covariates.Rmd) Examines relationships between covariates and the target variable, including multicollinearity diagnostics.
7. [07_monthly_rk.Rmd](r_scripts/07_monthly_rk.Rmd) Complete RK framework with monthly temporal resolution.
8. [08_hourly_rk_gaussian.Rmd](r_scripts/08_hourly_rk_gaussian.Rmd) Variant of the hourly RK framework using Gaussian-smoothed canopy height data.

---

## Example Output

Below is an example hourly regression–kriging temperature surface  (7 July 2023, 17:00):

![Regression Kriging Temperature Surface](plots/2023-07-07_1700_rk_prediction_map.png)

---

## Reproducibility

### Requirements

- R ≥ 4.2  
- RStudio recommended  

---

## Reference Selection

Hengl, T. (2009). A practical guide to geostatistical mapping. Vol. 52. Hengl Amsterdam, Netherlands.

Hengl, T.; Heuvelink, G. B. M. & Rossiter, D. (2007). About regression-kriging: From equations to case studies. In: Computers & Geosciences 33, 1301–1315. doi: 10.1016/j.cageo.2007.05.001.

Kolaxidis, N.; Ludwig, C.; Knoblauch, S.; Fürle, J.; Foshag, K.; Fendrich, S.; Lautenbach, S. & Zipf, A. (2025). Mitigating Heat Stress by Reducing Solar Exposure in Pedestrian Routing. In: Transactions in GIS 29(6), e70110. doi: 10.1111/tgis.70110.

Oliver, M. A. &Webster, R. (2015). Basic Steps in Geostatistics: The Variogram and Kriging. SpringerBriefs in Agriculture. Cham: Springer International Publishing. doi: 10.1007/978-3-319-15865-5.

Szymanowski, M.; Kryza, M. & Spallek, W. (2013). Regression-based air temperature spatial prediction models: an example from Poland. In: Meteorologische Zeitschrift 22(5), 577–585. doi: 10.1127/0941-2948/2013/0440.


