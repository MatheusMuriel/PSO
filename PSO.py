import numpy as np

"""
Classe que controla o algoritmo PSO
"""
class PSO:

    """
    Inicia e define os parametros para o PSO
    """
    def __init__(self, population, solution_space, g_best, g_best_fitness):
        self.population         = population
        self.solution_space     = solution_space
        self.g_best             = g_best
        self.g_best_fitness     = g_best_fitness

        self.contador = 0

    """
    Executa o algoritmo PSO
    """
    def execute(self):
        print("Inicio da iteração do PSO")

        while self.stop_condition():
            # Avalia a população antes ou dps do evaluete?
            for particula in self.population:
                print(particula)

            print(f"While {self.contador}")

            # Atualização do g_best

        print("Fim da iteração do PSO")

        pass
    #

    """
    Função que descide se já atingiu a condição de parada
    :return Um Booleano com True caso a condição de parada tenha sido atingida
    """
    def stop_condition(self):
        if self.contador >= 50:
            return True

        self.contador += 1
        return False

    #