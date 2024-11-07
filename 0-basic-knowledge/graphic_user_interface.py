import tkinter

top = tkinter.Tk()
btn = tkinter.Button()

btn['text'] = 'Click here!'
btn.pack()

def clicked():
    print("I'm clicked")

btn['command'] = clicked

# btn.config(text="Click here!", command="I'm clicked!")

tkinter.Label(text="I'm in the top window!").pack(side=tkinter.LEFT)
second = tkinter.Toplevel()
tkinter.Label(second, text="I'm in the second window!").pack()

def callback(event):
    print(event.x, event.y)

for i in range(10):
    b = tkinter.Button(text=i)
    b.pack(side="left")
    b["command"] = clicked

if __name__ == "__main__":
    tkinter.mainloop() # you don't need this in a interactive intepreter