## Experimental logs
- The first experiment run with MOZART-MOSAIC mechanism failed because the time step (dt=120 seconds) generates numerical instability (points with CFL>2). We changed the time step to dt=90 seconds, running only for meteorological conditions without any problem for two days of simulations. However, the model with MOZCART mechanism ran only 12 hours and failed. We saw the `rsl.error.0005`, see below:

```fortran
forrtl: severe (174): SIGSEGV, segmentation fault occurred
Image              PC                Routine            Line        Source             
wrf.exe            0000000004A057CA  Unknown               Unknown  Unknown
libpthread-2.28.s  0000145A47CE6D80  Unknown               Unknown  Unknown
wrf.exe            000000000355EE1B  Unknown               Unknown  Unknown
wrf.exe            000000000355BBCE  Unknown               Unknown  Unknown
wrf.exe            00000000026D1546  Unknown               Unknown  Unknown
wrf.exe            00000000026C8048  Unknown               Unknown  Unknown
wrf.exe            0000000001F6D035  Unknown               Unknown  Unknown
wrf.exe            0000000001F4B236  Unknown               Unknown  Unknown
wrf.exe            0000000001D98E69  Unknown               Unknown  Unknown
wrf.exe            00000000005E364F  Unknown               Unknown  Unknown
wrf.exe            0000000000405851  Unknown               Unknown  Unknown
wrf.exe            000000000040580F  Unknown               Unknown  Unknown
wrf.exe            00000000004057A2  Unknown               Unknown  Unknown
libc-2.28.so       0000145A475B1813  __libc_start_main     Unknown  Unknown
wrf.exe            00000000004056AE  Unknown               Unknown  Unknown
```

- Exp. 3 (WRF-Chem v4.2.1 with MOZCART) only run 14 hours. The rsl.error.0011 shows Unknown or SEGSEV processing.
- Exp. 4 (WRF-Chem v.4.2.1 with MOZCART) cannot run all the period, a SEGSEV ocurred. The WRF-Chem version 3.9.1 ran succesfully all period.
- Exp. 5 (WRF-Chem v4.4.1 with MOZCART) is running but frozen ata date `2019-06-25_20:43:30`. The `phot_opt = 4` (TUV) options in namelist.input as seeting up is different compared with previous experiments.
