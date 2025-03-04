class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        print(f"{item} wurde zum Inventar hinzugefügt.")
        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} wurde aus dem Inventar entfernt.")
            return True
        return False
        
    def has_item(self, item):
        return item in self.items
        
    def show_inventory(self):
        if not self.items:
            print("Dein Inventar ist leer.")
        else:
            print("In deinem Inventar befinden sich:")
            for item in self.items:
                print(f"- {item}")
