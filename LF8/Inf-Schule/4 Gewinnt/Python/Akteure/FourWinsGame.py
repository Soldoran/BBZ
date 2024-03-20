# -*- coding: utf-8 -*-

#Imports
import Player
import GUI
import Fields
import RuleSet
import os

class FourWinsGame:

# Konstruktor
    def __init__(self, player1: Player, player2: Player, gui: GUI, fields: Fields, ruleSet: RuleSet):
        self.player1 = PlayerClass
        self.player2 = PlayerClass
        self.gui = gui
        self.fields = fields
        self.ruleSet = ruleSet

# Funktionen
    def initializeGame(self):
        '''
        Initialisieren des Spieles.
        Abfragen der Spielerdaten (Name, Spielmodus)
        '''
        # Name und Spielmodus für Spieler 1, sowie die playerID
        self.player1.setName(self.gui.getName())
        self.player1.setGameMode(self.gui.getGameMode(self.player1.getName()))
        self.player1.setID('X')

        # Name und Spielmodus für Spieler 2, sowie die playerID
        self.player2.setName(self.gui.getName())
        self.player2.setGameMode(self.gui.getGameMode(self.player2.getName()))
        self.player2.setID('O')

    def startGame(self):
        '''
        Das Starten der eigentlichen Gameloop
        '''
        gameStopped = False
        turnCount = 1
        currentPlayer = self.player1
        curDraw = 0
        legalDraw = True
        gameisDraw = False

        while not gameStopped:
            os.system("cls")        # Leert das Fenster

            # Das Spielfeld zeichnen
            self.gui.outputField(self.fields.getFields())

            # Anzeigen welcher Spieler am Zug ist
            if turnCount % 2 == 0:
                currentPlayer = self.player2
            else:
                currentPlayer = self.player1

            print(f"Spieler {currentPlayer.getName()} ist am Zug.")

            # Den Zug von currentPlayer abfragen
            curDraw = currentPlayer.playDraw(self.gui)

            # Überprüpfen ob der Zug legal ist
            legalDraw = self.ruleSet.checkDraw(self.fields.getFields(), curDraw)

            if not legalDraw:
                print("Zug kann nicht ausgeführt werden. Drücke Enter-Taste um den Zug zu wiederholen.")
                input()
                continue
            else:
                # Zug ist legal, also muss nichts weiter getan werden

            # Nun kann der Zug ausgeführt werden
            self.fields.setFields(curDraw, currentPlayer.getID())

            # Überprüfen ob das Spiel beendet ist
            gameStopped = self.ruleSet.checkPlayerWon(self.fields.getFields(), currentPlayer, curDraw)

            if gameStopped:
                # Der Spieler hat gewonnen
            else:
                # Überprüfen ob es noch einen legalen Zug gibt, ansonsten wird das Spiel nicht gestoppt
                gameStopped != self.ruleSet.checkGameOver(self.fields.getFields())

            # Den nächsten Zug vorbereiten
            turnCount += 1

        # Ende der while not Loop

if __name__ == '__main__':
    p1 = Player()
    p2 = Player()
    gui = GUI()
    fields = Fields()
    rules = RuleSet()

    gameManager = FourWinsGame(p1, p2, gui, fields, rules)

    gameManager.initializeGame()
    gameManager.startGame()
