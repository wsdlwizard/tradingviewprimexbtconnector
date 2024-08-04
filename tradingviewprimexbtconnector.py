from datetime import datetime
from pytz import timezone
#from flask import Flask, request, jsonify
import tkinter as tk
import threading
import pyautogui
import easyocr
import time,json
import pandas as pd
import numpy as np
import win32gui
import pygetwindow as gw
import pickle
import os
import csv

#import cv2

class SettingsFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.amount_coords = (0,0)
        self.market_coords = (0,0)
        self.stop_coords = (0,0)
        self.limit_coords = (0,0)
        self.buy_coords = (0,0)
        self.sell_coords = (0,0)
        self.place_order_coords = (0,0)
        self.place_order_confirm = (0,0)
        self.close_position_coords = (0,0)
        self.close_position_confirm = (0,0)
        # Create label and text box in a group called "Settings"
        self.settings_label = tk.Label(self, text="Settings", font=("Arial", 14))
        self.settings_label.pack(side=tk.TOP)
        
        settings_frame = tk.Frame(self, bg="lightgray", highlightbackground="black", highlightthickness=1)
        settings_frame.pack(padx=10, pady=5)
        # Add some space between the label and the settings
        self.settings_separator = tk.Label(self, text="", height=2)
        self.settings_separator.pack(side=tk.TOP)
        tk.Label(settings_frame, text="Label0").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(settings_frame).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(settings_frame, text="Label1").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(settings_frame).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(settings_frame, text="Label2").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(settings_frame).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(settings_frame, text="Save", command=self.save_settings).grid(row=3, column=0,  pady=5)
        tk.Button(settings_frame, text="Update", command=self.update_settings).grid(row=3, column=1,  pady=5)
        # Add another label and text box below the first group
        self.label_mouse_coords = tk.Label(self, text="Mouse coords:").pack()
        self.mouse_coordinates_frame = tk.Frame(self)
        self.mouse_coordinates_frame.pack()

        label2 = tk.Label(self.mouse_coordinates_frame, text="X:")
        label2.grid(row=0, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(self.mouse_coordinates_frame)
        self.entry2.grid(row=0, column=1, padx=5, pady=5)

        label3 = tk.Label(self.mouse_coordinates_frame, text="Y:")
        label3.grid(row=1, column=0, padx=5, pady=5)
        self.entry3 = tk.Entry(self.mouse_coordinates_frame)
        self.entry3.grid(row=1, column=1, padx=5, pady=5)
    def save_settings(self):
        print("Settings saved!")
    def print_mouse_coordinate(self):
        x, y = pyautogui.position()
        self.entry2.delete(0, tk.END)
        self.entry2.insert(tk.END, str(x))
        self.entry3.delete(0, tk.END)
        self.entry3.insert(tk.END, str(y))
        return (x,y)
        #print(f"Mouse position: ({x}, {y})")
        #self.coord_text.set(f"Mouse position: ({self.x}, {self.y})")
        
    def update_settings(self):
        print("CLick on this Command box title bar THEN Position Cursor on Amount box to the right of the amount and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.amount_coords = ans
                print(f"Coords: {self.amount_coords}")
                break
        #print("Settings updated!")
        print("Position Cursor on Market box and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.market_coords = ans
                print(f"Coords: {self.market_coords}")
                break
        print("Position Cursor on Stop box and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.stop_coords = ans
                print(f"Coords: {self.stop_coords}")
                break
        print("Position Cursor on Limit box and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.limit_coords = ans
                print(f"Coords: {self.limit_coords}")
                break
        print("Position Cursor on Buy button near the side label and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.buy_coords = ans
                print(f"Coords: {self.buy_coords}")
                break
        print("Position Cursor on Sell button near the side label and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.sell_coords = ans
                print(f"Coords: {self.sell_coords}")
                break
        print("Position Cursor on Place Order button and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.place_order_coords = ans
                print(f"Coords: {self.place_order_coords}")
                break
        print("Position Cursor on Place Order Confirm button and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.place_order_confirm = ans
                print(f"Coords: {self.place_order_confirm}")
                break
        print("Position Cursor on Close Position button and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.close_position_coords = ans
                print(f"Coords: {self.close_position_coords}")
                break
        print("Position Cursor on Close Position Confirm button and press enter")
        while True:
            user_input = input("Press Enter to input coords...")
            if user_input == "":
                ans = self.print_mouse_coordinate()
                self.close_position_confirm = ans
                print(f"Coords: {self.close_position_confirm}")
                break
        self.save_coords()
        print("Settings updated!")
    def save_coords(self):
        with open('coords.pkl', 'wb') as f:
            pickle.dump([self.amount_coords,self.market_coords,self.stop_coords,self.limit_coords,self.buy_coords,self.sell_coords,self.place_order_coords,self.place_order_confirm,self.close_position_coords,self.close_position_confirm], f)
    def load_coords(self):
        with open('coords.pkl', 'rb') as f:
            self.amount_coords,self.market_coords,self.stop_coords,self.limit_coords,self.buy_coords,self.sell_coords,self.place_order_coords,self.place_order_confirm,self.close_position_coords,self.close_position_confirm = pickle.load(f)
        

class PrimeXBTConn(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.app = Flask(__name__)
        #self.webhook_thread = threading.Thread(target=self.run_flask_server)
        #self.webhook_thread.daemon = True
        #self.webhook_thread.start()
        #mouse coords for amount
        self.amount_coords = (0,0)
        self.market_coords = (0,0)
        self.stop_coords = (0,0)
        self.limit_coords = (0,0)
        self.buy_coords = (0,0)
        self.sell_coords = (0,0)
        self.place_order_coords = (0,0)
        self.place_order_confirm = (0,0)
        self.close_position_coords = (0,0)
        self.close_position_confirm = (0,0)
        self.amount = "1.01"
        # Create an instance of SettingsFrame
        self.settings_frame = SettingsFrame(self)
        #local widgets
        self.test_button = tk.Button(self, text="Test", command=self.test)
        self.test_button.pack()
        self.run_button = tk.Button(self, text="Run", command=self.run)
        self.run_button.pack()
        self.monitor_thread = threading.Thread(target=self.monitor)
        self.monitor_thread.daemon = True
        #self.monitor_thread.start()
        # Pack the settings frame into the main window
        self.settings_frame.pack(padx=10, pady=10)
        self.title("TradingView Connector Basic Model by patreon.com//wsdlwizard")
        self.geometry("800x600+2718+53")
        self.process_name_to_find = "Firefox"
        self.move_window_to_top_left(self.process_name_to_find)
        self.ascii_banner()
        print("\nThanks for downloading my code! Support me on Patreon: patreon.com/wsdlwizard\n")
        if os.path.exists('coords.pkl'):
            self.load_coords()
            #self.monitor_thread.start()
        else:
            print("No coords found")
            print("Please update settings")
            #self.init_primexbt()
            #self.save_coords()
    def test(self):
        self.load_coords()
        print("Testing Buying and selling small position...")
        self.new_mkt_order("0.01","Buy")
        time.sleep(2)
        self.close_position()
    def run(self):
        self.monitor_thread.start()
    def monitor(self):
        while True:
            print("Monitoring...")
            
            time.sleep(1)
    def load_coords(self):
        with open('coords.pkl', 'rb') as f:
            self.amount_coords,self.market_coords,self.stop_coords,self.limit_coords,self.buy_coords,self.sell_coords,self.place_order_coords,self.place_order_confirm,self.close_position_coords,self.close_position_confirm = pickle.load(f)
        

    def delete_back(self):
        print("Closing primexbtmanager")
    def move_window_to_top_left(self,process_name):
        try:
            # Get all windows matching the process name
            windows = gw.getWindowsWithTitle(process_name)

            if windows:
                # Assuming there's only one window with the given process name
                target_window = windows[0]
                target_window.moveTo(0, 0)  # Move to top-left corner
                print(f"Window Dimentions are {target_window.width} by {target_window.height}")
                target_window.size = (2666,1715)
                print(f"Moved '{target_window.title}' to the top-left corner.")
            else:
                print(f"No window found with process name '{process_name}'.")
        except Exception as e:
            print(f"Error: {e}")
    def move_window(self,hwnd, x, y, width, height):
        # Offset the x position by 7 (adjust as needed)
        win32gui.MoveWindow(hwnd, x - 7, y, width, height, True)
    def ascii_banner(self):
        print(" ____                               _                                  ")
        print("/ ___| _   _ _ __  _ __   ___  _ __| |_   _ __ ___   ___    ___  _ __  ")
        print("\\___ \\| | | | '_ \\| '_ \\ / _ \\| '__| __| | '_ ` _ \\ / _ \\  / _ \\| '_ \\ ")
        print(" ___) | |_| | |_) | |_) | (_) | |  | |_  | | | | | |  __/ | (_) | | | |")
        print("|____/ \\__,_| .__/| .__/ \\___/|_|   \\__| |_| |_| |_|\\___|  \\___/|_| |_|")
        print("|  _ \\ __ _| |_ _ __ ___  ___  _ __                                    ")
        print("| |_) / _` | __| '__/ _ \\/ _ \\| '_ \\                                   ")
        print("|  __/ (_| | |_| | |  __/ (_) | | | |                                  ")
        print("|_|   \\__,_|\\__|_|  \\___|\\___/|_| |_|                                  ")
    def click_drag_and_type(self,x, y, p,the_text,press_enter):
        """
        Clicks the mouse at given coordinates, drags p pixels to the left, and enters the text "0.5".

        Args:
        x: The X coordinate of the click.
        y: The Y coordinate of the click.
        p: The number of pixels to drag the mouse to the left.

        Raises:
        ValueError: If p is not a positive integer.
        """

        if not isinstance(p, int) or p < 0:
            raise ValueError("p must be a positive integer")

        # Click at the specified coordinates
        pyautogui.moveTo(x,y,1)
        pyautogui.click(x, y)
        time.sleep(0.1)
        # Drag the mouse to the left
        pyautogui.dragRel(-p, 0, duration=0.2)  # Adjust duration as needed
        time.sleep(0.1)
        # Type the text the_text
        if the_text != "":
            pyautogui.write(the_text)
        # Press Enter if specified
        time.sleep(0.2)
        if press_enter:
            pyautogui.press("enter")
    def new_mkt_order(self,amount,side):
        self.move_window_to_top_left(self.process_name_to_find)
        #self.click_drag_and_type(1923, 387, 0,"",False)
        time.sleep(0.1)
        self.click_drag_and_type(self.market_coords[0], self.market_coords[1], 0,"",False)
        self.click_drag_and_type(self.amount_coords[0], self.amount_coords[1], 200,amount,False)
        if side == "Buy":
            self.click_drag_and_type(self.buy_coords[0], self.buy_coords[1], 0,"",False)
        #elif side == "Sell":
        else:    
            self.click_drag_and_type(self.sell_coords[0], self.sell_coords[1], 0,"",False)
        time.sleep(0.1)
        #click and drag amount
        self.click_drag_and_type(self.place_order_coords[0], self.place_order_coords[1], 0,"",False)
        time.sleep(0.1)
        self.click_drag_and_type(self.place_order_confirm[0], self.place_order_confirm[1], 0,"",False)
    def close_position(self):
        self.move_window_to_top_left(self.process_name_to_find)
        self.click_drag_and_type(self.close_position_coords[0], self.close_position_coords[1], 0,"",False)
        time.sleep(0.1)
        self.click_drag_and_type(self.close_position_confirm[0], self.close_position_confirm[1], 0,"",False)

        