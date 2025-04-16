# Créé par arthur, le 16/04/2025 en Python 3.7
#importation de tkinter sous l'alias tk
import tkinter as tk

#création d'une interface tkinter
root = tk.Tk()
root.geometry("600x650")

#création de deux frames pour séparer affichage et boutons
frm = tk.Frame(root)
frm2=tk.Frame(root)

frm.grid(column=0,row=0)
frm2.grid(column=0,row=1)

#création de l'affichage
tk.Label(frm, text="Calculatrice").grid(column=0, row=0)
aff=tk.Label(frm, text="",font=("Arial", 20), bg="yellow", width=35, height=2)
aff.grid(column=0, row=1)

#création de memoire qui stock l'affichage et temporaire le dernier resultat.
mem=""
temp=""

#fonctions d'affichage
def affichage_final():
    global mem
    global temp
    aff['text']=eval(mem)
    temp=str(eval(mem))
    mem=""

def affichage():
    aff['text']=mem

#fonctions d'affectation des boutons
def F_un():
    global mem
    mem+="1"
    affichage()

def F_deux():
    global mem
    mem+="2"
    affichage()

def F_trois():
    global mem
    mem+="3"
    affichage()

def F_quatre():
    global mem
    mem+="4"
    affichage()

def F_cinq():
    global mem
    mem+="5"
    affichage()

def F_six():
    global mem
    mem+="6"
    affichage()

def F_sept():
    global mem
    mem+="7"
    affichage()

def F_huit():
    global mem
    mem+="8"
    affichage()

def F_neuf():
    global mem
    mem+="9"
    affichage()

def F_zero():
    global mem
    mem+="0"
    affichage()

def F_op2():
    global mem
    mem+="-"
    affichage()

def F_op1():
    global mem
    mem+="+"
    affichage()

def F_op3():
    global mem
    mem+="*"
    affichage()

def F_op4():
    global mem
    mem+="/"
    affichage()

def F_dec():
    global mem
    mem+="."
    affichage()

def F_par1():
    global mem
    mem+="("
    affichage()

def F_par2():
    global mem
    mem+=")"
    affichage()

def F_e():
    global mem
    mem+="(2.7182)"
    affichage()

def F_pi():
    global mem
    mem+="(3.1415)"
    affichage()


def F_ans():
    global mem
    global temp
    mem+=temp
    affichage()

def reset():
    global mem
    mem=""
    affichage()


#implémentation des boutons dans la frame 2
un=tk.Button(frm2,text="1",command=F_un,font=("Arial",25)).grid(column=0, row=0)
deux=tk.Button(frm2,text="2",command=F_deux,font=("Arial",25)).grid(column=1, row=0)
trois=tk.Button(frm2,text="3",command=F_trois,font=("Arial",25)).grid(column=2, row=0)
op1=tk.Button(frm2,text="+",command=F_op1,font=("Arial",25)).grid(column=3, row=0)

quatre=tk.Button(frm2,text="4",command=F_quatre,font=("Arial",25)).grid(column=0, row=1)
cinq=tk.Button(frm2,text="5",command=F_cinq,font=("Arial",25)).grid(column=1, row=1)
six=tk.Button(frm2,text="6",command=F_six,font=("Arial",25)).grid(column=2, row=1)
op2=tk.Button(frm2,text="-",command=F_op2,font=("Arial",25)).grid(column=3, row=1)

sept=tk.Button(frm2,text="7",command=F_sept,font=("Arial",25)).grid(column=0, row=2)
huit=tk.Button(frm2,text="8",command=F_huit,font=("Arial",25)).grid(column=1, row=2)
neuf=tk.Button(frm2,text="9",command=F_neuf,font=("Arial",25)).grid(column=2, row=2)
op3=tk.Button(frm2,text="*",command=F_op3,font=("Arial",25)).grid(column=3, row=2)

zero=tk.Button(frm2,text="0",command=F_zero,font=("Arial",25)).grid(column=0, row=3)
e=tk.Button(frm2,text="e",command=F_e,font=("Arial",25)).grid(column=1, row=3)
pi=tk.Button(frm2,text="π",command=F_pi,font=("Arial",25)).grid(column=2, row=3)
op4=tk.Button(frm2,text="/",command=F_op4,font=("Arial",25)).grid(column=3, row=3)

par1=tk.Button(frm2,text="(",command=F_par1,font=("Arial",25)).grid(column=0, row=4)
par2=tk.Button(frm2,text=")",command=F_par2,font=("Arial",25)).grid(column=1, row=4)
ans=tk.Button(frm2,text="ans",command=F_ans,font=("Arial",20)).grid(column=2, row=4)
dec=tk.Button(frm2, text=".", command=F_dec,font=("Arial",25)).grid(column=3, row=4)

res=tk.Button(frm2,text="res",command=affichage_final,font=("Arial",20)).grid(column=1, row=5)
quit=tk.Button(frm2, text="Quit", command=root.destroy,font=("Arial",20)).grid(column=2, row=5)
C=tk.Button(frm2, text="C", command=reset,font=("Arial",25)).grid(column=0, row=5)


root.mainloop()