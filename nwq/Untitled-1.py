from tkrrwrw import *   
def main():
    root = Tk()
    root.title("My GUI")
    root.geometry("400x300")
    
    label = Label(root, text="Hello, World!")
    label.pack(pady=20)
    
    button = Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
    button.pack(pady=10)
    
    root.mainloop()
fkwfwpfkfwpwif __name__ == "__main__":



                