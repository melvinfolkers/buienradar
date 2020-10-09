<img src="https://static.wixstatic.com/media/a9ca5e_825bd4d39e7d468faf735b801fa3dea4~mv2.png/v1/fill/w_1458,h_246,al_c,usm_0.66_1.00_0.01/a9ca5e_825bd4d39e7d468faf735b801fa3dea4~mv2.png" width="200">

# Buienradar

> this purpose of this repository is to collect data from the Dutch website www.buienradar.nl.

## Introduction

The json data feed from buienradar refreshes around 3 times per hour (https://data.buienradar.nl/2.0/feed/json). 
This repository demonstrate how you can collect this data and store it. 
Running this project on server will make it possible to create a dataset that can be used for multiple purposes (reporting, analysing)

## Forecast vs Actuals

A nice add-on would be to analyse the time-series dataset and compare it with the 5-day forecast. 
 
    


    actuals: Dataset containing the most recent measurements from the weather stations.
    forecast: Dataset contaning the 5-day forecast

## Maintainers:
- [Melvin Folkers](https://github.com/melvinfolkers)
