import tkinter as tk
from tkinter import messagebox

# Pila para rastrear las ventanas abiertas
window_stack = []

def open_new_window(window_function):
    # Cerrar la ventana actual si existe
    if window_stack:
        current_window = window_stack[-1]
        current_window.withdraw()  # Ocultar la ventana actual en lugar de destruirla
    
    # Abrir la nueva ventana
    new_window = window_function()
    window_stack.append(new_window)

def close_current_window():
    if window_stack:
        current_window = window_stack.pop()
        current_window.destroy()  # Cerrar la ventana actual
    
    # Mostrar la ventana anterior si existe
    if window_stack:
        previous_window = window_stack[-1]
        previous_window.deiconify()  # Mostrar la ventana anterior

def open_new_window1():
    new_window1 = tk.Toplevel()
    new_window1.title("Ventas Vitalis Farmacy")
    new_window1.geometry("1280x720")

    label = tk.Label(new_window1, text="Ventas", font=("Arial", 14))
    label.pack(pady=10)
    
    back_button = tk.Button(new_window1, text="←", command=close_current_window, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    return new_window1

def open_new_window2():
    new_window2 = tk.Toplevel()
    new_window2.title("Inventario Vitalis Farmacy")
    new_window2.geometry("1280x720")

    label = tk.Label(new_window2, text="Inventario", font=("Arial", 14))
    label.pack(pady=10)

    back_button = tk.Button(new_window2, text="←", command=close_current_window, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    return new_window2

def open_new_window4():
    new_window4 = tk.Toplevel()
    new_window4.title("Reporte de Ventas")
    new_window4.geometry("1280x720")

    label = tk.Label(new_window4, text="Reporte de Ventas", font=("Arial", 14))
    label.pack(pady=10)

    back_button = tk.Button(new_window4, text="←", command=close_current_window, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    return new_window4

def open_new_window5():
    new_window5 = tk.Toplevel()
    new_window5.title("Adquisición de Productos")
    new_window5.geometry("1280x720")

    label = tk.Label(new_window5, text="Adquisición de Productos", font=("Arial", 14))
    label.pack(pady=10)

    back_button = tk.Button(new_window5, text="←", command=close_current_window, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    return new_window5

def open_new_window3():
    new_window3 = tk.Toplevel()
    new_window3.title("Reporte y Analisis Vitalis Farmacy")
    new_window3.geometry("1280x720")

    label = tk.Label(new_window3, text="Reportes y Análisis", font=("Arial", 14))
    label.pack(pady=10)

    sales_report_button = tk.Button(new_window3, text="Reporte de Ventas", fg="White", bg="Red", font=("Arial", 14), command=lambda: open_new_window(open_new_window4))
    sales_report_button.pack(pady=10)

    product_acquisition_button = tk.Button(new_window3, text="Adquisición de Productos", fg="White", bg="Red", font=("Arial", 14), command=lambda: open_new_window(open_new_window5))
    product_acquisition_button.pack(pady=10)

    back_button = tk.Button(new_window3, text="←", command=close_current_window, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    return new_window3

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Inventario Vitalis Farmacy")
    root.geometry("1280x720")

    # Añadir la ventana principal a la pila
    window_stack.append(root)

    # Crear y mostrar una etiqueta
    label = tk.Label(root, text="Vitalis Farmacy", font=("Arial", 14))
    label.pack(pady=10)

    # Crear y mostrar botones para abrir nuevas ventanas
    button1 = tk.Button(root, text="Ventas", fg="White", bg="Red", font=("Arial", 16), command=lambda: open_new_window(open_new_window1))
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Inventario", fg="White", bg="Red", font=("Arial", 16), command=lambda: open_new_window(open_new_window2))
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Reportes y Análisis", fg="White", bg="Red", font=("Arial", 16), command=lambda: open_new_window(open_new_window3))
    button3.pack(pady=10)

    # Botón de regreso en la esquina superior izquierda
    back_button = tk.Button(root, text="Cerrar", command=root.destroy, font=("Arial", 12), bg="red", fg="white")
    back_button.place(x=0, y=0)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
