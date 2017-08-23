def productFib(prod):
  f1, f2 = 0, 1
  while prod > f1 * f2:
    f1, f2 = f2, f1 + f2
  return [f1, f2, prod == f1 * f2]
