import pyautogui
import time
import tkinter as tk
import keyboard

def type_text(text, wait_time):
    # Wait for the specified amount of time
    time.sleep(wait_time)
    # Identify the active window
    active_window = pyautogui.getActiveWindow()
    # Split the text into lines
    lines = text.splitlines()
    # Type each line
    for line in lines:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):  # if esc key is pressed
            break

def start_typing():
    text = text_entry.get('1.0', 'end-1c')
    wait_time = int(wait_entry.get())
    type_text(text, wait_time)

root = tk.Tk()
root.title("UdayAutoTyper")  # Set the title
root.geometry("500x500")  # Set the window size
root.config(bg='#1c1c1e')  # Set the background color to dark theme
root.resizable(False, False)  # Make the window non-resizable

text_label = tk.Label(root, text="Text:", font=("Helvetica", 14), bg='#1c1c1e', fg='white')
text_entry = tk.Text(root, height=10, width=50, font=("Helvetica", 14), bg='#262629', fg='white')
wait_label = tk.Label(root, text="Wait time (seconds):", font=("Helvetica", 14), bg='#1c1c1e', fg='white')
wait_entry = tk.Entry(root, font=("Helvetica", 14), bg='#262629', fg='white')
start_button = tk.Button(root, text="Start Typing", font=("Helvetica", 14), command=start_typing, bg='#00A8CC', fg='white')

text_label.pack()
text_entry.pack()
wait_label.pack()
wait_entry.pack()
start_button.pack(pady=20)

copyright_label = tk.Label(root, text="Created by Abhyuday Rai", font=("Helvetica", 10), bg='#1c1c1e', fg='white')
copyright_label.pack(side='bottom', pady=10)

root.mainloop()
#this is shivanshu pathak
