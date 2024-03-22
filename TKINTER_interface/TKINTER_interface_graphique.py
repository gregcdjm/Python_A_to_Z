from tkinter import *
import webbrowser

def opren_troll_yt():
    webbrowser.open_new("https://youtu.be/dQw4w9WgXcQ?t=42")

# création de la fenêtre
window = Tk()

# personalisation
window.title("Combat_1vs1")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap('TKINTER_interface./logo.ico')
window.config(background='grey')
# création d'un frame
frame = Frame(window, bg='grey', bd=1,relief=SUNKEN)

# Ajouter un texte
label_title = Label(frame, text = "Bienvenue sur Road To God", font=("papyrus", 40), bg='grey', fg='red')
label_title.pack(expand=YES)

#ajout second texte
label_sub_title = Label(frame, text = "Commencer à jouer !", font=("papyrus", 25), bg='grey', fg='red')
label_sub_title.pack(expand=YES)

# ajouter
frame.pack(expand=YES)

#ajouter un boutton
new_player= Button(frame, text="Enregistrer perso", font=("papyrus", 25), bg='black',
                    fg='white', command=opren_troll_yt)
new_player.pack(pady=20, fill=X)
#afficher
window.mainloop()