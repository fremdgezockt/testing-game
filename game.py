from character import Character
from room2 import Room2
from inventory import Inventory
import time
import sys

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Game:
    def __init__(self):
        type_text("Hallo und willkommen zu diesem Abenteuer!")
        player_name = input("Wie ist dein Name, mutiger Abenteurer? ")
        
        while True:
            try:
                player_age = int(input("Wie alt bist du? "))
                break
            except ValueError:
                type_text("Bitte gib eine gültige Zahl ein.")
        
        type_text("\nWähle deine Klasse:")
        type_text("- Krieger (stark und mutig)")
        type_text("- Schurke (wendig und geschickt)")
        type_text("- Magier (weise und mächtig)")
        
        while True:
            player_class = input("Wähle deine Klasse: ").lower()
            if player_class == "krieger":
                player_class = "Krieger"
                break
            elif player_class == "schurke":
                player_class = "Schurke"
                break
            elif player_class == "magier":
                player_class = "Magier"
                break
            else:
                type_text("Ungültige Eingabe. Bitte wähle zwischen Krieger, Schurke oder Magier.")
        
        self.player = Character(player_name, player_age, player_class)
        type_text(f"\nWillkommen {self.player.get_name()}, du mutiger {self.player.get_class()}! Dein Abenteuer beginnt...")
        
        self.is_running = True
        self.current_room = "start"
        self.right_door_locked = True
        self.chest_opened = False
        self.inventory = Inventory()
        
    def show_room_description(self):
        if self.current_room == "start":
            type_text("\nDu befindest dich in einem dunklen Raum.")
            type_text("Du siehst:")
            type_text(f"- Eine alte {'geöffnete' if self.chest_opened else 'verschlossene'} Truhe")
            type_text("- Eine Tür zur Linken")
            type_text(f"- Eine {'verschlossene ' if self.right_door_locked else ''}Tür zur Rechten")
    
    def show_inventory(self):
        if not self.inventory:
            type_text("Dein Inventar ist leer.")
        else:
            type_text("In deinem Inventar befinden sich:")
            for item in self.inventory:
                type_text(f"- {item}")
    
    def run(self):
        type_text("\nGib 'hilfe' ein für eine Liste der Befehle.")
        self.show_room_description()
        
        while self.is_running:
            command = input("\nWas möchtest du tun? ").lower().split()
            
            if not command:
                continue
                
            if command[0] == "charakter":
                type_text(f"\nCharakter Information:")
                type_text(f"Name: {self.player.get_name()}")
                type_text(f"Alter: {self.player.get_age()}")
                type_text(f"Klasse: {self.player.get_class()}")
            
            elif command[0] == "hilfe":
                type_text("""
                Verfügbare Befehle:
                - umschauen
                - untersuche [objekt] (z.B: truhe, tür links, tür rechts)
                - öffne [objekt] (z.B: truhe)
                - nehme [objekt] (z.B: schlüssel)
                - benutze [objekt]
                - inventar
                - charakter
                - beende (oder b)
                """)
            
            elif command[0] == "umschauen":
                self.show_room_description()
                
            elif command[0] == "untersuche":
                if len(command) < 2:
                    type_text("Was möchtest du untersuchen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "truhe":
                    if self.chest_opened:
                        type_text("In der Truhe findest du einen alten, rostigen Schlüssel.")
                    else:
                        type_text("Eine alte, staubige Holztruhe. Sie scheint nicht verschlossen zu sein.")
                elif objekt == "tür links":
                    type_text("Eine einfache Holztür. Sie ist nicht verschlossen.")
                elif objekt == "tür rechts":
                    if self.right_door_locked:
                        type_text("Eine massive Tür. Sie ist verschlossen. Du brauchst einen Schlüssel.")
                    else:
                        type_text("Die Tür ist nun entriegelt.")
                else:
                    type_text("Das kannst du nicht untersuchen.")
            
            elif command[0] == "öffne":
                if len(command) < 2:
                    type_text("Was möchtest du öffnen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "truhe":
                    if self.chest_opened:
                        type_text("Die Truhe ist bereits geöffnet.")
                    else:
                        type_text("Du öffnest die Truhe. Darin liegt ein alter, rostiger Schlüssel!")
                        self.chest_opened = True
                        antwort = input("Möchtest du den Schlüssel nehmen? (ja/nein) ").lower()
                        if antwort == "ja":
                            if not self.inventory.has_item("Rostiger Schlüssel"):
                                self.inventory.add_item("Rostiger Schlüssel")
                            else:
                                type_text("Du hast den Schlüssel bereits eingesteckt.")
                else:
                    type_text("Das kannst du nicht öffnen.")
                    
            elif command[0] == "nehme":
                if len(command) < 2:
                    type_text("Was möchtest du nehmen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "schlüssel" and self.chest_opened:
                    if not self.inventory.has_item("Rostiger Schlüssel"):
                        self.inventory.add_item("Rostiger Schlüssel")
                    else:
                        type_text("Du hast den Schlüssel bereits eingesteckt.")
                else:
                    type_text("Das kannst du nicht nehmen.")
                    
            elif command[0] == "benutze":
                if len(command) < 2:
                    type_text("Was möchtest du benutzen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "tür":
                    type_text("\nWelche Tür möchtest du benutzen?")
                    type_text("1: Tür links")
                    type_text("2: Tür rechts")
                    
                    while True:
                        auswahl = input("Wähle 1 oder 2: ")
                        if auswahl == "1":
                            room2 = Room2()
                            result = room2.run(self.player)
                            if result == "game_over" or result == "quit":
                                self.is_running = False
                            break
                        elif auswahl == "2":
                            if self.inventory.has_item("Rostiger Schlüssel"):
                                type_text("Du öffnest die rechte Tür mit dem rostigen Schlüssel...")
                                type_text("Dahinter findest du einen Raum voller Gold und Schätze!")
                                type_text("GRATULATION - Du hast gewonnen!")
                                self.is_running = False
                            else:
                                type_text("Die Tür ist verschlossen. Du brauchst einen Schlüssel.")
                            break
                        else:
                            type_text("Ungültige Eingabe. Bitte wähle 1 oder 2.")
                
                elif objekt == "tür links":
                    room2 = Room2()
                    result = room2.run(self.player)
                    if result == "game_over" or result == "quit":
                        self.is_running = False
                elif objekt == "tür rechts":
                    if self.inventory.has_item("Rostiger Schlüssel"):
                        type_text("Du öffnest die rechte Tür mit dem rostigen Schlüssel...")
                        type_text("Dahinter findest du einen Raum voller Gold und Schätze!")
                        type_text("GRATULATION - Du hast gewonnen!")
                        self.is_running = False
                    else:
                        type_text("Die Tür ist verschlossen. Du brauchst einen Schlüssel.")
                elif objekt == "truhe":
                    if not self.chest_opened:
                        type_text("Du öffnest die Truhe. Darin liegt ein alter, rostiger Schlüssel!")
                        self.chest_opened = True
                    else:
                        type_text("Die Truhe ist bereits geöffnet.")
                else:
                    type_text("Das kannst du nicht benutzen.")
            
            elif command[0] == "inventar":
                self.inventory.show_inventory()
                
            elif command[0] == "beende" or command[0] == "b":
                self.is_running = False
                type_text("Auf Wiedersehen!")
                
            else:
                type_text("Unbekannter Befehl. Gib 'hilfe' ein für eine Liste der Befehle.")

    def truhe(self):
        if "truhe" not in self.items_gefunden:
            print("Du siehst eine alte Holztruhe in der Ecke des Raums.")
            if self.frage_ja_nein("Möchtest du die Truhe öffnen?"):
                print("Du öffnest die Truhe und findest einen goldenen Schlüssel!")
                self.items_gefunden.append("truhe")
                self.inventar.append("Schlüssel")
            else:
                print("Du lässt die Truhe unberührt.")
        else:
            print("Die Truhe ist bereits leer.")

    def handle_input(self, command):
        command = command.lower().strip()
        words = command.split()
        
        if not words:
            return
        
        verb = words[0]
        noun = words[1] if len(words) > 1 else ""

        # Bewegungsbefehle vereinheitlichen
        if verb in ["geh", "gehe", "benutze"]:
            if "tür" in noun:
                self.tuer(noun)
                return
        
        # Standardbefehle
        if command == "hilfe":
            self.hilfe()
        elif command == "inventar":
            self.zeige_inventar()
        elif "tür" in command:
            self.tuer(command)
        elif "truhe" in command:
            self.truhe()
        else:
            print("Das verstehe ich nicht.")

if __name__ == "__main__":
    game = Game()
    game.run()