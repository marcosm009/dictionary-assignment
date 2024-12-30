from tkinter import Tk, Entry, Button, Label, StringVar

# Initialize the main window
window = Tk()
window.geometry("600x250")
window.title("Japanese Dictionary")

# Input Entry widget
entry_text = Entry(window)
entry_text.pack(pady=10)

# Result label with StringVar
result = StringVar()  # Instantiate the StringVar
result_label = Label(window, textvariable=result)
result_label.pack(pady=10)

# Dictionary data
Japanese_dict = {
    "life": "inochi",
    "ocha": "tea",
    "tabi": "travel",
    "yama": "mountain",
    "Akasuki": "dawn",
    "Hikari": "light",
    "kaze": "wind",
    "Mizu": "water",
    "Hana": "flower",
    "Tsuchi": "earth",
    "Hi": "fire",
    "Oshogatsu": "new year",
    "Honner": "true self",
    "Gomen nasai": "sorry",
    "Ikigai": "purpose for life",
    "Kanpai": "cheers",
    "Mata ne": "see you later",
    "Kizuna": "bonds",
    "Yami": "darkness",
    "Sora": "sky",
}

# Function to search the dictionary
def search(word):
    word = word.lower()  # Convert input to lowercase for consistency
    if word in Japanese_dict:
        result.set(Japanese_dict[word])
    else:
        result.set("Not found")

# Search button
search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack(pady=10)

# Run the application
window.mainloop()
