import random
from Individuo import Individuo


class Logica:

    def __init__(self):
        self.POBLACION=500
        self.GENERACIONES=5000
        pass


    def iniciar(self):

        #generar los genes de los individuos
        individuos = self.generar_individuos()
        for individuo in individuos:
            individuo.imprimir_genes()


    def generar_individuos(self):

        poblacion=[]

        for i in range(self.POBLACION):

            poblacion = []
            for i in range(self.POBLACION):
                poblacion.append(Individuo([random.randint(1, 8) for _ in range(8)]))
            return poblacion


        #print(poblacion)
        return poblacion
