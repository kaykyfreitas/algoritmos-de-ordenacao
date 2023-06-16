import csv
import random

def generate_csv_integers(file_name, quantity):
  numbers = list(range(1, quantity + 1))
  random.shuffle(numbers)
  with open(file_name, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(numbers)
  print("CSV file generated successfully!")
