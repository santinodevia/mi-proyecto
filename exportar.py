
import json


def exportar_json(datos, ruta="ventas.json"):
    """Exporta una lista de datos a un archivo JSON."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
