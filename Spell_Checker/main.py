# Spell Correction Program ---- {PROJECT}

""" REQUIRED LIBRARIES """
from spellchecker import SpellChecker


""" CREATING THE SPELLCLASS """

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word.lower())

            if corrected_word != word.lower():
                print(f"Correcting word: {word} → {corrected_word}")

            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    """ RUNNING THE SPELLCHECKER """
    def run(self):
        print("\n---- SpellChecker App Started ----")
        while True:
            text = input("Enter text to check (type 'exit' to quit): ")

            if text.lower() == "exit":
                print("\n---- SpellChecker App Ended ----")
                break

            corrected_text = self.correct_text(text)
            print(f"Corrected Text: {corrected_text}\n")


""" RUNNING THE MAIN PROGRAM """
if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()
