Penman
===============


.. #TODO. Links to other relevant materials
.. #TODO. remove to do notes down below
.. #TODO. fix sub/superscripts & equations


The combination equation (Penman, 1948)
---------------------------------------

Given the difficulty in directly observing evaporative fluxes – and the
need to estimate evaporation to determine irrigation of crops Penman
(1948) developed the *combination equation*. Only standard
meteorological observations at some height above either water or a
surface covered with well-watered short grass, were required.

This equation “combines” two physical controls on evaporation: the
supply of available energy `Q^*-Q_G` and the turbulent diffusion of
water vapour from the surface. Firstly, the sensible and latent heat
fluxes should be written in resistance notation

.. math::
   :label: qh

    Q_{H} = - \rho c_{p}\frac{T - T_{0}}{r_{h}}

.. math::
   :label: qe

    L_{v}E = - \frac{L_{v}}{R_{v}T}\frac{e - e_{0}}{r_{v}}


We can rewrite :eq:`qe` in terms of `r_h` and the effective psychrometer
const­ant `\gamma^*`:

.. math::
    :label: qe_1

    L_{v}E = - \rho c_{p}\frac{e - e_{0}}{{\gamma^*}r_{h}},

where the “thermodynamic” psychrometer constant is given by
`\gamma = \rho c_{p}/L_{v}\varepsilon` and has a value of 0.66 hPa
|K^-1| near sea level, the ratio of gas constants is
`\varepsilon=R_a/R_v`,
and the effective psychrometric constant is `\gamma^*=\gamma r_v/r_h`.

The key to estimating the exchange of sensible and latent heat with the
air above a surface is to establish the surface temperature `T_0`. If
this is not known, then it can be eliminated from the equations by
assuming that the saturation vapour pressure is a linear function of
temperature for small temperature differences. Additionally, it is
assumed that the surface vapour pressure is at saturation, i.e.

.. math::
    :label: e0

    e_{0}=e_{s}\left(T_{0}\right)=e_{s}(T)-s\left(T-T_{0}\right)


By substitution of :eq:`e0` into :eq:`qe`
we get `Q_E` in terms of `T-T_0` which is not known.
But by combining the new equation for `Q_E`, `T-T_0` may
be eliminated from :eq:`qh` for `Q_H`.

The final assumption is that of energy balance closure (EBC), i.e. that
`Q^*-Q_G=Q_H+Q_E`. By substitution of the new equation for `Q_H`,
we obtain the *Penman equation*

.. math::
    :label: penman

    L_{v}E =
    \frac
    {s\left( Q* - Q_{G} \right) + \rho c_{p}\left( e_{s}(T) - e \right)/r_{H}}
    {s + \gamma_{*}}

giving latent heat flux as a function of variables measured at one
height only.

Resistance notation
-------------------

In the combination equation, fluxes are recast in terms of aerodynamic
resistances. Thus, the momentum flux across a finite layer
:math:`\Delta z = \left( z_{2} - z_{1} \right)` can be expressed as

.. math::
    :label: tau

    \tau = \frac{\rho\left( u_{2} - u_{1} \right)}{r_{a}}

where `r_a` is the *aerodynamic resistance*. If `u_1` is taken to be
the `u(z_0)=0`, then the resistance can be related to the log law

.. math::
    :label: ra

    r_{a} = \frac{u(z)}{u_{*}^{2}}
    = \frac{ln\lbrack\frac{z - d}{z_{0}}\rbrack}{ku_{*}}
    = \frac{\left\lbrack ln\lbrack\frac{z - d}{z_{0}}\rbrack
    \right\rbrack^{2}}{k^{2}u(z)}


Notice that the quantity in square brackets depends only on the nature
of the surface: if that is known, then :math:`r_{a}` is determined only
by the single measurement of mean wind speed. For fluxes this leads to
an expression predicting a flux of some variable `\alpha`, `F_{\alpha}` in
the form

.. math::
    :label: fa

    F_{\alpha} = u_{*}^{2}
    \left( \frac{\phi_{m}}{\phi_{\alpha}} \right)
    \frac{\Delta\alpha}{\Delta u} \equiv \frac{\Delta\alpha}{r_{\alpha}},

in which
:math:`r_{\alpha} =
\left( \frac{\Delta u}{u_{*}^{2}} \right) \times
\left( \frac{\phi_{\alpha}}{\phi_{m}} \right)`
is the *aerodynamic resistance* of the layer (some authors use
*conductance,* which is the reciprocal of `r_{\alpha}`).
In the case of momentum, `\phi_{\alpha}=\phi_m`.
For non-neutral conditions:

.. math::
    :label: ra1

    r_{a} =
    \frac{\left\lbrack \ln\left( \frac{z - d}{z_{0}} \right)
    - \ \psi_{m}\ \left( z^{'}/L \right) \right\rbrack^{2}}
    {k^{2}u}.

Under *stable conditions*, the aerodynamic resistance for sensible heat
transfer (`r_h`) is usually taken as equal to `r_a`.
Under *unstable conditions*, the assumption
:math:`\frac{\phi_{h} =}{{\phi_{m}^{2}}_{m}}`
means than we need to
multiply `r_a` by :math:`\phi_{m}` to get `r_h`. In both cases, the
aerodynamic resistance for water vapour and other scalar fluxes is
generally assumed to be the same as that for sensible heat. Note that,
in general, `z` should be replaced by `z-d` if the sampling height is
not much greater than the zero-plane displacement height `d`.

The Penman-Monteith equation
----------------------------
Evaporation from a vegetated surface is also impacted by plant
physiology. Stomata in the leaves open to allow transfer of CO\ :sub:`2`
during photosynthesis, but can close when the plant is water stressed to
avoid undue loss of water vapour. Monteith (1965) adapted Penman’s
equation to allow for this effect, giving what we now know as the
*Penman-Monteith equation* where the symbols have the same meaning,
except that `\gamma^*` is an *apparent* psychrometer ‘constant’. Over crops
the resistance to evaporation is larger than the resistance to heat
transfer, due to *canopy resistance*. To allow for this, the effective
psychrometer constant is usually assumed to be of the form

.. math::
    :label: gamma

    \gamma_{*}
    = \gamma\left( \frac{r_{h} + r_{s}}{r_{h}} \right)
    = \gamma\left( 1 + \frac{r_{s}}{r_{h}} \right),

where `r_s` is an effective surface resistance. The latter depends in a
complicated way on soil moisture, type of vegetation, fractional cover,
and time of year. It is usual to consider it as the result of a
c\ *anopy* (or *crop*) *resistance* (`r_{sc}`) and a *bare soil
resistance* (`r_{ss}`) acting in parallel, so that

.. math::
    :label: rs

    \frac{1}{r_{s}}
    = \frac{\left( 1 - A \right)}{r_{\text{sc}}} + \frac{A}{r_{\text{ss}}}

where `A` is an effective fraction of bare soil area. Appropriate values
of crop resistance are known for various types of vegetation. For
‘moist’ surface conditions during the day, `r_{ss}` is usually taken to
be 100 s m\ :sup:`-1`.

Finally, `r_h` can be approximated by the aerodynamic resistance `r_a`
as it is more readily measurable. For observations close to the ground
(e.g. below 3 m) the stability correction can be neglected, and `r_a`
therefore estimated using (4). The Penman approach does not require
‘special’ equipment but assumptions about the transfer processes at the
Earth’s surface as well as the nature of the surface itself are needed.

The P-M equation is used practically by the FAO. Evapotranspiration is
computed for a grass reference crop (`ET_0`), then multiplied by a crop
coefficient (`K_c`) to give an estimate of actual evapotranspiration.
For instance, `K_c \sim 1 \textrm{ to } 1.2` for cabbage,
but 1.1 to 1.5 for sugar cane.
To aid calculation of irrigation requirements, `ET_0` is
expressed in `\textrm{mm day}^{-1}`
and can range from `1–3\textrm{ mm day}^{-1}` in cool,
arid regions to `5–6\textrm{ mm day}^{-1}` in warm tropical regions.

Penman Monteith Method Measurements
-----------------------------------

Meteorological variables measured at one height can be used to estimate
the evaporative flux from a surface using the Monteith (1965) adaptation
for vegetated surface of Penman (1948):

.. math::
    :label: qe_pm

    Q_{E} =
    \frac{s\left( Q^{*} - Q_{G} \right) + \rho c_{p}(e_{s} - e)/r_{H}}
    {s + \gamma\ (1 + r_{s}/r_{a})}

For the practical, some assumptions are made in addition to those made
in deriving the equation. The aerodynamic resistance for heat transfer
is assumed to be equal to that for momentum transfer, i.e. `r_h \sim r_a`.

Aerodynamic Resistance
----------------------

To calculate `r_a`, one could assume neutral conditions are applicable
or apply stability correction. Surface characteristics influence the
surface (`r_s`) or canopy resistance `r_c`.
Around the site the surface characteristics
vary with grass in the near fetch but arrange of
other land covers further away from the sensors.



Canopy or surface resistance
----------------------------

By re-arranging the PM equation, with EC and other observations you can
determine the surface resistance (`r_s`) or its inverse surface
conductance (`g_s`) (Ward et al. 2016):

.. math::
    :label: gs

    \frac{1}{g_{s}}
    = r_{s}
    = \left( \frac{s}{\gamma}\frac{Q_{H}}{Q_{E}} - 1\  \right)
    r_{\text{av}} + \frac{\rho c_{p}\text{VPD}}{\gamma Q_{E}}

where `\text{VPD}` (:math:`=e_s-e`) is the vapour pressure deficit.
For our purposes we will assume :math:`r_h \sim r_a \sim r_{av}`.
