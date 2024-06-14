from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

# SETTING UP TKINTER WINDOW
root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
root['bg'] = 'pink'
root.title('Real-time Translator')

# CREATING GUI
Label(root, text="Language Translator", font="Arial 20 bold").pack()

Label(root, text="Enter Text", font="Arial 13 bold", bg="white smoke").place(x=165, y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

Label(root, text="Output", font="Arial 13 bold", bg="white smoke").place(x=780, y=90)

Output_text = Text(root, font="arial 13 bold", height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')

def translate():
    try:
        # Ensure a language is selected
        selected_lang = dest_lang.get()
        if selected_lang not in LANGUAGES.values():
            raise ValueError("Please select a valid language")

        # Create a Translator object
        translator = Translator()

        # Get the language code for the selected language
        lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(selected_lang)]

        # Translate the input text to the selected destination language
        translation = translator.translate(Input_text.get(), dest=lang_code)

        # Clear the output text and insert the translation
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except ValueError as ve:
        print(f"Translation error: {ve}")
        Output_text.delete(1.0, END)
        Output_text.insert(END, str(ve))
    except Exception as e:
        print(f"Translation error: {e}")
        Output_text.delete(1.0, END)
        Output_text.insert(END, "Translation error occurred. Please try again.")

# Create a button for triggering translation
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)

# Start the Tkinter event loop
root.mainloop()
