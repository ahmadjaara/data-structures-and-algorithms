# Insert to Middle of an Array
The challenge is to write a function that take an array and a constant and then return a new array that put the new element at the middle of the array. 

for example :

array =[1,2,3,4,5],7
output will give me 
insertelementarray = [1,2,3 ,**7**,4,5]  

## Whiteboard Process
![Whiteboard challenge](/picture/insertShiftArray.jpg "Whiteboard challenge" )


## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
my approach is to create a new array that contain the value of origin array and the new element at the middle of it and then return this array 
i do that by using two for loop to fill the new array with value and i use a if statement to check the index to use it to put the new element at its location at the middle and before i start the loop i make an if statement to check firstly the length of the original array if it is odd or even 
### (big o ==> time(n+1)) ==> O(n) ==>time
since i use for loop the block of code inside it will occure as the value of the original array length +1 ==> (n+1)


### (big o ==> space(n+1)) ==> O(n) ==>space  
here the new array will have the same space of the original array plus one element so that ==> (n+1)


# stretch goal :
what if we want to erase the middle element from an array .

### problem domain: 
- erase the middle element form an array 

### algorithm
- create an empty array 
- find the length for the original array (l)
- if condition to check the array length (odd or even)
- for loop to fill the new array with the original array
- continue the loop at index equal to l/2 in even array length
- continuo the loop at index equal to (l-1)/2

### code :

        def erase_fun(a):

        l=len(a)
        ea=[]
        if l%2==0:
            
            for i in range(l):
            if i == l/2:
                continue
            else:
                ea+=[a[i]]
                
        else:
            
            for i in range(l):
            if i == (l-1)/2:
                continue
            else:
                ea+=[a[i]]
                
        return ea
Big o:
time ==> O(n)
space==> O(n-1)
