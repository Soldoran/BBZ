# -*- coding: utf-8 -*-

#Imports
from Player import Player
from GUI import GUI
from Field import Field
from RuleSet import RuleSet
import os

class FourWinsGame:

# Konstruktor
    def __init__(self, player1ID: chr, player2ID: chr):
        self.player1ID = player1ID
        self.player2ID = player2ID

        # Initialisieren der Attribute mit Standardwerten
        self.player1 = None
        self.player2 = None
        self.gui = None
        self.ruleSet = None
        self.fields = None

# Funktionen
    def initializeGame(self):
        '''
        Initialisieren des Spieles.
        Abfragen der Spielerdaten (Name, Spielmodus)
        '''
        # Das Spielfeld initialisieren
        self.fields = Field()

        # Das RuleSet initialisieren
        self.ruleSet = RuleSet()

        # Das GUI initialisieren
        self.gui = GUI()

        # Initialisieren Spieler 1
        name = self.gui.getName(1)
        gM = self.gui.getGameMode(name)
        iD = self.player1ID
        self.player1 = Player(iD, gM, name)

        # Initialisieren Spieler 2
        name = self.gui.getName(2)
        gM = self.gui.getGameMode(name)
        iD = self.player2ID
        self.player2 = Player(iD, gM, name)


    def startGame(self):
        '''
        Das Starten der eigentlichen Gameloop
        '''
        gameStopped = False
        turnCount = 1
        currentPlayer = None
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
                continue        # Springt zum Anfang der Schleife zurück
            else:
                # Zug ist legal, also muss nichts weiter getan werden
                pass

            # Nun kann der Zug ausgeführt werden
            self.fields.setFields(curDraw, currentPlayer.getID())

            # Überprüfen ob das Spiel beendet ist
            gameStopped = self.ruleSet.checkPlayerWon(self.fields, currentPlayer, curDraw)

            if gameStopped:
                # Der Spieler hat gewonnen
                os.system("cls")        # Leert das Fenster

                # Das Spielfeld zeichnen
                self.gui.outputField(self.fields.getFields())

                print(f"{currentPlayer.getName()} hat gewonnen!")
                input("Drücke Enter zum beenden.")
                pass
            else:
                # Überprüfen ob es noch einen legalen Zug gibt, ansonsten wird das Spiel nicht gestoppt
                gameStopped != self.ruleSet.checkGameOver(self.fields)

            # Den nächsten Zug vorbereiten
            turnCount += 1

        # Ende der while not Loop

if __name__ == '__main__':
    gameManager = FourWinsGame('X','O')

    gameManager.initializeGame()
    gameManager.startGame()
