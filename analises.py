import matplotlib.pyplot as plt
import numpy as np
import copy

from Particle import Particle
from ReadData import Input
from Encode import Encode
from ClassesToAnalise.Decode2 import Decode
from PSO import PSO

from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from matplotlib import animation
""" Hyperparans for solutions """
hyper_params = {
  "coeficente_populacional": 5,
  "population_size" : 30,
  "velocity_limit" : 2.0
}
IS_TESTE            = True
PLOT_3D             = True
ANIMATED_POSITIONS  = True
class FJSP():
  """ Inicia o ambiente para os testes das diversas soluções """
  def __init__(self):
    self.process_times = []
    self.quant_operations_per_jobs = []

    self.quant_of_jobs = 0
    self.quant_of_operations = []
    self.quant_of_machines = []

    self.solution_space_size = 0
    self.solution_space = None

    self.encode = None
    self.decode = None

    self.coeficente_populacional = hyper_params["coeficente_populacional"]
    self.population_size         = hyper_params["population_size"]
    self.population = []
    self.g_best = None
    self.g_best_fitness = None

    self.start_environment()
  #

  """ Inicia o ambiente para os testes das diversas soluções """
  def start_environment(self):
    """ Pega o arquivo com o problema """
    #file_path = './Data/2_Kacem/Kacem4.fjs'
    file_path = './Data/1_Brandimarte/BrandimarteMk1.fjs'
    input = Input(file_path)
    input_matrix_tuple = input.getMatrix()

    """ process_times: Matriz com os tempos de processamentos """
    self.process_times = input_matrix_tuple[0]

    """ quant_operations_per_jobs: Lista com o número de operações de cada job """
    self.quant_operations_per_jobs = input_matrix_tuple[1]

    """ Gerar população inicial """
    self.quant_of_jobs          = len(self.quant_operations_per_jobs)
    self.quant_of_operations    = self.process_times.shape[0]
    self.quant_of_machines      = self.process_times.shape[1]

    """ Calcula o tamanho do espaço de soluçoes """
    #self.solution_space_size = self.population_size ** 2
    self.solution_space_size = 900

    """ Inicia as classes de encode e decode para serem usados no problema """
    self.encode = Encode(self.solution_space_size,       self.process_times, self.quant_operations_per_jobs)
    self.decode = Decode(self.quant_operations_per_jobs, self.process_times)

    """ Inicia o espaço de soluções """
    self.solution_space = self.encode.initialize_solution_space()

    """ Iniciar a população e define o g_best """
    for _ in range(self.population_size):
      particle = Particle(self.solution_space_size, self.solution_space, self.decode, hyper_params, generate_random=True)
      self.population.append(particle)

      if (self.g_best_fitness is None) or (particle.fitness < self.g_best_fitness):
        self.g_best_fitness = particle.fitness
        self.g_best         = particle.position
      #
    #

    if IS_TESTE:
      self.plot_solution_space()
  #

  """ Executa e salva os resultados dos varios algoritmos """
  def execute_algorithmns(self):
    self.execute_direct_solution()
  #

  """ Teste com uma solução direta """
  def execute_direct_solution(self):
    positions_history = []
    for _ in range(0, 10):
      """ Salva a posição """
      positions = [p.position for p in self.population]
      positions.append(self.g_best)
      print(self.g_best)
      positions_history.append(positions)

      """ Percorre todas as particulas """
      for particula in self.population:
        """ Atualiza a posisão do particula """
        particula.update_position(self.g_best)

        """ Atualiza o seu fitness e seu p_best """
        particula.evaluate_value(self.solution_space, self.decode)

        """ Caso seja melhor, atualiza o g_best """
        if particula.fitness < self.g_best_fitness:
          self.g_best = particula.position
          self.g_best_fitness = particula.fitness
        #

        pass
      #

      pass
    #

    if not PLOT_3D:
      for pos in positions_history:
        x_coordinates = [x[0] for x in pos]
        y_coordinates = [x[1] for x in pos]
        plt.scatter(x_coordinates, y_coordinates)
        plt.show()
    #

    if ANIMATED_POSITIONS:
      self.animated_plot(positions_history)
    #

    self.save_list(positions_history)
    return positions_history
  #

  """ Plot a surface plot of fitness of solution space """
  def plot_solution_space(self):
    if PLOT_3D:
      import matplotlib;
      matplotlib.use("TkAgg")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xx = np.arange(0, self.population_size)
    yy = np.arange(0, self.population_size)

    X, Y = np.meshgrid(xx, yy)
    """ Make a list with fitness of all intens of solutions space """
    Z = np.array([[self.decode.decode(ss) for ss in s] for s in self.solution_space])

    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, rcount=800, ccount=800)
    ax.set_zlabel('Fitness')
    fig.suptitle('Fitness of Solution Space', fontsize=20)
    plt.show()
  #

  def animated_plot(self, hist):
    import matplotlib;
    matplotlib.use("TkAgg")
    def update(i):
      scat.set_offsets(hist[i])
      scat.set_array(colors)
      return scat,
    colors = np.ones(len(hist[0]))
    colors[len(colors) - 1] = 3
    fig, ax = plt.subplots()
    ax.set_xlim((0, np.max(hist[0]) + 3))
    ax.set_ylim((0, np.max(hist[0]) + 3))
    scat = ax.scatter([], [])
    ani = animation.FuncAnimation(fig, update, frames=len(hist), interval=1000, blit=True)
    plt.show()
    pass
  #

  def save_list(self, list_to_save):
    textfile = open("a_file.txt", "w")

    textfile.write("positions_history = [")
    for rodada in list_to_save:
      gbest=True
      textfile.write("[")
      for particula in rodada:
        textfile.write("[")
        textfile.write(str(particula[0]) + "," + str(particula[1]))
        textfile.write("],")
      #
      textfile.write("],\n")
    #
    textfile.write("]")

    textfile.close()
    pass
  #
#

if __name__ == '__main__':
  FJSP = FJSP()
  #FJSP.animated_plot()
  FJSP.execute_algorithmns()

  """interations = 1
  for i in range(interations):
    results = [FJSP]

    fitness_list = [result[1] for result in results]
    best_fitness_index = np.argmax(np.array(fitness_list))

    scheduling_list = [result[0] for result in results]
    scheduling = scheduling_list[best_fitness_index]

    Decode.decode(scheduling, plot_scheduling=True)
  ###"""
#