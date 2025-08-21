class MyIterator:
    def __init__(self,max_val=None):
        self.current = 1
        self.max_val = max_val

    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.current <= self.max_val:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# itr = MyIterator(8)
# for i in itr:
#     print(i)

def my_generator(num=None):
    res = 1
    while res <= num:
        yield res
        res += 1

# gen = my_generator(9)
# for i in gen:
#     print(i) 


def read_large_file(file_name = None):
    with open(file_name,'r') as file:
        for line in file:
            yield line.strip()

# for line in read_large_file('sahin.txt'):
#     print(line)


def fibonacci_generator():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b


# chaining iterators

def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:  # Filter condition
            yield line

def transform_errors(lines):
    for line in lines:
        yield line.upper()  # Transform to uppercase

# Pipeline
lines = read_lines("app_logs.txt")
errors = filter_errors(lines)
transformed_errors = transform_errors(errors)

# for error in transformed_errors:
#     print(error)


# advance thing using send method

def number_generator():
    value = 0
    while True:
        value = yield value  # Receive value via `send`

# gen = number_generator()
# print(next(gen))       # Start generator -> Output: 0
# print(gen.send(100))   # Resume with 100 -> Output: 100
# print(gen.send(200))   # Resume with 200 -> Output: 200


# nth Fibonacci number using generator

def generate_fibonacci():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b

def fib(n):
    g = generate_fibonacci() 
    for i in range(n-1):
        next(g)
    return next(g)

print(fib(8))




