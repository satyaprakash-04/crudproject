def factorial(n):
  if n == 0:
    result = 1
  elif n == 1:
    result = 1
  else:
    result = n * factorial(n-1)
  return result

print(factorial(5))
