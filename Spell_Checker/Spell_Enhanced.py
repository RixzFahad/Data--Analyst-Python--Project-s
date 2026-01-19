# SpellChecker GUI Program ---- {PROJECT}

""" REQUIRED LIBRARIES """
from spellchecker import SpellChecker
import tkinter as tk
from tkinter import messagebox, scrolledtext


class SpellCheckerAppGUI:
    """
    A GUI-based SpellChecker Application using Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the GUI and SpellChecker.
        """
        self.spell = SpellChecker()  # Initialize the spellchecker

        self.root = root
        self.root.title("🪄 SpellChecker App")
        self.root.geometry("600x400")
        self.root.config(bg="#2C3E50")  # Dark Blue Background

        # Title Label
        self.title_label = tk.Label(
            root,
            text="SpellChecker App",
            font=("Helvetica", 20, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.title_label.pack(pady=10)

        # Input Text Area
        self.input_label = tk.Label(
            root,
            text="Enter your text below:",
            font=("Helvetica", 12),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.input_label.pack(pady=5)

        self.input_text = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            width=70,
            height=8,
            font=("Helvetica", 12)
        )
        self.input_text.pack(pady=5)

        # Correct Button
        self.correct_button = tk.Button(
            root,
            text="✅ Correct Text",
            font=("Helvetica", 12, "bold"),
            bg="#1ABC9C",
            fg="#ffffff",
            command=self.correct_text_gui
        )
        self.correct_button.pack(pady=10)

        # Output Text Area
        self.output_label = tk.Label(
            root,
            text="Corrected Text:",
            font=("Helvetica", 12),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            width=70,
            height=8,
            font=("Helvetica", 12),
            state='disabled'  # Make output read-only
        )
        self.output_text.pack(pady=5)

    def correct_text_gui(self):
        """
        Correct the text entered by the user and display corrected text in the output box.
        """
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to correct!")
            return

        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word.lower())

            # If the spellchecker returns None, keep the original word
            if corrected_word is None:
                corrected_word = word

            corrected_words.append(corrected_word)

        corrected_text = ' '.join(corrected_words)

        # Display corrected text in output box
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, corrected_text)
        self.output_text.config(state='disabled')


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerAppGUI(root)
    root.mainloop()
