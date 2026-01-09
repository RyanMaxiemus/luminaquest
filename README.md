# 🎲 LuminaQuest: Terminal RPG

LuminaQuest is a text-based adventure engine powered by a **Local LLM**. It replaces static scripts with a dynamic AI Dungeon Master capable of gritty, unscripted storytelling.

## 🚀 Quick Start

1. **Prerequisites:**

   - Install [Ollama](https://ollama.com/)
   - Pull the model: `ollama run hermes3`

2. **Setup:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Play:**

   ```bash
   python main.py
   ```

## 🛠️ Tech Stack

- **AI Brain:** Hermes 3 (via Ollama)
- **State Management:** Pydantic
- **Interface:** Rich (Python CLI library)

## ⚖️ License

Distributed under the MIT License. See [LICENSE](/LICENSE) for more information.
