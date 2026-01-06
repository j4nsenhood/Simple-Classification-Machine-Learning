import tkinter as tk

window = tk.Tk()
window.title("Simple Classification Machine Learning")
window.geometry("400x300")
greeting = tk.Label(text="Input")
inputTest = tk.Entry(text="input something")
inputTestGet = inputTest.get()
outputLabel = tk.Label(text=inputTestGet)
greeting.pack()
inputTest.pack()
outputLabel.pack()
window.mainloop()
