import sys
import time
import threading
import tkinter as tk
from tkinter import ttk
import winsound


sys.path.append(r"C:\Users\felix\rocket_league_project")
# import rocket_league_project
# from rocket_league_project import rocket_scraper as scraper

import rocket_scraper as scraper
import rocket_graph as graph


# =============================================================================
# FUNCTION DEFINITIONS REGARDING START AND STOP BUTTONS
# =============================================================================

stop = False

def session_loop(platform, username):
    # when the start button is pressed, start_session() begins session_loop()
    print("starting")
    prev_stats, next_stats = [], [] # placeholders for the gathered info
    global stop
    stop = False
    
    
    while not stop:
        # previous work, not removed, so I still collect the data
        time.sleep(120)
        # scraper.get_stats(platform, username)
        
        # new work
        next_stats = scraper.get_stats2(platform, username)
        # can we register a new game?
        if prev_stats[4:9] == next_stats[4:9]: # no, not yet
            print("equality :/")
            pass
        if prev_stats[4:9] != next_stats[4:9]: # yes, we have a new game
            print(r"different :)")
            winsound.Beep(700,666)
            prev_stats = next_stats # reset previous stats
            extra_stats = [goal1_var.get(), goal2_var.get(), overtime_var.get(), forfeit_var.get()]
            # we are taking the new stats and the additional stats given
            scraper.write2table(username,next_stats + extra_stats)
            clear_values()
    print("stopped")
        
        
        

def start_session(platform, username):
    t = threading.Thread(target = session_loop, args = (platform, username))
    t.start()

def end_session():
    # when the stop button is pressed finish the session loop
    global stop
    stop = True
    print("stopping...")

def clear_values():
    overtime_var.set(0)
    forfeit_var.set(0)
    goal1_var.set("")
    goal2_var.set("")
    
       
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

label = tk.Label(root, text = "Rocket League Project")
label.grid(row = 0, columnspan=2)

tk.Label(root, text="Username: ").grid(row=10, column=0)
tk.Label(root, text="Platform: ").grid(row=20, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=10, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=20, column=1)

# intrasession buttons and boxes
overtime_var = tk.IntVar()
forfeit_var = tk.IntVar()
goal1_var = tk.StringVar()
goal2_var = tk.StringVar()

overtime_box = tk.Checkbutton(root, text="Overtime", variable = overtime_var)
overtime_box.grid(row = 30, column = 0)
forfeit_box = tk.Checkbutton(root, text="Forfeit", variable = forfeit_var)
forfeit_box.grid(row = 30, column = 1)
tk.Label(root, text = "Our goals: "). grid(row = 35, column = 0)
goal1_box = ttk.Combobox(root, width = 3, textvariable = goal1_var)
goal1_box["values"] = (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13)
goal1_box.grid(row = 35, column = 1)
tk.Label(root, text = "Their goals: "). grid(row = 36, column = 0)
goal1_box = ttk.Combobox(root, width = 3, textvariable = goal2_var)
goal1_box["values"] = (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13)
goal1_box.grid(row = 36, column = 1)

# buttons to start and stop a session
button_s = tk.Button(root, text="START", width = 15, height = 2, bg = "#93fa8c", command = lambda platform = "Epic", username = "filete_filete": start_session(platform, username))
button_s.grid(row = 40, column= 0)

button_s = tk.Button(root, text = "STOP", width = 15, height = 2, bg = "#fa8c8c", command = end_session)
button_s.grid(row = 40, column = 1)

button_g = tk.Button(root, text = "GRAPH 2v2mmr", width = 15, height = 2, command = graph.ranked2v2)
button_g.grid(row = 50, column = 0)

root.mainloop() # starts the event loop and keeps the window responsive