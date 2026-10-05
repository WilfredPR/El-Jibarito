from __future__ import annotations

from src.assistant import ElJibaritoAssistant


def main() -> None:
    assistant = ElJibaritoAssistant()
    print(assistant.greet())
    while True:
        user_input = input("Tú: ")
        if user_input.lower().strip() in {"exit", "quit", "salir"}:
            print("El Jibarito: Hasta luego. ¡Que tengas un buen día!")
            break
        print(f"El Jibarito: {assistant.respond(user_input)}")


if __name__ == "__main__":
    main()
