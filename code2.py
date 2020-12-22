import tkinter as ksi
import json
root = ksi.Tk()
root.title("Onee.chan!")
root.geometry("500x200")

result_text = ksi.StringVar(root)

with open("data.json") as jj:
    ksimon = json.load(jj)

def search(word):
    if word in ksimon:
        global result_text
        
        for meaning in ksimon[word]:
            result_text.set(meaning)
    else:
        result_text.set("Not found :(")
    

#snippet here

text_box =  ksi.Entry(root, bg = "gray",bd = 7,width = 40,font = 18)
text_box.pack()

search_button = ksi.Button(root,text = "search",command = lambda : search(text_box.get()))

search_button.pack(side = ksi.RIGHT)

result = ksi.Message(root,bg = "gray",textvariable = result_text)
result.pack()

root.mainloop()
