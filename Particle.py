import Decode as Decode
import numpy as np
import random

from enum import Enum

"""
Classe que representa e gerencia a entidade de uma particula
"""
class Particle:

    """
    Inicia a entidade da particula
    Caso generate_random seja True, chama o preenchedor de valores aleatorios
    """
    def __init__(self, limit_of_solution_space, solution_space, decoder, generate_random = False):
        self.position = None
        self.velocity = None
        self.direction = None
        self.p_best = None
        self.p_best_fitness = None
        self.value = None
        self.fitness = None

        if generate_random:
            self.fill_with_random_values(limit_of_solution_space, solution_space, decoder)
    #

    """
    Preenche a particula com valores aleatorios
    """
    def fill_with_random_values(self, limit_of_solution_space, solution_space, decoder):
        self.position = random.sample(range(0,limit_of_solution_space), 2)
        self.direction = Positions(random.choice(range(1,9)))
        self.velocity = random.choice(range(1, 9))
        self.evaluate_value(solution_space, decoder)
        self.p_best = self.value
    #

    """
    Atualiza a posição, velocidade e inercia da particula.
    Chamado pela iteração do PSO
    """
    def update_position(self, g_best):

        pass
    #

    """
    Calcula e atualiza os valores de posição, fitness e p_best da particula 
    """
    def evaluate_value(self, solution_space, decoder):
        self.value = solution_space[self.position[0], self.position[1]]
        fitness = decoder.decode(self.value)
        self.fitness = fitness

        if (self.p_best_fitness is None) or (fitness < self.p_best_fitness):
            self.p_best_fitness = fitness
            self.p_best = self.value
    #

class Positions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8
