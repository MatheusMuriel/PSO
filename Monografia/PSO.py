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
    def execute(self):
        #print("Inicio da iteração do PSO")
        positions_history = []
        #while self.stop_condition():
        for _ in range(0, 10):
            positions_history.append([p.position for p in self.population])

            for particula in self.population:

                """ Atualiza a posisão do particula """
                particula.update_position(self.g_best)

                """ Atualiza o seu fitness e seu p_best """
                particula.evaluate_value(self.solution_space, self.decoder)

                """ Caso seja melhor, atualiza o g_best """
                if particula.fitness < self.g_best_fitness:
                    self.g_best = particula.position
                    self.g_best_fitness = particula.fitness
                #
            #
        #
        positions_history.append([p.position for p in self.population])

        #print("Fim da iteração do PSO")

        #return self.g_best
        return positions_history

        return (self.g_best, positions_history)
    #

    """
    Função que descide se já atingiu a condição de parada
    :return Um Booleano com True caso a condição de parada tenha sido atingida
    """
    def stop_condition(self):
        if self.contador < 50:
            return True
        else:
            self.contador += 1
            return False
    #