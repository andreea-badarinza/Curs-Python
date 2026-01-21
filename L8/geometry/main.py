# main.py
# Importăm modulele din pachetul geometry

from circle import aria_cercului, circumferinta_cercului
from rectangle import aria_dreptunghiului, perimetru_dreptunghiului

raza = 7
lungime = 10
latime = 5

print("Aria cercului:", aria_cercului(raza))
print("Circumferința cercului:", circumferinta_cercului(raza))

print("Aria dreptunghiului:", aria_dreptunghiului(lungime, latime))
print("Perimetrul dreptunghiului:", perimetru_dreptunghiului(lungime, latime))
