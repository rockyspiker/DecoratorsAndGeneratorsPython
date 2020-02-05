def track(f):
  @memoize
  def wrapper(arg):
    wrapper.count += 1
    return f(arg)
  wrapper.count = 0
  return wrapper

def memoize(f):
  memo = {}
  def wrapper(arg):
    if arg not in memo:            
      memo[arg] = f(arg)
    else:
      print(arg, 'found in cache')
    return memo[arg]
  return wrapper

def log(f):
  def wrapper(arg):
    writeString = 'fib(' + str(arg) + ') = ' + str(f(arg)) + '\n'
    logfile = open('log.txt', 'a+')
    logfile.write(writeString)
    logfile.close()
    return f(arg)
  return wrapper  

def main():
    @track
    @log
    def fib(n):
        return n if n in (0,1) else fib(n-1) + fib(n-2)
    print(str(fib(10)) + ', calls =', fib.count)

if __name__ == '__main__':
    main()