# -*- coding: utf-8 -*-

#Imports
import os

class GUI:

# Konstruktor
    def __init__(self):
        pass


# Funktionen
    def outputField(self, field):
        '''
        Das Spielfeld ausgeben
        '''
        for i, row in enumerate(field):                   # Für jede Reihe in field
            for j, cell in enumerate(row):                # Für jede Zelle in einer Reihe
                #print("|")
                print(cell, end=" ")        # Den Inhalt der Zelle ausgeben und durch 'end=" "' fangen wir hier keine neue Zeile an, sondern fügen ein Leerzeichen hinzu

                if j < len(row):         # Solange die Zelle nicht die letzte in der Reihe ist
                    print("|", end=" ")     # Wird ein Trennzeichen hinzugefügt

            print()
            if i <= len(field):            # Prüfen ob wir uns in der letzten Reihe befinden
                for cell in row:            # Nun noch einmal iterieren um die Reihen optisch voneinander besser trennen zu können
                    print("---", end="")    # Für Jede Zelle geben wir '---' gefolgt von einem end="" (Kein Zeilenumsprung am ende)
                print()                     # print() gibt uns einen Zeilenumbruch am Ende der Schleife

    def getName(self, playerNr):
        '''
        Den Namen des Spielers abfragen
        '''
        name = input('Namen für Spieler ' + str(playerNr) + ': ') 
        return name

    def getGameMode(self, name):
        '''
        Abfragen, welchen Spielmodus der Spieler spielen möchte
        1 = Per Zufall
        2 = Per Eingabe
        '''
        gM_spieler = 0
        gM_Zufall = "\n\t[1] = Per Zufall"
        gM_Eingabe = "\n\t[2] = Per Eingabe"

        while gM_spieler == 0:
            gM_string = input(f"Wähle den Spielmodus für Spieler '{name}':{gM_Zufall}{gM_Eingabe}\n\nSpielmodus: ")

            if gM_string.isdigit():
                gM_Spieler = int(gM_string)

            if gM_Spieler == 1 or gM_Spieler == 2:
                break            
            else:
                gM_Spieler = 0
                print(f"Die Eingabe '{gM_string}' ist nicht gültig. Bitte wiederhole deine Eingabe.\n(Drücke eine Taste um weiter zu machen)")
                input()
                continue

        return gM_Spieler


    def getDraw(self, name):
        '''
        Fragt den Spieler in welche Spalte er einen Stein schmeißen möchte
        '''
        while True:
            try:
                column = int(input(f"{name} is am Zug. Bitte gebe die Spaltennummer ein, in der du deinen Stein platzieren möchtest (1-7): "))
                if 1 <= column <= 7:
                    return column - 1
                else:
                    print("Ungültige Eingabe! Bite gib eine Zahl zwischen 1 und 6 ein.")
            except ValueError:
                print("Ungültige Eingabe! Bitte gib eine Zahl ein.")
