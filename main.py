import tkinter as tk

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
#intxtfrm = tk.Frame(master=window)
input = tk.Text(master=window)
#inscr = tk.Scrollbar(master=input, command=input.yview)
mnufrm = tk.Frame(master=window)
output = tk.Text(master=mnufrm, height=1)
btn = tk.Button(master=mnufrm, text="Go", command=scour)
outscr = tk.Scrollbar(master=mnufrm, command=output.yview)


### PACKING ###
#intxtfrm.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

input.pack(fill=tk.BOTH, expand=True)
#inscr.pack(fill=tk.Y, side=tk.RIGHT, expand=True)
#input['yscrollcommand'] = inscr.set

mnufrm.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

btn.pack(side=tk.LEFT, expand=False)

output.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
outscr.pack(fill=tk.Y, side=tk.RIGHT, expand=True)
output.insert("1.0", "Output will appear here.")
output['yscrollcommand'] = outscr.set

### WINDOW LOOP ###
window.mainloop()