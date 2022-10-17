# Papila
Prediction of Air Pollution in Latin America and the Caribbean (PAPILA) is a research project focus to integer global and local emissions inventory of reactive gases, mainly for South America. The main motivation is to implement an air quality analysis and forecasting system using Eulerian models such as WRF-Chem and MUSICA to asses the air pollution impact on the human health. According to [Cartesana et al. (2022)](https://essd.copernicus.org/articles/14/271/2022/), the project started making an improved emissions inventory based on existing global data from CAMS-GLOB-ANT v4.1 and local inventory from countries as Argentina, Chile, and Colombia, including CO, NO$_x$, NMVOCs, NH$_3$, and SO$_2$ as anthropogenic annual emissions for the period 2014-2016, with a spatial resolution of 0.1° $\times$ 0.1° and 31-120° W and 34°N-58°S as modeling domain.

## Scope of work
- [ ] Model domain configuration,
  - [ ] D01. Papila suggests `450 x 455` grid points, 27 km x 27 km. Also, we have reference of the model setup from [Vara-Vela et al. (2021)](https://journals.ametsoc.org/view/journals/bams/102/9/BAMS-D-21-0018.1.xml) which the model domain consists of `378` $\times$ `402` horizontal grid points at a resolution of 20 km and with 30 vertical layers.
  - [ ] D02. `150` x `100` grid points with 9 km x 9 km horizontal resolution centering in the MASP. We have the reference of the model domain from [Gavidia-Calderon et al. (2018)](https://www.sciencedirect.com/science/article/pii/S1352231018306216?via%3Dihub).
- [ ] Prepare emissions inventory
  - [ ] Global anthropogenic emissions from CAMS
  - [ ] Biogenic emissions from MEGAN 3
  - [ ] Biomass burning emissions from [FINN](https://www2.acom.ucar.edu/modeling/finn-fire-inventory-ncar)
- [ ] Simulate with WRF-Chem v 4.2.1
  - [ ] Meteorological IC/BC: FNL GFS 0.25 for January, July, and September 2019. September is a interesting month when the biomass burning increase.
  - [ ] Chemical mechanism: MOZART/MOSAIC
  - [ ] Chemical IC/BC from CAM-Chem [output simulations](https://www.acom.ucar.edu/cam-chem/cam-chem.shtml)
 - [ ] Model evaluation
  

