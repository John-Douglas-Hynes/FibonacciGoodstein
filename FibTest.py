import TreeAlgs

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

def recursive_fib(root, top):
    queue = root.children
    new_root = fib_decomp(root.val)
    # to be finished later



### Testing nonsense

tr = TreeAlgs.tree(-1, [TreeAlgs.tree(101, [])])
tr.fibonacci_print(tr, '') 