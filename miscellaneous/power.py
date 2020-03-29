def power_rec(x, n):
  if n == 0:
   return 1
  if n == 1:
   return x
  
  temp = power_rec(x, n/2)
  if n % 2 == 0:
    return temp * temp
  else:
    return x * temp * temp

def power(x, n):
  is_negative = False
  if n < 0:
    is_negative = True
    n *= -1

  result = power_rec(x, n)

  if is_negative:
    return 1 / result
  
  return result

power(2,5)