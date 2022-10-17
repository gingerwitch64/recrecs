import tkinter as tk

kwfile = open("keywords.txt", "r")
keywords = kwfile.read().split(",")
kwfile.close()

def scour(text):
    out = []
    words = text.split()
    for word in words:
        if any(x in word for x in keywords) != -1:
            out.append(word)
        

def main():
    window = tk.Tk()
    input = tk.Text()


    window.mainloop()

if __name__ == "__main__":
    main()
