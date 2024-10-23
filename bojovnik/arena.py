#!/usr/bin/env python3

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print('------------------------Arena-------------------------- \n')
        print('Bojovnici: \n')

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subrocess
        if _sys.platform.startswith('win'):
            _sub.call(['cmd.exe', '/C', 'cls'])
        else:
            _subrocess.call(['clear'])

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f'Srdca: {bojovnik.graficky_zivot()}')
    
    def zapas(self):
        print('Vítejte v Aréně!')
        print(f'Dnes se utkqají {self._bojovnik_1} a  {self._bojovnik_2}:')
        print('Zápas může začít....', end = ' ')
        input()

        while self._bojovnik_1.nazivu and self._bojovnik_2.nazivu:
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._bojovnik_2.utoc(self._bojovnik_1)
            self._vykresli()
            
if __name__ == '__main__':
    from kostka import Kostka
    from bojovnik import Bojovnik
    k = Kostka(10)
    b1 = Bojovnik('Trump', 80, 20, 50, k)
    b2 = Bojovnik('Biden', 60, 40, 35, k)

    a = Arena(b1, b2, k)
    a.zapas()
