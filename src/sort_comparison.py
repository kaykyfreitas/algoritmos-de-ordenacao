import time
import matplotlib.pyplot as plt
from datetime import datetime
from src.file_reader import file_reader
from src.merge_sort import merge_sort
from src.bubble_sort import bubble_sort

class SortComparison:
  def __init__(self, filename, arrays_size):
    self.filename = filename
    self.sizes = arrays_size
    self.bubble_times = []
    self.bubble_comparisons = []
    self.bubble_swaps = []
    self.merge_times = []
    self.merge_comparisons = []
    self.merge_swaps = []

  def measure_merge_sort(self):
    integer_list = file_reader(self.filename)

    for size in self.sizes:
      array = integer_list[:size]
      merge_array = array.copy()

      merge_result, merge_comp, merge_swap = merge_sort(merge_array)

      start_time = time.time()
      merge_sort(merge_array.copy())
      end_time = time.time()
      merge_time = end_time - start_time

      self.merge_times.append(merge_time)
      self.merge_comparisons.append(merge_comp)
      self.merge_swaps.append(merge_swap)

  def measure_bubble_sort(self):
    integer_list = file_reader(self.filename)

    for size in self.sizes:
      array = integer_list[:size]

      bubble_array, bubble_comp, bubble_swap = bubble_sort(array.copy())

      start_time = time.time()
      bubble_sort(array.copy())
      end_time = time.time()
      bubble_time = end_time - start_time

      self.bubble_times.append(bubble_time)
      self.bubble_comparisons.append(bubble_comp)
      self.bubble_swaps.append(bubble_swap)

  def plot_comparison(self):
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    axs[0].plot(self.sizes, self.bubble_times, label='Bubble Sort')
    axs[0].plot(self.sizes, self.merge_times, label='Merge Sort')
    axs[0].set_xlabel('Tamanho do Array')
    axs[0].set_ylabel('Tempo de Execução (s)')
    axs[0].set_title('Comparação de Tempo de Execução')
    axs[0].legend()

    axs[1].plot(self.sizes, self.bubble_comparisons, label='Bubble Sort')
    axs[1].plot(self.sizes, self.merge_comparisons, label='Merge Sort')
    axs[1].set_xlabel('Tamanho do Array')
    axs[1].set_ylabel('Número de Comparações')
    axs[1].set_title('Comparação de Número de Comparações')
    axs[1].legend()

    axs[2].plot(self.sizes, self.bubble_swaps, label='Bubble Sort')
    axs[2].plot(self.sizes, self.merge_swaps, label='Merge Sort')
    axs[2].set_xlabel('Tamanho do Array')
    axs[2].set_ylabel('Número de Trocas')
    axs[2].set_title('Comparação de Número de Trocas')
    axs[2].legend()

    plt.style.use('default')
    plt.tight_layout()

    data_atual = datetime.now()
    timestamp_string = data_atual.strftime("%Y-%m-%d_%H-%M-%S")

    graph_filename = 'report/assets/graph_' + timestamp_string + '.png'
    plt.savefig(graph_filename)
    print('Graph saved to ' + graph_filename)
    plt.show()

  def generate_report(self):
    data_atual = datetime.now()
    timestamp_string = data_atual.strftime("%Y-%m-%d_%H-%M-%S")
    report = f'Relatório de execução dos algoritmos de ordenação:\n\n'
    report += f'Data de geração do relatório: {data_atual}\n\n'
    report += f'Tamanho dos arrays utilizados: {self.sizes}\n'
    report += f'Tempo de execução - Bubble Sort: {self.bubble_times} s\n'
    report += f'Tempo de execução - Merge Sort: {self.merge_times} s\n'
    report += f'Número de comparações - Bubble Sort: {self.bubble_comparisons}\n'
    report += f'Número de comparações - Merge Sort: {self.merge_comparisons}\n'
    report += f'Número de trocas - Bubble Sort: {self.bubble_swaps}\n'
    report += f'Número de trocas - Merge Sort: {self.merge_swaps}\n'

    report_filename = 'report/report_' + timestamp_string + '.txt'
    with open(report_filename, "w") as file:
      file.write(report)

    print('Report saved to ' + report_filename)

  def run_comparison(self):
    self.measure_bubble_sort()
    self.measure_merge_sort()
    self.generate_report()
    self.plot_comparison()
