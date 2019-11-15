# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:14:14 2019

@author: luizv
"""

from scipy.special import loggamma, gammasgn, lpmv
import scipy.special as special
import numpy as np


def factorial_quotient(num, den):
    return gammasgn(num + 1) * gammasgn(den + 1) * np.exp(
            loggamma(num + 1) - loggamma(den + 1))

def fac_plus_minus(n, m):
    """ Calculates the expression below avoiding overflows.
    
    .. math::
        \\frac{(n + m)!}{(n - m)!}
    """
    return factorial_quotient(n + m, n - m)

def legendre_p(degree, order, argument):
    """ Associated Legendre function of integer order
    """
    
    if degree < np.abs(order):
        return 0
    if order < 0:
        return pow(-1, -order) / fac_plus_minus(degree, -order) \
               * legendre_p(degree, -order, argument)
    return special.lpmv(order, degree, argument)

def legendre_tau(degree, order, argument, mv=True):
    """ Returns generalized Legendre function tau

    Derivative is calculated based on relation 14.10.5:
    http://dlmf.nist.gov/14.10
    """
    if not mv:
        return -np.sqrt(1 - argument ** 2) * special.lpmn(order, degree, argument)[1][order][degree]
    '''
    if argument == 1:
        argument = 1 - 1E-16
    if argument == -1:
        argument = -1 + 1E-16
    '''
    return (degree * argument * legendre_p(degree, order, argument) \
            - (degree + order) * legendre_p(degree - 1, order, argument)) \
            / (np.sqrt(1 - argument * argument))

def legendre_pi(degree, order, argument, overflow_protection=False):
    """ Generalized associated Legendre function pi
    
    .. math::
        \\pi_n^m(x) = \\frac{P_n^m(x)}{\\sqrt{1-x^2}}
    """
    if overflow_protection:
        if argument == 1:
            argument = 1 - 1E-16
        if argument == -1:
            argument = -1 + 1E-16
    return legendre_p(degree, order, argument) \
           / (np.sqrt(1 - argument * argument))