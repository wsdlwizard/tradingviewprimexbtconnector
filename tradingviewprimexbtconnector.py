from datetime import datetime
from pytz import timezone
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
#import cv2



class PrimeXBTConn(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TradingView Connector Basic Model by patreon.com//wsdlwizard")
        self.geometry("800x600+2718+53")
        self.process_name_to_find = "Firefox"
        self.move_window_to_top_left(self.process_name_to_find)
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