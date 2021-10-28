import matplotlib.pyplot as plt
import numpy as np
import copy

from Particle import Particle
from ReadData import Input
from Encode import Encode
from Decode import Decode
from PSO import PSO

from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

""" Hyperparans for solutions """
hyper_params = {
    "coeficente_populacional": 5,
    "population_size" : 10
}

IS_TESTE = False

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
        self.population_size         = hyper_params["coeficente_populacional"]
        self.population = []
        self.g_best = None
        self.g_best_fitness = None

        #self.fig = plt.figure(figsize=(10, 5))
        #self.fig.suptitle('PSO - FJSP')

        self.start_environment()

    """ Inicia o ambiente para os testes das diversas soluções """
    def start_environment(self):
        """ Pega o arquivo com o problema """
        file_path = './Data/2_Kacem/Kacem1.fjs'
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
            particle = Particle(self.solution_space_size, self.solution_space, self.decode, generate_random=True)
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
        self.execute_pso_base()
        #self.execute_direct_solution()
    #

    def execute_direct_solution(self):
        """ Teste com uma solução direta """
        """..."""
        self.decode.decode(self.solution_space[4, 4], True)
        """..."""
        pass
    #

    def execute_pso_base(self):
        """ Inicia a classe do PSO """
        PSO_algorithmn = PSO(self.population, self.solution_space, self.g_best, self.g_best_fitness, self.decode)

        """ Define quantas vezes vai ser executado """
        #iterations = self.coeficente_populacional * self.quant_of_machines * self.quant_of_jobs
        iterations = 1

        for iter in range(iterations):

            # Reseta parametros

            # Executa PSO
            #PSO_result = PSO_algorithmn.execute()
            #finded_solution = self.solution_space[ PSO_result[0], PSO_result[1] ]
            #fitness = self.decode.decode(finded_solution, True, self.fig)

            # Print para debug
            #print(f"Rodada {str(iter + 1)} => Melhor fitness: {fitness}")

            # Salva na lista de soluções para analises Futuras

            positions_history = PSO_algorithmn.execute()

            for pos in positions_history:
                x_coordinates = [x[0] for x in pos]
                y_coordinates = [x[1] for x in pos]
                plt.scatter(x_coordinates, y_coordinates)
                plt.show()

            print("Stop!")
        #

        print("STOP!!!")

        """ Teste com uma solução direta """
        """...
        P = copy.deepcopy(chrs)
        fitness_list = [Decode.decode(chr, quant_operations_per_jobs, process_times, 'decode', None) for chr in P]
        Pg = P[1]
        ..."""

        #fitness = Decode.decode(Pg, quant_operations_per_jobs, process_times, 'decode',None)

        #return (scheduling, fitness)
        pass

    """ Plot a surface plot of fitness of solution space """
    def plot_solution_space(self):
        #print("Start Plot")
        #fig = plt.figure()
        ax = self.fig.add_subplot(1,2,1, projection='3d')

        xx = np.arange(0, self.population_size)
        yy = np.arange(0, self.population_size)

        X, Y = np.meshgrid(xx, yy)
        """ Make a list with fitness of all intens of solutions space """
        Z = np.array([[self.decode.decode(ss) for ss in s] for s in self.solution_space])

        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, rcount=800, ccount=800)
        ax.set_zlabel('Fitness')
        #fig.suptitle('Fitness of Solution Space', fontsize=20)
        #plt.show()
        #print("End Plot")
    #

    def finalize_plot(self):
        self.fig.tight_layout()
        plt.show()
        plt.close()
    #
#

if __name__ == '__main__':
    print("Start...")

    FJSP = FJSP()
    FJSP.execute_algorithmns()
    FJSP.finalize_plot()

    """interations = 1
    for i in range(interations):
        results = [FJSP]

        fitness_list = [result[1] for result in results]
        best_fitness_index = np.argmax(np.array(fitness_list))

        scheduling_list = [result[0] for result in results]
        scheduling = scheduling_list[best_fitness_index]

        Decode.decode(scheduling, plot_scheduling=True)
    ###"""

    print("Fim...")
#