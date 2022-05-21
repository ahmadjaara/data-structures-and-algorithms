# Hashtables
<!-- Short summary or background information -->
Hash table is one of the most important data structures that uses a special function known as a hash function that maps a given value with a key to access the elements faster.

A Hash table is a data structure that stores some information, and the information has basically two main components, i.e., key and value. The hash table can be implemented with the help of an associative array. The efficiency of mapping depends upon the efficiency of the hash function used for mapping.

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:

set

    Arguments: key, value
    Returns: nothing
    This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    Should a given key already exist, replace its value from the value argument given to this method.

get

    Arguments: key
    Returns: Value associated with that key in the table

contains

    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.

keys

    Returns: Collection of keys

hash

    Arguments: key
    Returns: Index in the collection for that key

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- for **add/set** method the big o notation for time and space
O(1)and for space O(1) since there is no loop just if statment 

- for **get** method the big o notation for time 
O(1) when there is no list inside lisy=t at the hash table index position and O(n)
when there is a list inside list since i used a for loop to check the key nside this list 

- for **contain** method the big o notation for time
O(1) when there is no list inside list in  the hash table at this index position and O(n)
when there is a list inside list since i used a for loop to check the key inside this list

- for **keys** method the big o notation for time is O(n^2) since i used a loop inside loop to extract the keys value 
and for space is O(n) since i store the keys in a list 

- for **hash** method the big o notation for time is O(n) using a loop to calcu;ate the value for the index 
for space its o(1)

## API
<!-- Description of each method publicly available in each of your hashtable -->
### set method

- send the key to the GetHash method.
- Once you determine the index of where it should be placed, go to that index
- Check if something exists at that index already, if it doesn’t, add it with the key/value pair.
- If something does exist, add the new key/value pair to the data structure within that bucket.

### get

The get takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.

### contains 

The Contains method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the GetHash and check the hashtable if the key exists in the table given the index returned.

### keys

Returns: Collection of keys in the hash table

## hash

The Hash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.

