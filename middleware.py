# -*- coding: utf-8 -*-
#!/usr/bin/env python

import field  as fld
import numpy as npx
import beam_shapes as bsc
import sys

def tratar_entradas():
    resolucao = int(1)
    titulo = str("Intensidade do campo Elétrico")
   
    if  len(sys.argv) == 1 :
        return false
    else:
        if (sys.argv[1]) :
            resolucao = sys.argv[1]
            
        if(len(sys.argv) > 2):
            titulo = sys.argv[2]
            
        if(len(sys.argv) > 3):
            wl = sys.argv[3]
   
    gerar_visualizacao_intensidade_campo_eletrico(resolucao = resolucao, titulo = titulo)

def gerar_visualizacao_intensidade_campo_eletrico(wl = 1064E-9, resolucao = 1, titulo="Intensidade do campo Elétrico"):
    k = 2 * npx.pi / wl          # número de onda
    axicon = 2 * npx.pi / 180    # ângulo de axicon (\alpha)
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
    v1 = pw.norm(1E-6, npx.pi / 4, 0)    # um valor pra norma do campo elétrico em um ponto do espaço
    print(pw.plot_r(2E-5, sample=resolucao, title=titulo)) # Plotagem da intensidade (ao quadrado) campo elétrico num corte do plano-xz

tratar_entradas()