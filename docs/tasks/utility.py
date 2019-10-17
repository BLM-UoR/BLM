import numpy as np
import pandas as pd

# saturation vapour pressure [hPa]
def cal_vap_sat(Temp_C,Press_hPa):
    # temp_c= 0.001 if np.abs(Temp_C)<0.001 else Temp_C
    Press_kPa = Press_hPa/10

    if (0.001000 <= Temp_C < 50):
        e_mb = 6.1121*np.exp(((18.678 - Temp_C/234.5)*Temp_C)/(Temp_C + 257.14))
        f = 1.00072 + Press_kPa*(3.2E-6 + 5.9E-10*Temp_C**2)
        es_hPa = e_mb*f

    if (-40< Temp_C <= -0.001000):
        e_mb = 6.1115*np.exp(((23.036 - Temp_C/333.7)*Temp_C)/(Temp_C + 279.82))
        f = 1.00022 + Press_kPa*(3.83E-6 + 6.4E-10*Temp_C**2)
        es_hPa = e_mb*f

    if (-0.001< Temp_C < 0.001):
        es_hPa=cal_vap_sat(0.001,Press_hPa)
    
    return es_hPa

# density of dry air [kg m-3]
def cal_dens_dry(RH_pct,Temp_C,Press_hPa):
    gas_ct_dry=8.31451/0.028965 #dry_gas/molar
    es_hPa=cal_vap_sat(Temp_C,Press_hPa)
    Ea_hPa=RH_pct/100*es_hPa
    dens_dry = ((Press_hPa - Ea_hPa)*100)/(gas_ct_dry*(273.16 + Temp_C))
    return dens_dry


# density of vapour [kg m-3]
def cal_dens_vap(RH_pct,Temp_C, Press_hPa):
    gas_ct_wv = 8.31451/0.0180153 #dry_gas/molar_wat_vap
    es_hPa=cal_vap_sat(Temp_C,Press_hPa)
    Ea_hPa=RH_pct/100*es_hPa
    vap_dens = (Ea_hPa*100/((Temp_C + 273.16)*gas_ct_wv))
    return vap_dens


# specific heat capacity of air mass [J kg-1 K-1]
def cal_cpa(Temp_C, RH_pct, Press_hPa):
    # heat capacity of dry air depending on air temperaure
    cpd = 1005.0 + ((Temp_C + 23.16)**2)/3364.0
    # heat capacity of vapour
    cpm = 1859 + 0.13*RH_pct + (19.3 + 0.569*RH_pct)*(Temp_C/100.) + (10.+0.5*RH_pct)*(Temp_C/100.)**2

    # density of dry air
    rho_d=cal_dens_dry(RH_pct,Temp_C,Press_hPa)

    # density of vapour
    rho_v=cal_dens_vap(RH_pct,Temp_C, Press_hPa)

    # specific heat
    cpa = cpd*(rho_d/(rho_d + rho_v)) + cpm*(rho_v/(rho_d + rho_v))
    return cpa


# air density [kg m-3]
def cal_dens_air(Press_hPa,Temp_C):
     #dry_gas/molar
    gas_ct_dry=8.31451/0.028965

    # air density [kg m-3]
    dens_air = (Press_hPa*100)/(gas_ct_dry*(Temp_C + 273.16))
    return dens_air


# Obukhov length
def cal_Lob(QH, UStar, Temp_C, RH_pct, Press_hPa, g=9.8,k=0.4):
    # gravity constant/(Temperature*Von Karman Constant)
    G_T_K = (g/(Temp_C + 273.16))*k

    # air density [kg m-3]
    rho=cal_dens_air(Press_hPa,Temp_C)

    # specific heat capacity of air mass [J kg-1 K-1]
    cpa=cal_cpa(Temp_C, RH_pct, Press_hPa)
    
    # Kinematic sensible heat flux [K m s-1]
    H=QH/(rho*cpa)
    
    # temperature scale
    uStar=np.max([0.01,UStar])
    TStar=-H/uStar
    
    # Obukhov length
    Lob = (uStar**2)/(G_T_K*TStar)

    return Lob