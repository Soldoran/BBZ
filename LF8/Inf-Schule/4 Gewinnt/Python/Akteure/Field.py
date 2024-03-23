# -*- coding: utf-8 -*-

#Imports

class Field:

# Konstruktor
    def __init__(self):
        # Das leere Spielfeld instanziieren
        self.fields = [[" " for _ in range(7)] for _ in range(6)]


# Funktionen
    def getFields(self):
        return self.fields

    def setFields(self, col, val):
        if (0 <= col < len(self.fields[0])):          # Wenn 'col' größer oder gleich 0 ist und gleichzeitig kleiner der länge einer Reihe ist
            row = len(self.fields) - 1

        while row >= 0:                                 # Iterrieren solange 'row' größer oder gleich 0 ist
            if self.fields[row][col] == " ":          # Nun schauen ob das Feld leer ist, und wenn ja, einen Stein platzieren
                self.fields[row][col] = val
                return True                             # Zug war gültig

            row -= 1                                    # Wir gehen eine Reihe weiter nach oben

        return False                                    # Zug war ungültig


    def getLastRow(self):
        return self.fields[-1]

    def getLastCol(self):
        return self.fields[0][-1]
