class SuperList(list):
    
    def __len__(self) -> int:
        return 1000

l = SuperList()

l.append(10)
print(len(l))
print(issubclass(SuperList, list))