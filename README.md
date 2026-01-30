# 🎲 LuminaQuest

> A gritty, dynamic terminal RPG engine that transforms your CLI into a living world, powered by local LLMs through Ollama.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Tech: Python](https://img.shields.io/badge/Tech-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tech: Ollama](https://img.shields.io/badge/Tech-Ollama-black?logo=ollama)](https://ollama.com/)
[![AI: Hermes 3](https://img.shields.io/badge/AI-Hermes_3-6A0DAD)](https://ollama.com/library/hermes3)

---

## 🧐 What is this?

**LuminaQuest** is a focused terminal-based adventure engine designed to replace static, pre-written game scripts with a dynamic AI Dungeon Master. By leveraging **Hermes 3** via **Ollama**, it creates unscripted, immersive narratives that adapt to every player choice. The engine maintains complex game states including inventory, health, and location, ensuring a consistent RPG experience while allowing for infinite storytelling possibilities directly in your terminal.

## 🛠️ Tech Stack

This project is a lightweight Python application built for local-first AI interactions.

| Component        | Technology   | Key Libraries/Frameworks         |
| :--------------- | :----------- | :------------------------------- |
| **Language**     | Python 3.10+ | Core Runtime                     |
| **AI Interface** | Ollama       | `ollama-python`                  |
| **UI/Terminal**  | Rich         | `rich` (Panels, Prompts, Colors) |
| **Data Models**  | Pydantic     | `pydantic` (State Serialization) |
| **AI Model**     | Hermes 3     | Llama-3-based fine-tune          |

## 🚀 Quick Start

The following instructions are optimized for a Linux environment (Ubuntu/Debian).

### Prerequisites

1.  **Install Ollama**

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2.  **Pull the AI Model**
    ```bash
    ollama pull hermes3
    ```

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/RyanMaxiemus/luminaquest.git
    cd luminaquest
    ```

2.  **Setup Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Game**
    ```bash
    python3 main.py
    ```

## 🎮 How to Play

Once the game starts, you can interact with the Dungeon Master using natural language.

- **Actions:** Simply type what you want to do (e.g., "Examine the glowing runes" or "Talk to the mysterious hooded figure").
- **Commands:**
  - `status` or `i`: View your health, location, and inventory.
  - `save` or `s`: Save your current progress.
  - `help` or `h`: Show available commands.
  - `quit` or `q`: Exit the adventure.

## 🤝 Contributing

Got an idea for a better system prompt? Want to add a combat system or a fancy GUI? We’d love to have you involved!

1.  **Spotted a bug?** Open an issue and let us know. We appreciate the heads-up.
2.  **Have a feature idea?** Let's chat about it in the issues first so we're on the same page.
3.  **Ready to code?** Fork the repo, create a branch, and keep your commits clean (e.g., `feat: add inventory weight system`).
4.  **Send the PR:** We'll review it and get your changes merged as soon as we can.

Let's build the ultimate terminal-based AI adventure together.
