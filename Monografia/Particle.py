import Decode as Decode
import numpy as np
import random

"""
Classe que representa e gerencia a entidade de uma particula
"""
class Particle:
    """
    Inicia a entidade da particula e chama o preenchedor de valores aleatorios
    """
    def __init__(self, solution_space_size, solution_space, decoder, hyper_params):
        self.position = None
        self.velocity = None
        self.p_best = None
        self.p_best_fitness = None
        self.value = None
        self.fitness = None
        self.last_position = None
        self.solution_space_size = solution_space_size
        self.solution_space_limit = solution_space.shape[0]
        self.velocity_limit = hyper_params["velocity_limit"]

        self.fill_with_random_values(self.solution_space_limit, solution_space, decoder)
    #

    """
    Preenche a particula com valores aleatorios
    """
    def fill_with_random_values(self, solution_space_limit, solution_space, decoder):
        """ Começa em 1 e deduz 1 do limite
        para ele não ir parar nas bordas e não conseguir movimentar """
        random_position = np.array(random.sample(range(1, solution_space_limit - 1), 2))

        """ Converte de array para list para manter o padrão de datatype da solução """
        self.position = [int(random_position[0]), int(random_position[1])]

        """ Sorteia aleatoriamente uma possição anterior """
        """ Se for '+1' vai criar um vetor de movimento para a frente """
        """ Se for '-1' vai criar um vetor de movimento para a traz """
        self.last_position = random_position + 1 if random.choice([True, False]) else random_position - 1

        """ Sorteia uma velocidade aleatoria """
        self.velocity = random.uniform(0, self.velocity_limit)

        """ Calcula a qualidade da possição """
        self.evaluate_value(solution_space, decoder)

        """ Define a posição sorteada como pBest inicial """
        self.p_best = self.position
    #

    """
    Atualiza a posição, velocidade e inercia da particula.
    Chamado pela iteração do PSO
    """
    def update_position(self, g_best, g_best_count, approach):
        p_best_vector   = np.array([self.p_best[0],  self.p_best[1]  ])
        g_best_vector   = np.array([g_best[0],       g_best[1]       ])

        """ Posição atual da particula """
        innitial_position   = np.array([self.position[0], self.position[1]])

        """ Calcula a inercia da particula """
        inertia_vector      = np.array(innitial_position + self.velocity)

        """ Calcula a media entre os vetores """
        median_best_vector = ((p_best_vector + g_best_vector) / 2)
        
        """ Soma a possição inicial para a movimentação ser com base no na posição atual """
        final_vector =  ((median_best_vector + innitial_position)) / 2
        
        if approach == 1:
            """ Abordagem padrão """
            final_vector = final_vector + (self.velocity_limit * random.random())
        elif approach == 2:
            """ Abordagem dinâmica """
            if g_best_count > 5:
                final_vector = final_vector + (self.velocity_limit * (inertia_vector * random.random()))
            else:
                final_vector = final_vector + (self.velocity_limit * random.random())
            #
        #

        if final_vector is not None:
            """ Zera caso seja um numero negativo (tenha ido para fora do mapa) """
            if final_vector[0] < 0:
                final_vector[0] = 0
            #
            if final_vector[1] < 0:
                final_vector[1] = 0
            #

            """ Tratativa para caso seja maior que o limite da matriz (tenha ido para fora do mapa) """
            if final_vector[0] >= self.solution_space_limit:
                final_vector[0] = self.solution_space_limit - 1
            #
            if final_vector[1] >= self.solution_space_limit:
                final_vector[1] = self.solution_space_limit - 1
            #

            """ Define a posição da particula"""
            self.position = [int(final_vector[0]), int(final_vector[1])]
        #
    #

    """
    Calcula e atualiza os valores de posição, fitness e p_best da particula 
    """
    def evaluate_value(self, solution_space, decoder):
        """ Pega no espaço de soluções a solução da posição atual da particula """
        self.value = solution_space[self.position[0], self.position[1]]

        """ Calcula o fitness da posição atual """
        self.fitness = decoder.decode(self.value)

        """ Caso seja melhor atualiza o pBest """
        if (self.p_best_fitness is None) or (fitness < self.p_best_fitness):
            self.p_best_fitness = fitness
            self.p_best = self.position
        #
    #
