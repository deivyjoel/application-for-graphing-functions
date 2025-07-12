import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from graficar_funciones.backend import FigureBuilder

"""
Archivo backend de la GUI para el usuario.
Crea clases que herenda de tk.Frame permitiendo un mejor orden en la estructura de la GUI.
Cada clase representa una parte fundamental de la página
"""

class TitleFrame(tk.Frame):
    """
    Contenedor gráfico que muestra el título principal de la interfaz de usuario.
    
    Este componente encapsula un Label estilizado con fuente grande y negrita,
    centrado dentro de un Frame. Se utiliza como encabezado para la ventana principal
    
    Example:
        >>> titulo = TitleFrame(root, "Graficador de funciones")
        >>> titulo.pack()
    """
    def __init__(self, parent, texto):
        """
        Inicializa el frame con un Label que contiene el texto del titulo.
        
        Args:
            parent(tk.Widget) : Contenedor padre donde se colocará el frame
            texto(str) : Texto que se mostrará como título.
        """
        super().__init__(parent)
        tk.Label(self, text=texto, font=("Arial", 16, "bold italic"), ).pack(fill = 'both', expand = True)
        
        
class InputAndOptions(tk.Frame):
    """
     Contenedor de interfaz gráfica para ingresar una función simbólica
    y seleccionar operaciones como derivar o integrar
    
    This frame includes:
        - Un entry para ingresar la función simbólica
        - Dos checkbuttons: uno para 'Derivar', otro para 'Integrar'.
        - Un botón 'Graficar' y un botón 'limpiar' que ejecuta según on_submit_callback1 y on_submit_callback2
    
    Example:
        >>> opciones = InputAndOptions(root, callbac1, callback2)
        >>> opciones.pack()    
    """
    def __init__(self, parent, on_submit_callback1, on_submit_callback2):
        """
        Inicializa un contenedor con los widgets necesarios.
        
        Args:
            parent (tk.Widget): Contenedor padre donde se colocará el frame.
            on_submit_callback1 (callable) : Función que se ejecuta al presionar el botón 'Graficar'.
            on_submit_callback2 (callable) : Función que se ejecuta al presionar el botón 'Limpiar'.
        """
        super().__init__(parent)
        
        contenido = tk.Frame(self)
        contenido.grid(row = 0, column = 0)
        
        tk.Label(contenido, text='Función: ').grid(row= 0, column = 0, padx= 5, pady=5)
        
        self.entry = tk.Entry(contenido)
        self.entry.grid(row = 0, column= 1, padx=5, pady = 5)
        
        self.checkbutton1_estado = tk.BooleanVar()
        self.checkbutton2_estado = tk.BooleanVar()

        self.checkbutton1 = tk.Checkbutton(contenido, text= 'Derivar', variable = self.checkbutton1_estado, fg = "red")
        self.checkbutton2 = tk.Checkbutton(contenido, text= 'Integrar', variable = self.checkbutton2_estado, fg = "green")
        self.checkbutton1.grid(row = 1, column = 0, padx=5, pady=5)
        self.checkbutton2.grid(row = 1, column = 1, padx=5, pady=5)
        
        self.button1 = tk.Button(contenido, text='Graficar', command = on_submit_callback1)
        self.button1.grid(row = 2, column = 0, padx = 2, pady = 5)
        
        self.button2 = tk.Button(contenido, text= "Limpiar", command = on_submit_callback2)
        self.button2.grid(row = 2, column = 1, padx = 5, pady = 5)
        
        self.grid_columnconfigure(0, weight=1)
        
    def get_data(self):
        """
        Retorna los valores ingresados por el usuario.
        
        Returns:
            dict: Un diccionario con las siguientes claves:
                - "funcion" (str): Texto ingresado en el Entry.
                - "derivar" (bool): Estado del Checkbutton 'derivar'
                - "integrar" (bool): Estado del checkbutton 'Integrar'
        """
        return {
            "funcion": self.entry.get(),
            "derivar": self.checkbutton1_estado.get(),
            "integrar": self.checkbutton2_estado.get()
        }


class GraphicCanvas(tk.Frame):
    """
    
    """
    def __init__(self, parent, figure_builder : FigureBuilder):
        super().__init__(parent)
        self.figure_builder = figure_builder
        self.canvas_widget = FigureCanvasTkAgg(self.figure_builder.get_figure(), master=self)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().pack()

    def update_graphic(self):
        self.canvas_widget.draw()
        
        

        
        
        
        
