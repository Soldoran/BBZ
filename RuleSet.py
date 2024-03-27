# -*- coding: utf-8 -*-

#Imports
from Player import Player
from Field import Field
import os

class RuleSet:

# Konstruktor
    def __init__(self):
        '''
        Konstruktor für die Klasse RuleSet.
        '''
        pass


# Funktionen
    def checkDraw(self, field, col):
        '''
        Prüft ob ein Spielfeld noch frei belegbar ist.
        Wenn ja:
            gibt 'True' zurück, andernfalls 'False'
        '''
        for row in field:
            if row[col] == " ":
                return True
        return False

    def checkPlayerWon(self, field, player, col):
        '''
        Prüft ob ein der 4 Siegbedingungen
            Vertikal,
            Horizontal,
            Diagonal Links oben nach Rechts unten,
            Diagonal von Rechts oben nach Links unten
        erfüllt ist und gibt im Falle 'True' zurück.
        Andernfalls wird 'False' zurückgegeben.
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
        Prüft ob die oberste Reihe bereits mit Spielersymbolen gefüllt ist.
        Wenn ja, wird 'True' zurück gegeben, andernfalls 'False'.
        '''
        fields = field.getFields()
        return all(cell != " " for cell in fields[-1])

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
