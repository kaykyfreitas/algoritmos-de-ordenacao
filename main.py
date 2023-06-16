from src.file_generator import generate_csv_integers
from src.sort_comparison import SortComparison

file_name = 'data/file.csv'
quantity_numbers = 200000
arrays_size = [1000, 5000, 10000, 15000, 20000]

def main():
  generate_csv_integers(file_name, quantity_numbers)
  comparison = SortComparison(file_name, arrays_size)
  comparison.run_comparison()

if __name__ == '__main__':
  main()