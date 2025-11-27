#Instance and class Attributes

class Player:
    player_count = 0
    
    def __init__(self, name , level):
        self.name = name
        self.level = level
        Player.player_count += 1


p1 = Player("Alice", 5)
p2 = Player("Bob", 10)

print("Total players created:", Player.player_count)