"""
Archivo encargado de la lógica para graficar funciones a partir de expresiones simbólicas ingresadas como string.

La expresión es transformada mediante `sympify()` en un objeto simbólico de SymPy y posteriormente convertida a una función evaluable por NumPy con `lambdify()`.

Las funciones se grafican utilizando NumPy para la generación de puntos y Matplotlib para la representación gráfica.
"""

import matplotlib.figure as mpl_figure
import numpy as np
from sympy import symbols, sympify, diff, Expr, integrate, latex
from sympy.utilities.lambdify import lambdify
from typing import Callable

# Variable simbólica global usada para las expresiones
var_x = symbols('x')


def string_to_symbolic(string_function: str) -> Expr:
    """
    Convierte una cadena de texto a una expresión simbólica de SymPy.

    Args:
        string_function (str): Expresión matemática como string.

    Returns:
        sympy.Expr: Expresión simbólica correspondiente.
    """
    return sympify(string_function)


def symbolic_to_callable(symbolic_function: Expr) -> Callable:
    """
    Convierte una expresión simbólica de SymPy a una función evaluable con NumPy.

    Args:
        symbolic_function (sympy.Expr): Expresión simbólica.

    Returns:
        Callable: Función compatible con arrays de NumPy.
    """
    return lambdify(var_x, symbolic_function, "numpy")


class Function:
    """
    Clase que representa y opera con funciones simbólicas de SymPy.

    Permite derivar, integrar y evaluar la función sobre arreglos NumPy.
    Se utiliza para abstraer operaciones matemáticas en el proyecto.

    Available Methods:
        - derive(): Retorna una nueva instancia derivada.
        - integrate(): Retorna una nueva instancia integrada.
        - evaluate(x_vals): Evalúa la función para los valores dados.

    Example:
        >>> f = Function(sympy_expr)
        >>> f_derived = f.derive()
        >>> result = f.evaluate([1, 2, 3])
        >>> f_integrated = f.integrate()
    """
    def __init__(self, symbolic_function: Expr, color: str = "blue"):
        """
        Inicializa una instancia de Function.

        Args:
            symbolic_function (sympy.Expr): La función simbólica.
            color (str): El color de su gráfica, por defecto azul.

        Attributes:
            symbolic_function (sympy.Expr): Expresión simbólica.
            color (str): Color de la gráfica.
            callable_function (Callable): Versión evaluable con NumPy.
        """
        self.color = color
        self.symbolic_function = symbolic_function
        self.callable_function = symbolic_to_callable(symbolic_function)

    def derive(self) -> "Function":
        """
        Deriva la función simbólica.

        Returns:
            Function: Nueva instancia de la función derivada.
        """
        derived = diff(self.symbolic_function, var_x)
        return Function(derived, color="red")

    def integrate(self) -> "Function":
        """
        Integra la función simbólica.

        Returns:
            Function: Nueva instancia con la función integrada.
        """
        integral = integrate(self.symbolic_function, var_x)
        return Function(integral, color="green")

    def evaluate(self, x_vals: list | np.ndarray) -> np.ndarray:
        """
        Evalúa la función para los valores dados.

        Args:
            x_vals (list or np.ndarray): Valores de entrada.

        Returns:
            np.ndarray: Resultados de la evaluación.
        """
        return self.callable_function(x_vals)


class FigureBuilder:
    """
    Clase encargada de construir y gestionar una figura de Matplotlib para la representación de funciones matemáticas.

    Configura los ejes, las rejillas y líneas guía de la gráfica, y proporciona métodos para trazar funciones, limpiar el gráfico y obtener la figura para su visualización.

    Available Methods:
        - plot_function(functions: list[Function]): Dibuja una o más funciones sobre el eje.
        - clear(): Limpia el gráfico y restablece su configuración inicial.
        - get_figure(): Devuelve el objeto Figure para su incrustación en la GUI.

    Example:
        >>> fig_builder = FigureBuilder()
        >>> fig_builder.plot_function([function])
        >>> fig_builder.clear()
        >>> fig_builder.get_figure()
    """
    def __init__(self):
        """
        Inicializa la figura y el eje con configuraciones predeterminadas de visualización.

        Attributes:
            figure (Figure): Objeto Figure de Matplotlib que contiene el gráfico.
            axe (Axes): Subgráfico donde se dibujan las funciones y los ejes.
        """
        self.figure = mpl_figure.Figure()
        self.axe = self.figure.add_subplot(111)
        self._configure_axes()

    def _configure_axes(self):
        """
        Configura los ejes del gráfico: etiquetas, límites, rejillas y líneas guía.
        """
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
        """
        Grafica una lista de funciones sobre el eje actual.

        Args:
            functions (list[Function]): Lista de instancias de la clase Function que serán evaluadas y graficadas.
        """
        for function in functions:
            xpoints = np.linspace(-50, 50, 300)
            ypoints = function.evaluate(xpoints)
            self.axe.plot(xpoints, ypoints, label=f"${latex(function.symbolic_function)}$", color=function.color)
        self.axe.legend()

    def clear(self):
        """
        Limpia la figura eliminando los gráficos actuales y restablece la configuración predeterminada de los ejes.
        """
        self.axe.cla()
        self._configure_axes()

    def get_figure(self):
        """
        Retorna el objeto Figure de Matplotlib para su visualización en la GUI.

        Returns:
            Figure: Figura de Matplotlib con la configuración actual.
        """
        return self.figure
