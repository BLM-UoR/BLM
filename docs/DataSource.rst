.. _DataSources:

Data Sources
============

In this course, we focus on the :term:`AmeriFlux` datasets for analysis.
The :term:`URAO` dataset might also be used, so some knowledge of both will be helpful.



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
    :class: longtable
    :header-rows: 1

.. _amf_site:

.. tip::
    Refer to `AmeriFlux Site Search page
    <https://ameriflux.lbl.gov/sites/site-search/>`_
    for full details of all sites used here.


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
    :class: longtable
    :header-rows: 1


- Surface Energy Balance

.. csv-table::
    :file: var-SEB.csv
    :widths: 1,3,1
    :class: longtable
    :header-rows: 1

- Standard Meteorological Conditions

.. csv-table::
    :file: var-MET.csv
    :widths: 1,3,1
    :class: longtable
    :header-rows: 1

- Others

.. csv-table::
    :file: var-Other.csv
    :widths: 1,3,1
    :class: longtable
    :header-rows: 1



MODIS data associated with AmeriFlux sites
*********************************************

`MODIS land products`_ provides summaries of selected datasets for validation of models and remote-sensing products and to characterise field sites.
Specifically, we use the LAI product in the class to help understand the relationships between surface parameters (e.g., albedo, surface resistance, etc.) and vegetation phenology.


.. _MODIS land products: https://doi.org/10.5067/MODIS/MCD15A3H.006


Useful papers for understanding AmeriFlux datasets
******************************************************

.. TODO: update reading list by modify entries with keyword `reading`
    in the ``blm-res.bib`` file; modify the `note` record for remarks.

.. the `rl` style below is defined in `conf.py`;
    unfortunately, less flexibility in formatting can be achieved. Journal format -AMS


.. bibliography:: amf-refs.bib
   :style: rl
   :list: enumerated
   :filter: Keywords % "ameriflux"

URAO
---------

Please visit `URAO documentation site
<http://www.met.reading.ac.uk/~sws09a/MODE3_help.html>`_
for information about observations at URAO.
