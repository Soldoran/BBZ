# -*- coding: utf-8 -*-
# Imports
import random
import os

class Player:

# Konstruktor
    def __init__(self, player_id, game_mode, name=None):
       self.playerID = player_id
       self.gameMode = game_mode

       if name is None:
           self.name = "Spieler" + str(player_id)
       else:
           self.name = name

# Funktionen
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getID(self):
        return self.playerID

    def setID(self, playerID):
        self.playerID = playerID

    def getGameMode(self):
        return self.gameMode

    def setgameMode(self, gameMode: int):
        # Diese Klasse ist von Inf-Schule nicht vorgesehen
        self.gameMode = gameMode

    def playDraw(self, gui):
        # Mensch oder Computer
        if (self.gameMode == 2):
            # Mensch
            col = gui.getDraw(self.name)
            return col
        else:
            # Computer
            # Zufallsentscheidung
            col = random.randint(0,6)
            print ("Col: " + str(col))
            return col

if __name__ == '__main__':
    os.system("cls")

    print(f"Initialize Player: Bob")
    p = Player('O', 2, "Bob")

    print(f"Player named '{p.getName()}' initialized.")
    print(f"Change Playername from '{p.getName()}' to 'Alfred'.")
    p.setName('Alfred')
    print(f"New Playername is: {p.getName()}")

    print(f"Current PlayerID is: '{p.getID()}'")
    print(f"Set PlayerID to 'X'")
    p.setID('X')
    print(f"New PlayerID for Player '{p.getName()}' is: {p.getID()}")

    print(f"Current Gamemode for '{p.getName()}' is: {p.getGameMode()}")
    print(f"Change Gamemode...")
    p.setgameMode(1)
    print(f"New Gamemode for Player '{p.getName()}' is: {p.getGameMode()}")

    print("Testing complete.")
    input("Press Enter to Exit.")
