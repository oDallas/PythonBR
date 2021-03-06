# -*- coding: utf-8 -*-

# Classe Bola: Crie uma classe que modele uma bola:
#    a. Atributos: Cor, circunferência, material
#    b. Métodos: trocaCor e mostraCor


class Bola(object):
    def __init__(self, material, circulo, cor):
        self.material = material.title()
        self.circulo = circulo
        self.cor = cor.title()

    def __str__(self):
        return """
╔══════════╤═════════╤══════════╗
║ Material │ Círculo │ Cor      ║
╟──────────┼─────────┼──────────╢
║ {:<8.8} │ {:<7.2f} │ {:<8.8} ║
╚══════════╧═════════╧══════════╝
""".format(self.material, self.circulo, self.cor)


if __name__ == '__main__':
    circulo = float(input('Circulo: '))
    material = input('Material: ')
    cor = input('Cor: ')

    bola = Bola(material, circulo, cor)
    print(bola)
