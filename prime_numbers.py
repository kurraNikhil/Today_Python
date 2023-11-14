def is_prime(n):
  
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


if __name__ == '__main__':
  primes = []
  for i in range(2, 20):
    if is_prime(i):
      primes.append(i)

  print('Prime numbers less than 20 are:')
  for prime in primes:
    print(prime)
