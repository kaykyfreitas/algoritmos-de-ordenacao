def file_reader(filename):
  list = []
  with open(filename,'r') as file:
    for value in file:
      list.append(value)

  list = list[0]
  stringList = list.split(';')
  return [int(variable) for variable in stringList]
