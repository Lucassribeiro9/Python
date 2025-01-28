from collections.abc import Sequence
class Mylist(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
        
    def append(self, value):
        self._data[0] = value
        self._index += 1
    
    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value
    
if __name__ == "__main__":
    mylist = Mylist()
    mylist.append("Carlos")
    mylist.append("Miguel")
    mylist.append("Juan")
    for item in mylist:
        print(item)
    
