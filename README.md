# Python con Tipos (Type Hints)

## ¿Qué es el tipado en Python?

Python es un lenguaje de tipado dinámico, lo que significa que las variables pueden cambiar de tipo durante la ejecución del programa. Sin embargo, desde Python 3.5, podemos usar **type hints** (anotaciones de tipo) para indicar explícitamente qué tipos de datos esperamos que tengan nuestras variables y funciones.

## Sintaxis Básica

Las anotaciones de tipo se añaden usando dos puntos (`:`) después del nombre de la variable o parámetro, y una flecha (`->`) para indicar el tipo de retorno:

```python
def funcion(parametro: tipo) -> tipo_retorno:
    return valor
```

## Ventajas del Tipado en Python

### 1. **Detección de Errores Temprana** 🐛
Los type checkers como Mypy, Pylance o Pyright pueden detectar errores de tipo antes de ejecutar el código:
```python
def sumar(a: int, b: int) -> int:
    return a + b

resultado = sumar(5, "10")  # ❌ Error detectado: se espera int, no str
```

### 2. **Mejor Autocompletado** 📝
Los editores de código (VS Code, PyCharm) pueden ofrecer autocompletado más preciso cuando conocen los tipos:
```python
def procesar_texto(texto: str) -> int:
    return len(texto.upper())  # El editor sabe que texto tiene métodos de str
```

### 3. **Documentación Automática** 📚
Los tipos sirven como documentación integrada en el código:
```python
def crear_usuario(nombre: str, edad: int, email: str) -> dict:
    """Es evidente qué tipos espera y devuelve la función"""
```

### 4. **Mantenimiento Facilitado** 🔧
Otros desarrolladores (o tu yo futuro) entienden rápidamente qué tipos maneja cada función:
```python
def calcular_promedio(calificaciones: list[float]) -> float:
    # Es claro que espera una lista de números decimales
    return sum(calificaciones) / len(calificaciones)
```

### 5. **Refactorización Segura** ♻️
Al cambiar código, los type checkers alertan si algo se rompe:
```python
def convertir_a_entero(valor: str) -> int:
    return int(valor)  # Si cambias el retorno a str, el type checker te lo dirá
```

### 6. **Mejor Rendimiento** ⚡
Algunas herramientas pueden optimizar el código basándose en información de tipos.

### 7. **Escalabilidad** 📈
En proyectos grandes, el tipado hace que el código sea más robusto y fácil de escalar.

## Tipos Básicos Más Comunes

| Tipo | Ejemplo | Descripción |
|------|---------|------------|
| `int` | `5` | Números enteros |
| `float` | `3.14` | Números decimales |
| `str` | `"Hola"` | Cadenas de texto |
| `bool` | `True` | Valores booleanos |
| `list` | `[1, 2, 3]` | Listas (mutable) |
| `dict` | `{"clave": "valor"}` | Diccionarios |
| `tuple` | `(1, 2)` | Tuplas (inmutable) |
| `set` | `{1, 2, 3}` | Conjuntos |
| `None` | `None` | Sin valor |

## Tipos Genéricos (Python 3.9+)

Para especificar qué contiene una colección:

```python
lista_enteros: list[int] = [1, 2, 3]
diccionario: dict[str, int] = {"edad": 25}
tupla: tuple[str, int, float] = ("Ana", 25, 1.70)
```

## Verificar Tipos

### Con Mypy (Type Checker oficial)
```bash
pip install mypy
mypy practica.py
```

Mypy analizará tu código y reportará errores de tipo sin ejecutarlo:
```
practica.py:10: error: Argument 1 to "sumar" has incompatible type "str"; expected "int"
```

### Con Pylance (Extensión de VS Code)
[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) es una extensión oficial de Microsoft para VS Code que verifica tipos automáticamente mientras escribes.

**Instalación:**
1. Abre VS Code
2. Ve a Extensiones (Ctrl+Shift+X)
3. Busca "Pylance"
4. Instala la extensión oficial de Microsoft

Pylance marcará automáticamente los errores de tipo con subrayados rojos y sugerencias.

### Con el Autoevaluador (Integrado)
Este curso incluye un autoevaluador que se ejecuta al hacer:
```bash
python practica.py
```

Muestra automáticamente si tus tipos y lógica son correctos.

## Ejemplo Completo

Ver el archivo `ejemplos_tipado.py` para ejemplos prácticos de funciones tipadas.

---

**Conclusión**: El tipado en Python no es obligatorio, pero es una excelente práctica que mejora la calidad del código, facilita la detección de errores y hace que el código sea más mantenible y escalable.
