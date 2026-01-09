import ollama
from .models import GameState

class GameMaster:
    def __init__(self, model: str = "hermes3"):
        self.model = model
        self.system_prompt = """You are an expert dungeon master running a text adventure RPG.

Rules:
- Create engaging, immersive narratives
- Keep responses to 2-3 paragraphs maximum
- Always end with 2-4 possible actions the player could take
- Remember and reference previous events
- Be creative but consistent with the established world
- Adapt difficulty and story to the player's choices
- Use vivid descriptions but stay concise

Format your responses with the story first, then list possible actions."""

    def generate_response(self, state: GameState, player_input: str) -> str:
        """Generate story response based on game state and player action"""

        # Build context from current game state
        context = f"""Current Game State:
Player: {state.player_name}
Location: {state.location}
Health: {state.health}/100
Inventory: {', '.join(state.inventory) if state.inventory else 'Empty'}

"""

        # Add recent history for context (last 4 interactions)
        if state.history:
            context += "Recent Events:\n"
            for event in state.history[-4:]:
                context += f"- Player: {event.get('action', 'Started adventure')}\n"
                if 'result' in event:
                    context += f"  Result: {event['result'][:100]}...\n"

        context += f"\nPlayer's Current Action: {player_input}"

        # Send to LLM
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": context}
            ]
        )

        return response['message']['content']
