"""
PRÁCTICA: Agregar type hints a funciones
==========================================

En esta práctica debes AGREGAR type hints a las siguientes funciones.

Requisitos:
  ✓ Añade type hints completos en la firma de cada función
  ✓ Los parámetros deben tener anotaciones de tipo
  ✓ Añade el tipo de retorno con ->
  ✓ Implementa la lógica de la función según la descripción
  ✓ Verifica tu solución comparando con solucion.py

Nivel: Medio

TIP: En cada función verás qué tipos espera en la sección "Returns" del docstring
"""

# =============================================================================
# FUNCIÓN 1: Validar y procesar un email
# =============================================================================

def validar_email(email):
    """
    Valida un email y retorna un diccionario con el resultado.
    
    Args:
        email: Cadena de texto con el email a validar
    
    Returns:
        Diccionario con:
        - "valido": bool indicando si es válido
        - "razon": str explicando por qué no es válido (si aplica)
    
    Criterios de validación:
        - Debe contener exactamente un símbolo '@'
        - La parte antes de '@' debe tener al menos 1 carácter
        - Debe contener un punto '.' después del '@'
        - La extensión (después del último '.') debe tener 2-4 caracteres
        - No puede empezar ni terminar con punto
    
    Ejemplos:
        validar_email("usuario@ejemplo.com") -> {"valido": True, "razon": ""}
        validar_email("usuario@ejemplo") -> {"valido": False, "razon": "..."}
        validar_email("usuario@@ejemplo.com") -> {"valido": False, "razon": "..."}
    """
    pass

    

# =============================================================================
# FUNCIÓN 2: Análisis de palabras en un texto
# =============================================================================

def analizar_texto(texto):
    """
    Analiza un texto y retorna estadísticas sobre él.
    
    Args:
        texto: Cadena de texto a analizar
    
    Returns:
        Diccionario con:
        - "total_palabras": int - cantidad de palabras
        - "total_caracteres": int - cantidad de caracteres (sin espacios)
        - "palabras_unicas": int - cantidad de palabras diferentes
        - "promedio_longitud": float - longitud promedio de palabras
        - "palabra_mas_larga": str - la palabra con más caracteres
    
    Notas:
        - Considera "palabras" como secuencias separadas por espacios
        - Ignora puntuación (puedes asumir texto limpio)
        - La longitud promedio debe ser un float redondeado a 2 decimales
    
    Ejemplo:
        analizar_texto("hola mundo hola") -> {
            "total_palabras": 3,
            "total_caracteres": 10,
            "palabras_unicas": 2,
            "promedio_longitud": 3.33,
            "palabra_mas_larga": "mundo"
        }
    """
    pass


# =============================================================================
# FUNCIÓN 3: Gestionar inventario de productos
# =============================================================================

def actualizar_inventario(inventario, operaciones):
    """
    Actualiza un inventario realizando operaciones de compra/venta.
    
    Args:
        inventario: Diccionario donde claves son nombres de productos
                    y valores son cantidades disponibles
        operaciones: Lista de diccionarios con operaciones, cada uno con:
                     - "producto": str - nombre del producto
                     - "cantidad": int - cantidad (positiva para compra, negativa para venta)
    
    Returns:
        Diccionario actualizado con los nuevos valores de inventario
    
    Reglas:
        - Si el producto no existe en inventario, debe crearse con la cantidad
        - No se puede vender más de lo disponible (ignorar esa operación)
        - El inventario no puede ser negativo
        - Retorna el inventario actualizado
    
    Ejemplo:
        inv = {"manzanas": 10, "naranjas": 5}
        ops = [
            {"producto": "manzanas", "cantidad": -3},  # Vender 3
            {"producto": "plátanos", "cantidad": 8},   # Comprar 8 nuevos
        ]
        resultado = {"manzanas": 7, "naranjas": 5, "plátanos": 8}
    """
    pass


# =============================================================================
# FUNCIÓN 4: Clasificar estudiantes por calificación
# =============================================================================

def clasificar_estudiantes(estudiantes, limite_aprobado=6.0):
    """
    Clasifica estudiantes en categorías según su calificación.
    
    Args:
        estudiantes: Lista de diccionarios con campos:
                     - "nombre": str
                     - "calificacion": float (0-10)
        limite_aprobado: float - calificación mínima para aprobar (default 6.0)
    
    Returns:
        Diccionario con:
        - "aprobados": list - estudiantes con calificación >= limite_aprobado
        - "reprobados": list - estudiantes con calificación < limite_aprobado
        - "promedio_general": float - promedio de todos
        - "mejor_estudiante": str - nombre del estudiante con mejor nota
        - "peor_estudiante": str - nombre del estudiante con peor nota
    
    Notas:
        - El promedio debe estar redondeado a 2 decimales
        - Si la lista está vacía, retorna listas vacías y 0 para promedios
    
    Ejemplo:
        datos = [
            {"nombre": "Ana", "calificacion": 8.5},
            {"nombre": "Bob", "calificacion": 5.0},
            {"nombre": "Carlos", "calificacion": 9.0}
        ]
        resultado = {
            "aprobados": [{"nombre": "Ana", ...}, {"nombre": "Carlos", ...}],
            "reprobados": [{"nombre": "Bob", ...}],
            "promedio_general": 7.5,
            "mejor_estudiante": "Carlos",
            "peor_estudiante": "Bob"
        }
    """
    pass


# =============================================================================
# FUNCIÓN 5: Convertidor de unidades
# =============================================================================

def convertir_unidades(valor, unidad_origen, unidad_destino):
    """
    Convierte un valor de una unidad a otra.
    
    Args:
        valor: cantidad a convertir
        unidad_origen: unidad de partida
        unidad_destino: unidad de llegada
    
    Returns:
        float - valor convertido, redondeado a 4 decimales
               o -1 si la conversión no es posible
    
    Conversiones soportadas (caso insensible):
        Distancia:
        - "km" <-> "m" <-> "cm"
        - "milla" <-> "km"
        
        Peso:
        - "kg" <-> "g"
        - "kg" <-> "libra"
        
        Temperatura (casos especiales):
        - "celsius" <-> "fahrenheit"
        - "celsius" <-> "kelvin"
    
    Notas:
        - Las conversiones deben ser bidireccionales
        - Si la conversión no es posible, retorna -1
        - Las unidades pueden venir en cualquier caso (km, KM, Km)
    
    Ejemplo:
        convertir_unidades(5, "km", "m") -> 5000.0
        convertir_unidades(32, "fahrenheit", "celsius") -> 0.0
        convertir_unidades(10, "km", "libra") -> -1  # No es posible
    """
    pass


# =============================================================================
# ZONA DE PRUEBAS (descomenta para probar)
# =============================================================================

if __name__ == "__main__":
    # Importar el autoevaluador
    from autoevaluar import verificar_solucion
    
    # Ejecutar la autoevaluación
    verificar_solucion()
