# Assessing the Impact of Open Environmental Data on Temperature Predictions Using Regression-Kriging

## Primary Research Goals
This study incorporates high-temporal-resolution air temperature data from weather measurement sensors to account for city-scale differences in climatic and environmental conditions. In order to meet the demand for spatially continuous climatological datasets, Regression Kriging is applied to estimate continuous air-temperature surfaces across the city of Heidelberg. Next to air temperature, elevation, tree canopy height and building height will be included as covariates, as their influence on thermal comfort is widely cited. The resulting high-resolution continuous temperature grids provide a valuable addition to the existing city-wide location-based air temperature measurements, with the potential to enhance heat-adaptive routing by offering a subjective representation of thermal conditions at the neighbourhood scale.

## Fundamental research questions of this study:
- *RQ 1:* How accurately can regression–kriging predict spatial patterns of hourly air temperature in an urban environment using a sparse sensor network under different meteorological conditions?
- *RQ 2:* Which environmental and urban covariates explain spatial variability in urban air temperature, and how does their relative explanatory importance vary over the diurnal cycle and across meteorological conditions?
- *RQ 3:* How does temporal aggregation scale affect the performance and outcomes of RK-based temperature interpolation?

## How to run the analysis
The analysis is based on 8 RMarkdown files which include the following information:
1. [01_hourly_rk.Rmd](r_scripts/01_hourly_rk.Rmd) is the entire RK framwork with hourly temporal resolution.
2. [02_hourly_rk_results.Rmd](r_scripts/01_hourly_rk_results.Rmd) incorporates code for the creation of output plots.
3. [03_hourly_rk_model_comparison.Rmd](r_scripts/03_hourly_rk_model_comparison.Rmd) can be run to compare the hourly RK predictions against the Stadtklimaanalyse of the city of Heidelberg (2023).
4. [04_hourly_mlr.Rmd](r_scripts/04_hourly_mlr.Rmd) is the deterministic component (MLR) of the RK framwork with hourly temporal resolution.
5. [05_hourly_mlr_results.Rmd](r_scripts/05_hourly_mlr_results.Rmd) incorporates code for the creation of output plots.
6. [06_multicollinearity_covariates.Rmd](r_scripts/06_multicollinearity_covariates.Rmd) is the analysis of covariates regarding relationships with the target variable and addressing multicollinearity.
7. [07_monthly_rk.Rmd](r_scripts/07_monthly_rk.Rmd) is the entire RK framwork with monthly temporal resolution.
8. [08_hourly_rk_gaussian.Rmd](r_scripts/08_hourly_rk_gaussian.Rmd) is the entire RK framwork with hourly temporal resolution jusr adjusted to run with gaussian-smoothed canopy height data.


## Example Regression-Kriging Temperature Surface for the Study Area

![Regression Kriging Temperature Surface](/plots/2023-07-09_1400_rk_prediction_map.png)
