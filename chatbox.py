import json
from difflib import get_close_matches
from tkinter import Tk, Entry, Button, Text, Scrollbar


class Chatbot:
    def __init__(self, window):
        window.title('Brioche')
        window.geometry('800x600')
        window.resizable(1, 1)
        self.message_session = Text(window, bd=4, relief="groove", font=("Times", 15), undo=True, wrap="word")
        self.message_session.insert('1.0', "Brioche :Que voulez-vous commander ?\n")
        self.message_session.config(width=35, height=15, bg="green", fg="white", state='disable')
        self.overscroll = Scrollbar(window, command=self.message_session.yview)
        self.overscroll.config(width=10)
        self.message_session["yscrollcommand"] = self.overscroll.set
        self.message_position = 1.5
        self.send_button = Button(window, text='Envoyer', fg='white', bg='#00813b', width=8, font=('Times', 12),
                                  relief='groove', command=self.reply_to_you)
        # Message_Entry est la zone ede saisie de la commande
        self.Message_Entry = Entry(window, width=32, font=('Times', 10))
        self.Message_Entry.bind('<Return>', self.reply_to_you)
        self.message_session.place(x=20, y=20)
        self.overscroll.place(x=380, y=50)
        self.send_button.place(x=0, y=360)
        self.Message_Entry.place(x=90, y=365)
        # Le fichier json avec les mots clé dedans
        self.Brain = json.load(open('mathweb.json', encoding='utf-8'))

    def add_chat(self, message):
        self.message_position += 1.5
        # Pour supprimer lorsque nous cliquons sur envoyer en effaçant tout le texte
        self.Message_Entry.delete(0, 'end')
        self.message_session.config(state='normal')
        self.message_session.insert(self.message_position, message)
        # Pour voir la dernière ligne saisie
        self.message_session.see('end')
        # Cinfigure la zone  de reponse pour ne pas qu'on puisse saisir quelque chose là-bas
        # Message session est la zone de reponse
        self.message_session.config(state='disabled')

    # La methode pour répondre
    def reply_to_you(self,event=None):
        # Lit la saisie de la commande sous format majuscule
        message = self.Message_Entry.get().lower()
        message = 'Vous: ' + message + '\n'
        # Retourne une liste des meilleurs résultats avec la fonction
        close_match = get_close_matches(message, self.Brain.keys())
        if close_match:
            reply = 'Brioche: ' + self.Brain[close_match[0]][0] + '\n'
        else:
            reply = 'Brioche: ' + 'Désolé n\'avons pas celà dans notre menus !\n'
        self.add_chat(message)
        self.add_chat(reply)


root = Tk()
Chatbot(root)
root.mainloop()
