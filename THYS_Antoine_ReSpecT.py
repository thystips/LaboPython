# -*-coding:utf-8 -*

import argparse
import sys
from time import strftime
import datetime
import getopt

class ReSpecT(object):

   def __init__(self):
      parser = argparse.ArgumentParser( description = 'Projet ReSpecT', usage = '''
python THYS_Antoine_ReSpecT.py <commande> [PARAM].
Les fonctions du programme:
   coucou      Affiche “Coucou à toi aussi.”
   push -f     Affiche “NE JAMAIS FAIRE DE “PUSH FORCE” SUR GIT, SACREBLEU !”
   upsideDown  Affiche [PARAM] à l’envers.
   montre      Affiche l’heure courante
   trie        Affiche la liste des entiers passés en paramètres dans l’ordre croissant. [NB] est le
nombre d’entiers à trier.
   trie -desc  Affiche la liste des entiers passés en paramètres dans l’ordre décroissant. [NB] est le
nombre d’entiers à trier.''' )
      parser.add_argument('command', help='Nom de la fonction à exécuter')
      args = parser.parse_args(sys.argv[1:2])
      if not hasattr(self, args.command):
         print ('Commande non reconnue')
         parser.print_help()
         exit(1)
      getattr(self, args.command)()

   def coucou(self):
      print ('Coucou à toi aussi.')

   def push(self):
      parser = argparse.ArgumentParser()
      parser.add_argument('-f','--force', action='store_true')
      args = parser.parse_args(sys.argv[2:])
      if args.force:
         print ('NE JAMAIS FAIRE DE “PUSH FORCE” SUR GIT, SACREBLEU !')

   def upsidedown(self):
      parser = argparse.ArgumentParser()
      parser.add_argument('text')
      args = parser.parse_args(sys.argv[2:])
      txt1 = args.text
      txt2 = ''.join(reversed(txt1))
      print(txt2)

   def montre(self):
      montre= datetime.datetime.now()
      date = montre.strftime('%Y/%m/%d-%H:%M')
      print(date)

   def trie(self):
      if '-desc' in sys.argv:
         list = sys.argv[3:3+int(sys.argv[3])]
         print(' '.join(sorted(list, reverse=True)))
      else:
         list = sys.argv[2:2+int(sys.argv[2])]
         print(' '.join(sorted(list)))

if __name__ == '__main__':
   ReSpecT()
