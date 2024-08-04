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
    def delete_back(self):
        print("Closing primexbtmanager")