import pytest
from hashtable.hash_table import HashaTable

def test_key_value_add(hastable):
    hastable["first_value"]=10
    assert hastable["first_value"] ==10

def test_key_null(hastable):
    assert hastable["first_value_not_store"]==None

def test_keys_collection(hastable):
    hastable["good"]="1"
    hastable["bad"]="2"
    hastable["hot"]="3"
    hastable["cold"]="4"
    hastable["cold"]="5"
    hastable["cold"]="6"
    assert hastable.keys()==['hot', 'bad', 'cold', 'good']

def test_Collision(hastable):
    hastable["good"]="1"
    hastable["bad"]="2"
    hastable["hot"]="3"
    hastable["cold"]="4"
    hastable["cold"]="5"
    hastable["clod"]="6"
    assert hastable.map[hastable.hash("cold")]==[["cold","4"],["cold","5"],["clod","6"]]
def test_Collision_index(hastable):
    assert hastable.hash("hello")==892

def test_Collision_retrieve(hastable):
    hastable["good"]="1"
    hastable["bad"]="2"
    hastable["hot"]="3"
    hastable["cold"]="4"
    hastable["cold"]="5"
    hastable["clod"]="6"
    #hastable.map[hastable.hash("cold")]==[["cold","4"],["cold","5"],["clod","6"]]
    assert hastable.map[hastable.hash("cold")][1]==["cold","5"]
    assert  hastable["clod"]=="6"

@pytest.fixture
def hastable():
    hash_table=HashaTable()
    return hash_table