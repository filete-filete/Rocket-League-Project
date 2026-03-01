import time
import threading
import tkinter as tk
import winsound

import rocket_league_project.rocket_scraper as scraper

# =============================================================================
# FUNCTION DEFINITIONS REGARDING START AND STOP BUTTONS
# =============================================================================

stop = False

def session_loop(platform, username):
    # when the start button is pressed, start_session() begins session_loop()
    global stop
    stop = False
    while not stop:
        winsound.Beep(700,666)
        scraper.get_stats(platform, username)
        time.sleep(60)
        

def start_session(platform, username):
    t = threading.Thread(target = session_loop, args = (platform, username))
    t.start()

def end_session():
    # when the stop button is pressed finish the session loop
    global stop
    stop = True
    print("stop")
    
    
# =============================================================================
# POTENTIAL USERNAMES
# =============================================================================

# platform = "Epic"
# username = "filete_filete"
# # platform = "PS4"
# # username = "pool__rabbit"

# =============================================================================
# CREATING THE GUI: GRAPHIC USE INTERFACE
# =============================================================================

root = tk.Tk() # creates the window

# What follows are the widgets

label = tk.Label(root, text = "Rocket League Project").grid(row = 0, column = 0)

tk.Label(root, text="Username: ").grid(row=1, column=0)
tk.Label(root, text="Platform: ").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1) 

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Overtime", variable=var1).grid(row=3, column = 0)
tk.Checkbutton(root, text="Forfeit", variable=var2).grid(row=3, column = 1)

button_s = tk.Button(root, text="START", padx=30, pady=20, bg = "#93fa8c", command = lambda platform = "Epic", username = "filete_filete": start_session(platform, username))
button_s.grid(row = 4, column= 0)

button_s = tk.Button(root, text = "STOP", padx=30, pady=20, bg = "#fa8c8c", command = end_session)
button_s.grid(row = 4, column = 1)

text = tk.Text(root, height = 10, width = 28)
text.grid(row = 5, columnspan = 2)

root.mainloop() # starts the event loop and keeps the window responsive