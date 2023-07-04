```python
import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Onlyfans Manager AI")
        self.root.geometry("800x600")

        # Define the DOM elements
        self.chatbot = tk.Text(self.root, height=20, width=50)
        self.payment = tk.Text(self.root, height=20, width=50)
        self.analytics = tk.Text(self.root, height=20, width=50)
        self.content = tk.Text(self.root, height=20, width=50)
        self.engagement = tk.Text(self.root, height=20, width=50)
        self.revenue = tk.Text(self.root, height=20, width=50)

        # Pack the DOM elements
        self.chatbot.pack()
        self.payment.pack()
        self.analytics.pack()
        self.content.pack()
        self.engagement.pack()
        self.revenue.pack()

    def display_message(self, message, message_type):
        if message_type == "PaymentSuccess":
            messagebox.showinfo("Payment", message)
        elif message_type == "PaymentFailure":
            messagebox.showerror("Payment", message)
        elif message_type == "PerformanceReport":
            self.analytics.insert(tk.END, message)
        elif message_type == "ChatbotResponse":
            self.chatbot.insert(tk.END, message)

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
```