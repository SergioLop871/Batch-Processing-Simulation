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

