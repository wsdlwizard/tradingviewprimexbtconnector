import tkinter as tk
from tkinter import messagebox
from tradingviewprimexbtconnector import PrimeXBTConn
from flask import Flask, request

app = Flask(__name__)

if __name__ == "__main__":
    def on_closing():
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            print("Logging out of PrimeXBT...")
            app.delete_back()
            app.destroy()
    app = PrimeXBTConn()
    # Use the protocol method to register a handler for the WM_DELETE_WINDOW protocol
    app.protocol("WM_DELETE_WINDOW", on_closing)
    # Create a new Flask instance
    webhook_app = Flask(__name__)

    @webhook_app.route('/webhook', methods=['POST'])
    def handle_webhook():
        print("Received webhook message:", request.json)
        with open('webhook.log', 'a') as f:
            f.write(str(request.json) + '\n')
        return 'OK'

    # Run the Flask instance in a separate thread
    import threading
    t = threading.Thread(target=webhook_app.run, args=("0.0.0.0", 80))
    t.start()

    app.mainloop()