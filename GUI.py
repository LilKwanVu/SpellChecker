from bkTree import BKTree
from editDistance import levenshtein_distance
from tkinter import *

if __name__ == "__main__":
    file = open('google-10000-english.txt')
    list = file.read().split()
    tree = BKTree(words=list)

    window = Tk()
    window.title('SPELLING CHECKER: ')
    window.geometry("600x100")

    lbl = Label(window, text='Enter your word: ', fg='black', font=('Times New Roman', 18))
    lbl.grid(column=0, row=1)

    txt = Entry(window, width=30,font=('Times New Roman', 18))
    txt.grid(column=1, row=1)


    def suggest():
        word = txt.get().lower().strip()
        result = tree.search(word, 2)
        if len(result) == 0:
            lbl2.configure(text='Not found!')
            return
        elif result[0][0] == 0:
            lbl2.configure(text='Correctly spelled!')
            return
        else:
            lst = []
            for i in result[0:5]:
                lst.append(i[1].word)
            lbl2.configure(text='Did you mean: {}, {}, {}, {} or {}?'.format(*lst))
            return

    lbl2 = Label(window, fg='red', font=('Times New Roman', 18),)
    lbl2.place(relx = 0.0,
                 rely = 1.0,
                 anchor ='sw')

    btn = Button(window, text='CHECK', command=suggest)
    btn.grid(column=1, row=2)

    window.mainloop()
