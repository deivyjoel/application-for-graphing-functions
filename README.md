# Graficador de Funciones Matemáticas

Aplicación educativa en Python para graficar funciones simbólicas, junto con sus derivadas e integrales, mediante una interfaz gráfica simple y modular.

---

## Tecnologías utilizadas
- **Python 3.12**
- **Tkinter** (Interfaz gráfica)
- **SymPy** (Álgebra simbólica)
- **Matplotlib** (Gráficos)
- **NumPy** (Evaluación numérica)

---

## Instalación
1. Clona este repositorio:
```bash
git clone https://github.com/deivyjoel/application-for-graphing-functions.git
cd application-for-graphing-functions
```

2. Crea un entorno virtual e instala las dependencias.
```bash
python -m venv venv
source venv/Scripts/activate   # En Windows
pip install -r requirements.txt
```

## ¿Cómo funciona?

<img width="598" height="630" alt="image" src="https://github.com/user-attachments/assets/62a52041-c0c5-4181-ab66-88aef4cd9473" />


1. Ingresá una función simbólica como string, por ejemplo:
```text
x**2 + 2*x
```
2. Puedes seleccionar:
- Derivar
- Integrar
3. El programa graficará:
- Función original
- Derivada (rojo)
- Integral (verde)
