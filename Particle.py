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
    def __init__(self, solution_space_size, solution_space, decoder, generate_random = False):
        self.position = None
        self.velocity = None
        self.direction = None
        self.p_best = None
        self.p_best_fitness = None
        self.value = None
        self.fitness = None
        self.last_position = None
        self.solution_space_size = solution_space_size
        self.solution_space_limit = solution_space.shape[0]

        if generate_random:
            self.fill_with_random_values(self.solution_space_limit, solution_space, decoder)
    #

    """
    Preenche a particula com valores aleatorios
    """
    def fill_with_random_values(self, solution_space_limit, solution_space, decoder):
        """ Começa em 1 e deduz 1 do limite para ele não ir parar nas bordas e não conseguir movimentar """
        self.position = np.array(random.sample(range(1, solution_space_limit - 1), 2))

        """ Sorteia aleatoriamente uma possição anterior """
        """ Se for '+1' vai criar um vetor de movimento para a frente """
        """ Se for '-1' vai criar um vetor de movimento para a traz """
        self.last_position = self.position + 1 if random.choice([True, False]) else self.position - 1

        self.velocity = random.uniform(1.0, 2.0) # Todo - jogar no hyper parametro

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

        print("Stop!")

        p_best_vector   = np.array([self.p_best[0],  self.p_best[1]  ])
        g_best_vector   = np.array([g_best[0],       g_best[1]       ])

        median_best_vector = ((p_best_vector + g_best_vector)/2)

        innitial_position = np.array([x_position, y_position])
        inertia_vector = (innitial_position * velocity)

        """ Deduz a possição inicial para ele setar o calculo com base no zero do vetor """
        """ E então soma a innercia e obtem a posição final """
        final_vector = (median_best_vector - innitial_position) + (inertia_vector /2)

        print("Stop!")

        if final_vector is not None:
            new_x_position = final_vector[0]
            new_y_position = final_vector[1]

            """ Validações para caso seja numero negativo (tenha ido para fora do mapa) """
            if new_x_position < 0:
                new_x_position = 0
            #
            if new_y_position < 0:
                new_y_position = 0
            #

            """ Validação para caso seja maior que o limite matrix (tenha ido para fora do mapa) """
            if new_x_position >= self.solution_space_limit:
                new_x_position = self.solution_space_limit - 1
            #
            if new_y_position >= self.solution_space_limit:
                new_y_position = self.solution_space_limit - 1
            #

            self.position = [int(new_x_position), int(new_y_position)]

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
