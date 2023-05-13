def lsrch(items, find):
  if items:
    for item in range(len(items)):
      if items[item] == find:
        return f'Item found {items[item]} at index number {item}'
  return 'No item was searched as the given list was empty'

alist = [1, 2, 4, 5, 6, 0, 9, 8, 7]
result = lsrch(alist, 0)
print(result)
