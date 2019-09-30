.. _URAO:

URAO
====================


.. **To do:**

.. #TODO: FiG needs to be added
.. #TODO: link to BB, where?
.. #TODO: Links to other relevant materials
.. #TODO: remove to do notes down below

.. **end of todo**


.. _safety:

Safety
------

The Observatory should be regarded as a laboratory environment. The same guidelines apply as for other laboratory courses in the Department (see Departmental Handbook

BB : `MPCS Programme Info <https://www.bb.reading.ac.uk/webapps/portal/execute/tabs/tabAction?tabId=_110_1&tab_tab_group_id=_154_1>`_.


#. Do not make adjustments to mains-supplied instruments or attempt to modify any apparatus without consulting either a demonstrator or a technician.
#. You should not work in the Observatory outside the class contact   period, except by special arrangement with a supervising member of
staff or a laboratory technician.
#. On the Observatory, beware of guy ropes attached to masts and overhead instruments. Be especially careful if the ground is muddy.
Work in the area you have been shown to work in, as some cables and   soil heat flux plates may be near the surface.
#. Wear suitable, protective footwear (i.e. NOT flip-flops) and beware of low-lying objects which you could trip over. Wear appropriately    warm clothes.
#. Always ask if there are any points which are not clear.




Instruments
-----------

Eddy Covariance (EC) mast
~~~~~~~~~~~~~~~~~~~~~~~~~

The EC mast at the URAO has a **sonic anemometer** (Gill R3, Figure 1)
which derives the wind-speed from transit times of acoustic pulses
travelling in both directions along a fixed path. The wind-speed
component along the path is proportional to the difference between the
transit times. Three sets of transducer pairs are used to derive the
three components of the wind vector u, v, w. In addition, the speed of
sound can be deduced:

Also, on the EC mast is an **open path infra-red gas analyser** (Li-Cor,
LI-7500, Figure 1) to measures both CO2 and H2O. It uses the principle
of radiation absorption by water and carbon dioxide molecules at certain
wavelengths. A differential measurement is made to compare transmittance
at a wavelength with strong absorption adjacent to a wavelength where
absorption is negligible. For water vapour (carbon dioxide) the
wavelength is 2.59 `\mathrm{\mu m}` (4.26 `\mathrm{\mu m}`)
and the reference wavelength is 2.4 `\mathrm{\mu m}` (3.95 `\mathrm{\mu m}`).
The ratio of light intensity at the two wavelengths is
proportional to the amount of water vapour present.

The IRGA at URAO is an open-path rather than a closed-path instrument
(where air is sucked down a tube into the instrument itself). The q
specific humidity of water vapour is expressed in units of kg kg-1. The
absolute humidity (`\text{kg m}^{-3}`) is derived by taking
the molecular weight of
water into account (1 mol = 18 g = 0.018 kg) and similarly for carbon
dioxide concentrations (molar mass 44 g `\text{mol}^{-1}`). The instruments are
mounted close to each other at a height of 3 m. A Campbell CR3000 logger
is used to record the data at a sampling rate of 10 Hz.

.. #FIXME - Figures need to be inserted**

Figure 1: Gill R3 sonic anemometer (bird optional!) and Li-7500 eddy
covariance system;

Wind and temperature profile mast (6.4 m)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A profile of 8 pulse **cup anemometers** and 4 **platinum resistance
thermometers** (PRTs) are mounted at various heights (Table 1). The
coincident temperature and wind profiles allow both stability and
surface fluxes to be derived. Each anemometer produces electrical pulses
at a rate proportional to its rotation speed. The PRT output voltage is
proportional to the PRT resistance


.. csv-table:: Height of wind (U) and temperature measurements (T) at RUAO
    :file: URAO-heights.csv
    :widths: auto
    :width: 10
    :header-rows: 1
    :stub-columns: 1




Logging of sensors
~~~~~~~~~~~~~~~~~~

Programmed data loggers sample the data at different time intervals. Raw
samples (e.g. from EC system) or just statistics (e.g. an average from
pyranometer) are recorded. During data processing calibration
coefficients are applied.

Data from the Observatory
-------------------------

Data can be downloaded from: https://metdata.reading.ac.uk/ext/

Ask your instructor for download token in class if you need one.


Types of data
~~~~~~~~~~~~~

#. 5 min averaged logger output.

   - Includes individual radiation fluxes, soil heat flux,
     temperature (T), wind speed (WS), wind direction (Wdir),
     station pressure, rainfall, and relative humidity (RH).

#. Eddy covariances - 30-min averages.

   -  Fully processed EC fluxes: These have been subjected to the
      numerous corrections (Kotthaus and Grimmond 2012, 2014a) that
      are regularly undertaken for EC fluxes.

#. 5-min WMO-standard processed output:

   -  This includes the wind profile data and the temperature profile
      data. Radiation data (make certain you use the corrected
      longwave radiation data)

#. 0.1s Sonic Licor

   -  Raw EC data - these files are very large so do **NOT download data**
      until you know what you really want/need.

References: See :ref:`refs`.
