# -*- coding: utf-8 -*-
"""
Created on Fri Nov 8 20:27:29 2019

@author: luizv
"""


import numpy as np
import matplotlib.pyplot as plt

import field_components as fcs


class SphericalElectricField:
    def __init__(self, wave_number, bscs={'TM': {}, 'TE': {}}):
        self.tm_bscs = bscs['TM']
        self.te_bscs = bscs['TE']
        self.degrees = set()
        self.wave_number = wave_number
        for _, m in self.tm_bscs:
            self.degrees.add(m)

    def radial(self, radial, theta, phi):
        return fcs.radial_electric_i_tm(radial, theta, phi,
                                        self.wave_number,
                                        degrees=self.degrees,
                                        bscs=self.tm_bscs)

    def theta_tm(self, radial, theta, phi):
        return fcs.theta_electric_i_tm(radial, theta, phi,
                                        self.wave_number, degrees=self.degrees,
                                        bscs=self.tm_bscs)

    def theta_te(self, radial, theta, phi):
        return fcs.theta_electric_i_te(radial, theta, phi,
                                        self.wave_number, degrees=self.degrees,
                                        bscs=self.te_bscs)

    def theta(self, radial, theta, phi):
        return self.theta_tm(radial, theta, phi) \
             + self.theta_te(radial, theta, phi)

    def phi_tm(self, radial, theta, phi):
        return fcs.phi_electric_i_tm(radial, theta, phi,
                                      self.wave_number, degrees=self.degrees,
                                      bscs=self.tm_bscs)

    def phi_te(self, radial, theta, phi):
        return fcs.phi_electric_i_te(radial, theta, phi,
                                      self.wave_number, degrees=self.degrees,
                                      bscs=self.te_bscs)

    def phi(self, radial, theta, phi):
        return self.phi_tm(radial, theta, phi) \
             + self.phi_te(radial, theta, phi)

    def norm(self, radial, theta, phi):
        return np.linalg.norm(np.array([
                self.radial(radial, theta, phi),
                self.theta(radial, theta, phi),
                self.phi(radial, theta, phi)]
                ))

    def x_comp(self, radial, theta, phi):
        x_comp = self.radial(radial, theta, phi) * np.sin(theta) * np.cos(phi)\
               + self.theta(radial, theta, phi) * np.cos(theta) * np.cos(phi) \
               - self.phi(radial, theta, phi) * np.sin(phi)
        return x_comp
    
    def plot_r(self, r_max, sample=200):
        rs = np.linspace(-r_max, r_max, sample)
        xs, zs = np.meshgrid(rs, rs)
        r = lambda x, z: np.sqrt(x ** 2 + z ** 2)
        t = lambda x, z: np.arctan2(z, x)
        grid = np.abs(np.vectorize(self.norm)(r(xs, zs), t(xs, zs), 0)) ** 2
        grid = np.nan_to_num(grid)
        rr = r_max * 1E6
        plt.xlabel('x [$\mu$m]')
        plt.ylabel('z [$\mu$m]')
        plt.imshow(grid.transpose(), extent=[-rr, rr, -rr, rr], cmap='inferno')
        plt.colorbar()
        plt.show()