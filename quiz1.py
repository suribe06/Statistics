#Made by Sebastian Daza and Santiago Uribe

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import resample

theta = 34 #parametro
poblacion = [x for x in range(1,theta+1)]

theta_1 = max(poblacion)
theta_2 = 2*np.mean(poblacion)

mse_1, mse_2 = [], []

n_space = [50, 100, 1000]#tamanos de muestra
for n in n_space:
    vec_theta_1 = []
    vec_theta_2 = []
    for i in range(10000):
        samples = resample(poblacion, n_samples=n, replace=True)#seleccion de muestra
        #calcular estimadores
        theta_1_hat = max(samples)
        theta_2_hat = 2 * np.mean(samples)
        vec_theta_1.append(theta_1_hat)
        vec_theta_2.append(theta_2_hat)

    #Calculo de MSE para la muestra
    esper_theta_1 = np.mean(vec_theta_1)
    var_theta_1 = np.var(vec_theta_1)
    mse_theta_1 =  var_theta_1 + ((esper_theta_1 - theta_1)**2)
    mse_1.append(mse_theta_1)

    esper_theta_2 = np.mean(vec_theta_2)
    var_theta_2 = np.var(vec_theta_2)
    mse_theta_2 =  var_theta_2 + ((esper_theta_2 - theta_2)**2)
    mse_2.append(mse_theta_2)

    #Generar histogramas
    plt.clf()
    plt.figure(figsize=(6,5))
    plt.hist(vec_theta_1)
    plt.axvline(theta_1, color='k', linestyle='dashed', linewidth=1, label='$\\theta_1$')
    plt.title(f'Histogram for n={n}')
    plt.ylabel("Frequency")
    plt.xlabel("$\\widehat{\\theta_1}$")
    plt.legend()
    plt.savefig(f"theta1_n{n}.png")

    plt.clf()
    plt.figure(figsize=(8,5))
    sns.histplot(vec_theta_2, kde=True, stat="density", linewidth=0, color='darkblue')
    plt.axvline(theta_2, color='k', linestyle='dashed', linewidth=1)
    plt.title(f'Histogram for n={n}')
    plt.ylabel("Density")
    plt.xlabel("$\\widehat{\\theta_2}$")
    plt.legend(labels=['Probability Density Function','$\\theta_2$', '$\\widehat{\\theta_2}$ Probability Density'])
    plt.savefig(f"theta2_n{n}.png")

for i in range(len(n_space)):
  print(f'Para tamano de muestra n={n_space[i]}: MSE theta_1 = {mse_1[i]}, MSE theta_2 = {mse_2[i]}')
