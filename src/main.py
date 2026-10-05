from __future__ import annotations

from src.assistant import ElJibaritoAssistant


def main() -> None:
    """Main CLI loop for El Jibarito assistant."""
    assistant = ElJibaritoAssistant()
    print(assistant.greet())
    print()
    while True:
        try:
            user_input = input("Tú: ").strip()
            if user_input.lower() in {"exit", "quit", "salir", "adiós", "adios"}:
                print("El Jibarito: Hasta luego. ¡Que tengas un buen día!")
                break
            if not user_input:
                continue
            print(f"El Jibarito: {assistant.respond(user_input)}")
            print()
        except KeyboardInterrupt:
            print("\nEl Jibarito: Hasta luego. ¡Que tengas un buen día!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
