################################################################
# Leet Code: Define Hash Table data structure, with fixed number of elements  
# DS: Dictonary
# Problem Number: 3
################################################################

class custom_dict:
    def __init__(self, num_elements):
        self.num_keys = num_elements
        self.dict = [None]*self.num_keys
    
    def custom_get(self,key):
        return self.dict[hash(key) % self.num_keys]
        
    ##Add and update kind of the same 
    def custom_add(self,key,value):
        self.dict[(hash(key) % self.num_keys)] =  value
        print(r"value added at: ",str(hash(key) % self.num_keys))
    
    ##Deleting an element 
    def custom_del(self,key):
        self.dict.pop((hash(key) % self.num_keys))
        
    def show_dict(self):
        print(self.dict)
        

def main():
    obj = custom_dict(7)
    obj.custom_add(2,50)
    obj.custom_add(3,60)
    obj.custom_add('key',9)
    obj.show_dict()

if __name__ == '__main__':
    main()
