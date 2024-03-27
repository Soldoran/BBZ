# -*- coding: utf-8 -*-
# Imports
import random
import os

class Player:

    def __init__(self, player_id, game_mode, name=None):
        '''
        Konstruktor für die Klasse Player.

        Parameter:
        player_id: chr
            Das Symbol welches für den Spieler benutzt wird.
        game_mode: int
            Der Spielmodus des Spielers
        name=None: string
            Der Name des Spielers
        '''
        self.playerID = player_id
        self.gameMode = game_mode

         if name is None:
            self.name = "Spieler " + str(player_id)
        else:
            self.name = name

    def getName(self):
        '''
        Getter für den Spielernamen.
        Gibt den Namen des Spielers zurück.
        '''
        return self.name

    def setName(self, name):
        '''
        Setter für den Spielernamen.
        Setzt den Namen des Spielers auf den Wert 'name'

        Parameter
        name: string
            Der Name, für den Spieler
        '''
        self.name = name

    def getID(self):
        '''
        Getter für die ID des Spielers.
        Gibt die ID des Spielers zurück
        '''
        return self.playerID

    def setID(self, playerID):
        '''
        Setter für die ID des Spielers.
        Setzt die ID des Spielers auf den Wert 'playerID'

        Parameter
        playerID: chr
            Der Character, welcher für den Spieler benutzt wird.
        '''
        self.playerID = playerID

    def getGameMode(self):
        '''
        Getter für den Spielmodus des Spielers.
        Gibt den Spielmodus des Spielers zurück.

        Spielmodi:
        1 - Zufällig (Computer)
        2 - Eingabe (Spieler)
        '''
        return self.gameMode

    def setgameMode(self, gameMode: int):
        '''
        Setter für den Spielmodus des Spielers.
        Setzt den Spielmodus des Spielers auf den Wert 'gameMode'

        Parameter:
        gameMode: int

        Spielmodi:
        1 - Zufällig (Computer)
        2 - Eingabe (Spieler)
        '''
        self.gameMode = gameMode

    def playDraw(self, gui):
        '''
        Führt den Zug des Spielers anhand des Spielmodus mithilfe der GUI-Methode 'getDraw(name)' aus.

        Parameter:
        gui: GUI
        '''

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
