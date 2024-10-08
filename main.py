import tkinter as tk
from tkinter import messagebox
from tradingviewprimexbtconnector import PrimeXBTConn




if __name__ == "__main__":
    def on_closing():
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            print("Logging out of PrimeXBT...")
            app.delete_back()
            app.destroy()
    app = PrimeXBTConn()
    # Use the protocol method to register a handler for the WM_DELETE_WINDOW protocol
    app.protocol("WM_DELETE_WINDOW", on_closing)
   

    
    

    # Run the Flask instance in a separate thread
    
    #t = threading.Thread(target=webhook_app.run, args=("0.0.0.0", 80))
    #t.daemon = True
    #t.start()

    app.mainloop()