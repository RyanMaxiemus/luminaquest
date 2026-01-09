from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from pathlib import Path
from .models import GameState
from .llm import GameMaster

console = Console()

class GameEngine:
    def __init__(self):
        self.gm = GameMaster()
        self.state = None
        self.save_dir = Path("saves")
        self.save_dir.mkdir(exist_ok=True)

    def start_menu(self):
        """Display main menu and handle choice"""
        console.print(Panel.fit(
            "[bold cyan]🎮 TERMINAL RPG 🎮[/bold cyan]\n"
            "[dim]Powered by Hermes 3[/dim]",
            border_style="cyan"
        ))

        console.print("\n[yellow]1.[/yellow] New Game")
        console.print("[yellow]2.[/yellow] Load Game")
        console.print("[yellow]3.[/yellow] Exit\n")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3"])

        if choice == "1":
            self.new_game()
        elif choice == "2":
            self.load_game()
        else:
            console.print("[cyan]Farewell, adventurer![/cyan]")
            return False

        return True

    def new_game(self):
        """Start a new game"""
        console.clear()
        console.print(Panel("[bold green]Starting New Adventure[/bold green]"))

        name = Prompt.ask("\n[yellow]What is your character's name?[/yellow]")

        self.state = GameState(
            player_name=name,
            location="the entrance of a mysterious dungeon"
        )

        # Generate opening scene
        console.print("\n[dim]The adventure begins...[/dim]\n")
        intro = self.gm.generate_response(self.state, "Begin the adventure. Describe the starting scene.")

        console.print(Panel(intro, title="[bold]The Story Begins[/bold]", border_style="green"))

        self.state.history.append({
            "action": "Started adventure",
            "result": intro[:200]
        })

    def load_game(self):
        """Load an existing save file"""
        saves = list(self.save_dir.glob("*.json"))

        if not saves:
            console.print("[red]No save files found![/red]")
            input("\nPress Enter to continue...")
            return

        console.print("\n[yellow]Available saves:[/yellow]")
        for i, save in enumerate(saves, 1):
            console.print(f"{i}. {save.stem}")

        choice = Prompt.ask("Choose a save", choices=[str(i) for i in range(1, len(saves) + 1)])

        self.state = GameState.load(saves[int(choice) - 1])
        console.print(f"\n[green]Loaded game: {self.state.player_name}[/green]")
        console.print(f"[dim]Location: {self.state.location}[/dim]")
        console.print(f"[dim]Health: {self.state.health}/100[/dim]\n")

    def save_game(self):
        """Save current game state"""
        if not self.state:
            return

        save_path = self.save_dir / f"{self.state.player_name.lower().replace(' ', '_')}.json"
        self.state.save(save_path)
        console.print(f"\n[green]✓ Game saved![/green]")

    def show_status(self):
        """Display current player status"""
        console.print(f"\n[cyan]═══ Status ═══[/cyan]")
        console.print(f"[yellow]Name:[/yellow] {self.state.player_name}")
        console.print(f"[yellow]Location:[/yellow] {self.state.location}")
        console.print(f"[yellow]Health:[/yellow] {self.state.health}/100")
        console.print(f"[yellow]Inventory:[/yellow] {', '.join(self.state.inventory) if self.state.inventory else 'Empty'}")
        console.print(f"[cyan]═════════════[/cyan]\n")

    def play_turn(self):
        """Execute one turn of gameplay"""
        action = Prompt.ask("\n[bold cyan]What do you do?[/bold cyan]")

        # Handle special commands
        if action.lower() in ['quit', 'exit', 'q']:
            if Confirm.ask("\nSave before exiting?"):
                self.save_game()
            return False

        if action.lower() in ['save', 's']:
            self.save_game()
            return True

        if action.lower() in ['status', 'stat', 'i']:
            self.show_status()
            return True

        if action.lower() in ['help', 'h']:
            console.print("\n[yellow]Commands:[/yellow]")
            console.print("  [cyan]save/s[/cyan] - Save game")
            console.print("  [cyan]status/i[/cyan] - Show status")
            console.print("  [cyan]help/h[/cyan] - Show this help")
            console.print("  [cyan]quit/q[/cyan] - Exit game\n")
            return True

        # Generate story response
        console.print("\n[dim]The dungeon master considers...[/dim]\n")

        try:
            response = self.gm.generate_response(self.state, action)
            console.print(Panel(response, border_style="blue", title="[bold]Story[/bold]"))

            # Update game history
            self.state.history.append({
                "action": action,
                "result": response[:200]
            })

        except Exception as e:
            console.print(f"[red]Error generating response: {e}[/red]")
            console.print("[yellow]Make sure Ollama is running and hermes3 is installed.[/yellow]")

        return True

    def run(self):
        """Main game loop"""
        if not self.start_menu():
            return

        console.print("\n[dim]Type 'help' for commands[/dim]")

        playing = True
        while playing:
            try:
                playing = self.play_turn()
            except KeyboardInterrupt:
                console.print("\n\n[yellow]Game interrupted![/yellow]")
                if Confirm.ask("Save before exiting?"):
                    self.save_game()
                break
            except Exception as e:
                console.print(f"\n[red]Unexpected error: {e}[/red]")
                if Confirm.ask("Continue playing?"):
                    continue
                else:
                    break

        console.print("\n[bold cyan]Thanks for playing! May your adventures continue...[/bold cyan]\n")
