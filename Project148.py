
from tkinter import *
import random

root= Tk()
root.title("List")
root.geometry("400x400")

random_list = Label(root)
random_number_list = Label(root)
item_list = Label(root)


def list1():
    list1 = random.sample(range(1,7),1)
    random_list["text"] = "Put This Item in the Bag : " + str(list1)
    random_list.sort()
    random_number_list["text"] = "random sorted list : " + str(list1)
    item_list["text"] = "Phone, Snacks, lunch, Water bottle, Speaker, Chair" + str(list1)

btn=Button(root, text="Which item should I put in the bag?", command=list1)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)

btn=Button(root, text="Phone, Snacks, lunch, Water bottle, Speaker, Chair")
btn.place(relx = 0.5, rely = 0.2, anchor=CENTER)

random_list.place(relx=0.5, rely=0.7, anchor=CENTER)
random_number_list.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
