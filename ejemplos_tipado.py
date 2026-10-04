"""
Ejemplos de funciones con type hints en Python
Ilustra el uso de tipos básicos: int, float, str, list, dict
"""

# ============================================================================
# EJEMPLOS CON INT
# ============================================================================

def sumar(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b


def multiplicar(base: int, exponente: int) -> int:
    """Calcula la potencia de un número entero."""
    return base ** exponente


def factorial(n: int) -> int:
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ============================================================================
# EJEMPLOS CON FLOAT
# ============================================================================

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    import math
    return math.pi * (radio ** 2)


def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32


def calcular_promedio(calificaciones: list[float]) -> float:
    """Calcula el promedio de una lista de calificaciones."""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def precio_con_impuesto(precio_base: float, porcentaje_impuesto: float) -> float:
    """Calcula el precio final con impuestos."""
    return precio_base * (1 + porcentaje_impuesto / 100)


# ============================================================================
# EJEMPLOS CON STR
# ============================================================================

def saludar(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    return f"¡Hola, {nombre}!"


def contar_vocales(texto: str) -> int:
    """Cuenta las vocales en un texto."""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in texto if letra in vocales)


def invertir_texto(texto: str) -> str:
    """Invierte una cadena de texto."""
    return texto[::-1]


def es_palindromo(texto: str) -> bool:
    """Verifica si una palabra es palíndroma."""
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]


def formatear_nombre(nombre_completo: str) -> str:
    """Formatea un nombre con cada palabra en mayúscula inicial."""
    return nombre_completo.title()


# ============================================================================
# EJEMPLOS CON LIST
# ============================================================================

def filtrar_pares(numeros: list[int]) -> list[int]:
    """Filtra solo los números pares de una lista."""
    return [n for n in numeros if n % 2 == 0]


def ordenar_descendente(numeros: list[int]) -> list[int]:
    """Ordena una lista de números de mayor a menor."""
    return sorted(numeros, reverse=True)


def eliminar_duplicados(items: list) -> list:
    """Elimina duplicados manteniendo el orden."""
    vistos = set()
    resultado = []
    for item in items:
        if item not in vistos:
            vistos.add(item)
            resultado.append(item)
    return resultado


def concatenar_listas(lista1: list[str], lista2: list[str]) -> list[str]:
    """Concatena dos listas de strings."""
    return lista1 + lista2


def mapear_a_mayusculas(palabras: list[str]) -> list[str]:
    """Convierte todas las palabras a mayúsculas."""
    return [palabra.upper() for palabra in palabras]


def encontrar_minimo(numeros: list[float]) -> float:
    """Encuentra el valor mínimo en una lista."""
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return min(numeros)


# ============================================================================
# EJEMPLOS CON DICT
# ============================================================================

def crear_usuario(nombre: str, edad: int, email: str) -> dict[str, str | int]:
    """Crea un diccionario con datos de usuario."""
    return {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "tipo": "usuario"
    }


def obtener_valor_seguro(diccionario: dict[str, int], clave: str, valor_por_defecto: int = 0) -> int:
    """Obtiene un valor del diccionario con un valor por defecto."""
    return diccionario.get(clave, valor_por_defecto)


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Cuenta la frecuencia de cada palabra en una lista."""
    frecuencias: dict[str, int] = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def invertir_diccionario(diccionario: dict[str, int]) -> dict[int, str]:
    """Invierte un diccionario (clave se convierte en valor y viceversa)."""
    return {valor: clave for clave, valor in diccionario.items()}


def filtrar_diccionario(datos: dict[str, int], valor_minimo: int) -> dict[str, int]:
    """Filtra un diccionario manteniendo solo pares cuyo valor es mayor o igual al mínimo."""
    return {clave: valor for clave, valor in datos.items() if valor >= valor_minimo}


def fusionar_diccionarios(dic1: dict[str, int], dic2: dict[str, int]) -> dict[str, int]:
    """Fusiona dos diccionarios."""
    return {**dic1, **dic2}


# ============================================================================
# EJEMPLO COMBINADO: Tipos múltiples
# ============================================================================

def procesar_estudiantes(
    estudiantes: list[dict[str, str | int]],
    calificacion_minima: float
) -> dict[str, list[dict[str, str | int]]]:
    """
    Procesa una lista de estudiantes y los clasifica por aprobados/reprobados.
    
    Args:
        estudiantes: Lista de diccionarios con datos de estudiantes
        calificacion_minima: Calificación mínima para aprobar
    
    Returns:
        Diccionario con dos claves: 'aprobados' y 'reprobados'
    """
    aprobados = []
    reprobados = []
    
    for estudiante in estudiantes:
        if isinstance(estudiante.get("calificacion"), (int, float)):
            if estudiante["calificacion"] >= calificacion_minima:
                aprobados.append(estudiante)
            else:
                reprobados.append(estudiante)
    
    return {
        "aprobados": aprobados,
        "reprobados": reprobados
    }


# ============================================================================
# PRUEBAS (Main)
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("EJEMPLOS CON TIPOS EN PYTHON")
    print("=" * 70)
    
    # int
    print("\n[INT] Suma:", sumar(5, 3))
    print("[INT] Factorial de 5:", factorial(5))
    
    # float
    print("\n[FLOAT] Área de círculo (r=5):", f"{calcular_area_circulo(5):.2f}")
    print("[FLOAT] Promedio:", calcular_promedio([8.5, 9.0, 7.5, 8.0]))
    print("[FLOAT] 25°C en Fahrenheit:", f"{convertir_celsius_a_fahrenheit(25):.1f}°F")
    
    # str
    print("\n[STR] Saludo:", saludar("María"))
    print("[STR] Vocales en 'Python':", contar_vocales("Python"))
    print("[STR] '¿Eres tú?' invertido:", invertir_texto("¿Eres tú?"))
    print("[STR] ¿Es 'radar' palíndroma?:", es_palindromo("radar"))
    
    # list
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n[LIST] Números pares en", numeros, ":", filtrar_pares(numeros))
    print("[LIST] Ordenado descendente:", ordenar_descendente(numeros))
    print("[LIST] Sin duplicados [1,2,2,3,3,3]:", eliminar_duplicados([1, 2, 2, 3, 3, 3]))
    
    # dict
    print("\n[DICT] Usuario creado:", crear_usuario("Juan", 30, "juan@email.com"))
    palabras = ["python", "python", "java", "python", "c"]
    print("[DICT] Frecuencias:", contar_frecuencias(palabras))
    
    # Ejemplo combinado
    estudiantes = [
        {"nombre": "Ana", "calificacion": 9.0},
        {"nombre": "Bob", "calificacion": 5.5},
        {"nombre": "Carlos", "calificacion": 8.5},
        {"nombre": "Diana", "calificacion": 4.0},
    ]
    resultado = procesar_estudiantes(estudiantes, 7.0)
    print("\n[COMBINADO] Estudiantes aprobados:", resultado["aprobados"])
    print("[COMBINADO] Estudiantes reprobados:", resultado["reprobados"])
    
    print("\n" + "=" * 70)
    print("[OK] Todos los ejemplos ejecutados correctamente")
    print("=" * 70)
