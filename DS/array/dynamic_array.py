class Array:
    def __init__(self):
        self.array = []
        self.update_length()

    def update_length(self):
        self.length = len(self.array)
    
    def add(self, element):
        self.array.append(element)
        self.update_length()

    def remove_element(self, element):
        self.array.remove(element)
        self.update_length()

    def remove_index(self, index):
        del self.array[index]
        self.update_length()

    def show(self):
        print(self.array)
        

