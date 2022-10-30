def just_some_addition(a, b):
  if not isinstance(a, int):
    a = int(a)
  if not isinstance(b, int):
    b = int(b)

  return a + b

if __name__ == '__main__':
    print(just_some_addition(1, '2'))
