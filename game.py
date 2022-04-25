from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random

window = Tk()
window.title("Laboratorijas darbs")
window.geometry("600x250")
window.configure(background = "lightgray")

def rules():
    rules = """Spēles sākumā ir dota skaitļu virkne: 54792. Spēlētāji izpilda 
    gājienus pēc kārtas. Gājiena laikā skaitļu virkne tiek apskatīta no kreisās 
    puses uz labo pusi un tajā var aizvietot jebkuru divu blakusstāvošo skaitļu 
    kombināciju, pamatojoties uz šādiem nosacījumiem: ja divu blakusstāvošu 
    skaitļu summa ir lielāka par 9, tad to aizvieto ar 1, ja skaitļu summa ir 
    mazāka par 9, tad to aizvieto ar 2, ja summa ir vienāda ar 9, tad to aizvieto 
    ar 3. Spēle beidzas, kad virknē paliek divi skaitļi. Ja pēdējo divu skaitļu 
    summa ir lielāka par 4,tad uzvar tas, kurš uzsāka spēli. Ja skaitļu summa ir 
    mazāka par 4, tad uzvarotrs spēlētajs. Ja skaitļu summa ir vienāda ar 4, 
    tad rezultāts ir neizšķirts"""
    tkinter.messagebox.showinfo("Noteikumi", rules)

def clear_btn():
    entry.delete(0, END)

def check_winner_user_start():
    global label
    var = label.cget("text")
    if var == "32" or "52":
        check_winner.config(text = "Apsveicam, Jus uzvarejat!")
    if var == "12" or "11" or "21":
        check_winner.config(text = "Diemzel dators uzvareja!")
    if var == "22":
        check_winner.config(text = "Neizskirts!")

def check_winner_computer_start():
    global label
    var = label.cget("text")
    if var == "32" or "52":
        check_winner.config(text = "Diemzel dators uzvareja!")
    if var == "12" or "11" or "21":
        check_winner.config(text = "Apsveicam, Jus uzvarejat!")
    if var == "22":
        check_winner.config(text = "Neizskirts!")

def new_game():
    #global player
    #player = random.choice(players)
    label.config(text = "54792")
    check_winner.config(text = "")
    player_move1.config(text = "")
    player_move2.config(text = "")
    player_move3.config(text = "")
    computer_move1.config(text = "")
    computer_move2.config(text = "")
    computer_move3.config(text = "")

player_move1 = Button(window, text = "1. gajiens", width = 7)
player_move2 = Button(window, text = "2. gajiens", width = 7)
player_move3 = Button(window, text = "3. gajiens", width = 7)
computer_move1 = Button(window, text = "1. gajiens", width = 7)
computer_move2 = Button(window, text = "2. gajiens", width = 7)
computer_move3 = Button(window, text = "3. gajiens", width = 7)

def player_start():
    player_move1.config(text = "1. gajiens", command = user_move_first)
    player_move1.place(x = 20, y = 155)

    computer_move2.config(text = "2. gajiens", command = computer_move_second)
    computer_move2.place(x = 420, y = 155)

    player_move3.config(text = "3. gajiens", command = user_move_third)
    player_move3.place(x = 20, y = 185)

    check_winner_btn.config(command = check_winner_user_start)
  
def computer_start():
    computer_move1.config(text = "1. gajiens", command = computer_move_first)
    computer_move1.place(x = 490, y = 155)

    player_move2.config(text = "2. gajiens", command = user_move_second)
    player_move2.place(x = 90, y = 155)

    computer_move3.config(text = "3. gajiens", command = computer_move_third)
    computer_move3.place(x = 490, y = 185)

    check_winner_btn.config(command = check_winner_computer_start)


def user_move_first():
    global entry
    var = entry.get()
    #label.config(text = var)
    if var == "54":
        label.config(text = "3792")
    elif var == "47":
        label.config(text = "5192")
    elif var == "79":
        label.config(text = "5412")
    elif var == "92":
        label.config(text = "5471")  
        
def computer_move_second():
    global label
    var = label.cget("text")
    if var == "3792":
        pc_choise = random.randint(1,3)
        if pc_choise == 1:
            label.config(text = "192")
        elif pc_choise == 2:
            label.config(text = "312")
        elif pc_choise == 3:
            label.config(text = "371")

    if var == "5192":
        pc_choise = random.randint(1,3)
        if pc_choise == 1:
            label.config(text = "292")
        elif pc_choise == 2:
            label.config(text = "512")
        elif pc_choise == 3:
            label.config(text = "511")

    if var == "5412":
        pc_choise = random.randint(1,3)
        if pc_choise == 1:
            label.config(text = "312")
        elif pc_choise == 2:
            label.config(text = "522")
        elif pc_choise == 3:
            label.config(text = "542")
    
    if var == "5471":
        pc_choise = random.randint(1,3)
        if pc_choise == 1:
            label.config(text = "371")
        elif pc_choise == 2:
            label.config(text = "511")
        elif pc_choise == 3:
            label.config(text = "542")

def user_move_third():
    global label
    entryVar = label.cget("text")
    var = entry.get()
    if entryVar == "192":
        if var == "19":
            label.config(text = "12")
        elif var == "92":
            label.config(text = "11")
    if entryVar == "312":
        if var == "31":
            label.config(text = "22")
        elif var == "12":
            label.config(text = "32")
    if entryVar == "371":
        if var == "37":
            label.config(text = "11")
        elif var == "71":
            label.config(text = "32")

    if entryVar == "292":
        if var == "29":
            label.config(text = "12")
        elif var == "92":
            label.config(text = "21")
    if entryVar == "512":
        if var == "51":
            label.config(text = "22")
        elif var == "12":
            label.config(text = "52")
    if entryVar == "511":
        if var == "51":
            label.config(text = "21")
        elif var == "11":
            label.config(text = "52")

    if entryVar == "312":
        if var == "31":
            label.config(text = "22")
        elif var == "12":
            label.config(text = "32")
    if entryVar == "522":
        if var == "52":
            label.config(text = "22")
        elif var == "22":
            label.config(text = "52")
    if entryVar == "542":
        if var == "54":
            label.config(text = "32")
        elif var == "42":
            label.config(text = "52")
    
    if entryVar == "371":
        if var == "37":
            label.config(text = "11")
        elif var == "71":
            label.config(text = "32")
    if entryVar == "511":
        if var == "51":
            label.config(text = "21")
        elif var == "11":
            label.config(text = "52")
    if entryVar == "542":
        if var == "54":
            label.config(text = "32")
        elif var == "42":
            label.config(text = "52")


def computer_move_first():
    global label
    var = label.cget("text")
    pc_choise = random.randint(1,4)
    if pc_choise == 1:
        label.config(text = "3792")
    elif pc_choise == 2:
        label.config(text = "5192")
    elif pc_choise == 3:
        label.config(text = "5412")
    elif pc_choise == 3:
        label.config(text = "5471")

def user_move_second():
    global label
    entryVar = label.cget("text")
    var = entry.get()
    if entryVar == "3792":
        if var == "37":
            label.config(text = "192")
        elif var == "79":
            label.config(text = "312")
        elif var == "92":
            label.config(text = "371")

    if entryVar == "5192":
        if var == "51":
            label.config(text = "292")
        elif var == "19":
            label.config(text = "512")
        elif var == "92":
            label.config(text = "511")

    if entryVar == "5412":
        if var == "54":
            label.config(text = "312")
        elif var == "41":
            label.config(text = "522")
        elif var == "12":
            label.config(text = "542")

    if entryVar == "5471":
        if var == "54":
            label.config(text = "371")
        elif var == "47":
            label.config(text = "511")
        elif var == "71":
            label.config(text = "542")

def computer_move_third():
    global label
    var = label.cget("text")
    if var == "192":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "12")
        elif pc_choise == 2:
            label.config(text = "11")
    if var == "312":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "22")
        elif pc_choise == 2:
            label.config(text = "32")
    if var == "371":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "11")
        elif pc_choise == 2:
            label.config(text = "32")
    
    if var == "292":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "12")
        elif pc_choise == 2:
            label.config(text = "21")
    if var == "512":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "22")
        elif pc_choise == 2:
            label.config(text = "52")
    if var == "511":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "32")
        elif pc_choise == 2:
            label.config(text = "52")

    if var == "312":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "22")
        elif pc_choise == 2:
            label.config(text = "32")
    if var == "522":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "22")
        elif pc_choise == 2:
            label.config(text = "52")
    if var == "542":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "32")
        elif pc_choise == 2:
            label.config(text = "52")
    
    if var == "371":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "11")
        elif pc_choise == 2:
            label.config(text = "32")
    if var == "511":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "21")
        elif pc_choise == 2:
            label.config(text = "52")
    if var == "542":
        pc_choise = random.randint(1,2)
        if pc_choise == 1:
            label.config(text = "32")
        elif pc_choise == 2:
            label.config(text = "52")

label = Label(window, text = "54792", width = 5, bg = "white", fg = "black", font = "CourierNew 40 bold", anchor = CENTER)
label.place(x = 217.5, y = 53)

start_choose = Label(window, text = "Kurs veiks pirmo gajienu - Lietotajs / Dators")
start_choose.place(x = 182.5, y= 30)

start_player = Button(window, text = "Lietotajs", command = player_start)
start_player.place(x = 81.25, y = 70)

start_computer = Button(window, text = "Dators", command = computer_start)
start_computer.place(x = 465, y = 70)

input_txt = Label(window, text = "Ievadiet divciparu skaitli seit:")
input_txt.place(x = 3, y = 130)

entry = Entry(window, width = 5)
entry.focus_set()
entry.place(x = 162, y = 131)

label_computer = Label(window, text = "Nospiezat pogu, lai dators veiktu gajienu")
label_computer.place(x = 375, y = 130)

reset_btn = Button(text = "Jauna spele", command = new_game)
reset_btn.place(x = 102, y = 0)

exit_btn = Button(window, text = "Exit", command = window.destroy)
exit_btn.place(x = 0, y = 0, width = 35)

rules_btn = Button(window, text = "Noteikumi", command = rules)
rules_btn.place(x = 35, y = 0)

check_winner_btn = Button(window, text = "Check winner")
check_winner_btn.place(x = 260, y = 200)

check_winner = Label(window, text = "", width = 25)
check_winner.place(x = 210, y = 225)

#frame = Frame(window)
#frame.pack()


window.mainloop()