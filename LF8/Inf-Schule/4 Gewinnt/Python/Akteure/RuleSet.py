# -*- coding: utf-8 -*-

#Imports
from Player import Player
from Field import Field
import os

class RuleSet:

# Konstruktor
    def __init__(self):
        pass


# Funktionen
    def checkDraw(self, field, col):
        '''
        Überprüfen ob ein Zug legal ist (In der Spalte war noch Platz)
        '''
        for row in field:        # Wir gehen jede Reihe einmal durch, mit 'row[col]' schauen wir anschließend an die richtige Koordinate
            if row[col] == " ":
                return True         # Hier ist es egal, wo in der Spalte der Zug legal ist, daher können wir bei einem Treffer direkt 'True' zurückgeben
        return False                # Wir hatten keinen Treffer, also ist der Zug nicht legal. Wir geben 'False' zurück

    def checkPlayerWon(self, field, player, col):
        '''
        Überprüfen ob der letzte Zug einen Spieler zum Sieg geführt hat
        '''
        # Variablen
        fields = field.getFields()
        lastRow = field.getLastRow()
        lastCol = field.getLastCol()
        teamcolor = player.getID()
        touchingStones = []

        # Check Rows
        for row in fields:
            for column in row:
                if column == teamcolor:
                    touchingStones.append(column)
                else:
                    if column != lastCol:
                        touchingStones = []

        if len(touchingStones) == 4:
            return True

        # Check Columns
        for row in fields:
            if row[col] == teamcolor:
                touchingStones.append(row[col])
            else:
                touchingStones = []

        if len(touchingStones) == 4:
            return True

        # Check Diagonal von links oben nach rechts unten
        for (i, row) in enumerate(fields):
            if i < len(fields) - 3:
                for (j, col) in enumerate(row):
                    if j > len(row) - 4:
                        # Diagonale nicht möglich
                        continue
                    else:
                        # Diagonale möglich
                        if (row[j] == teamcolor and
                            fields[i + 1][j + 1] == teamcolor and
                            fields[i + 2][j + 2] == teamcolor and
                            fields[i + 3][j + 3] == teamcolor):
                            return True
                        else:
                            #print(f"Checked: '{row[j]}' + '{row[j+1]}' + '{row[j+2]}' + '{row[j+3]}'")
                            pass
            else:
                # Zu wenig Zeilen nach unten hin
                continue

        # Check Diagonal von rechts oben nach links unten
        for (i, row) in enumerate(fields):
            if i < len(fields) - 3:
                for (j, col) in enumerate(row):
                    if j < len(row) - 4:
                        # Diagonale nicht möglich
                        continue
                    else:
                        # Diagonale möglich
                        if (row[j] == teamcolor and
                            fields[i + 1][j - 1] == teamcolor and
                            fields[i + 2][j - 2] == teamcolor and
                            fields[i + 3][j - 3] == teamcolor):
                            return True
                        else:
                            pass
            else:
                # Zu wenig Zeilen nach unten hin
                continue
        
        # Keine Siegbedingung wurde erfüllt
        return False


    def checkGameOver(self, field):
        '''
        Überprüfen ob es noch freie Felder in der letzten Reihe gibt, um einen legalen Zug auszuführen
        '''
        fields = field.getFields()
        return all(cell != " " for cell in fields[-1])   # Da beim letzten legalen Zug in der obersten Reihe ein freies Feld sein muss, reicht es, sich diese Zeile anzuschauen

if __name__ == '__main__':
    rules = RuleSet()
    field = Field()

    # Testfelder für Siegbedingungen
    fullField = [["Z" for _ in range(7)] for _ in range(6)]
    turnField = [
            ["O", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            ["O", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            ["O", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "]
            ]
    horizontalWinField = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["O", "O", "O", " ", " ", " ", " "],
            ["X", "X", "X", "X", " ", " ", " "]
            ]

    verticalWinField = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            ["X", "O", " ", " ", " ", " ", " "],
            ["X", "O", " ", " ", " ", " ", " "],
            ["X", "O", " ", " ", " ", " ", " "]
            ]
    diagonalLeftRightWinField = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " "],
            ["O", "X", " ", " ", " ", " ", " "],
            ["X", "O", "X", " ", " ", " ", " "],
            ["O", "X", "O", "X", " ", " ", " "]
            ]
    diagonalRightLeftWinField = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "X", " ", " ", " "],
            [" ", " ", "X", "O", " ", " ", " "],
            [" ", "X", "O", "X", " ", " ", " "],
            ["X", "O", "X", "O", " ", " ", " "]
            ]

    # Clear Screen
    os.system("cls")

    # Initialisieren des Spielers zum TestenWin
    player = Player("X", 2, "Bob")

    # Testen der Logik für legalen Zug
    field.fields = turnField
    print("Testing legal move. Expection: False")
    val = rules.checkDraw(field.fields, 0)
    print(f"Result: {val}\n")

    # Testen der Logik ob ein Spieler Gewonnen hat (in mehreren Schritten)
    # Schritt 1: Horizontal
    field.fields = horizontalWinField
    print("Testing horizontal Win. Expection: True")
    val = rules.checkPlayerWon(field, player, 3)
    print(f"Result: {val}\n")

    # Schritt 2: Vertikal
    field.fields = verticalWinField
    print("Testing vertical Win. Expection: True")
    val = rules.checkPlayerWon(field, player, 0)
    print(f"Result: {val}\n")

    # Schritt 3: Diagonal von Links oben nach Rechts unten
    field.fields = diagonalLeftRightWinField
    print("Testing diagonal upper left to lower right Win. Expection: True")
    val = rules.checkPlayerWon(field, player, 3)
    print(f"Result: {val}\n")

    # Schritt 4 Diagnoal von Rechts oben nach links unten
    field.fields = diagonalRightLeftWinField
    print("Testing diagonal upper right to lower left Win. Expection: True")
    val = rules.checkPlayerWon(field, player, 3)
    print(f"Result: {val}\n")

    # Testen der Logik ob das Spiel im unentschieden endet
    field.fields = fullField
    print("Testing Game Over ('Game tied'). Expection: True")
    val = rules.checkGameOver(field)
    print(f"Result: {val}\n")
    input("Tests Complete.\nPress Enter to Exit")
