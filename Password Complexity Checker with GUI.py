import re
import tkinter as tk
from tkinter import messagebox

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8

    def check_uppercase(self):
        return re.search(r'[A-Z]', self.password) is not None

    def check_lowercase(self):
        return re.search(r'[a-z]', self.password) is not None

    def check_digit(self):
        return re.search(r'\d', self.password) is not None

    def check_special(self):
        return re.search(r'[^A-Za-z0-9]', self.password) is not None

    def analyze_password(self):
        return {
            'length': self.check_length(),
            'uppercase': self.check_uppercase(),
            'lowercase': self.check_lowercase(),
            'digit': self.check_digit(),
            'special_char': self.check_special()
        }

    def suggest_password(self):
        analysis = self.analyze_password()
        suggestions = []

        if not analysis['length']:
            suggestions.append("Password should be at least 8 characters long.")
        if not analysis['uppercase']:
            suggestions.append("Include at least one uppercase letter.")
        if not analysis['lowercase']:
            suggestions.append("Include at least one lowercase letter.")
        if not analysis['digit']:
            suggestions.append("Include at least one digit.")
        if not analysis['special_char']:
            suggestions.append("Include at least one special character.")

        return suggestions

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")

        self.label = tk.Label(root, text="Enter your password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(root, show="*", width=40)
        self.password_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=10)

    def check_password(self):
        password = self.password_entry.get()
        analyzer = PasswordAnalyzer(password)
        analysis = analyzer.analyze_password()
        suggestions = analyzer.suggest_password()

        result_message = "Password analysis results:\n"
        result_message += f"Length: {'Passed' if analysis['length'] else 'Failed'}\n"
        result_message += f"Uppercase: {'Passed' if analysis['uppercase'] else 'Failed'}\n"
        result_message += f"Lowercase: {'Passed' if analysis['lowercase'] else 'Failed'}\n"
        result_message += f"Digit: {'Passed' if analysis['digit'] else 'Failed'}\n"
        result_message += f"Special Character: {'Passed' if analysis['special_char'] else 'Failed'}\n"

        if suggestions:
            result_message += "\nPassword suggestions:\n" + "\n".join(suggestions)
        else:
            result_message += "\nPassword meets all security requirements."

        messagebox.showinfo("Password Analysis Results", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()
