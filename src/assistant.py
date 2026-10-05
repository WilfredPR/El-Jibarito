from __future__ import annotations

import json
import random
from typing import Dict, List, Optional

from src.config import DEFAULT_CONFIG


class ElJibaritoAssistant:
    """Main assistant class for El Jibarito."""

    def __init__(self, config: Optional[Dict] = None):
        self.config = DEFAULT_CONFIG
        if config:
            self.config = self.config.__class__(**config)

        self.greetings = [
            "Hola, soy El Jibarito. ¿En qué te puedo ayudar hoy?",
            "¡Buenas! Yo soy El Jibarito, tu asistente de la casa.",
            "Listo para ayudarte en la cocina, la sala o la oficina.",
            "Bienvenido. Soy El Jibarito, con la energía de un buen desayuno."
        ]

        self.responses = {
            "kitchen": [
                "Tengo ideas para desayuno, almuerzo o recetas rápidas.",
                "Puedo ayudarte con recetas y tiempos de cocina.",
                "¿Qué vamos a preparar hoy? Tengo ideas para mofongo, alcapurrias y más."
            ],
            "living room": [
                "La sala está lista para relajarse, música o entretenimiento.",
                "Puedo ayudarte con la iluminación y el ambiente de la casa.",
                "¿Quieres música, películas, o simplemente charlar?"
            ],
            "computer room": [
                "Aquí puedo ayudarte con orden, foco y productividad.",
                "¿Quieres ayuda con tu computador o con tu setup?",
                "Estoy listo para ayudarte a concentrarte o resolver problemas técnicos."
            ],
            "bedroom": [
                "La habitación es tu espacio privado. ¿Necesitas relajarte o descansar?",
                "Puedo ayudarte con alarmas, música para dormir, o recordatorios."
            ],
            "default": [
                "Estoy aquí para ayudarte con tu casa y tu día.",
                "Puedo ayudarte con tareas, ambiente, música y recordatorios.",
                "Dime en qué cuarto estás y qué necesitas."
            ],
        }

    def greet(self) -> str:
        """Return a greeting from El Jibarito."""
        return random.choice(self.greetings)

    def respond(self, user_input: str) -> str:
        """Generate a response based on user input."""
        text = user_input.strip().lower()

        if not text:
            return "Estoy aquí. Dime qué necesitas."

        # Room-based responses
        if "kitchen" in text or "cocina" in text or "comida" in text:
            return random.choice(self.responses["kitchen"])

        if "living" in text or "sala" in text or "salón" in text:
            return random.choice(self.responses["living room"])

        if "computer" in text or "oficina" in text or "pc" in text or "computadora" in text:
            return random.choice(self.responses["computer room"])

        if "bedroom" in text or "habitación" in text or "cuarto" in text or "dormir" in text:
            return random.choice(self.responses["bedroom"])

        # Feature-based responses
        if "weather" in text or "clima" in text or "tiempo" in text:
            return "Puedo ayudarte a revisar el clima, y luego sugerirte el mejor plan para hoy."

        if "reminder" in text or "recordatorio" in text or "alarm" in text or "alarma" in text:
            return "Puedo ayudarte a crear recordatorios y programar tareas simples."

        if "music" in text or "música" in text or "canción" in text:
            return "Suena bien. Podemos poner música o ayudarte a crear el ambiente perfecto."

        if "hello" in text or "hola" in text or "hi" in text:
            return self.greet()

        if "help" in text or "ayuda" in text:
            return "Soy El Jibarito. Puedo ayudarte con la cocina, la sala, el cuarto de computadora, o tu habitación. ¿Dónde necesitas ayuda?"

        # Default response
        return random.choice(self.responses["default"]) + " ¿Quieres que te ayude con la cocina, la sala, el cuarto de computadora, o tu habitación?"

    def status(self) -> Dict[str, str]:
        """Return the current status and configuration of El Jibarito."""
        return {
            "name": self.config.name,
            "language": self.config.language,
            "wake_word": self.config.wake_word,
            "default_room": self.config.default_room,
            "personality": self.config.personality,
        }


if __name__ == "__main__":
    assistant = ElJibaritoAssistant()
    print(assistant.greet())
    print(assistant.respond("Hola"))
    print(json.dumps(assistant.status(), ensure_ascii=False, indent=2))
