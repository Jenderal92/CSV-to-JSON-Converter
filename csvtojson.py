import csv
import json

def display_banner():
    print("=" * 50)
    print(" " * 10 + "CSV to JSON Converter")
    print(" " * 10 + "Created by Python 2.7")
    print("=" * 50)
    print("\n")

def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            
        with open(json_file_path, 'w') as json_file:
            json.dump(rows, json_file, indent=4)
        
        print("\nKonversi berhasil! File JSON disimpan di: {}".format(json_file_path))
    except Exception as e:
        print("\nTerjadi kesalahan saat konversi: {}".format(str(e)))


if __name__ == "__main__":
    display_banner()
    csv_file_path = raw_input("Masukkan nama file CSV (misal: data.csv): ")
    json_file_path = raw_input("Masukkan nama file JSON hasil (misal: data.json): ")
    csv_to_json(csv_file_path, json_file_path)
