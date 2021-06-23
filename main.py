from BK_Tree import BKTree
from EditDistance import editDistance
from tkinter import *

if __name__ == "__main__":
    tree = BKTree(editDistance)
    file = open('google-10000-english.txt')
    list = file.read().split()
    for item in list:
        tree.insert(item.lower())

    window = Tk()
    window.title('SPELLING CHECKER: ')
    window.geometry("900x150")

    lbl = Label(window, text='Enter your word: ', fg='black', font=('Times New Roman', 18))
    lbl.grid(column=0, row=1)

    txt = Entry(window, width=30)
    txt.grid(column=1, row=1)


    def suggest():
        word = txt.get().lower().strip()
        dist1 = tree.search(word, 1)
        dist2 = tree.search(word, 2)
        if dist1 == 0 or dist2 == 0:
            lbl2.configure(text='Correctly spelled!!!')
            return
        elif len(dist1) == 0 or len(dist2) == 0:
            lbl2.configure(text='Not found!!!')
            return
        else:
            guesses = []
            for word in dist1:
                guesses.append(word)
            for word in dist2:
                guesses.append(word)
            lbl2.configure(text='Did you mean: {}, {}, {}, {}, {} ?'.format(*guesses))
            return


    lbl2 = Label(window, fg='red', font=('Times New Roman', 18))
    lbl2.grid(column=0, row=3)

    btn = Button(window, text='CHECK', command=suggest)
    btn.grid(column=1, row=2)

    window.mainloop()
