#import random
import numpy as np

""" Class that represent the enconding of Solution Space """
class Encode:

    """ Init the class that represent the enconding of problem """
    def __init__(self, solution_space_size, process_times, quant_operations_per_jobs):
        self.solution_space_size        = solution_space_size
        self.process_times              = process_times
        self.quant_operations_per_jobs  = quant_operations_per_jobs

        self.quant_of_jobs = len(quant_operations_per_jobs)

        self.quant_of_machines = process_times.shape[1]
        self.half_of_scheduling = process_times.shape[0]

        self.solution_size = self.half_of_scheduling * 2
    #

    """ Return a list with all operations, represented by number of his job """
    def ordened_operations(self):
        operations = []
        for jb, op in enumerate(self.quant_operations_per_jobs):
            for _ in range(op):
                operations.append(jb+1)
        #

        return operations
    #

    """ Method to create a random solution space """
    def generate_solution_space(self):
        """ Inicializa uma lista vazia para o agendamento das maquinas e das operações """
        """ Importante tomar cuidado com inicializar como 0 ou empty por isso influencia no resultado final por lixo de memoria """
        range_of_machines = range(1, self.quant_of_machines+1)
        matrix_dimensions = (self.solution_space_size, self.half_of_scheduling)
        machines_scheduling   = np.random.choice(range_of_machines, matrix_dimensions)
        operations_scheduling = np.random.choice(range_of_machines, matrix_dimensions)

        """ Faz uma shallow copy da lista de operações """
        operations = np.copy(self.ordened_operations())

        """ Percore cada solução do espaço de soluções """
        for solution_i in range(self.solution_space_size):

            """ Randomiza a lista de operações """
            np.random.shuffle(operations)

            """ Faz uma shallow copy das operações para esse agendamento """
            operations_scheduling[solution_i] = np.copy(operations)

            """ Inicia as listas de jobs e de maquinas, ambas vazias """
            jobs_list       = np.arange(self.quant_of_jobs)
            machines_list   = np.zeros(self.quant_of_machines, dtype=int)

            """ Itera uma vez para cada job """
            for _ in range(self.quant_of_jobs):

                """ Escolhe um Job aleatoriamente """
                job_num = np.random.choice(jobs_list)

                """ Indice de inicio e fim nas operações desse job """
                index_of_start_operation = sum(self.quant_operations_per_jobs[:job_num])
                index_of_end_operation = index_of_start_operation + self.quant_operations_per_jobs[job_num]

                """ Percorre todas as operações desse job """
                for operation in range(index_of_start_operation, index_of_end_operation):

                    """ Lista temporaria de cargas de trabalho """
                    load = []
                    for (process_time, machine_load) in zip(self.process_times[operation], machines_list):
                        if process_time != -1:
                            load.append(process_time + machine_load)
                    #

                    """ Lista temporaria de indice de carga de trabalho """
                    load_indexes = []
                    for (index, process_time) in enumerate(self.process_times[operation]):
                        if process_time != -1:
                            load_indexes.append(index)
                    #

                    """ Indices da maquina e da carga com menor carga de trabalho """
                    less_busy_machine_index = np.argmin(load)
                    less_busy_load_index = load_indexes[less_busy_machine_index]

                    """ Grava na lista de agendamento de maquinas a maquina com menor carga de trabalho """
                    machines_scheduling[solution_i][operation] = less_busy_machine_index+1

                    """ Grava a carga na lista de maquinas """
                    machines_list[less_busy_load_index] = load[less_busy_machine_index]
                #

                """ Exclui esse job excolhido da lista de jobs """
                np.delete(jobs_list, job_num)
            #

        #

        solution_space = np.hstack((machines_scheduling, operations_scheduling))
        return solution_space
    #

    """ Method that create and return a random solution space """
    def initialize_solution_space(self):
        random_solution_space = self.generate_solution_space()

        dimension_size = int(np.sqrt(self.solution_space_size))
        solution_space_shape = (dimension_size, dimension_size, self.solution_size)

        solution_space = random_solution_space.reshape(solution_space_shape)

        return solution_space
    #