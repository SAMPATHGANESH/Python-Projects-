#creating a mad libs '''my first python project by own'''
from tkinter import *
root = Tk()
root.geometry('800x300')
root.title('funny story generator')
Label(root,text='funny story generator',font='arial 20 italic').pack()
Label(root,text='CLICK FOR STORY ',font='arial 15 bold').place(x=40,y = 50)

#story 
def story1():
    name = input("enter your name")
    world = input("world you wanna visit")
    number = input("number of days you wanna live in the spaceship")
    feeling = input('how will you feel')
    city = input("enter your home town ")


    print("Hello my name is astronaut "+name+" I am on my way to planet "
    +world+"  I will be gone for "+number+" days.I am very  "+feeling+
    " about the trip but I  will misss my  "
    +city+'.' )
def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  
#button
Button(root,text = 'space  story',font = "cambria 10 ", command = story1).place(x = 40,y = 40)
Button(root,text = 'apple  story',font = "cambria 10 ", command = madlib3).place(x = 80,y = 80)

root.mainloop()
