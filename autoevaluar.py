"""
AUTOEVALUACIÓN: Verificar type hints en la práctica
====================================================

USO: Desde tu practica.py, llama a esto al final:

    from autoevaluar import verificar_solucion
    
    if __name__ == "__main__":
        verificar_solucion()

Verifica:
  1. Tipos: ¿Los type hints son correctos?
  2. Resultado: ¿La función funciona correctamente?
"""

import inspect
from typing import get_type_hints
import sys

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def _obtener_modulos():
    """Obtiene los módulos practica y solucion"""
    try:
        import practica
        import solucion
        return practica, solucion
    except ImportError as e:
        print(f"Error: No se pueden importar los módulos. {e}")
        return None, None


def verificar_tipos(nombre_func, modulo_practica, modulo_solucion):
    """Verifica si los type hints son correctos"""
    func_practica = getattr(modulo_practica, nombre_func, None)
    func_solucion = getattr(modulo_solucion, nombre_func, None)
    
    if not func_practica or not func_solucion:
        return False, None, None
    
    try:
        hints_practica = get_type_hints(func_practica)
        hints_solucion = get_type_hints(func_solucion)
    except:
        hints_practica = {}
        hints_solucion = {}
    
    correcto = hints_practica == hints_solucion
    return correcto, hints_practica, hints_solucion


def ejecutar_test(nombre_func, modulo_practica, casos_prueba):
    """Verifica si la función funciona correctamente"""
    func = getattr(modulo_practica, nombre_func, None)
    if not func:
        return False
    
    for entrada, esperado in casos_prueba:
        try:
            resultado = func(*entrada)
            if resultado != esperado:
                return False
        except:
            return False
    
    return True


def obtener_casos_prueba(nombre_func):
    """Retorna casos de prueba para cada función"""
    casos = {
        "validar_email": [
            (("usuario@ejemplo.com",), {"valido": True, "razon": ""}),
            (("usuario@ejemplo",), {"valido": False, "razon": "Debe contener un punto '.' después del '@'"}),
            (("usuario@@ejemplo.com",), {"valido": False, "razon": "Debe contener exactamente un símbolo '@'"}),
        ],
        "analizar_texto": [
            (("hola mundo hola",), {
                "total_palabras": 3,
                "total_caracteres": 13,
                "palabras_unicas": 2,
                "promedio_longitud": 4.33,
                "palabra_mas_larga": "mundo"
            }),
        ],
        "actualizar_inventario": [
            (
                ({"manzanas": 10}, [{"producto": "manzanas", "cantidad": -3}]),
                {"manzanas": 7}
            ),
        ],
        "clasificar_estudiantes": [
            (
                ([{"nombre": "Ana", "calificacion": 8.5}],),
                {
                    "aprobados": [{"nombre": "Ana", "calificacion": 8.5}],
                    "reprobados": [],
                    "promedio_general": 8.5,
                    "mejor_estudiante": "Ana",
                    "peor_estudiante": "Ana"
                }
            ),
        ],
        "convertir_unidades": [
            ((5, "km", "m"), 5000.0),
            ((32, "fahrenheit", "celsius"), 0.0),
            ((10, "km", "libra"), -1),
        ],
    }
    return casos.get(nombre_func, [])


def verificar_solucion():
    """Función principal a invocar desde practica.py o solucion.py"""
    
    # Importar módulos
    modulo_practica, modulo_solucion = _obtener_modulos()
    if not modulo_practica or not modulo_solucion:
        return
    
    # Detectar si se ejecuta desde solucion.py
    import __main__
    es_solucion = hasattr(__main__, '__file__') and 'solucion' in __main__.__file__
    
    if es_solucion:
        # Si se ejecuta desde solucion.py, comparar solucion con solucion
        modulo_a_evaluar = modulo_solucion
        modulo_referencia = modulo_solucion
    else:
        # Si se ejecuta desde practica.py, comparar practica con solucion
        modulo_a_evaluar = modulo_practica
        modulo_referencia = modulo_solucion
    
    funciones = [
        "validar_email",
        "analizar_texto",
        "actualizar_inventario",
        "clasificar_estudiantes",
        "convertir_unidades"
    ]
    
    print("\n" + "="*70)
    print("AUTOEVALUACION - PRACTICA DE TYPE HINTS")
    print("="*70 + "\n")
    
    print(f"{'Funcion':<30} {'Tipos':<10} {'Resultado':<10}")
    print("-" * 70)
    
    for nombre_func in funciones:
        # Verificar tipos
        tipos_ok, hints_practica, hints_solucion = verificar_tipos(nombre_func, modulo_a_evaluar, modulo_referencia)
        estado_tipos = "PASA" if tipos_ok else "NO PASA"
        
        # Verificar resultado
        casos = obtener_casos_prueba(nombre_func)
        resultado_ok = ejecutar_test(nombre_func, modulo_a_evaluar, casos)
        estado_resultado = "PASA" if resultado_ok else "NO PASA"
        
        print(f"{nombre_func:<30} {estado_tipos:<10} {estado_resultado:<10}")
    
    print("="*70 + "\n")


if __name__ == "__main__":
    verificar_solucion()
