#Trying to make a software!!!

import turtle as tt


#Variables Selection...
Fname= tt.simpledialog.askstring("Log in", "What's your first name?")
Lname= tt.simpledialog.askstring("Log in", "What's your last name?")
Age= tt.simpledialog.askstring("Log in", "How old are you?")

#Screen Setup...
sc= tt.getscreen()
sc.setup(300,150)
sc.bgcolor("Light Blue")
tt.title("Chat with A.I.")
tt.write(f"{Fname} {Lname}.\nHe is {Age} years old.", move=False, align="center")
tt.ht()

#Surety...
print(Fname, Lname ,"\nHe is", Age, "years old")

if __name__=="__main__":
    mainloop()
