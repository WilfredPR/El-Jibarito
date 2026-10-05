# El Jibarito

A Puerto Rican-inspired AI assistant with a 3D-printed Jibarito body and LED face screen.

## Project vision

El Jibarito is a smart home / personal assistant built with a warm, friendly Puerto Rican personality. It is designed to feel like a playful, helpful companion with a custom physical form inspired by the classic Puerto Rican sandwich.

This project is being developed in phases:

1. Voice assistant core
2. Personality and local knowledge base
3. LED face and animation system
4. 3D-printed shell design integration
5. Smart home and room automation features

## Core concept

- Voice-driven assistant
- Puerto Rican bilingual personality (English + Spanish)
- Home and room assistant for kitchen, living room, bedroom, and computer room
- Friendly, expressive LED face
- Personality inspired by local culture and humor
- Built for a Raspberry Pi and 3D-enclosed hardware setup

## Recommended hardware

- Raspberry Pi 4 or 5
- USB microphone
- Small speaker or amplifier
- LED face display or matrix screen
- 3D-printed body shell (Bambu Lab A1 mini)
- Optional: Wi-Fi / smart plug integration for home automation

## Recommended software stack

- Python
- Speech recognition library
- Text-to-speech library
- GPIO / screen control libraries
- Optional: Flask or simple local web dashboard

## Project structure

```text
El-Jibarito/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── assistant.py
│   ├── config.py
│   ├── voice.py
│   ├── led_face.py
│   └── home_features.py
├── tests/
│   └── test_basic.py
└── docs/
    └── hardware-notes.md
```

## Example personality responses

- "Hola, soy El Jibarito. ¿En qué te puedo ayudar hoy?"
- "Estoy listo para ayudarte en la cocina, la sala, o la oficina."
- "No te preocupes, aquí estoy con la energía de un buen desayuno y un buen consejo."

## Current focus

The first milestone is to build a simple local assistant with:

- wake word / command listening
- text-to-speech
- simple commands for weather, reminders, and room checking
- starter LED face expressions

## Getting started

1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the assistant: `python src/main.py`
5. Expand with hardware integrations

## License

MIT
