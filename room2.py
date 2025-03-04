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
