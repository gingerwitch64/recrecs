import tkinter as tk

try:
    kwfile = open("keywords.txt", "r")
    keywords = kwfile.read().split(",")
    kwfile.close()
except:
    cferr = True
    kwfile = open("keywords.txt", "x")
    kwfile.close()
    kwfile = open("keywords.txt", "r")
    keywords = kwfile.read().split(",")
    kwfile.close()

punct = [".","?","!","\n"]

def scour():
    text = input.get("1.0",tk.END)
    out = []
    sentence = 1
    sentword = 1
    words = text.split()
    for word in words:
        if any(x in word for x in punct):
            sentword = 0
        if any(x in word.lower() for x in keywords):
            out.append(f"Keyword found in '{word}' as word number {sentword} in sentence {sentence}.\n")
        if any(x in word for x in punct):
            sentence += 1
        sentword += 1
    output.delete("1.0", tk.END)

    if out == []:
        output.insert("1.0", "No keywords found.")
    else:
        for item in out:
            output.insert(f"{out.index(item)+1}.0", item)

### OBJECTS ###
window = tk.Tk()
input = tk.Text(master=window)
inscr = tk.Scrollbar(master=window, command=input.yview)
output = tk.Text(master=window, height=1)
btn = tk.Button(master=window, text="Go", command=scour)
outscr = tk.Scrollbar(master=window, command=output.yview)


### WINDOW CONFIGURATION ###
window.title("recrecs")
window.rowconfigure([0,1], minsize=10, weight=1)
window.columnconfigure([0,1,2], minsize=10, weight=0)
window.resizable(width=False, height=True)

### PACKING ###
input.grid(row=0, column=1, sticky="nesw")
inscr.grid(row=0, column=2, sticky="nsw")

btn.grid(row=1, column=0, padx=5, pady=5)
output.grid(row=1, column=1, sticky="nesw")
outscr.grid(row=1, column=2, sticky="nsw")

if cferr:
    output.insert("1.0", "keywords.txt not found, so it was auto-created.")
else:
    output.insert("1.0", "Output will appear here.")

input['yscrollcommand'] = inscr.set
output['yscrollcommand'] = outscr.set

### WINDOW LOOP ###
window.mainloop()
