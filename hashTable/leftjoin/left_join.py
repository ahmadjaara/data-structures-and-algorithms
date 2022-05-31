from hashtable.hash_table import HashaTable
"""
function leftjoin (hashmap1,hashmap2):
   keylist=hashmap1.key()
   outputlist=[]
  for key inside keylist:
     templist=[]
    # add the key
     templist.add(key)
    #add the value
    templist.add(hashmap1[key])
    if hashmap2[key] not empty:
    templist.add(hashmap2[key])
    else:
    templist.add(none)
  return outputlist

"""
def left_join(hashtableleft,hashtableright):
    keylist=hashtableleft.keys()
    print(keylist)
    outputlist=[]
    for key in keylist:
        templist=[]
        # add the key
        templist.append(key)
        #add the value
        templist.append(hashtableleft[key])
        if hashtableright[key] != None:
            templist.append(hashtableright[key])
        else:
            templist.append("NULL")
        outputlist.append(templist)

    return outputlist

if __name__=="__main__":
    hashtableone = HashaTable()
    hashtableone["diligent"]="employed"
    hashtableone["fond"]="enamored"
    hashtableone["guide"]="usher"
    hashtableone["outfit"]="garb"
    hashtableone["wrath"]="anger"
    
    hashtabletwo = HashaTable()
    hashtabletwo["diligent"]="idle"
    hashtabletwo["fond"]="averse"
    hashtabletwo["guide"]="follow"
    hashtabletwo["flow"]="jam"
    hashtabletwo["wrath"]="delight"

    print(left_join(hashtableone,hashtabletwo))
    print(hashtableone["guide"])
