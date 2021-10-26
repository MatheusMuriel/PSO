import os
import numpy as np
import matplotlib.pyplot as plt

class Decode:

    def __init__(self, quant_operations_per_jobs, process_times):
        self.quant_operations_per_jobs = quant_operations_per_jobs
        self.process_times = process_times
        self.quant_of_jobs = len(quant_operations_per_jobs)
        self.quant_of_machines = process_times.shape[1]
        self.half_of_scheduling = process_times.shape[0]
        self.max_of_operations = np.max(quant_operations_per_jobs)

    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.barh.html
    def draw_gatt(self, start_time, end_time, fig):
        colors = {0:'red', 1:'blue', 2:'yellow', 3:'orange', 4:'green'}

        ax = fig.add_subplot(1, 2, 2)

        # i = Machine_index ; j = Operation_index
        for i in range( self.quant_of_machines ): # Vai de linha em linha do plot (começando do 0)
            for j in range( self.half_of_scheduling ):
                current_start_time      = start_time[i][j]
                current_end_time        = end_time[i][j]
                current_diference_time  = current_end_time - current_start_time
                #if current_diference_time > 0:
                if end_time[i][j] != 0 and end_time[i][j] - start_time[i][j] != 0:
                    operation = self.find_machine_of_a_operation(j)
                    bar_width = current_diference_time
                    bar_left = current_start_time
                    bar_color = colors[operation[0] - 1]
                    #bar_str = operation[0] # Somente o numero do Job
                    bar_str = operation     # Numero do Job e da Operação

                    ax.barh(y=i, width=bar_width, height=0.5, left=bar_left, color=bar_color, edgecolor='black')
                    ax.text(x=bar_left + 0.1, y=i, s=bar_str, fontsize=8)

        #ax.yticks(np.arange(i + 1), np.arange(1, i + 2))

        #self.save_plot_image(plt)
    #

    # Função para salvar a image de um plot em um arquivo
    def save_plot_image(self, plt):
        path = './BestFitness/BrandimarteMk1/'
        if not os.path.exists(path):
            os.makedirs(path)

        img_path = path + 'best_fitness.png'
        if os.path.exists(img_path):
            os.remove(img_path)

        plt.savefig(img_path)

    # Encontrar o indice de uma operação em uma máquina
    def find_one_operation_in_a_machine(self, i, j):
        if i == 1:
            op_index = j - 1
        else:
            op_index = sum(self.quant_operations_per_jobs[:i - 1]) + j - 1

        return op_index

    # Dado o índice de uma operação, descobre qual em qual maquina está
    """ retorna uma tupla (maquina, operação) """
    def find_machine_of_a_operation(self, operation_index):
        job_op_list = [
            (i + 1, j + 1) for i in range( self.quant_of_jobs ) for j in range(self.quant_operations_per_jobs[i])
        ]
        job_op = job_op_list[operation_index]
        return job_op
    #

    # Decode a Scheduling and return the Fitness
    def decode(self, scheduling, plot_scheduling=False, fig=None):
        machines_matrix = np.zeros((self.quant_of_jobs, self.max_of_operations), dtype=int)
        times_matrix    = np.zeros((self.quant_of_jobs, self.max_of_operations), dtype=int)

        machines_scheduling   = scheduling[:self.half_of_scheduling]
        operations_scheduling = scheduling[self.half_of_scheduling:]

        operation_index = 0
        for i in range( self.quant_of_jobs ):
            for j in range( self.quant_operations_per_jobs[i] ):
                count = 0
                process_time = self.process_times[operation_index]

                # Todo for-each with index
                for index in range( len(process_time) ):
                    if process_time[index] != -1:
                        count+=1

                    if count == machines_scheduling[operation_index]:
                        machines_matrix[i][j] = index+1
                        times_matrix[i][j]  = process_time[index]
                        break

                # Todo Remove
                #if count < machine_scheduling[operation_index]:
                #    print("false")

                operation_index+=1

        #print(machines_matrix)
        #print(times_matrix)

        start_time = np.zeros(
            (self.quant_of_machines, self.half_of_scheduling),
            dtype=int
        )

        end_time = np.zeros(
            (self.quant_of_machines, self.half_of_scheduling),
            dtype=int
        )

        op_count_dict = {}
        machine_operations = np.zeros(self.quant_of_machines, dtype=int)

        for os in operations_scheduling:
            if os in op_count_dict:
                op_count_dict[os] += 1
            else:
                op_count_dict[os] = 1
            #

            operation_count = op_count_dict[os]
            operation_index = self.find_one_operation_in_a_machine(os, operation_count)

            machine_number     = machines_matrix[os-1][operation_count-1]
            pro_time           = times_matrix [os-1][operation_count-1]

            machine_operation  = machine_operations[machine_number-1]
            current_start_time = start_time[machine_number-1][operation_index]
            current_end_time   = end_time  [machine_number-1][operation_index]

            previous_operation_index = self.find_one_operation_in_a_machine(os, operation_count - 1)
            previous_machine_number = machines_matrix[os-1][operation_count-2]

            if machine_operation == 0 and operation_count == 1 :
                current_start_time = 0
                current_end_time   = pro_time
            #

            elif machine_operation == 0 and operation_count > 1 :
                prev_m_num          = machines_matrix[os-1][operation_count-2]
                prev_end_time       = end_time[prev_m_num-1][previous_operation_index]
                current_start_time  = prev_end_time
                current_end_time    = prev_end_time + pro_time
            #

            elif machine_operation > 0:
                flag=0
                prev_end_time = 0

                if operation_count == 1 :
                    free_start = 0
                else:
                    prev_end_time = end_time[previous_machine_number-1][previous_operation_index]
                    free_start = prev_end_time
                #

                order_start_time = np.sort(start_time[machine_number-1][end_time[machine_number-1] > 0])
                order_end_time   = np.sort(end_time  [machine_number-1][end_time[machine_number-1] > 0])

                for index in range(len(order_start_time)):
                    if order_start_time[index] - free_start >= pro_time:
                        current_start_time = free_start
                        current_end_time   = free_start + pro_time
                        flag = 1
                        break
                    #

                    if order_end_time[index] - free_start >= 0:
                        free_start = order_end_time[index]
                    #
                #

                if flag == 0:
                    free_start = max(np.max(end_time[machine_number-1]), prev_end_time)
                    current_start_time = free_start
                    current_end_time   = free_start + pro_time
                #
            #

            machine_operation += 1

            machine_operations[machine_number - 1]          = machine_operation
            start_time[machine_number - 1][operation_index] = current_start_time
            end_time  [machine_number - 1][operation_index] = current_end_time
        #

        #print(scheduling)
        if plot_scheduling:
            self.draw_gatt(start_time, end_time, fig)
        #

        fitness = np.max(end_time)

        return fitness
    #
