import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def init_window():

    window= tk.Tk()
    window.title("Primera Aplicación")
    window.geometry('400x200')
    entrada1=tk.Entry(window,width = 10 )
    entrada2=tk.Entry(window,width = 10)

    entrada1.grid(column = 1, row = 1) 
    entrada2.grid(column = 1, row = 2) 

    label_entrada1=tk.Label(window, text = "ingrese primer numero")
    label_entrada1.grid(column = 0, row = 1)
    label_entrada2=tk.Label(window, text = "ingrese segundo numero")
    label_entrada2.grid(column = 0, row = 2)
    label_operador = tk.Label(window, text = ' Escoja un operador',font=('Arial Bold',10))
    label_operador.grid(column= 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text = "", font=('Arial bold',15))
    label_resultado.grid(column = 3, row = 5)
    def calculadora(num1,num2,operador):
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        else:
            resultado = num1 ** num2
        return resultado 

    def click_calcular(label, num1, num2, operador):
        if num1== "" and num2 == "":
            messagebox.showinfo("ERROR","Por favor ingresa una entrada valida")
        else:
            valor1 = float(num1)
            valor2 = float(num2)
            res = calculadora(valor1,valor2,operador)
            label.configure(text=' = ' + str(res))
            label_num1.configure(text=entrada1.get())
            label_operador.configure(text=combo_operadores.get())
            label_num2.configure(text=entrada2.get())
            
    
    boton= tk.Button(window, command= lambda:click_calcular(label_resultado,entrada1.get(),entrada2.get(),combo_operadores.get()),text= "calcular",bg="purple",fg="white" )
    boton.grid(column = 1, row = 4)

    def limpiar():
        entrada1.delete(0,100)
        entrada2.delete(0,100)
        label_num1.configure(text="")
        label_operador.configure(text="")
        label_num2.configure(text="")
        label_resultado.configure(text="")


    boton_limpiar=tk.Button(window,command=limpiar,text="Borrar",bg="purple",fg="white")
    boton_limpiar.grid(column = 2, row = 4)

    label_num1=tk.Label(window,text="",font=('Arial bold',12))
    label_num1.grid(column=0,row=5 )
    label_operador=tk.Label(window,text="",font=('Arial bold',12))
    label_operador.grid(column=1,row=5)
    label_num2=tk.Label(window,text="",font=('Arial bold',12))
    label_num2.grid(column=2,row= 5)
    window.mainloop()
def main():
    init_window()
main()