Data Sources
============

In this course, we focus on the :term:`AmeriFlux` datasets for analysis.
The :term:`URAO` dataset might also be used,
so some knowledge of both will be helpful.



Period selection
----------------

.. note::

   Raw observational data undergoing a large amount of processing prior to be used (e.g. calculation of fluxes using :ref:`EC` techniques). They are usually collected with preliminary, or even without, "cleaning".

   It is thus crucial to consider different aspects for different parameters:

   * cloud cover (e.g. this is important for the first plot)

   * vegetation state (e.g. are leaves on the trees?) (:ref:`LAI`)

   * wind direction (e.g. does land cover type vary with wind direction?)

   * Check that most of the data are available.

   * Look carefully at the turbulent heat fluxes,
     i.e. small numbers of 30 min periods can be missing
     – that is ok



AmeriFlux
---------

.. tip::
   Become familiar with `AmeriFlux website and data. <https://ameriflux.lbl.gov/>`_


Sites for analysis
******************************

.. csv-table::
    :file: AMF-Site-Sel.csv
    :widths: auto
    :header-rows: 1




Key variables for analysis
******************************

.. tip::
    Refer to `AmeriFlux Data Variables
    <https://ameriflux.lbl.gov/data/aboutdata/data-variables/>`_
    for full details of all measured variables.

- Surface Radiation Balance

.. csv-table::
    :file: var-SRB.csv
    :widths: 1,3,1
    :header-rows: 1


- Surface Energy Balance

.. csv-table::
    :file: var-SEB.csv
    :widths: 1,3,1
    :header-rows: 1

- Standard Meteorological Conditions

.. csv-table::
    :file: var-MET.csv
    :widths: 1,3,1
    :header-rows: 1

- Others

.. csv-table::
    :file: var-Other.csv
    :widths: 1,3,1
    :header-rows: 1





URAO
---------

Please visit `URAO documentation site
<http://www.met.reading.ac.uk/~sws09a/MODE3_help.html>`_
for information of observations at URAO.
