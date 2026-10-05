from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional


@dataclass
class AssistantConfig:
    """Configuration for El Jibarito assistant."""
    name: str = "El Jibarito"
    language: str = "es"
    personality: str = (
        "A friendly Puerto Rican AI assistant with warmth, humor, and practical help. "
        "Speaks naturally in Spanish and English, uses a welcoming tone, and feels like a helpful home companion."
    )
    wake_word: str = "jibarito"
    default_room: str = "living room"
    rooms: List[str] = None
    skills: List[str] = None

    def __post_init__(self):
        if self.rooms is None:
            self.rooms = ["kitchen", "living room", "bedroom", "computer room"]
        if self.skills is None:
            self.skills = [
                "weather",
                "reminders",
                "music",
                "lighting",
                "kitchen recipes",
                "time and schedule",
                "home status",
            ]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


DEFAULT_CONFIG = AssistantConfig()


def load_config(path: str) -> AssistantConfig:
    """Load configuration from JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return AssistantConfig(**data)
    except FileNotFoundError:
        return DEFAULT_CONFIG
    except json.JSONDecodeError:
        return DEFAULT_CONFIG


def save_config(config: AssistantConfig, path: str) -> None:
    """Save configuration to JSON file."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(config.to_dict(), fh, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    config = DEFAULT_CONFIG
    print(json.dumps(config.to_dict(), ensure_ascii=False, indent=2))
