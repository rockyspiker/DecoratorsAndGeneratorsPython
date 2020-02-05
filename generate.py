def produce(rawStr):
  multBool = False
  multiples = 0
  newString = ''
  for char in rawStr:
    newString = ''
    if char.isdigit() and multBool == False:
      multiples = int(char)
      multBool = True
    else:
      for i in range(multiples+1):
        newString += char
      multiples = 0
      multBool = False
      yield newString

def consume(gen):
  index = 1
  for chars in gen:
    for char in chars:
      if index%3 == 0:
        print(char, end = ' ')
      else:
        print(char, end = '')
      index += 1

def main():
  print('___Produce Section___\n')
  gen = produce('A4BC0Z')
  for i in gen:
    print(i, end=' ')
  print('\n\n___Consume Section___\n')
  consume(produce('A4BC0Z'))
  print('\n')

if __name__ == '__main__':
  main()