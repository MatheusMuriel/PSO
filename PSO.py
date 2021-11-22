import numpy as np

"""
Classe que controla o algoritmo PSO
"""
class PSO:

    """
    Inicia e define os parametros para o PSO
    """
    def __init__(self, population, solution_space, g_best, g_best_fitness, decoder):
        self.population         = population
        self.solution_space     = solution_space
        self.g_best             = g_best
        self.g_best_fitness     = g_best_fitness
        self.decoder            = decoder

        self.contador = 0

    """
    Executa o algoritmo PSO
    :return A melhor posição encontrada (g_best)
    """
    def execute(self, aprout, exec):
        positions_history = []
        g_best_count = 0
        g_best_changes = 0

        solutioned = False
        while not solutioned:
            g_best_changed = False
            positions = [p.position for p in self.population]
            positions.append(self.g_best)
            positions_history.append(positions)
            for particula in self.population:
                particula.update_position(self.g_best, g_best_count, aprout)
                particula.evaluate_value(self.solution_space, self.decode)
                if particula.fitness < self.g_best_fitness:
                    self.g_best = particula.position
                    self.g_best_fitness = particula.fitness
                    g_best_changed = True
                #
            #
            if g_best_changed:
                g_best_count = 0
                g_best_changes += 1
            else:
                g_best_count += 1
            #

            if g_best_count > 50:
                solutioned = True
            pass
        #

        if SAVE_POPULATION_HISTORY:
            self.save_population_history(positions_history, aprout, exec)
        #

        solution = self.solution_space[self.g_best[0], self.g_best[1]]
        self.save_solution(self.g_best, self.g_best_fitness, solution, aprout, exec)
    #

    def save_population_history(self, population_history,aprout, exec):
        if not os.path.exists(self.path_to_save):
           os.makedirs(self.path_to_save)
        np.save(f'{self.path_to_save}/particles_positions_history{aprout}_exec{exec}.npy', population_history)
    #

    def save_solution(self, gbest, fitness, solution, aprout, exec):
        if not os.path.exists(self.path_to_save):
            os.makedirs(self.path_to_save)
        #

        np.save(f'{self.path_to_save}/gbest_aprout{aprout}_exec{exec}.npy', gbest)
        np.save(f'{self.path_to_save}/fitness_aprout{aprout}_exec{exec}.npy', fitness)
        np.save(f'{self.path_to_save}/solution_aprout{aprout}_exec{exec}.npy', solution)
    #