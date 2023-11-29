def search(values, value):
    for index in range(len(values)):
        if values[index] == value:
            return f"{value} found at index {index} which is at position {index+1} in the given list."
    return f"{value} not found in the given list."

items = []
while True:
    print("Enter an element to insert. \nPress !q to stop.")
    element = input("Type the value and press Enter: ")
    if element != '!q':
        items.append(element)
    else:
        break
value = input("\nEnter value that you want to search in list: ")

result = search(items, value)
print(result)
