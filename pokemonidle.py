import random
from tkinter import *


pok1_health = 100
pok2_health = 100

window=Tk()
my_canvas=Canvas(window,width=1500,height=800)
my_canvas.pack(fill="both",expand=True)


def move_fun1():
    coordinates=my_canvas.coords(my_image1)
    if(coordinates[0]>900):
        my_canvas.move(my_image1, -2, 0)
        window.after(20,move_fun1)


#function for moving bulbasaur on the right(player)
def move_fun2():
    coordinates=my_canvas.coords(my_image2)
    if(coordinates[0]>900):
        my_canvas.move(my_image2, -2, 0)
        window.after(20,move_fun2)


#function for moving squirtle on the right(player)
def move_fun3():
    coordinates=my_canvas.coords(my_image3)
    if(coordinates[0]>900):
        my_canvas.move(my_image3, -2, 0)
        window.after(20,move_fun3)


#function for moving charmander on the left(opponent)
def move_fun11():
    coordinates=my_canvas.coords(my_image11)
    if(coordinates[0]<400):
        my_canvas.move(my_image11, 2, 0)
        window.after(20,move_fun11)


#function for moving bulbasaur on the left(opponent)
def move_fun22():
    coordinates=my_canvas.coords(my_image22)
    if(coordinates[0]<250):
        my_canvas.move(my_image22, 2, 0)
        window.after(20,move_fun22)


#function for moving squirtle on the left(opponent)
def move_fun33():
    coordinates=my_canvas.coords(my_image33)
    if(coordinates[0]<400):
        my_canvas.move(my_image33, 2, 0)
        window.after(20,move_fun33)


#disabling the radiobuttons after the pokemon is selected
def disable_Poke_radio():
    radio1.configure(state=DISABLED) 
    radio2.configure(state=DISABLED) 
    radio3.configure(state=DISABLED)
    but1.configure(state=DISABLED ) 


#function for displaying the pokemon and their moves on the screen
def select_poke():
    
  #  entry1=Entry(window,text=value)
   # my_canvas.create_window(1400,20,window=entry1)
    #tmsg.showinfo("selected",{var_pok.get()})
    if var_pok.get()==1:
        move_fun1()  
        move_fun11()
        my_canvas.create_window(100,20,window=label2)
        my_canvas.create_window(1200,95,window=radio4)
        my_canvas.create_window(1300,95,window=radio5)
        my_canvas.create_window(1200,125,window=but2)
        

    elif var_pok.get()==2:
        move_fun2() 
        move_fun22() 
        my_canvas.create_window(100,20,window=label2)
        my_canvas.create_window(1200,95,window=radio6)
        my_canvas.create_window(1300,95,window=radio7)
        my_canvas.create_window(1200,125,window=but2)
        

    elif var_pok.get()==3:
        move_fun3()
        move_fun33()  
        my_canvas.create_window(100,20,window=label2)
        my_canvas.create_window(1200,95,window=radio8)
        my_canvas.create_window(1300,95,window=radio9)
        my_canvas.create_window(1200,125,window=but2)

    disable_Poke_radio()



def select_move():
    print("hello")

#define background image
bg=PhotoImage(file='D:\pokemon\\background1.png')
my_canvas.create_image(0,0, image=bg,anchor=NW)


#defining images for pokemon
photo_image1 = PhotoImage(file='D:\pokemon\\charmander_bg.png')
my_image1 = my_canvas.create_image(1550,700,image=photo_image1,anchor=SW)

photo_image2 = PhotoImage(file='D:\pokemon\\bulbasaur3bg.png')
my_image2 = my_canvas.create_image(1550,700,image=photo_image2,anchor=SW)

photo_image3 = PhotoImage(file='D:\pokemon\\squirtle_bg.png')
my_image3 = my_canvas.create_image(1500,700,image=photo_image3,anchor=SW)


photo_image11 = PhotoImage(file='D:\pokemon\\squirtel_left_bg.png')
my_image11 = my_canvas.create_image(-350,700,image=photo_image11,anchor=SW)

photo_image22 = PhotoImage(file='D:\pokemon\\charmender_left_bg.png')
my_image22 = my_canvas.create_image(-500,700,image=photo_image22,anchor=SW)

photo_image33 = PhotoImage(file='D:\pokemon\\bulbasaur_left_bg.png')
my_image33 = my_canvas.create_image(-350,700,image=photo_image33,anchor=SW)


#declaring 2 integer variables for storing the value of radio buttons
var_pok=IntVar()
var_atk=IntVar()



#defining the value of radiobuttons according to the pokemons 
radio1=Radiobutton(window,text="Charmander",variable=var_pok,value=1)
radio2=Radiobutton(window,text="Bulbasaur",variable=var_pok,value=2)
radio3=Radiobutton(window,text="Squirtle",variable=var_pok,value=3)


#When the button 'select' is clicked, the function select_poke will be called
but1=Button(window,text="select",command=select_poke)
my_canvas.create_window(1200,75,window=but1)


#Giving the label
label1=Label(window,text="Ash chooses")
my_canvas.create_window(1200,20,window=label1)

label2=Label(window,text="Gary chooses bulbasaur")

my_canvas.create_window(1200,45,window=radio1)
my_canvas.create_window(1300,45,window=radio2)
my_canvas.create_window(1400,45,window=radio3)

#function for moving charmander on the right(player)

#declaring the button 'select your move'
but2=Button(window,text="select Your Move",command=select_move)

#declaring radiobuttons for attacks
radio4=Radiobutton(window,text="Scratch",variable=var_atk,value=1)
radio5=Radiobutton(window,text="Ember",variable=var_atk,value=2)
radio6=Radiobutton(window,text="Pound",variable=var_atk,value=3)
radio7=Radiobutton(window,text="Vine Whip",variable=var_atk,value=4)
radio8=Radiobutton(window,text="Tackle",variable=var_atk,value=5)
radio9=Radiobutton(window,text="Watergun",variable=var_atk,value=6)
radio10=Radiobutton(window,text="Heal",variable=var_atk,value=7)
    


moves = {"Pound": range(11,26),
         "Vine whip": range(23,26), 
         "Scratch": range(13,26),
         "Ember": range(16,26),
         "Tackle": range(18,26),
         "Watergun": range(13,26),
         "Heal": range(10,20) }

'''class Pokemon:
    """ Define our general Character which we base our player and enemy off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Pokemon):
    """ The player, they start with 100 health and have the choice of three moves """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = var_atk.get()
            if choice == "Heal":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == 1 or choice == 2:
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            if choice == "Tackle" or choice == "Watergun":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))

                break
            if choice == "Pound" or choice == "Vine whip":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Enemy(Pokemon):
    """ The enemy, also starts with 100 health and chooses moves at random """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if pokemon2 == 'charmander':

            if self.health <= 35:

                # increasing probability of heal when under 35 health, bit janky
                moves_1 = ["Scratch", "Ember", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Scratch", "Ember"]
                cpu_choice = random.choice(moves_2) 
            if cpu_choice == "Scratch" or cpu_choice == "Ember":
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                print("\nThe CPU attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
            if cpu_choice == "Heal":
                self.health += int(random.choice(moves[cpu_choice]))
                print("\nThe CPU uses heal and its health is now {0.health}.".format(self))
    
        if pokemon2 == 'squirtle':
            if self.health <= 35:
                # increasing probability of heal when under 35 health, bit janky
                moves_1 = ["Tackle", "Watergun", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Tackle", "Watergun"]
                cpu_choice = random.choice(moves_2)  
            if cpu_choice == "Tackle" or cpu_choice == "Watergun":
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                print("\nThe CPU attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
            if cpu_choice == "Heal":
                self.health += int(random.choice(moves[cpu_choice]))
                print("\nThe CPU uses heal and its health is now {0.health}.".format(self))

        if pokemon2 == 'bulbasaur':
            if self.health <= 35:
                # increasing probability of heal when under 35 health, bit janky
                moves_1 = ["Pound", "Vine whip", "Heal"]
                cpu_choice = random.choice(moves_1)
            else:
                moves_2= ["Pound", "Vine whip"]
                cpu_choice = random.choice(moves_2)
            if cpu_choice == "Pound" or cpu_choice == "Vine whip":
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                print("\nThe CPU attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
            if cpu_choice == "Heal":
                self.health += int(random.choice(moves[cpu_choice]))
                print("\nThe CPU uses heal and its health is now {0.health}.".format(self))
      
def battle(player, enemy):
    
  
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print("\nThe health of the CPU is now {0.health}.".format(enemy))
        enemy.attack(player)
        if player.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(player))
    # outcome
    if player.health > 0:
        print("You defeated the CPU!")
    if enemy.health > 0:
        print("You were defeated by the CPU!")

if __name__ == '__main__':
    battle(Player(), Enemy())




###########################################################################
'''
