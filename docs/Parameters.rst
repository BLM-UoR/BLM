
.. #TODO: Links to other relevant materials

.. #TODO: remove to do notes down below


Model Parameters
================

Land surface models use parameters to describe the surface. For example
to model the latent heat flux using the `Penman Monteith equation
<Penman.rst>`__ the following parameters are needed.

.. _albedo:

Albedo
------

From the short-wave radiation (K), within the :eq:`qnet` :ref:`radB` the albedo (`\alpha`) is calculated:

.. math::
    :label: alb

    \alpha= K_{\uparrow} / K_\downarrow

using the incoming (:math:`\downarrow`) and outgoing (:math:`\uparrow`) shortwave radiation
(K) fluxes.

Typical Values
''''''''''''''''''''''''''

.. #TODO: get students to crowd-source this section

- Land cover type
- Time of year
- Time of day
- Location
- Reference

.. _roughness:

Roughness length (:math:`z_0`) and displacement height (:math:`d`)
------------------------------------------------------------------

If the displacement height is known, or is negligible, the logarithmic
law equation can be rearranged with observed :math:`z_0` and mean wind
speed to allow :math:`z_0` to be determined. As this may vary we
normally take median of a minimum of 20 results for a wind direction
sector. If you have a period with a lot of *neutral* conditions you may be
able to get a lot of samples rapidly.

.. math::

    𝑧_0 = (𝑧−𝑑) exp ⁡[−(𝑈_𝑧 𝜅)/𝑢_∗ ]

How does it vary with wind direction?
'''''''''''''''''''''''''''''''''''''''

A rule of thumb for calculating d is to assume it is ~0.7 `h` where `h` is
the height of the canopy. As the heights may vary with direction you can
determine how much this may vary. What are expected to be consistent
sectors?

The wind profile can also be used to determine :math:`z_0` and :math:`d`
if there are more than 2 levels in the profile. This requires fitting a
straight line (linear regression) through the data to determine the
intercept, which provides the `z_0+d` value.
See equations 1-2 in :cite:`grimmond1998aerodynamic`.

For `References <References.rst>`__ see list
