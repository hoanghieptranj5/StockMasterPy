import csv

class CSVWriter:
    @staticmethod
    def write_to_csv(data, filename='stock_data.csv'):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Date", "Close", "Change", "Volume", "Open", "High", "Low"])
            for entry in data:
                writer.writerow(entry.values())

