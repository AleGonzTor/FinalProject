
import os
from decoration import Decoration
from constants import*
fondo = Decoration(0, 0, "nuevo//Sprites/fondo.png", layer=0)
fondo.escala(WIDTH, HEIGHT)
decoraciones_1=[
   fondo,
   Decoration(100,200,"nuevo/Sprites/arbol.png",layer=1),
   Decoration(300,180,"nuevo/Sprites/arbol.png",layer=1),
   Decoration(900,500,"nuevo/Sprites/arbusto.png",layer=1),
   Decoration(320,180,"nuevo/Sprites/hongo.png",layer=2),
   Decoration(30,30,"nuevo/Sprites/nube.png",layer=1),
   Decoration(500,30,"nuevo/Sprites/nube.png", layer=1),
   Decoration(480,480,"nuevo/Sprites/flechaderecha.png",layer=1),
   Decoration(320,260,"nuevo/Sprites/pasto.png",layer=2),
   Decoration(900,30,"nuevo/Sprites/nube.png",layer=1)

]
decoraciones_1[2].escala(180,200)
decoraciones_1[1].escala(80,100)
decoraciones_1[3].escala(40,60)
decoraciones_1[5].escala(140,160)