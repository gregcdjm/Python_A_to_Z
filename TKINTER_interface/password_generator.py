import string
from tkinter import *
from random import randint, choice

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)        

#creer la fenetre
window = Tk()
window.title("Génerateur de mdp")
window.geometry("720x480")
window.iconbitmap('TKINTER_interface./logo.ico')
window.config(background='blue')

#creation de la frame principale
frame = Frame(window, bg= "yellow")

#creation image
width = 300
height = 300
image = PhotoImage(file="TKINTER_interface./lock.png").zoom(35).subsample(32)
canvas = Canvas(frame ,width= width, height= height, bg= 'green', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg='yellow')

#creer un titre
label_title = Label(right_frame, text="Entrez mot de passe", font=("Helvetica", 20), bg= "purple", fg="white")
label_title.pack()

#creer un champs/entrée/input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg= "purple", fg="white")
password_entry.pack()

#creation button
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg= "purple", fg="white", command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

#creation barre de menu
menu_bar = Menu(window)

#crer menu
file_menu = Menu(menu_bar,  tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer notre fenêtre
window.config(menu=menu_bar)

#aficher la fenetre
window.mainloop()