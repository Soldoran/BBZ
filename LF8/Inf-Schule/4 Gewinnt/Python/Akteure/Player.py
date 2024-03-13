# -*- coding: utf-8 -*-
# Imports

class Player:

# Konstruktor
   def __init__(self, player_id, game_mode, name=None):
       self.player_id = player_id
       self.game_mode = game_mode

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

    def playDraw(self, gui):
        # Mensch oder Computer
        if (self.name != ("Spieler" + self.player_id))
            # Mensch
            col = gui.getDraw(self.__name)
            return col
        else
            # Computer
            # Zufallsentscheidung
            col = random.randint(0,6)
            print ("Col: " + str(col))
            return col
