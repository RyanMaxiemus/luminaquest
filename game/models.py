from pydantic import BaseModel
from typing import List
from pathlib import Path

class GameState(BaseModel):
    player_name: str
    location: str
    inventory: List[str] = []
    health: int = 100
    history: List[dict] = []

    def save(self, filepath: Path):
        """Save game state to JSON file"""
        filepath.write_text(self.model_dump_json(indent=2))

    @classmethod
    def load(cls, filepath: Path):
        """Load game state from JSON file"""
        return cls.model_validate_json(filepath.read_text())
