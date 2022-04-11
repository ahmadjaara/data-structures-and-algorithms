
table of content  

| table of content |  |
| ----------- | ----------- |
| challenge no| URL challenge |
| 1 | <https://github.com/ahmadjaara/data-structures-and-algorithms/edit/main/README.md> |
| 2  | <https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/insertShiftArray.md>  |
| 3  | <https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/BinarySearch.md> |
|linklist| <https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/linklist/README.md>|
|stack&queue| <https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/stackandqueue/READMES%26Q.md>|
|ReadPsudoQueue|<https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/stackandqueue/ReadPsudoQueue.md>|
|Animal shelter|<<https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/stackandqueue/ReadAnimalShelter.md>|
|stackandbracket|<https://github.com/ahmadjaara/data-structures-and-algorithms/blob/stack-queue-brackets/stackandqueue/ReadStackBracketCheck.md>|
|Trees |<https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/Tree/README.md>|
|Tree max method|<https://github.com/ahmadjaara/data-structures-and-algorithms/blob/main/Tree/Readtree_max.md>|

# data-structures-and-algorithms

The challenge is to write a function that take an array and return new array that has the reverse element of the original array using whiteboard
for example :
array =[1,2,3,4,5]
output will give
revarray = [5,4,3,2,1]  

## Whiteboard Process

![Whiteboard challenge](/picture/array-reverse.jpeg "Whiteboard challenge" )

## Approach & Efficiency

What approach did you take?

- know the array length
- initiate a variable for (empty array,index)
- loop reversely in the original array index and put the value inside the empty   array

Discuss Why. What is the Big O space/time for this approach?

### (big o ==> time(2n))

since I used one for loop so the repetition for the block inside the for loop equal the input array length and by the increase of the array length the more the repetition for that block
so that the time for the process will increase linearly.
(2n) the "2" here since i used another for loop that count the array length.

### (big o ==> space(n))

the output array will be the same as the input array length
so that its take the same space as input array  
and by increasing the input array length the output array length will increase so that the space that will take from memory increase linearly as the input increase.
