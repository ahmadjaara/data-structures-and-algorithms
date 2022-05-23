
class HashaTable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        # self.map = [None]*size
        self.map = [[]]*size
        # self.map = [LinkedList()]*size

    def set(self,key, value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table

        """
        idx = self.get_hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])

    def get(self, key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        by __getitem__ we can call the element as we are dealing with dectionary

        """
        # call the get hash method and send the key to it
        idx = self.get_hash(key)
        # get that index and look it up from the map
        # return the value stroed in that index
        for elment in self.map[idx]:
            if any(isinstance(x, list) for x in elment):
                for i in elment:
                    if i[0]==key:
                        return i[1]
            else:
                if elment[0]==key:
                    return elment[1],self.map[idx]
        return None 
        
    def contains(self,key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """
        idx = self.get_hash(key)
        # get that index and look it up from the map
        # return the value stroed in that index
        for elment in self.map[idx]:
            if any(isinstance(x, list) for x in elment):
                for i in elment:
                    if i[0]==key:
                        return True
            else:
                if elment[0]==key:
                    return True
        return False 

    def keys(self):
        """
        Argument:no argument
        Returns: Collection of keys
        """
        collection=[]
        for element in self.map:
            if element:
                for elem in element:
                    if not (elem[0] in collection):
                        collection.append(elem[0])
        return collection

    def hash(self,key):
        """  
        Arguments: key
        Returns: Index in the collection for that key
        """
        idx = self.get_hash(key)
        return idx

    def get_hash(self,key):
        """
        - ascii code of a key summation
        - encode chars in key into oct and add it to ascii sum
        - Prime = 19 then multiply it by ascii sum
        - mod the result over self.size
        - return the hashed value
        """
        # Hello
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch) #86
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def add(self, key, value):
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = self.get_hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])


    # def find(self, key):
    def __getitem__(self, key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        by __getitem__ we can call the element as we are dealing with dectionary

        """
        # call the get hash method and send the key to it
        idx = self.get_hash(key)
        # get that index and look it up from the map
        # return the value stroed in that index
        for elment in self.map:
            if any(isinstance(x, list) for x in elment):
                for i in elment:
                    if i[0]==key:
                        return i[1],self.map[idx]
            else:
                if len(elment)!=0:
                    if elment[0]==key:
                        return elment[1]
        return None 

    def __setitem__(self, key, value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in 
        """
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = self.get_hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])
if __name__ == "__main__":
    hashtable = HashaTable()
    hashtable.add("cloud", "AWS")
    hashtable.add("cloud", "Azure")
    hashtable.add("could", "Rainy")
    hashtable.add("name", "Python")
    hashtable["ahmad"]="best"
    # print(hashtable["name"])
    # print(hashtable.get_hash("python"))
    # print(hashtable.map[hashtable.hash("could")])
  
    # print(hashtable.contains("ahmad1"))
    hashtable.add("name2", "java")
    # print(hashtable["name2"])
    # print(hashtable.keys())

    hash_table2=HashaTable()
    hash_table2.add("first_value",10)
    idx=hash_table2.hash("first_value")
    # print(hash_table2["first_value15"])
    # print(hash_table2.hash("hello"))
    print( hashtable["name"])