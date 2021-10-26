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

        #while self.stop_condition():
        for _ in range(0,1):
            # Avalia a população antes ou dps do evaluete?
            for particula in self.population:
                #print(particula)
                particula.evaluate_value(self.solution_space, self.decoder)

                # Atualização do g_best
                if particula.fitness < self.g_best_fitness:
                    self.g_best = particula.position
                    self.g_best_fitness = particula.fitness



        #print("Fim da iteração do PSO")

        return self.g_best
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