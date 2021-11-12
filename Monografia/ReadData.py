import numpy as np

class Input:
    
    def __init__(self, inputFile: str):
        self.machines = []
        self.operations = []
        self.__proNum = []
        self.__lines = None
        self.__input = inputFile
        self.Mac_Num=0
        self.Job_Num=0
        self.quant_operations_per_jobs=[]
    #

    def getMatrix(self):
        self.__readExample()
        self.__initMatrix()
        for i in range(len(self.__lines)-1):
            lo = 0
            hi = 0
            for j in range(self.__proNum[i]):
                head = int(self.__lines[i][lo])
                hi = lo + 2 * head + 1

                lo += 1
                while lo < hi:
                    self.machines[i][j].append(int(self.__lines[i][lo]))
                    self.operations[i][j].append(int(self.__lines[i][lo + 1]))
                    lo += 2


        p_table=self.DataConversion()
        return (p_table, self.quant_operations_per_jobs)
    #

    def __readExample(self):
        with open(self.__input) as fileObject:
            self.__lines = fileObject.readlines()

        self.__lines[0] = self.__lines[0].lstrip().rstrip().split("\t")

        self.Job_Num=int(self.__lines[0][0])
        self.Mac_Num=int(self.__lines[0][1])

        # Ajuste de dados
        del self.__lines[0]
        # Aqui para ser um a menos

        for i in range(len(self.__lines)-1):

            self.__lines[i] = self.__lines[i].lstrip().rstrip().split(" ")
            operation=int(self.__lines[i].pop(0))
            self.quant_operations_per_jobs.append(operation)
            self.__proNum.append(operation)
            while "" in self.__lines[i]:
                self.__lines[i].remove("")
    #

    def __initMatrix(self):
        for i in range(len(self.__proNum)):
            self.machines.append([])
            self.operations.append([])
            for _ in range(self.__proNum[i]):
                self.machines[i].append([])
                self.operations[i].append([])
    #

    def DataConversion(self):
        total_of_operations = np.sum(self.quant_operations_per_jobs)
        
        # Matriz de tempo de processamento process_times: número total de processos * m;
        # entre eles, o processamento não é possível e é representado por -1
        process_times = np.ones((total_of_operations,self.Mac_Num), dtype=int)*(-1)
        index = 0
        for (i1, i2) in zip(self.machines, self.operations):
            for (j1,j2) in zip(i1, i2):
                for (k1,k2) in zip(j1, j2):
                    process_times[index][k1-1]=k2
                index += 1

        return process_times
    #

#