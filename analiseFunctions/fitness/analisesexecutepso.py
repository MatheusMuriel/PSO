import matplotlib.pyplot as plt
import numpy as np

path_base = "/home/muriel/projects/Faculdade/TCC/Implementações/DPSO_FJSP/analiseFunctions/fitness"

"""#Load Data"""
fitness = np.load(f"{path_base}/fitness.npy", allow_pickle=True)[()]

ft_p1_c3_a1 = fitness[f"problem_{1}"][f"coef_{3}"][f"approach_{1}"]
ft_p1_c3_a2 = fitness[f"problem_{1}"][f"coef_{3}"][f"approach_{2}"]
ft_p1_c5_a1 = fitness[f"problem_{1}"][f"coef_{5}"][f"approach_{1}"]
ft_p1_c5_a2 = fitness[f"problem_{1}"][f"coef_{5}"][f"approach_{2}"]
ft_p1_c6_a1 = fitness[f"problem_{1}"][f"coef_{6}"][f"approach_{1}"]
ft_p1_c6_a2 = fitness[f"problem_{1}"][f"coef_{6}"][f"approach_{2}"]
ft_p2_c3_a1 = fitness[f"problem_{2}"][f"coef_{3}"][f"approach_{1}"]
ft_p2_c3_a2 = fitness[f"problem_{2}"][f"coef_{3}"][f"approach_{2}"]
ft_p2_c5_a1 = fitness[f"problem_{2}"][f"coef_{5}"][f"approach_{1}"]
ft_p2_c5_a2 = fitness[f"problem_{2}"][f"coef_{5}"][f"approach_{2}"]
ft_p2_c6_a1 = fitness[f"problem_{2}"][f"coef_{6}"][f"approach_{1}"]
ft_p2_c6_a2 = fitness[f"problem_{2}"][f"coef_{6}"][f"approach_{2}"]
ft_p3_c3_a1 = fitness[f"problem_{3}"][f"coef_{3}"][f"approach_{1}"]
ft_p3_c3_a2 = fitness[f"problem_{3}"][f"coef_{3}"][f"approach_{2}"]
ft_p3_c5_a1 = fitness[f"problem_{3}"][f"coef_{5}"][f"approach_{1}"]
ft_p3_c5_a2 = fitness[f"problem_{3}"][f"coef_{5}"][f"approach_{2}"]
ft_p3_c6_a1 = fitness[f"problem_{3}"][f"coef_{6}"][f"approach_{1}"]
ft_p3_c6_a2 = fitness[f"problem_{3}"][f"coef_{6}"][f"approach_{2}"]
ft_p4_c3_a1 = fitness[f"problem_{4}"][f"coef_{3}"][f"approach_{1}"]
ft_p4_c3_a2 = fitness[f"problem_{4}"][f"coef_{3}"][f"approach_{2}"]
ft_p4_c5_a1 = fitness[f"problem_{4}"][f"coef_{5}"][f"approach_{1}"]
ft_p4_c5_a2 = fitness[f"problem_{4}"][f"coef_{5}"][f"approach_{2}"]
ft_p4_c6_a1 = fitness[f"problem_{4}"][f"coef_{6}"][f"approach_{1}"]
ft_p4_c6_a2 = fitness[f"problem_{4}"][f"coef_{6}"][f"approach_{2}"]

fitness_min_max = np.load(f"{path_base}/fitness_min_max.npy", allow_pickle=True)
median_fitness = np.load(f"{path_base}/median_fitness.npy", allow_pickle=True)

"""## Função de Plot"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
def plot_fitness_analise():
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)

  fig.suptitle("Problema 1")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p1_c3_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p1_c3_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p1_c5_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p1_c5_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p1_c6_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p1_c6_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 2")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p2_c3_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p2_c3_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p2_c5_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p2_c5_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p2_c6_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p2_c6_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################

  
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 3")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p3_c3_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p3_c3_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p3_c5_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p3_c5_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p3_c6_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p3_c6_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 4")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p4_c3_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p4_c3_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p4_c5_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p4_c5_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p4_c6_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p4_c6_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
"""#..."""

"""## Função de Plot"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
def plot_fitness_analise():
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)

  fig.suptitle("Problema 1")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p1_c3_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p1_c3_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p1_c5_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p1_c5_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p1_c6_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p1_c6_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 2")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p2_c3_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p2_c3_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p2_c5_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p2_c5_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p2_c6_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p2_c6_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################

  
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 3")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p3_c3_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p3_c3_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p3_c5_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p3_c5_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p3_c6_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p3_c6_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 4")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p4_c3_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p4_c3_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p4_c5_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p4_c5_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p4_c6_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p4_c6_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
"""#..."""

"""## Função de Plot"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
def plot_fitness_analise():
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)

  fig.suptitle("Problema 1")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p1_c3_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p1_c3_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p1_c5_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p1_c5_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p1_c6_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p1_c6_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 2")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p2_c3_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p2_c3_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p2_c5_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p2_c5_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p2_c6_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p2_c6_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################

  
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 3")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p3_c3_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p3_c3_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p3_c5_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p3_c5_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p3_c6_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p3_c6_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 4")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p4_c3_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p4_c3_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p4_c5_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p4_c5_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p4_c6_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p4_c6_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
"""#..."""

"""## Função de Plot"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
def plot_fitness_analise():
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)

  fig.suptitle("Problema 1")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p1_c3_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p1_c3_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p1_c5_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p1_c5_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p1_c6_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p1_c6_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 2")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p2_c3_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p2_c3_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p2_c5_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p2_c5_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p2_c6_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p2_c6_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################

  
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 3")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p3_c3_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p3_c3_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p3_c5_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p3_c5_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p3_c6_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p3_c6_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 4")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p4_c3_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p4_c3_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p4_c5_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p4_c5_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p4_c6_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p4_c6_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
"""#..."""

"""## Função de Plot"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
def plot_fitness_analise():
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)

  fig.suptitle("Problema 1")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p1_c3_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p1_c3_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p1_c5_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p1_c5_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p1_c6_a1, bins=limits_p1, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p1_c6_a2, bins=limits_p1, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 2")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p2_c3_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p2_c3_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p2_c5_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p2_c5_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p2_c6_a1, bins=limits_p2, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p2_c6_a2, bins=limits_p2, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################

  
  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 3")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p3_c3_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p3_c3_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p3_c5_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p3_c5_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p3_c6_a1, bins=limits_p3, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p3_c6_a2, bins=limits_p3, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
  ######################################


  fig = plt.figure(figsize=figsize)
  ax = fig.subplots(nrows=1, ncols=3)
  fig.suptitle("Problema 4")
  ######################################
  ax[0].title.set_text("50x50")
  ax[0].hist(ft_p4_c3_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[0].hist(ft_p4_c3_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[0].set_xlabel('Makespan')
  ax[0].set_ylabel('Frequência')
  ax[0].legend(loc='upper right')

  ax[1].title.set_text("70x70")
  ax[1].hist(ft_p4_c5_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[1].hist(ft_p4_c5_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[1].set_xlabel('Makespan')
  ax[1].set_ylabel('Frequência')
  ax[1].legend(loc='upper right')

  ax[2].title.set_text("90x90")
  ax[2].hist(ft_p4_c6_a1, bins=limits_p4, alpha=alpha_back,  color=color_back,  rwidth=largura_bar_back,  label=label_back)
  ax[2].hist(ft_p4_c6_a2, bins=limits_p4, alpha=alpha_front, color=color_front, rwidth=largura_bar_front, label=label_front, edgecolor=edgecolor_front)
  ax[2].set_xlabel('Makespan')
  ax[2].set_ylabel('Frequência')
  ax[2].legend(loc='upper right')
  ######################################
  plt.show()
"""#..."""

"""# Parametros e plotagem"""
limits_p1            = np.arange(9,15)
limits_p2            = np.arange(10,23)
limits_p3            = np.arange(6,19)
limits_p4            = np.arange(15,29)
figsize           = (15,4)
label_back        = "Approach 1"
label_front       = "Approach 2"
largura_bar_back  = 1.0
largura_bar_front = 0.5
edgecolor_front   = "black"
color_back        = "red"
color_front       = "blue"
alpha_back        = 1
alpha_front       = 0.7

plot_fitness_analise()

