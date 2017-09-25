def presses(phrase):
    phrase = phrase.upper()
    keypads = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
    nPresses = 0
    for i in phrase:
        for j in keypads:
            if i in j:
                nPresses += j.index(i) +1

    return nPresses
