import matplotlib.figure as mpl_figure
import numpy as np
from sympy import symbols, sympify, diff, Expr, integrate, latex
from sympy.utilities.lambdify import lambdify
from typing import Callable

#Variable simbólica global usada para las expresiones
var_x=symbols('x')


def string_to_symbolic(string_function: str) -> Expr:
    """
    Convierte una cadena de texto a una expresión simbólica de SymPy.
    
    Args:
        string_funcion (str) : Expresión matemática como string.
    
    Returns:
        sympy.Expr: Expresión simbólica correspondiente
    """
    return sympify(string_function)
    

def symbolic_to_callable(symbolic_function: Expr) -> Callable:
    """
    Convierte una expresión simbólica de SymPy a una expresión evaluable con Numpy.

    Args:
        symbolic_function (sympy.Expr) : Expresión simbólica.
    
    Returns:
        Callable : Función compatible con arrays de NumPy

    """
    return lambdify(var_x, symbolic_function, "numpy")


class Function():
    """
    Clase para representar y operar con funciones simbólica de SymPy.
    
    Available methods:
        -derive(): Retorna una nueva instancia derivada
        -evaluate(x_vals): Evalúa la función para los valores dados.
    
    Example:
        >>> f = Function(sympy_expr)
        >>> f_derived = f.derive()
        >>> resultado = f.evaluate([1,2,3])
        
    """
    def __init__(self, symbolic_function : Expr, color : str = "blue"):
        """
        
        Inicializa una instancia de Function.

        Args:
            symbolic_function (sympy.Expr) : La función simbólica.
        
        Atributtes:
            symbolic_function (sympy.Expr) : Expresión simbólica
            callable_function (callable) :  Versión evaluable con NumPy
            
        """
        self.color = color
        self.symbolic_function = symbolic_function
        self.callable_function = symbolic_to_callable(symbolic_function)
    
    def derive(self) -> "Function":
        """
        Deriva la función simbólica.
        
        Returns:
            Function: Nueva instancia la función derivada.
        """
        
        derived = diff(self.symbolic_function, var_x)
        return Function(derived, color = "red")

    def integrate(self) -> "Function":
        """
        Integra simbólicamente la función respecto a x.

        Returns:
            Function: Nueva instancia con la función integrada.
        """
        
        integral = integrate(self.symbolic_function, var_x)
        return Function(integral, color = "green")
    
    def evaluate(self, x_vals: list | np.ndarray) -> np.ndarray:
        """
        Evalúa la función para los valores dados
        
        Args:
            x_vals(list or np.ndarray) : Valores de entrada.
            
        Returns:
            list or npdarray: Resultados de la evaluación
        
        """
        return self.callable_function(x_vals)
    
class FigureBuilder():
    def __init__(self):
        self.figure = mpl_figure.Figure()
        self.axe = self.figure.add_subplot(111)
        self._configure_axes()

    def _configure_axes(self):
        self.axe.set_xlabel('x')
        self.axe.set_ylabel('f(x)')
        self.axe.set_xlim(-50, 50)
        self.axe.set_ylim(-50, 50)
        self.axe.set_xticks(np.arange(-50, 51, 10))
        self.axe.set_yticks(np.arange(-50, 51, 10))
        self.axe.axhline(y=0, color='gray', linewidth=0.8)
        self.axe.axvline(x=0, color='gray', linewidth=0.8)
        self.axe.grid(True, which='both', linestyle='--', linewidth=0.5, color='lightgray')

    def plot_function(self, functions: list[Function]):
        for function in functions:
            xpoints = np.linspace(-50, 50, 300)
            ypoints = function.evaluate(xpoints)
            self.axe.plot(xpoints, ypoints, label=f"${latex(function.symbolic_function)}$", color = function.color )
        self.axe.legend()

    def clear(self):
        self.axe.cla() 
        self._configure_axes()

    def get_figure(self):
        return self.figure

        

#Modificaciones respecto a la lógica de la creación de FigureBuilder()
'''
def Figure(function: Function = None) -> mpl_figure:
    """
    Crea una figura de matploblib con una configuración predeterminada.
    
    Args: 
        function(Function) : Función matemática para gráficar en la figura.
    
    Returns:
        matploblib.figure.Figure: La instancia con la configuración final.
    """
    figure = mpl_figure.Figure()
    axe = figure.add_subplot(111)
    axe.set_xlabel('x')
    axe.set_ylabel('f(x)')
    axe.set_xticks(np.arange(-50, 50, 10))
    axe.set_yticks(np.arange(-50, 50, 10))
    axe.set_xlim(-50, 50)
    axe.set_ylim(-50, 50)
    axe.axhline(y=0, color='gray', linewidth=0.5)
    axe.axvline(x=0, color='gray', linewidth=0.5)
    axe.grid(True, which='both', linestyle='--', linewidth=0.5, color='lightgray')
     
    if function:
        xpoints = np.linspace(-50, 50, 100)
        ypoints = function.evaluate(xpoints)
        axe.plot(xpoints, ypoints)

    return figure
'''

'''
class GraphicFunction():
    """
    Clase para graficar una instancia de Function usando Matploblib.
    
    Available methods:
        -plot(function): Grafica la función.
        -get_figure(): Retorna el objeto figura (matploblib.figure.Figure).
    
    Example:
        >>> grafico1 = GraphicFunction()
        >>> grafico1.plot(f)
        >>> grafico1.getfigure()  
    """
    
    def __init__(self):
        """
        Inicializa el objeto gráfico con configuración predeterminada

        Atributtes:
            figure(Figure): Figura de Matplotlib.
            axe(Axes): Contenedor para los elementos del grafico.
            xpoints(np.ndarray): Valores de x para graficar
        """
        
        self.figure = figure.Figure()
        self.axe = self.figure.add_axes((0, 0, 1, 1))
        self.xpoints = np.linspace(-50, 50, 100)
        self.axe.set_xlabel('x')
        self.axe.set_ylabel('f(x)')
        self.axe.set_xlim(-50, 50)
        self.axe.set_ylim(-50, 50)
        self.axe.axhline(y=0, color='gray', linewidth=0.5)
        self.axe.axvline(x=0, color='gray', linewidth=0.5)

    def plot(self, function: Function = None) -> None:
        """
        Grafica una función sobre el eje X definido.
        
        Args:
            function(Function): Instancia de Function a grafica.
            
        Returns:
            None
        """
        if function:
            ypoints = function.evaluate(self.xpoints)
            self.axe.plot(self.xpoints, ypoints)
            
    def get_figure(self) -> figure:
        """
        Retorna el objeto figura de matploblib para incrustarlo en la GUI.
        
        Returns:
            Figure: Instancia de matploblib.figure.Figure con el gráfico.
        """
        return self.figure
'''





