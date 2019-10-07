.. _SEB:

Surface energy balance
======================

The surface energy balance (SEB) can be defined for an extensive simple
surface as (units: :math:`\mathrm{W \ m^{-2}}`):

.. math::
    :label: seb

    Q^*= Q_H + Q_E +Q_G

where :math:`Q^*` is the net all wave radiation, the turbulent sensible
heat flux (`Q_H`) and the turbulent latent heat flux (`Q_E`) and
the soil heat flux (`Q_G`) (units: :math:`\mathrm{W \ m^{-2}}`).

Note other notation that is used for the SEB are (in the same order as above):

.. math::

    R_n= H + LE + G

Bowen ratio
-----------

The Bowen ratio (`\beta`) is

.. math::
    :label: bowen

    \beta= Q_H / Q_E

.. _radB:

Radiation balance
=================
.. TODO fix label to seb

The `Q^*` (or `R_n`) within the SEB :ref:`SEB` consists of:

.. math::
    :label: qstar

    Q^*= K_\downarrow- K_{\uparrow} + L_\downarrow- L_{\uparrow}

which includes the
incoming (:math:`\downarrow`) and outgoing (:math:`\uparrow`) shortwave
(K) and longwave radiation (L) fluxes.


SEB and Radiation Balance Measurements
===================================================

Each of these fluxes can be directly measured or modelled using several
methods (and data inputs).

Examples of instruments in the :ref:`URAO` are listed.  From papers you will be able to determine how the fluxes and other variables are measured at the site you are studying.

Radiation fluxes
----------------------
Various types of radiometers are used. For shortwave radiation, pyranometers are used, and for longwave radiation, pyrgeometers are used. The source area or field of view of a radiation sensor is fixed by geomtery.

Turbulent heat Fluxes
----------------------

The turbulent heat fluxes and momentum can be measured using Eddy
Covariance techniques (see :ref:`EC`). These require a sonic anemometer and an infrared gas analyser.

As the source area of EC sensors varies with wind direction, fetch, stability etc, the surface characteristics may change with time if the fetch is not homogeneous.

SEB and Radiation Balance Modelling
===================================================

Generally, to calculate a convective or conductive flux, data are needed to determine the size of the gradient
(e.g. temperature difference) and the ability of the medium (e.g. air,
soil) to transfer heat (or mass). The latter may use a resistance
scheme, an eddy diffusivity, or other approach, which changes with the
state of the medium (e.g. stability if air, moisture state if soil).


One method to model the latent heat flux uses the Penman Monteith equation
(`Penman <Penman.rst>`__).



