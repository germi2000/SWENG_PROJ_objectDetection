import csv

class Logger:
    def __init__(self):
        self.csv_filename = "detected_shapes.csv"
        
    def write_data(self, detected_shapes):
        with open(self.csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Pattern", "Color"])
            for shape_data in detected_shapes:
                writer.writerow(shape_data)
        print(f"Data has been written to {self.csv_filename}")