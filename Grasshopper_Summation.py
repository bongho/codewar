def summation(num):
    result = 0
    for i in range(1,num+1):
        result += i
    return result
#xrange is a sequence object  that evaluates lazily.
def summation(num):
    return sum(xrange(num + 1))
    
