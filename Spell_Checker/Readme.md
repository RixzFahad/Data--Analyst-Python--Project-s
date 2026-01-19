# SpellChecker GUI Project

## Overview

This project is a **GUI-based SpellChecker Application** built using Python. It utilizes the `pyspellchecker` library for correcting misspelled words and `Tkinter` for a modern, interactive graphical user interface.

## Features

* **GUI-Based:** User-friendly interface with input and output boxes.
* **Scrolled Text:** Supports large paragraphs of text.
* **Real-Time Feedback:** Corrected text displayed instantly.
* **Color Theme:** Dark blue background with turquoise button for a modern look.
* **Validation:** Warns user if input is empty.
* **Read-Only Output:** Prevents accidental editing of corrected text.

## Required Libraries

```bash
pip install pyspellchecker
```

`Tkinter` comes pre-installed with Python, so no additional installation is needed.

## File Structure

```
SpellCheckerApp/
│
├── spellchecker_gui.py       # Main GUI application script
└── README.md                 # Project documentation
```

## spellchecker_gui.py

```python
from spellchecker import SpellChecker
import tkinter as tk
from tkinter import messagebox, scrolledtext

class SpellCheckerAppGUI:
    """
    A GUI-based SpellChecker Application using Tkinter.
    """

    def __init__(self, root):
        self.spell = SpellChecker()
        self.root = root
        self.root.title("🪄 SpellChecker App")
        self.root.geometry("600x400")
        self.root.config(bg="#2C3E50")

        # Title Label
        self.title_label = tk.Label(root, text="SpellChecker App", font=("Helvetica", 20, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.title_label.pack(pady=10)

        # Input Text Area
        self.input_label = tk.Label(root, text="Enter your text below:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.input_label.pack(pady=5)

        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8, font=("Helvetica", 12))
        self.input_text.pack(pady=5)

        # Correct Button
        self.correct_button = tk.Button(root, text="✅ Correct Text", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="#ffffff", command=self.correct_text_gui)
        self.correct_button.pack(pady=10)

        # Output Text Area
        self.output_label = tk.Label(root, text="Corrected Text:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8, font=("Helvetica", 12), state='disabled')
        self.output_text.pack(pady=5)

    def correct_text_gui(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to correct!")
            return

        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word.lower())
            corrected_words.append(corrected_word)

        corrected_text = ' '.join(corrected_words)

        # Display corrected text in output box
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, corrected_text)
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerAppGUI(root)
    root.mainloop()
```

## How to Use

1. Run the program:

```bash
python spellchecker_gui.py
```

2. Enter your text in the **input box**.
3. Click the **"Correct Text"** button.
4. Corrected text will appear in the **output box**.
5. Close the window or click **Exit** to quit.

## Future Enhancements

* Highlight corrected words in different colors.
* Add **Copy to Clipboard** button.
* Support for **file input/output**.
* Multi-language support.
* Dark/Light theme toggle.

---

Created by **Your Name** | Python GUI & NLP Project
