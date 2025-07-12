"""
Archivo principal de la aplicación.
Crea e inicializa la interfaz gráfica del graficador de funciones,
conectando los componentes visuales y la lógica de graficado simbólico.
"""
import tkinter as tk
from gui_usuario.backend import TitleFrame, InputAndOptions, GraphicCanvas
from graficar_funciones.backend import Function, string_to_symbolic, FigureBuilder

def main():
    #Se instancia de la clase Tk.
    root = tk.Tk()
    root.geometry("600x600")
    
    #Frame del titulo
    title = TitleFrame(root, "Graficador de funciones")
    title.pack(padx=5, pady=5, fill = 'both', side = 'top', expand = True)
    
    #Comando que se realiza cuando se presiona el botón 'graficar'
    def boton_graficar(): 
        """
        Toma los datos del input, convierte la función a simbólica,
        aplica derivación o integración si se selecciona,
        y actualiza el gráfico.
        """
        data = input_frame.get_data()
        funciones = []
        try:
            if data["funcion"]:
                simb = string_to_symbolic(data["funcion"])
                f = Function(simb)
                funciones.append(f)
                
                if data["derivar"]:
                    funciones.append(f.derive())
                
                if data["integrar"]:
                    funciones.append(f.integrate())
            
            
            if funciones:
                figure.clear()
                figure.plot_function(funciones)
                graphic_frame.update_graphic()

        except Exception as e:
            print('Error:', e)
            
    #Comando que se realiza cuando se presiona el botón 'limpiar'
    def boton_limpiar():
        """
        Limpia el gráfico actual.
        """
        try:
            figure.clear()
            graphic_frame.update_graphic()
        except Exception as e:
            print('Error: ', e)
    
    #Frame de la entrada con sus botones
    input_frame = InputAndOptions(root, on_submit_callback1=boton_graficar, on_submit_callback2= boton_limpiar)
    input_frame.pack(padx=5, pady=5, fill = 'both', side = 'bottom', expand = True)

    #Frame del gráfico 
    figure = FigureBuilder()
    graphic_frame = GraphicCanvas(root, figure)
    graphic_frame.pack(padx=5, pady=5, fill='both', expand = True)
    
    #Método principal que inicia el flujo del programa
    root.mainloop()

if __name__ == '__main__':
    main()