# -*- coding: utf-8 -*-

#Imports

class Field:

# Konstruktor
    def __init__():
        # Das leere Spielfeld instanziieren
        self.fields = [
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " "]
                ]

        pass

# Funktionen
    def getFields():
        return self.fields

    def setFields(self, col, val):
        if (0 <= col < len(self.__fields[0])):          # Wenn 'col' größer oder gleich 0 ist und gleichzeitig kleiner der länge einer Reihe ist
            row = len(self.__fields) - 1

        while row >= 0:                                 # Iterrieren solange 'row' größer oder gleich 0 ist
            if self.__fields[row][col] == " ":          # Nun schauen ob das Feld leer ist, und wenn ja, einen Stein platzieren
                self.__fields[row][col] = val
                return True                             # Zug war gültig

            row -= 1                                    # Wir gehen eine Reihe weiter nach oben

        return False                                    # Zug war ungültig


    def getLastRow():
        return self.lastRow

    def setLastCol():
        return self.lastCol
