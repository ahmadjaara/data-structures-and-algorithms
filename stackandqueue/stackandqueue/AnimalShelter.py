from stackandqueue.queue import Queue 

class AnimalShelter :
    def __init__(self):
        self.cat_que = Queue()
        self.dog_que = Queue()
    def enqueue(self,animal):
        """
        its a method to add the dog or cat animal to 
        its queue
        input :str dag or cat 
        """
        str_animal=str(animal)

        if str_animal == "cat":
             self.cat_que.enqueue(str_animal)
        elif str_animal == "dog":
             self.dog_que.enqueue(str_animal)
        else:
            return "not dog or cat"

    def dequeue_pets(self,pref) :
        """
        its a method to take out a cat or animal from the 
        shellter 
        input :str pref:cat or dog
        output : str cat or dog and if there is no pets 
        it return none 
        """
        str_pref=pref
        
        if str_pref == "cat":
            return self.cat_que.dequeue()
        elif str_pref == "dog":
            return self.dog_que.dequeue()
        else:
            return None
        

if __name__=="__main__":
    queue = AnimalShelter()
    queue.enqueue("animal")
    queue.enqueue("dog")
    queue.enqueue("dog")
    queue.enqueue("cat")

    print(queue.dequeue_pets("asd"))
 


    # queue.enqueue(3)
    # queue.enqueue(2)