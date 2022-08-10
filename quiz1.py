#Made by Sebastian Daza and Santiago Uribe

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import resample

theta = 34 #parametro
n_space = [50, 100, 1000]#tamanos de muestra

for n in n_space:
    vec_theta_1 = []
    vec_theta_2 = []
    for i in range(10000):
        poblacion = [x for x in range(theta)]
        samples = resample(poblacion, n_samples=n, replace=True)#seleccion de muestra
        #calcular estimadores
        theta_1 = max(samples)
        theta_2 = 2 * np.mean(samples)
        vec_theta_1.append(theta_1)
        vec_theta_2.append(theta_2)

    #Generar histogramas
    plt.clf()
    plt.hist(vec_theta_1)
    plt.title("Histogram for $\\theta_1$ and n={}".format(n))
    plt.ylabel("Frequency")
    plt.xlabel("$\\theta_1$")
    plt.savefig(f"theta1_n{n}.png")

    plt.clf()
    sns.histplot(vec_theta_2, kde=True, stat="density", linewidth=0, color='darkblue')
    plt.title("Histogram for $\\theta_2$ and n={}".format(n))
    plt.ylabel("Frequency")
    plt.xlabel("$\\theta_2$")
    plt.savefig(f"theta2_n{n}.png")


"""
Comentarios de los resultados obtenidos:


"""
