# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:21:36 2019

@author: luizv
"""
import field  as fld # classe do campo elétrico
import numpy as np
import beam_shapes as bsc

def gerar_visualizacao_intensidade_campo_eletrico(wl = 1064E-9, resolucao = 200, titulo="Intensidade do campo Elétrico"):
	k = 2 * np.pi / wl          # número de onda
	axicon = 2 * np.pi / 180    # ângulo de axicon (\alpha)
	tmbscs = {}                 # fatores de forma (modo TM) [BSCs]
    
    #criando fatores de forma
	for n in range(1, 1000):
	    tmbscs[(n, 1)] = bsc.bessel_bsc_tm(n, 1, axicon, k=k)
	    tmbscs[(n, -1)] = bsc.bessel_bsc_tm(n, -1, axicon, k=k)
	tebscs = {}                 # fatores de forma (modo TE)
	for n in range(1, 1000):
	    tebscs[(n, 1)] = bsc.bessel_bsc_te(n, 1, axicon, k=k)
	    tebscs[(n, -1)] = bsc.bessel_bsc_te(n, -1, axicon, k=k)
	bscs = {'TM': tmbscs, 'TE': tebscs} # Todos os BSCs devem estar neste formato

	pw = fld.SphericalElectricField(k, bscs=bscs)   # objeto que descreve o campo elétrico
	v1 = pw.norm(1E-6, np.pi / 4, 0)    # um valor pra norma do campo elétrico em um ponto do espaço
	print(v1)
	pw.plot_r(2E-5, sample=resolucao, title=titulo) # Plotagem da intensidade (ao quadrado) campo elétrico num corte do plano-xz


gerar_visualizacao_intensidade_campo_eletrico(resolucao=2)