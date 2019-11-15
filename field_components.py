# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:28:55 2019

@author: luizv
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:02:23 2019

@author: luizv
"""

import numpy as np

from glmtscatt.specials import (_riccati_bessel_j, _riccati_bessel_y,
                           legendre_p, legendre_tau, legendre_pi,
                           riccati_bessel_j, riccati_bessel_y,
                           d_riccati_bessel_j, d_riccati_bessel_y,
                           d2_riccati_bessel_j, d2_riccati_bessel_y,
                           riccati_bessel_radial_i, riccati_bessel_radial_s)
from glmtscatt.utils import (get_max_it, one, exp_im, m_exp_im,
                             inverse, multiply_function)

def plane_wave_coefficient(degree, wave_number_k):
    """ Computes plane wave coefficient :math:`c_{n}^{pw}` """
    return (1 / (1j * wave_number_k)) \
        * pow(-1j, degree) \
        * (2 * degree + 1) / (degree * (degree + 1))


def radial_electric_i_tm(radial, theta, phi,
                              wave_number_k, degrees=[-1, 1],
                              bscs={}):
    """ Computes the radial component of incident electric field in TM mode.
    """
    result = 0
    n = 1

    riccati_bessel_list = _riccati_bessel_j(get_max_it(radial, wave_number_k),
                                            wave_number_k * radial)
    riccati_bessel = riccati_bessel_list[0]

    max_it = get_max_it(radial, wave_number_k)

    # while n <= get_max_it(radial, wave_number_k):
    while n <= max_it:
        for m in degrees:
            if n >= m:
                increment = plane_wave_coefficient(n, wave_number_k) \
                          * bscs[(n, m)] \
                          * (d2_riccati_bessel_j(n, wave_number_k * radial)
                             + riccati_bessel[n]) \
                          * legendre_p(n, abs(m), np.cos(theta)) \
                          * np.exp(1j * m * phi)
                result += increment
        n += 1

    return wave_number_k * result

def theta_electric_i_tm(radial, theta, phi, wave_number_k,
                        degrees=[-1, 1], bscs={}):
    """ Computes the theta component of inciding electric field in TM mode.
    """
    result = 0
    n = 1
    # Due to possible singularity near origin, we approximate null radial
    # component to a small value.
    radial = radial or 1E-16

    riccati_bessel_list = _riccati_bessel_j(get_max_it(radial, wave_number_k),
                                            wave_number_k * radial)
    d_riccati_bessel = riccati_bessel_list[1]
    max_it = get_max_it(radial, wave_number_k)
    while n <= max_it:
        for m in degrees:
            if n >= m:
                increment = plane_wave_coefficient(n, wave_number_k) \
                          * bscs[(n, m)] \
                          * d_riccati_bessel[n] \
                          * legendre_tau(n, abs(m), np.cos(theta)) \
                          * np.exp(1j * m * phi)
                result += increment
        n += 1
    return result / radial

def theta_electric_i_te(radial, theta, phi, wave_number_k,
                        degrees=[-1, 1], bscs={}):
    """ Computes the theta component of inciding electric field in TE mode.
    """
    result = 0
    n = 1
    # Due to possible singularity near origin, we approximate null radial
    # component to a small value.
    radial = radial or 1E-16

    riccati_bessel_list = _riccati_bessel_j(get_max_it(radial, wave_number_k),
                                            wave_number_k * radial)
    riccati_bessel = riccati_bessel_list[0]
    max_it = get_max_it(radial, wave_number_k)
    while n <= max_it:
        for m in degrees:
            if n >= m:
                increment = m \
                          * plane_wave_coefficient(n, wave_number_k) \
                          * bscs[(n, m)] \
                          * riccati_bessel[n] \
                          * legendre_pi(n, abs(m), np.cos(theta)) \
                          * np.exp(1j * m * phi)
                result += increment
        n += 1

    return result / radial

def phi_electric_i_tm(radial, theta, phi, wave_number_k,
                      degrees=[-1, 1], bscs={}):
    """ Computes the phi component of inciding electric field in TM mode.
    """
    result = 0
    n = 1
    # Due to possible singularity near origin, we approximate null radial
    # component to a small value.
    radial = radial or 1E-16

    riccati_bessel_list = _riccati_bessel_j(get_max_it(radial, wave_number_k),
                                            wave_number_k * radial)
    d_riccati_bessel = riccati_bessel_list[1]

    max_it = get_max_it(radial, wave_number_k)
    while n <= max_it:
        for m in degrees:
            if n >= m:
                increment = m \
                          * plane_wave_coefficient(n, wave_number_k) \
                          * bscs[(n, m)] \
                          * d_riccati_bessel[n] \
                          * legendre_pi(n, abs(m), np.cos(theta)) \
                          * np.exp(1j * m * phi)
                result += increment
        n += 1

    return 1j * result / radial

def phi_electric_i_te(radial, theta, phi, wave_number_k,
                      degrees=[-1, 1], bscs={}):
    """ Computes the phi component of inciding electric field in TE mode.
    """
    result = 0
    n = 1
    m = 0
    # Due to possible singularity near origin, we approximate null radial
    # component to a small value.
    radial = radial or 1E-16

    riccati_bessel_list = _riccati_bessel_j(get_max_it(radial, wave_number_k),
                                            wave_number_k * radial)
    riccati_bessel = riccati_bessel_list[0]

    max_it = get_max_it(radial, wave_number_k)
    while n <= max_it:
        for m in degrees:
            if n >= m:
                increment = plane_wave_coefficient(n, wave_number_k) \
                          * bscs[(n, m)] \
                          * riccati_bessel[n] \
                          * legendre_tau(n, abs(m), np.cos(theta)) \
                          * np.exp(1j * m * phi)
                result += increment
        n += 1

    return 1j * result / radial