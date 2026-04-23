def fibonacci(integer):
    fib_table = {0:1, 1:1}
    for x in range(2, integer+1):
        fib_table[x] = fib_table[x-1] + fib_table[x-2]
    return fib_table

fib_table = fibonacci(50)

def get_largest_fib(integer):
    x=0
    while fib_table[x] <= integer:
        x = x +1
    return (x-1, fib_table[x-1])

def fib_decomp(integer):
    arr = []
    while integer > 0:
        curr = get_largest_fib(integer)
        arr.append(curr[0])
        integer = integer - curr[1]
    return arr

def string_decomp(integer):
    return ' + '.join(f'F{{{x}}}' for x in fib_decomp(integer))

class tree:
    def __init__(self, val = 0, children = []):
        self.val = val
        self.children = children

def recursive_fib(root, top):
    if root.children == []:
        if root.val > top:
            children = []
            for x in fib_decomp(root.val):
                children.append(tree(val = x, children = []))


### Testing nonsense

print(f'1001 = {string_decomp(1001)}')
print(f'{fib_table[15]} + {fib_table[6]} + {fib_table[1]} = {fib_table[15] + fib_table[6] + fib_table[1]}')
arr = fib_decomp(1001)
recursive_fib(arr, 5)