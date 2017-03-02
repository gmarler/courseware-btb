def gen_squares(max_root):
  for n in range(max_root):
    yield n ** 2

squares = gen_squares(5)

# for square in squares: print(square)

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))