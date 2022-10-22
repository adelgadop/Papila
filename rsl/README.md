## Experimental logs
- The first experimental run failed because dt=120 seconds. Intead, we set-up dt=90 and run 12 hours, after that the run falls the `rsl.error.0005` for the second run shows:

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

A dt=60 seconds will use for the 3th experiment with MOZCART chemical mechanism.
