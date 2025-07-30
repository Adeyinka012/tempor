from tkinter import *
window=Tk()
window.title("Event handler0")
window.geometry("100x100")
def handle_keypress(event):
    """Print the character accosiated to the key pressed"""
    print("You pressed:", event.char)
# bind keypress event handler keypress
window.bind("<KeyPress>", handle_keypress)
def handle_click(event):
    """Print the coordinates of th mouse click"""
    print("Mouse clicked at:", event.x, event.y)
button=Button(text="  click Me")
button.pack()
#bind click event handler click
button.bind("<Button-1>", handle_click)

window.mainloop()