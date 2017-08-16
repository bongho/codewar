def tower_builder(n_floors):
    floors = []
    n = n_floors
    for i in range(n_floors):
        print(i)
        n -= 1
        floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
    return floors
    
    
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
    
def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]
