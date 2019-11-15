# -*- coding: utf-8 -*-
"""
Created on Fri Nov 8 19:04:17 2019

@author: luizv
"""

import numpy as np
from scipy.special import loggamma, gammasgn, jv
from utils import legendre_tau, legendre_pi, factorial_quotient

def bessel_bsc_tm(n, m, axicon, v=0,
                  rho0=0, phi0=0, z0=0, k=2 * np.pi / 1064E-9):

    lpi = m * legendre_pi(n, m, np.cos(axicon))
    ltau = legendre_tau(n, m, np.cos(axicon)) / np.cos(axicon)
    pre_mul = pow(1j, m + 1) / 2 * pow(-1, (m + np.abs(m)) / 2) \
            * factorial_quotient(n - m, n + np.abs(m)) \
            * np.exp(k * np.cos(axicon) * z0)
    t_plus = jv(m - v + 1, k * rho0 * np.sin(axicon)) \
           * np.exp(-1j * (m - v + 1) * phi0) \
           * (lpi - ltau)
    t_minus = jv(m - v - 1, k * rho0 * np.sin(axicon)) \
           * np.exp(-1j * (m - v - 1) * phi0) \
           * (lpi + ltau)
    return pre_mul * (t_plus + t_minus)

def bessel_bsc_te(n, m, axicon, v=0,
                  rho0=0, phi0=0, z0=0, k=2 * np.pi / 1064E-9):
    lpi = m * legendre_pi(n, m, np.cos(axicon))
    ltau = legendre_tau(n, m, np.cos(axicon)) / np.cos(axicon)
    pre_mul = pow(1j, m + 1) / 2 * pow(-1, (m + np.abs(m)) / 2) \
            * factorial_quotient(n - m, n + np.abs(m)) \
            * np.exp(k * np.cos(axicon) * z0)
    t_plus = jv(m - v + 1, k * rho0 * np.sin(axicon)) \
           * np.exp(-1j * (m - v + 1) * phi0) \
           * (lpi - ltau)
    t_minus = jv(m - v - 1, k * rho0 * np.sin(axicon)) \
           * np.exp(-1j * (m - v - 1) * phi0) \
           * (lpi + ltau)
    return 1j * pre_mul * (t_plus - t_minus)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    # test for v = 0, m = 1
    ns = [n for n in range(1, 500)]
    tm_bscs = [np.linalg.norm(bessel_bsc_te(n, -1, 2 * np.pi / 180)) for n in ns]
    plt.plot(ns, tm_bscs)
    