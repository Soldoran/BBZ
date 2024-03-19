# -*- coding: utf-8 -*-

#Imports

class RuleSet:

# Konstruktor
    def __init__(self):
        pass


# Funktionen
    def checkDraw(self, field, col):
        '''
        Überprüfen ob ein Zug legal ist (In der Spalte war noch Platz)
        '''
        for row in field[0]:        # Wir gehen jede Reihe einmal durch, mit 'row[col]' schauen wir anschließend an die richtige Koordinate
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
            for col in row:
                if row[col] == teamcolor:
                    touchingStones.append(cell)
                else:
                    if col != lastCol:
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
        for i in range(len(fields) - 3):
            for j in range(len(fields[0])) - 3:
                if all(fields[i+k][j+k] == teamcolor for k in range(4)):
                    return True

        # Check Diagonal von rechts oben nach links unten
        for i in range(len(fields) - 3):
            for j in range(len(fields[0])) - 3:
                if all(fields[i-k][j-k] == teamcolor for k in range(4)):
                    return True

        return False


    def checkGameOver(self, field):
        '''
        Überprüfen ob es noch freie Felder in der letzten Reihe gibt, um einen legalen Zug auszuführen
        '''
        return all(cell == " " for cell in field[-1])   # Da beim letzten legalen Zug in der obersten Reihe ein freies Feld sein muss, reicht es, sich diese Zeile anzuschauen
