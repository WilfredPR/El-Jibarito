"""Basic tests for El Jibarito assistant."""

from __future__ import annotations

from src.assistant import ElJibaritoAssistant


def test_basic_assistant_response() -> None:
    """Test that assistant generates valid responses."""
    assistant = ElJibaritoAssistant()

    greeting = assistant.greet()
    assert isinstance(greeting, str)
    assert len(greeting) > 0

    kitchen_response = assistant.respond("kitchen")
    assert isinstance(kitchen_response, str)
    assert len(kitchen_response) > 0

    living_room_response = assistant.respond("living room")
    assert isinstance(living_room_response, str)
    assert len(living_room_response) > 0


def test_status_contains_name() -> None:
    """Test that assistant status contains required fields."""
    assistant = ElJibaritoAssistant()
    status = assistant.status()
    assert "name" in status
    assert status["name"] == "El Jibarito"
    assert "language" in status
    assert "wake_word" in status


def test_room_detection() -> None:
    """Test that assistant correctly identifies room commands."""
    assistant = ElJibaritoAssistant()
    
    kitchen = assistant.respond("cocina")
    assert "receta" in kitchen.lower() or "comida" in kitchen.lower()
    
    living = assistant.respond("sala")
    assert "música" in living.lower() or "iluminación" in living.lower() or "relajarse" in living.lower()


def test_empty_input() -> None:
    """Test that assistant handles empty input gracefully."""
    assistant = ElJibaritoAssistant()
    response = assistant.respond("")
    assert isinstance(response, str)
    assert len(response) > 0
