from tkinter import *
from PIL import Image,ImageTk
from pygame import mixer
from random import randint
 
mixer.init ()

largeur,hauteur = 0,0
Yv, Vv= 0, 6
Xg, Yg, Vg = 0, 0, 0
etat_saut_g = 0
vitesse_random = 6
sound = 0

fenetre = Tk()
fenetre.title ("Jeu Froggy")

img= Image.open("Nenu.png")
img = img.resize ((40,34))
curseur= ImageTk.PhotoImage(img)

img2= Image.open("crapaud.png")
img2 = img2.resize ((40, 34))
craniv= ImageTk.PhotoImage(img2)


ecr_img = Image.open ("landscape.png")
ecr_img = ecr_img.resize ((900, 600))
fond2 = ImageTk.PhotoImage (ecr_img)

def quitter (event) :
	fenetre.quit ()
		
fenetre.bind ("<KeyPress-q>", quitter)

def saut (event) :
		global Vv,Yg, Vg, etat_saut_g
		if etat_saut_g == 0 :
			etat_saut_g = 1
			Vg = Vv / 1.75

fenetre.bind ("<space>", saut)	

dessin = Canvas (width = 900,height = 600, bg = "black" )
dessin.pack()

def accueil ()  :
	
	global curseur, sound, fond2
	
	dessin.create_image (0,0, anchor = NW,image = fond2)	
	dessin.create_text (450, 150, font = ("Arial",8,"bold"), fill = "white", text = "Le but du jeu est de sauter au dessus de la voiture ")
	dessin.create_text (450, 250, font = ("Arial",8,"bold"), fill = "white", text = "Barre espace : Pour sauter avec la grenouille")
	dessin.create_text (450, 300, font = ("Arial",8,"bold"), fill = "white", text = "Touche Entrée : Pour commencer la partie/pour valider un choix")
	dessin.create_text (450, 350, font = ("Arial", 8, ), fill = "white", text = 'Pour une expérience plus immersive activez le son ;)')
	dessin.create_text (450, 400, font = ("Arial",8,"bold"), fill = "white", text = "Touche Q : Pour quitter le jeu")
	dessin.create_text (450, 450, font = ("Arial",8,"bold"), fill = "white", text = "Touche Echap : Pour revenir au menu précédent")
	
	"""if sound == 0 :
		mixer.music.load ('undertale-ost-all-start-menu-theme.mp3')
		mixer.music.play ()"""

	def depart (event) :
		fenetre.unbind("<Return>")
		dessin.create_text (450, 300, text = 'wesh', fill = 'white')
		fenetre.after (0, niv)
	fenetre.bind ("<Return>", depart)
	

def niv () :
	
	global niveau, cur, Yc
	Yc = 300
	
	dessin.delete ('all')
	dessin.create_image (0,0, anchor = NW,image = fond2)
	cur = dessin.create_image (375,Yc, image = curseur)
	dessin.create_text (450, 250, text = "Choix de la difficulté :", fill = "white", font = ("Arial", 8, "bold"))
	dessin.create_text (450, 300, text = "Facile", fill = "white")
	dessin.create_text (450, 350, text = "Moyen", fill = "white")
	dessin.create_text (450, 400, text = "Difficile", fill = "white")
	dessin.create_text (790, 20, text = "Paramètres", fill = "white", font = ("Arial", 8, "bold"))

	def up (event) :
		global cur, Yc
		dessin.delete (cur)
		if Yc == 350 or Yc == 400 :
			cur = dessin.create_image (375,Yc - 50, image = curseur)
			Yc = Yc - 50
		elif Yc  == 300 :
			cur = dessin.create_image (680,20, image = curseur)
			Yc = 20
		elif Yc == 20 : 
			cur = dessin.create_image (375, 400, image = curseur) 
			Yc = 400
		return
	fenetre.bind ('<Up>', up)
	
	def down (event) :
		global cur, Yc
		dessin.delete (cur)
		if Yc == 300 or Yc == 350  : 
			cur = dessin.create_image (375,Yc + 50, image = curseur)
			Yc = Yc + 50
		elif Yc == 400  :
			cur = dessin.create_image (680,20, image = curseur)
			Yc = 20
		elif Yc == 20 :
			cur = dessin.create_image (375,300, image = curseur)
			Yc = 300
		return
	fenetre.bind ('<Down>', down)
	
	def select (event) :
		global Yc, niveau
		fenetre.unbind ('<Return>')
		fenetre.unbind ("<Up>")
		fenetre.unbind ('<Down>')
		if Yc == 300 :
			niveau = "facile"
			fenetre.after (0, jeu)
		elif Yc == 350 :
			niveau = "moyen"
			fenetre.after (0, jeu)
		elif Yc == 400 :
			niveau = "difficile"
			fenetre.after (0, jeu)
		elif Yc == 20 :
			fenetre.after (0, para)
		return
	fenetre.bind ('<Return>', select)
	
	def sortie (event) :
		fenetre.unbind ('<Escape>')
		dessin.delete ('all')
		fenetre.after (0, accueil)
	fenetre.bind ('<Escape>', sortie)

def para () :
	
	global sound, cur, Yc, son
	
	Yc = 300
	
	dessin.delete ('all')
	dessin.create_image (0,0, anchor = NW,image = fond2)
	cur = dessin.create_image (350,Yc, image = curseur)
	if sound == 1 :
		son = dessin.create_text (450, 300, fill = 'white', text = 'Sound off', font = ('Arial', 8, 'bold'))
	elif sound == 0 :
		son = dessin.create_text (450, 300, fill = 'white', text = 'Sound on', font = ('Arial', 8, 'bold'))
	dessin.create_text (450, 450, fill = 'white', text = 'Echap pour quitter ce menu')
	dessin.create_text (450, 500, fill= 'white', text = 'Touche q pour quitter le jeu')
	
	def son (event) :
		global sound, son, Yc
		if Yc == 300 :
			fenetre.unbind ('<Return>')
			if sound == 0 :
				dessin.delete ('all')
				dessin.create_image (0,0, anchor = NW,image = fond2)
				son  = dessin.create_text (450, 300, fill = 'white', text = 'Sound off', font = ('Arial', 8, 'bold'))
				mixer.music.pause ()
				fenetre.after (500, niv)
				sound = 1
			else :
				dessin.delete ('all')
				dessin.create_image (0,0, anchor = NW,image = fond2)
				son = dessin.create_text (450, 300, fill = 'white', text = 'Sound on', font = ('Arial', 8, 'bold'))
				mixer.music.play()
				fenetre.after (500, niv)
				sound = 0
	fenetre.bind ('<Return>', son)
	
	def sortie (event) :
		fenetre.unbind ('<Escape>')
		dessin.delete ('all')
		fenetre.after (0, niv)
	fenetre.bind ('<Escape>', sortie)
	

def jeu () :

	global score, grenouille,grenouille_rip, fond,voiture
	global Xg,Yg,Vg
	global Xv, Yv, Vv
	global largeur, hauteur
	global sound 
	
	if sound == 1 :
		mixer.music.pause()
	else :
		mixer.music.pause ()
		mixer.music.load ('undertale-megalovania.mp3')
		mixer.music.play()
	
	score = 0
	Xv = 0
	
	photo = Image.open ("fond.png")
	photo = photo.resize ((900, 600))
	largeur,hauteur = photo.size
	fond = ImageTk.PhotoImage(photo)
	dessin.create_image (0,0,anchor = NW,image = fond)	
	
	Yv = hauteur - 90
	Xg = largeur - 200
	Yg = hauteur  - 85
	Vg = 0 
	Vv = 6
	
	photo2 = Image.open("crapaud.png")	
	grenouille = ImageTk.PhotoImage(photo2)
	
	photo3 = Image.open ("car.png")
	voiture = ImageTk.PhotoImage(photo3)
	
	img_rip = Image.open("g_rip.png")
	grenouille_rip = ImageTk.PhotoImage(img_rip)		

	
	animation ()

def animation () :

	global score, etat_saut_g, niveau, sound, comptage 
	global grenouille,grenouille_rip, fond,voiture,photo2
	global Xg,Yg,Vg
	global Xv, Yv, Vv, vitesse_random
	global largeur, hauteur
	
	dessin.delete ('all')
	dessin.create_image (0,0,anchor = NW, image = fond)
	cg = dessin.create_image (Xg,Yg,anchor = NW, image = grenouille)
	dessin.create_image (Xv,Yv,anchor = NW, image = voiture)
	dessin.create_text (largeur /2, 20, text = "Score :", fill = "black", font = ("Arial",8,"bold"))
	dessin.create_text (largeur /2 + 80, 20, text = score, fill = "black", font = ("Arial",8,"bold"))
	
	Xv = Xv+Vv
	if Xv > largeur :
		score = score + 1
		Xv = -200
		vitesse_random = randint (7, 12)
	
		if niveau == "facile" :
			Vv = 6
		elif niveau == "moyen" :
			Vv = vitesse_random
		elif niveau == "difficile" :
			Vv = Vv + 0.5


	if etat_saut_g == 1 :
		Yg = Yg - Vg 
		if Yg <= hauteur - 280 :
			etat_saut_g = 2
	if etat_saut_g == 2 :
		Yg = Yg + Vg
		if  Yg >= hauteur - 85 :
			Vg = 0
			
	if Vg == 0 : 
		etat_saut_g = 0
		
		
	if (Xv >= Xg + 96) or (Xv + 160 <= Xg) or (Yg + 80 < Yv) :
			fenetre.after (1, animation)
			
	else :
			if sound == 0 :
				mixer.music.pause()
				mixer.music.load("mario-dead-sound.mp3")
				mixer.music.play()
			Vv= 0
			Yg = Yg + 50
			dessin.delete(cg)
			dessin.create_image(Xg,Yg,anchor = NW, image = grenouille_rip)
			fenetre.after (3500, fin)
			return	
	
def fin ()  :
	
	global sound 
	
	
	dessin.delete ('all')
	dessin.create_text (450, 300, font = ("Arial",14,"bold"), fill = "red", text = "Game Over")	
	dessin. create_text (450, 400, font = ("Arial", 8,'bold'), fill = "red", text = "Votre score = ")
	dessin. create_text (580, 400, font = ("Arial", 8,'bold'), fill = "red", text =  score)
	dessin.create_text (450, 500, fill = 'red', text = "Pour rejouer appuyer sur entrée")
	
	if sound == 0 :
		mixer.music.pause ()
		mixer.music.load ('undertale-ost-011-determination.mp3')
		mixer.music.play ()
	
	def replay (event) :
		global running
		dessin.delete('all')
		accueil ()
		return	
	fenetre.bind ("<Return>", replay)
	
accueil()
mainloop()		


