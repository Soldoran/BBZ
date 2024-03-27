# -*- coding: utf-8 -*-

class Field:

    def __init__(self):
        '''
        Konstruktor der Klasse Field.
        Initialisiert ein Leeres Spielfeld.
        Dimension des Spielfeldes:
            7 Breit
            6 Hoch
        '''
        self.fields = [[" " for _ in range(7)] for _ in range(6)]

    def getFields(self):
        '''
        Getter für das Spielfeld.
        Gibt das Spielfeld zurück.
        '''
        return self.fields

    def setFields(self, col, val):
        '''
        Überprüft ob in der gewählten Spalte noch mindestens ein freies Feld verfügbar ist,
        setzt in die Spalte 'col' den Wert der SpielerID 'val' und gibt anschließend 'True' zurück,
        andernfalls 'False'.

        Parameter:
        col: int
            Die Spalte, in welche der Spielstein gesetzt werden soll
        val: chr
            Der Character des Spielers, welcher in die nächste freie Position gesetzt werden soll
        '''
        if (0 <= col < len(self.fields[0])):
            row = len(self.fields) - 1

        while row >= 0:
            if self.fields[row][col] == " ":
                self.fields[row][col] = val
                return True
            else:
                row -= 1
        # Es wurde kein Gültiger Zug gefunden
        return False


    def getLastRow(self):
        '''
        Getter für die Letzte Reihe des Spielfeldes.
        Gibt die letzte Reihe des Spielfeldes zurück.
        '''
        return self.fields[-1]

    def getLastCol(self):
        '''
        Getter für die letzte Spalte des Spielfeldes.
        Gibt die letzte Spalte des Spielfeldes zurück.
        '''
        return self.fields[0][-1]
