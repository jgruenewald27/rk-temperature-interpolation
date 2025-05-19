# Masterthesis

## General goals of the thesis
Fundamental research questions of this thesis:
1.	To what extent does a more locally adapted interpolation model outperform a simpler machine-learning-based approach such as Random Forest in accurately predicting temperature values based on surrounding environmental factors?
2.	How do selected environmental covariates influence the accuracy of temperature interpolation? Do they meaningfully enhance model performance, or can reliable results be achieved without them?
3.	How does the temporal resolution of temperature data affect interpolation accuracy? Can reliable interpolation be achieved using high-frequency data such as hourly means, or is a coarser resolution—such as daily or even monthly means—necessary to provide a robust basis for interpolation?
4.	Can a robust interpolation framework be developed using only a single reference value from DWD stations for any given city, and how significantly can this approach be enhanced by integrating additional covariates?
5.	What role does data quality and spatial distribution of temperature measurements play in determining the effectiveness of temperature interpolation models?

## Statement of objectives
The comprehensive availability of temperature data is crucial for understanding the impacts of climate change on urban environments and for developing effective adaptation strategies. In particular, gaining insights into spatial temperature variability across urban areas can inform climate-resilient urban planning and behavioural adaptations, such as movement patterns and heat-mitigating infrastructure.
A key phenomenon in this context is the urban heat island (UHI) effect, which intensifies heat exposure in densely built-up areas. Addressing UHI through strategies like heat-adaptive urban routing relies on the ability to accurately map temperature distributions across cities. This thesis aims to contribute to that effort by developing an approach for temperature interpolation across urban surfaces.
The study will focus on the city of Heidelberg, utilizing data from a network of climate stations distributed throughout the city that provide temperature measurements at regular intervals. Using these point-based observations, the goal is to interpolate a continuous temperature surface that reflects local microclimatic conditions.
The chosen method for interpolation is regression kriging, which combines linear regression with geostatistical techniques. This approach allows for the integration of environmental covariates to improve interpolation accuracy. The following covariates will be considered due to their known influence on urban temperatures:
- Global Forest Canopy Height
- Global Average Gross Building Height 
- Elevation
- Proximity to Water Bodies (TBD)

A central aim of this thesis is to evaluate whether a complex locally adapted regression kriging model, incorporating these environmental covariates, significantly improves interpolation results compared to a simpler regression-only approach that derives a correction factor without spatial correlation modelling.
An additional objective is to ensure that the methodology is scalable to other regions. For this reason, the analysis will be based exclusively on globally available datasets for the covariates, increasing its potential for replication and application in diverse geographic contexts.
Finally, the thesis will examine the influence of data quality and spatial distribution of climate observations on interpolation outcomes. This analysis is essential for assessing the robustness of the approach and understanding its limitations in scenarios with sparse or unevenly distributed data.
As an outlook, the developed approach will be tested in additional German cities using DWD climate stations as the source of temperature data. The goal is to assess whether the method performs reliably in different urban contexts. A particularly promising outcome would be the ability to accurately estimate temperature surfaces in areas with minimal observational data, including cities that have only a single reference station. Such results would underscore the value of this method for broad-scale, data-scarce climate applications.

A backup of the used datasets can be found on Drive.