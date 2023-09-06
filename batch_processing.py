import time 
from tkinter import *

root = Tk()
root.title("Batch Processing Simulation")

def add_process():
    print(program_number_field.get())

#Falta: Añadir los tamaños de los botones, labels
programmer_name_label = Label(root, text="Nombre del Programador:")
programmer_name_field = Entry(root)
operation_label = Label(root, text="Operación:")
operation_field = Entry(root)
estimated_maximum_time_label = Label(root, text="Tiempo Máximo Estimado (TMA):")
estimated_maximum_time_field = Entry(root)
program_number_label = Label(root, text="Número de Programa:")
program_number_field = Entry(root)
add_process = Button(root, text="Agregar Proceso", command=add_process)

#Falta: Cambiar al sistema de grid
programmer_name_label.pack()
programmer_name_field.pack()
operation_label.pack()
operation_field.pack()
estimated_maximum_time_label.pack()
estimated_maximum_time_field.pack()
program_number_label.pack()
program_number_field.pack()
add_process.pack()


root.mainloop()

#Falta agregar sleep y limpiar pantalla
class Proceso:
    def __init__(self, nombre_programador, operacion, datos, tiempo_maximo, numero_programa):
        self.nombre_programador = nombre_programador
        self.operacion = operacion
        self.datos = datos
        self.tiempo_maximo = tiempo_maximo
        self.numero_programa = numero_programa
        self.tiempo_transcurrido = 0

    def ejecutar(self):
        resultado = None
        if self.operacion == '+':
            resultado = sum(self.datos)
        elif self.operacion == '-':
            resultado = self.datos[0] - self.datos[1]
        elif self.operacion == '*':
            resultado = self.datos[0] * self.datos[1]
        elif self.operacion == '/':
            if self.datos[1] != 0:
                resultado = self.datos[0] / self.datos[1]
        elif self.operacion == 'residuo':
            resultado = self.datos[0] % self.datos[1]
        elif self.operacion == 'porcentaje':
            resultado = (self.datos[0] / 100) * self.datos[1]
        return resultado

def capturar_proceso():
    nombre_programador = input("Nombre del programador: ")
    operacion = input("Operación a realizar (+, -, *, /, residuo, porcentaje): ")
    while operacion not in ('+', '-', '*', '/', 'residuo', 'porcentaje'):
        print("Operación no válida. Intente de nuevo.")
        operacion = input("Operación a realizar (+, -, *, /, residuo, porcentaje): ")
    datos = []
    for i in range(2):
        dato = float(input(f"Ingrese dato {i + 1}: "))
        datos.append(dato)
    tiempo_maximo = float(input("Tiempo Máximo Estimado (mayor a 0): "))
    while tiempo_maximo <= 0:
        print("Tiempo Máximo Estimado debe ser mayor a 0. Intente de nuevo.")
        tiempo_maximo = float(input("Tiempo Máximo Estimado (mayor a 0): "))
    numero_programa = input("Número de Programa (ID) único: ")
    return Proceso(nombre_programador, operacion, datos, tiempo_maximo, numero_programa)


def ejecutar_lote(lote):
    for proceso in lote:
        print("\nLote en Ejecución:")
        print(f"Numero de programa (ID): {proceso.numero_programa}")
        print(f"Tiempo Máximo Estimado: {proceso.tiempo_maximo}")
        print("\nProceso en Ejecución:")
        print(f"Nombre: {proceso.nombre_programador}")
        print(f"Operación: {proceso.operacion} {proceso.datos}")
        tiempo_transcurrido = 0
        while tiempo_transcurrido < proceso.tiempo_maximo:
            resultado = proceso.ejecutar()
            tiempo_transcurrido += 1
            proceso.tiempo_transcurrido += 1
            print(f"Tiempo transcurrido en ejecución: {tiempo_transcurrido}")
            print(f"Tiempo restante por ejecutar: {proceso.tiempo_maximo - tiempo_transcurrido}")
            if resultado is not None:
                print(f"Resultado de la operación: {proceso.operacion} {proceso.datos} = {resultado}")
            else:
                print("Error: División por cero (operación no válida)")

def main():
    lotes_pendientes = []
    reloj_global = 0
    
    N = int(input("Introduce la cantidad de procesos: "))
    procesos_capturados = 0
    lote_actual = []
    
    while procesos_capturados < N:
        proceso = capturar_proceso()
        lote_actual.append(proceso)
        procesos_capturados += 1
        if len(lote_actual) == 5 or procesos_capturados == N:
            lotes_pendientes.append(lote_actual)
            lote_actual = []
    
    while lotes_pendientes:
        lote_en_ejecucion = lotes_pendientes.pop(0)
        print("\nNúmero de lotes pendientes:", len(lotes_pendientes))
        print("\nLote en Ejecución:")
        for proceso in lote_en_ejecucion:
            proceso.tiempo_transcurrido = 0
        ejecutar_lote(lote_en_ejecucion)
        reloj_global += sum(proceso.tiempo_maximo for proceso in lote_en_ejecucion)
    
    print("\n¡Todos los procesos han sido ejecutados!")
    print("Reloj Global:", reloj_global)

if __name__ == "__main__":
    main()


