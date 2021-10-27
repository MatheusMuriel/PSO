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
        self.limit_of_solution_space = limit_of_solution_space

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
        self.p_best = self.position
    #

    """
    Atualiza a posição, velocidade e inercia da particula.
    Chamado pela iteração do PSO
    """
    def update_position(self, g_best):
        x_position = self.position[0]
        y_position = self.position[1]
        velocity = self.velocity
        direction = self.direction

        # Todo - Por a declaração disso em outro lugar
        """
        Lambdas functions que definem a logica de movimentos na matrix 2d
        x: x position
        y: y position
        v: velocidade de movimento
        "*" é um operador que faz o unpack da tupla para parametros de função
        """
        up_movement         = lambda x, y, v: (x, y-v, v)
        down_movement       = lambda x, y, v: (x, y+v, v)
        left_movement       = lambda x, y, v: (x-v, y, v)
        right_movement      = lambda x, y, v: (x+v, y, v)
        up_left_movement    = lambda x, y, v: up_movement(*left_movement(x, y, v))
        up_right_movement   = lambda x, y, v: up_movement(*right_movement(x, y, v))
        down_left_movement  = lambda x, y, v: down_movement(*left_movement(x, y, v))
        down_right_movement = lambda x, y, v: down_movement(*right_movement(x, y, v))


        """ Direciona para qual movimento vais er executado """
        if direction == Positions.UP:
            new_position = up_movement(x_position, y_position, velocity)
        elif direction == Positions.DOWN:
            new_position = down_movement(x_position, y_position, velocity)
        elif direction == Positions.LEFT:
            new_position = left_movement(x_position, y_position, velocity)
        elif direction == Positions.RIGHT:
            new_position = right_movement(x_position, y_position, velocity)
        elif direction == Positions.UP_LEFT:
            new_position = up_left_movement(x_position, y_position, velocity)
        elif direction == Positions.UP_RIGHT:
            new_position = up_right_movement(x_position, y_position, velocity)
        elif direction == Positions.DOWN_LEFT:
            new_position = down_left_movement(x_position, y_position, velocity)
        elif direction == Positions.DOWN_RIGHT:
            new_position = down_right_movement(x_position, y_position, velocity)
        #

        if new_position is not None:
            new_x_position = new_position[0]
            new_y_position = new_position[1]

            """ Validações para caso seja numero negativo (tenha ido para fora do mapa) """
            if new_x_position < 0:
                new_x_position = 0
            #
            if new_y_position < 0:
                new_y_position = 0
            #

            """ Validação para caso seja maior que o limite matrix (tenha ido para fora do mapa) """
            if new_x_position >= self.limit_of_solution_space:
                new_x_position = self.limit_of_solution_space - 1
            #
            if new_y_position >= self.limit_of_solution_space:
                new_y_position = self.limit_of_solution_space - 1
            #

            self.position = (new_x_position, new_y_position)

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
            self.p_best = self.position
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
