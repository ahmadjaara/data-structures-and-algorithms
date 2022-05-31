from leftjoin.left_join import *

def test_case1():
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

    assert left_join(hashtableone,hashtabletwo) == [['wrath', 'anger', 'delight'], ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]

def test_case_empty_hashtable():
    hashtableone = HashaTable()
    hashtabletwo = HashaTable()
    assert left_join(hashtableone,hashtabletwo) == []

def test_case_one_empty_hashtable():
    hashtableone = HashaTable()
    hashtableone["diligent"]="employed"
    hashtableone["fond"]="enamored"
    hashtableone["guide"]="usher"
    hashtableone["outfit"]="garb"
    hashtableone["wrath"]="anger"

    hashtabletwo = HashaTable()
    hashtabletwo["diligentlk"]="idle"
    hashtabletwo["fondalscl"]="averse"
    hashtabletwo["guideakjc"]="follow"
    hashtabletwo["flowkjca"]="jam"
    hashtabletwo["wrathac"]="delight"

    assert left_join(hashtableone,hashtabletwo) == [['wrath', 'anger', 'NULL'], ['outfit', 'garb', 'NULL'], ['diligent', 'employed', 'NULL'], ['guide', 'usher', 'NULL'], ['fond', 'enamored', 'NULL']]
