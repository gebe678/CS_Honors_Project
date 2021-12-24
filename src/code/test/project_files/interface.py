import tkinter as tk

# main function
def main():
    # create the window
    window = tk.Tk()

    # create a label widget
    greeting = tk.Button(text="Hello, Tkinter", height=3)
    greeting.pack()

    # run the event loop
    window.mainloop()

if __name__ == "__main__":
    main()

