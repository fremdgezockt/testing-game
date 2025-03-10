class Room2:
    def __init__(self):
        self.is_running = True
        self.current_room = "room2"
        
    def show_room_description(self):
        print("\nDu befindest dich in einem Schlafzimmer.")
        print("Du siehst:")
        print("- Eine Tür zurück zum vorherigen Raum")
        print("- Ein großes Fenster")
        print("- Ein altes Bett")
        print("- Einen massiven Holzschrank")
    
    def run(self, player):
        print("\nDu betrittst den Raum und stellst fest das dies hier ein Schlafzimmer ist.")
        self.show_room_description()
        
        while self.is_running:
            command = input("\nWas möchtest du tun? ").lower().split()
            
            if not command:
                continue
                
            if command[0] == "hilfe":
                print("""
                Verfügbare Befehle:
                - umschauen
                - untersuche [objekt] (z.B: tür, fenster, bett, schrank)
                - benutze [objekt]
                - beende
                """)
            
            elif command[0] == "umschauen":
                self.show_room_description()
                
            elif command[0] == "untersuche":
                if len(command) < 2:
                    print("Was möchtest du untersuchen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "tür":
                    print("Eine einfache Holztür, die zurück zum vorherigen Raum führt.")
                elif objekt == "fenster":
                    print("Ein großes Fenster mit schweren Vorhängen. Draußen ist es stockdunkel.")
                elif objekt == "bett":
                    print("Ein altes, verstaubtes Bett. Es sieht schon lange unbenutzt aus.")
                elif objekt == "schrank":
                    print("Ein massiver Holzschrank. Seine Türen sind geschlossen.")
                else:
                    print("Das kannst du nicht untersuchen.")
                    
            elif command[0] == "benutze":
                if len(command) < 2:
                    print("Was möchtest du benutzen?")
                    continue
                    
                objekt = " ".join(command[1:])
                if objekt == "tür":
                    print("Du gehst zurück zum vorherigen Raum.")
                    self.is_running = False
                    return "start"
                else:
                    print("Das kannst du nicht benutzen.")
            
            elif command[0] == "beende":
                self.is_running = False
                print("Auf Wiedersehen!")
                return "quit"
                
            else:
                print("Unbekannter Befehl. Gib 'hilfe' ein für eine Liste der Befehle.")

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
            elif "fenster" in noun:
                self.fenster()
                return
            elif "bett" in noun:
                self.bett()
                return
        
        # Standardbefehle
        if command == "hilfe":
            self.hilfe()
        elif command == "inventar":
            self.zeige_inventar()
        elif "tür" in command:
            self.tuer(command)
        elif "fenster" in command:
            self.fenster()
        elif "bett" in command:
            self.bett()
        elif "truhe" in command:
            self.truhe()
        else:
            print("Das verstehe ich nicht.")

    def tuer(self, command):
        if "rote" in command or "rot" in command:
            print("\nDu gehst durch die rote Tür zurück in den ersten Raum.")
            self.game.aktuelle_raum = "raum1"
        else:
            print("Diese Tür gibt es hier nicht.")

    def fenster(self):
        print("\nDu gehst zum Fenster. Plötzlich gibt der Boden unter dir nach!")
        print("Eine Falltür öffnet sich und du stürzt in die Tiefe...")
        print("Du landest hart in einem dunklen Verlies.")
        print("\n--- SPIEL VERLOREN ---")
        self.game.spielaktiv = False

    def bett(self):
        if "bett" not in self.items_gefunden:
            if self.game.spielerklasse == "krieger":
                print("\nDu findest eine wunderschöne schlafende Prinzessin im Bett!")
                print("Sie erwacht, schenkt dir einen Kuss und verschwindet wie durch Zauberhand.")
            elif self.game.spielerklasse == "magier":
                print("\nZwischen den Kissen findest du ein altes, staubiges Zauberbuch!")
                print("Die Seiten sind voller mystischer Formeln und Zaubersprüche.")
                self.inventar.append("Zauberbuch")
            elif self.game.spielerklasse == "schurke":
                print("\nUnter dem Kopfkissen entdeckst du einen prall gefüllten Goldbeutel!")
                print("Das war ein erfolgreicher Fund!")
                self.inventar.append("Goldbeutel")
            self.items_gefunden.append("bett")
        else:
            print("Du hast das Bett bereits untersucht und alles Interessante gefunden.")

    def raumbeschreibung(self):
        print("\nDu befindest dich in einem weiteren Raum.")
        print("Hier siehst du:")
        print("- Eine rote Tür (führt zurück)")
        print("- Ein Fenster an der Wand")
        print("- Eine alte Truhe")
        print("- Ein großes Bett")
