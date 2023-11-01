import csv
import tkinter as tk
from tkinter import filedialog
import os

class Logger:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main Tkinter window
        self.csv_filename = None  # Initialize to None

    def select_log_file(self):
        # Default file name
        default_file_name = "detected_shapes_log.csv"
        
        # Get the path of the currently running script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        
        # Combine the script directory with the default file name
        default_file_path = os.path.join(script_dir, default_file_name)

        # Open a file dialog to select the log file path with the default path and name
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
                                                initialfile=default_file_name, initialdir=default_file_path)
        if file_path:
            self.csv_filename = file_path

    def write_data(self, detected_shapes):
        if self.csv_filename is None:
            self.select_log_file()  # Prompt the user to select the log file path

        if self.csv_filename:
            with open(self.csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Pattern", "Color"])
                for shape_data in detected_shapes:
                    writer.writerow(shape_data)
            print(f"Data has been written to {self.csv_filename}")

