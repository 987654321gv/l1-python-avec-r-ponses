"""

"""
from tkinter import *
class morpion(Frame):
    def __init__(self,boss=None,width=6,height=2,color='#ddffff',colorgagne='#ffffdd',taille=3):
        Frame.__init__(self,boss)
        self.pack()
        self.colorgagne=colorgagne
        self.dernier = []
        self.color=color
        self.grille=[]
        self.turn=0
        self.turns=('X','O')
        self.colors=('#ff0000','#0000ff')
        self.g=[]
        self.taille=taille
        for line in range(taille):
            li=[]
            l2=[]
            for p in range(taille):
                li.append(Button(self,width=width,height=height,command=lambda pos=(line,p):self.jouer(pos),font='arial 30',background=self.color))
                li[-1].grid(row=line*3, column=p*3,sticky=NSEW,rowspan=3,columnspan=3)
                l2.append('V')
            self.grille.append(li)
            self.g.append(l2)
        Button(self,text='rejouer',command=self.rejouer).grid(row=taille*3, column=0,columnspan=taille,sticky=NSEW)
        Button(self,text='annuler',command=self.annuler).grid(row=taille*3, column=taille,sticky=NSEW,columnspan=taille)
        Button(self, text='quitter', command=boss.destroy).grid(row=taille*3, column=self.taille*2,columnspan=taille,sticky=NSEW)
    def jouer(self,position):
        if self.g[position[0]][position[1]]!='V':
            return

        self.grille[position[0]][position[1]].configure(text=self.turns[self.turn],foreground=self.colors[self.turn])
        self.g[position[0]][position[1]]=self.turns[self.turn]
        self.dernier.append(position)
        self.turn=not(self.turn)
        for allignement in self.get_all_allignments():
            if any([self.g[line][col] for line,col in allignement]==[turn]*self.taille for turn in self.turns):
                for line,col in allignement:
                    self.grille[line][col].configure(background=self.colorgagne)

    def get_all_allignments(self)->list[list[list[int,int]]]:
        return [[[line,col] for col in range(self.taille)] for line in range(self.taille)]+\
               [[[line,col] for line in range(self.taille)] for col in range(self.taille)]+\
               [[[line,line] for line in range(self.taille)]]+\
               [[[line,-line-1] for line in range(self.taille)]]

    def rejouer(self):
        self.dernier = []
        self.turn=0
        for line in range(self.taille):
            for p in range(self.taille):
                self.grille[line][p].configure(text='',background=self.color)
                self.g[line][p]='V'
    def annuler(self):
        if self.dernier==[]:
            self.bell()
            return


        dernier=self.dernier.pop()
        self.grille[dernier[0]][dernier[1]].configure(text='')
        self.g[dernier[0]][dernier[1]] = 'V'
        self.turn = not (self.turn)

        for line in range(self.taille):
            for p in range(self.taille):
                self.grille[line][p].configure(background=self.color)
        for allignement in self.get_all_allignments():
            if any([self.g[line][col] for line,col in allignement]==[turn]*self.taille for turn in self.turns):
                for line,col in allignement:
                    self.grille[line][col].configure(background=self.colorgagne)



if __name__ == '__main__':
    f=Tk()
    f.resizable(width=0,height=0)
    morpion(f,taille=3)
    f.mainloop()