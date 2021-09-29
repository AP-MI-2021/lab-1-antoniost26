'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  flag=False
  if n > 1:
    for i in range(2, int((n/2)+1)):
      if n % i:
        flag=True
  return flag

  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  prod = 1
  for i in lst:
    prod *= i
  return prod


  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if x == 0:
    return y
  if y == 0:
    return x
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  if y == 0:
    return x
  else:
    return get_cmmdc_v2(y, x % y)
  
  
def main():
  lst = 1, 3, 6, 8
  print(is_prime(13), get_product(lst), get_cmmdc_v1(6, 30), get_cmmdc_v2(6, 30))

if __name__ == '__main__':
  main()
