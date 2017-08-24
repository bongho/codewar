def diamond(n):
    if n%2 == 0 or n < 1:
        return None
    else:
        diamond_lst = ["*" * n]
        for i in range(1, int((n + 1) / 2)):
            diamond_lst.insert(0, (" " * i) + (("*") * (n - 2 * i)))
            diamond_lst.append((" " * i) + (("*") * (n - 2 * i)))
        return "\n".join(diamond_lst) + "\n"
        
def diamond(n):
    if not n%2 or n<1: return None
        d = [" "*i+"*"*(n-2*i)+"\n" for i in range(int(n/2),0,-1)]
        return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])
