def merge_sort(array):
  if len(array) <= 1:
    return array, 0, 0

  mid = len(array) // 2
  left_half, left_comp, left_swaps = merge_sort(array[:mid])
  right_half, right_comp, right_swaps = merge_sort(array[mid:])

  merged, merge_comp, merge_swaps = merge(left_half, right_half)
  comparisons = left_comp + right_comp + merge_comp
  swaps = left_swaps + right_swaps + merge_swaps

  return merged, comparisons, swaps

def merge(left, right):
  merged = []
  left_index = right_index = 0
  comparisons = 0
  swaps = 0

  while left_index < len(left) and right_index < len(right):
    comparisons += 1
    if left[left_index] < right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    else:
      merged.append(right[right_index])
      right_index += 1
      swaps += 1

  while left_index < len(left):
    merged.append(left[left_index])
    left_index += 1

  while right_index < len(right):
    merged.append(right[right_index])
    right_index += 1

  return merged, comparisons, swaps
