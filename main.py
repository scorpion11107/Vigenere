import core, tkinter as tk

window = tk.Tk()
window.title("Vigenere")
window.geometry("600x400")
window.resizable(False, False)

keyLabel = tk.Label(window, text = "Key:")
keyTextArea = tk.Text(window, height = 4, width = 70)

textLabel = tk.Label(window, text = "Text:")
textTextArea = tk.Text(window, height = 4, width = 70)

codeButton = tk.Button(window, text = "Code", command = lambda : (resultTextArea.insert(0, core.code(textTextArea.get(0), keyTextArea.get(0), core.generateTable()))))
decodeButton = tk.Button(window, text = "Decode")

resultTextArea = tk.Text(window, height = 4, width = 70)

keyLabel.place(x = 10, y = 10)
keyTextArea.place(x = 5, y = 30)

textLabel.place(x = 10, y = 100)
textTextArea.place(x = 5, y = 120)

codeButton.place(x = 10, y = 220)
decodeButton.place(x = 10, y = 250)

resultTextArea.place(x = 5, y = 290)

window.mainloop()