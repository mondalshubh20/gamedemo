from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()

root.title("rock-paper-scissors")
root.configure(background="cadetblue3")

# images
rock_image = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_image = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_image = ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_imgage_com = ImageTk.PhotoImage(Image.open("rock.png"))
paper_imgage_com = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_imgage_com = ImageTk.PhotoImage(Image.open("scissor.png"))

# insert images
user_label = Label(root, image=scissor_image, bg="cadetblue3")
com_label = Label(root, image=scissor_imgage_com, bg="cadetblue3")
com_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# points
Player_points = Label(root, text=0, font=("Helvetica", 36), bg="cadetblue3", fg="red")
computer_points = Label(root, text=0, font=("Helvetica", 36), bg="cadetblue3", fg="red")
computer_points.grid(row=1, column=1)
Player_points.grid(row=1, column=3)

# indication
user_indicator = Label(root, font=("Helvetica", 36), text="USER", bg="cadetblue3", fg="black")
computer_indicator = Label(root, font=("Helvetica", 36), text="COMPUTER", bg="cadetblue3", fg="black")
user_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)

# messages
Message = Label(root, font=("Helvetica", 24), bg="cadetblue3", fg="black", text="")
Message.grid(row=3, column=2)

# update message
def updateMessage(X):
    Message.config(text=X)

# update user points
def updateUser_point():
    point = int(Player_points["text"])
    point += 1
    Player_points["text"] = str(point)

# update Computer points
def updateCom_point():
    point = int(computer_points["text"])
    point += 1
    computer_points["text"] = str(point)

# Winner
def winner(player, computer):
    if player == computer:
        updateMessage("It's a Draw!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOSE")
            updateCom_point()
        else:
            updateMessage("YOU WIN")
            updateUser_point()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("YOU LOSE")
            updateCom_point()
        else:
            updateMessage("YOU WIN")
            updateUser_point()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("YOU LOSE")
            updateCom_point()
        else:
            updateMessage("YOU WIN")
            updateUser_point()
    else:
        pass

# update choice
choices = ["rock", "paper", "scissor"]

def update_Choice(choice):
    # Computer choice
    Computer_choice = choices[randint(0, 2)]
    if Computer_choice == "rock":
        com_label.configure(image=rock_imgage_com)
    elif Computer_choice == "paper":
        com_label.configure(image=paper_imgage_com)
    else:
        com_label.configure(image=scissor_imgage_com)

    # User choice
    if choice == "rock":
        user_label.configure(image=rock_image)
    elif choice == "paper":
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)

    winner(choice, Computer_choice)

# button
rock = Button(root, width=25, height=2, text="ROCK", bg="#FFB90F", fg="black", command=lambda: update_Choice("rock"))
paper = Button(root, width=25, height=2, text="PAPER", bg="#FF1493", fg="black", command=lambda: update_Choice("paper"))
scissor = Button(root, width=25, height=2, text="SCISSOR", bg="#00C957", fg="black", command=lambda: update_Choice("scissor"))

rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

root.mainloop()
