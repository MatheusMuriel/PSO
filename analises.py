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
  #Quantidade de particulas
  "population_size" : 30,
  #Define o valor que vai multiplicar para gerar espaço de soluções
  "coeficente_populacional": 2.0,
  #Velocidade maxima de uma particula
  "velocity_limit" : 0
}

""" Variaveis de controle """
#file_path = './Data/1_Brandimarte/BrandimarteMk1.fjs'
file_path = './Data/2_Kacem/Kacem3.fjs'

PLOT_SOLUTION_SPACE = False
PLOT_3D             = False
PLOT_POSITIONS      = False
ANIMATED_POSITIONS  = True
interval_plot       = 200

SAVE_POPULATION_HISTORY = True
SAVE_SOLUTION_SPACE     = False
SAVE_ENCODER            = False
SAVE_DECODER            = False

""" Classe para formulação do problema de FJSP """
class FJSP():
  """ Inicia o ambiente para os testes das diversas soluções """
  def __init__(self):
    self.process_times = []
    self.quant_operations_per_jobs = []

    self.quant_of_jobs = 0
    self.quant_of_operations = []
    self.quant_of_machines = []

    self.solution_space_size = 0
    self.solution_space_array_dimension = 0
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
    #file_path = './Data/2_Kacem/Kacem1.fjs'
    #file_path = './Data/1_Brandimarte/BrandimarteMk1.fjs'
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
    quantion_of_solutions = np.round(self.population_size ** self.coeficente_populacional)
    """ Faz um round da raiz para pegar a raiz quadrada perfeita mais proxima """
    self.solution_space_array_dimension = int(np.round(np.sqrt(quantion_of_solutions)))
    self.solution_space_size = self.solution_space_array_dimension ** 2
    print(f"Tamanho do espaço de soluções: {self.solution_space_size}")

    """ Inicia as classes de encode e decode para serem usados no problema """
    self.encode = Encode(self.solution_space_size,       self.process_times, self.quant_operations_per_jobs)
    self.decode = Decode(self.quant_operations_per_jobs, self.process_times)

    if SAVE_ENCODER:
      self.save_encoder_data(self.encode)
    #
    if SAVE_DECODER:
      self.save_decoder_data(self.decode)
    #

    """ Inicia o espaço de soluções """
    self.solution_space = self.encode.initialize_solution_space()
    if SAVE_SOLUTION_SPACE:
      self.save_solution_space(self.solution_space)
    #

    if PLOT_SOLUTION_SPACE:
      self.plot_solution_space()
    #

    """ Iniciar a população e define o g_best """
    for _ in range(self.population_size):
      particle = Particle(self.solution_space_size, self.solution_space, self.decode, hyper_params, generate_random=True)
      self.population.append(particle)

      if (self.g_best_fitness is None) or (particle.fitness < self.g_best_fitness):
        self.g_best_fitness = particle.fitness
        self.g_best         = particle.position
      #
    #

    pass
  #

  """ Executa e salva os resultados dos varios algoritmos """
  def execute_algorithmns(self):
    self.execute_direct_solution()
    pass
  #

  """ Teste com uma solução direta """
  def execute_direct_solution(self):
    print("Start Calc")
    positions_history = []
    g_best_count = 0

    solutioned = False
    #for _ in range(0, 20):
    while not solutioned:
      g_best_changed = False
      #print(g_best_count)
      """ Salva a posição """
      positions = [p.position for p in self.population]
      positions.append(self.g_best)
      #print(self.g_best)
      positions_history.append(positions)
      #print("::::::::::::::::::::::::::::::::::::")
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
          g_best_changed = True
        #
      #
      if g_best_changed:
        print("Changed!!")
        print(g_best_count)
        g_best_count = 0
      else:
        g_best_count += 1
      #

      if g_best_count > 50:
        solutioned = True
      pass
    #

    if PLOT_POSITIONS and (not PLOT_3D):
      for pos in positions_history:
        x_coordinates = [x[0] for x in pos]
        y_coordinates = [x[1] for x in pos]
        plt.scatter(x_coordinates, y_coordinates)
        plt.show()
    #

    if SAVE_POPULATION_HISTORY:
      self.save_population_history(positions_history)
    #


    if ANIMATED_POSITIONS:
      self.animated_plot(positions_history)
    #

    #self.save_list(positions_history)
    return positions_history
  #

  """ Plot a surface plot of fitness of solution space """
  def plot_solution_space(self):
    if PLOT_3D:
      import matplotlib;
      matplotlib.use("TkAgg")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #self.solution_space_size

    xx = np.arange(0, self.solution_space_array_dimension)
    yy = np.arange(0, self.solution_space_array_dimension)

    X, Y = np.meshgrid(xx, yy)
    """ Make a list with fitness of all intens of solutions space """
    Z = np.array([[self.decode.decode(ss) for ss in s] for s in self.solution_space])

    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, rcount=800, ccount=800)
    ax.set_zlabel('Fitness')
    fig.suptitle('Fitness of Solution Space', fontsize=20)
    plt.show()
  #

  def animated_plot(self, positions_history):
    import matplotlib;
    matplotlib.use("TkAgg")

    def update(i):
      scat.set_offsets(positions_history[i])
      scat.set_array(colors)
      txt_title.set_text(f"Interação: {str(i)}")
      return scat,

    colors = np.ones(len(positions_history[0]))
    colors[len(colors) - 1] = 3

    fig, ax = plt.subplots()
    ax.set_xlim((0, np.max(positions_history[0]) + 3))
    ax.set_ylim((0, np.max(positions_history[0]) + 3))
    scat = ax.scatter([], [])
    txt_title = ax.set_title("Interação: 0")
    ani = animation.FuncAnimation(fig, update, frames=len(positions_history), interval=interval_plot, blit=False)
    plt.show()
    pass
  #

  def save_population_history(self, population_history):
    np.save('executions_data\particles_positions_history.npy', population_history)
  #

  def save_solution_space(self, solution_space):
    np.save('executions_data\solution_space.npy', solution_space)
  #

  def save_encoder_data(self, encoder):
    np.save("executions_data/encoder_process_times.npy", encoder.process_times) # TODO adicionar numero de execução
    textfile = open("executions_data/encoder_data.txt", "w")
    textfile.write("encoder_data = {\n")
    textfile.write(f"\t\"solution_space_size\"       : {encoder.solution_space_size},\n")
    textfile.write(f"\t\"quant_operations_per_jobs\" : {encoder.quant_operations_per_jobs},\n")
    textfile.write(f"\t\"quant_of_jobs\"             : {encoder.quant_of_jobs},\n")
    textfile.write(f"\t\"quant_of_machines\"         : {encoder.quant_of_machines},\n")
    textfile.write(f"\t\"half_of_scheduling\"        : {encoder.half_of_scheduling},\n")
    textfile.write(f"\t\"solution_size\"             : {encoder.solution_size},\n")
    textfile.write(f"\t\"process_times\"             : np.load(\"encoder_process_times.npy\")\n")  # TODO adicionar numero de execução
    textfile.write("}")
    textfile.close()
    pass
  #

  def save_decoder_data(self, decoder):
    np.save("executions_data/decoder_process_times.npy", decoder.process_times) # TODO adicionar numero de execução
    textfile = open("executions_data/decoder_data.txt", "w")
    textfile.write("decoder_data = {\n")
    textfile.write(f"\t\"quant_of_jobs\":             {decoder.quant_of_jobs},\n")
    textfile.write(f"\t\"quant_of_machines\":         {decoder.quant_of_machines},\n")
    textfile.write(f"\t\"quant_operations_per_jobs\": {decoder.quant_operations_per_jobs},\n")
    textfile.write(f"\t\"max_of_operations\":         {decoder.max_of_operations},\n")
    textfile.write(f"\t\"half_of_scheduling\":        {decoder.half_of_scheduling},\n")
    textfile.write(f"\t\"process_times\":             np.load(\"decoder_process_times.npy\")\n") #TODO adicionar numero de execução
    textfile.write("}")
    textfile.close()
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