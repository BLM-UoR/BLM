Wind Profile
============


.. #TODO Links to other relevant materials
.. #TODO remove to do notes down below




Wind profile in neutral conditions
----------------------------------

The variation of mean wind speed :math:`\bar{u}` with height z (in
surface layer, above the RSL) above an aerodynamically rough surface can
be represented by a logarithmic relation:


.. math::
    :label: uz_ntrl

    \bar{u}(z) = \frac{u_{*}}{k}\ln\left\lbrack \frac{(z - d)}{z_{0}} \right\rbrack


where :math:`u_{*}` is the **friction velocity**
(:math:`u_{*}^{2} = - \overline{u'w'}`) rate of vertical transfer by
turbulence of horizontal momentum per unit mass of air), :math:`z_{0}` is
the roughness length of the surface for momentum, *d* is the zero-plane
displacement and *k* is von Karman's constant (0.4). The logarithmic law
is strictly valid only in **neutral conditions**, i.e. when the effect
of buoyancy on turbulence is small compared to the effect of wind shear.
In such conditions, the temperature profile in the surface layer will be
close to adiabatic (i.e. :math:`dT/dz=–9.8 \textrm{ K km}^{-1}`
or potential temperature is constant with height).
When the sensible heat flux is significantly
different from zero, Monin-Obukhov theory (or other) must be used.

Wind and temperature profile in non-neutral conditions
------------------------------------------------------

.. #TODO: needs Modifications

Modifications to the logarithmic profile are required in conditions of
non-neutral stability. Here we use **Monin-Obukhov theory** of the surface layer that derives relations between the vertical
variation of wind speed u(z) and potential temperature :math:`\theta(z)` (which
approximates the measured temperature T close to the surface), the
scaling factors for momentum and temperature, :math:`u^*` and :math:`T^*`,
and the **Monin‑Obukhov stability parameter**

.. math::
    :label: zol

    \frac{z'}{L} = - \frac{k\left( z - d \right)\frac{g}{\theta_{0}}\frac{H}{\rho c_{p}}}{u_{*}^{3}}

where L is the **Obukhov length** and *z’= z - d*. NB: the surface
temperature :math:`\theta_0` is an absolute temperature (units: K). The
logarithmic profile relation can be rewritten for wind speed to include
the stability corrections

.. math::
    :label: uz_crt

    \bar{u}(z) = \frac{u_{*}}{k}\left\lbrack \ln\left( \frac{z - d}{z_{0}} \right) - \Psi_{m}\left( \frac{z - d}{L} \right) + \Psi_{m}\left( \frac{z_{0}}{L} \right) \right\rbrack

and similarly, for potential temperature:

.. math::
    :label: tz_crt

    \bar{\theta}(z) = \theta_{0} + \frac{T_{*}}{k}\left\lbrack \ln\left( \frac{z - d}{z_{h}} \right) - \Psi_{h}\left( \frac{z - d}{L} \right) + \Psi_{h}\left( \frac{z_{h}}{L} \right) \right\rbrack

where the **turbulent temperature scale** is given by
:math:`T_{*} = - \overline{w^{'}T^{'}}/u_{*} = - Q_{H}/(\rho c_{p}u_{*})`,
:math:`\Psi_{m}` is the **integral** **stability correction function** for momentum
and `\Psi_{h}` is the integral stability correction function for heat. Note that
both `T_*` and `z’/L` have the opposite sign to `Q_H` (which is positive in unstable conditions and negative in stable conditions).
If `z'/z \gg 1` then the third term can assumed to be negligible
(Garratt 1992)


Profiles and fluxes of moisture
-------------------------------

Just as surface layer profiles of momentum and temperature follow a
logarithmic form in neutral conditions, humidity in the surface layer
has the same form, being transported by the same eddies. Thus, the
profile is given by

.. math::
    :label: qz_ntrl

    \overline{q}\left( z \right) - {\overline{q}}_{0} = \frac{q_{*}}{k}\ln\left( \frac{z - d}{z_{q}} \right)

where *q* is specific humidity, subscript *0* denotes a surface
measurement, *z\ q* is the equivalent “roughness length” for humidity,
and *d* is the zero-plane displacement height of a plant canopy over
which measurements are being made). *q\ \** is a scaling variable,
defined as

.. math::
    :label: qstar

    q_{*} = \frac{- \overline{w'q'}}{u_{*}}

and thus the dimensionless moisture profile is defined as

.. math::
    :label: phi_q

    \phi_{q} = \frac{k\left( z - d \right)}{q_{*}}\frac{\partial\overline{q}}{\partial z}.

The moisture flux can be written in various equivalent forms

.. math::
    :label: flux_q

    E = \rho\overline{w'q'} = u_{*}q_{*} = - \rho K_{q}\frac{\partial\overline{q}}{\partial z}

where :math:`K_{q}` is the eddy diffusivity for moisture.
In neutral conditions it is assumed :math:`K_m =K_h =K_q=k(z-d)u_*`.
Moisture follows Monin-Obukhov similarity just as other scalar variables do.
This was not established at the Kansas experiments due to limitations in the accuracy
of the measurements.
