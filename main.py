

#Trying to make a software!!!


import turtle as tt


#Variables Selection...
Fname= tt.simpledialog.askstring("Log in", "What's your first name?")
Lname= tt.simpledialog.askstring("Log in", "What's your last name?")
Age= tt.simpledialog.askstring("Log in", "How old are you?")


#Screen Setup...
sc= tt.getscreen()
sc.setup(300,150,startx= -90,starty= 300)
sc.bgcolor("Light Blue")
tt.title("Chat with Chibby")
tt.ht()


#Start Chat...
tt.write(f"My name is {Fname} {Lname}.\nI'm {Age} years old.\n", move=False, align="center")
tt.pencolor("white")
tt.write(f"Hello {Fname}! How can I help you?",move=False, align="center")


while True:
    text = tt.simpledialog.askstring("", "Reply")
    if text.lower() =="who are you?":
        tt.clear()
        tt.write("I'm a ChatBot!\n",move=False, align="center")
        continue
    elif text.lower() =="what is your name?":
        tt.clear()
        tt.write("My name is Chibby!\n",move=False, align="center")
        continue
    elif text.lower() =="":
        tt.clear()
        tt.write("Sorry, I didn't hear you.\n",move=False, align="center")
        continue
    else:
        tt.clear()
        tt.write("See you soon!\n",move=False, align="center")
        break


#Close and clear chat...
tt.exitonclick()


#Surety...
print(Fname, Lname ,"\nHe is", Age, "years old")

if __name__=="__main__":
    sc.mainloop()




    
