import tkinter as tk
import requests

def create_ticket():
    name = entry_name.get()
    company = entry_company.get()
    email = entry_email.get()
    issue = entry_issue.get()
    anydesk_id = entry_anydesk.get()

    # Freshdesk API call to create ticket
    # (Use the previous code snippet to create the Freshdesk ticket)

root = tk.Tk()
root.title("Freshdesk Ticket Logger")

# ... (Tkinter setup for entry fields and submit button)
# (Please refer to the previous Tkinter example for the GUI setup)

root.mainloop()
