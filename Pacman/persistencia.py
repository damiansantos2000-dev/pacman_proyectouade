
import json
import uuid
from pathlib import Path
from datetime import datetime


class GestorPuntuaciones:
    def __init__(self, nombre_archivo="puntuaciones.json"):
        self._nombre_archivo = Path(__file__).with_name(
            nombre_archivo
        )

    @property
    def nombre_archivo(self):
        return str(self._nombre_archivo)

    def _leer_archivo(self):
        if not self._nombre_archivo.exists():
            return []

        try:
            with open(
                self._nombre_archivo, "r", encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            return datos if isinstance(datos, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    def guardar_puntuacion(self, nombre, puntaje):
        puntuaciones = self._leer_archivo()

        registro = {
            "id": str(uuid.uuid4()),
            "nombre": nombre,
            "puntaje": puntaje,
            "fecha": datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )
        }

        puntuaciones.append(registro)

        with open(
            self._nombre_archivo, "w", encoding="utf-8"
        ) as archivo:
            json.dump(
                puntuaciones,
                archivo,
                ensure_ascii=False,
                indent=4
            )

    def obtener_mejores_puntuaciones(self):
        puntuaciones = self._leer_archivo()

        puntuaciones.sort(
            key=lambda registro: registro.get("puntaje", 0),
            reverse=True
        )

        return puntuaciones[:5]
