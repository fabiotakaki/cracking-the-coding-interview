# Author: Fabio S. Takaki
# Hashtable for objects, strings for keys :)

class Hashtable:

  def __init__(self, slots=10):
    self.slots = slots
    self.data = [[] for _ in range(self.slots)]

  def hash(self, key):
    return sum([ord(c) for c in key]) % self.slots

  def get_data(self):
    return self.data
    
  def insert(self, key, obj):
    h = self.hash(key)
    self.data[h].append([key, obj])
    return self.data
  
  def get_by_key(self, key):
    h = self.hash(key)
    item = None
    for i in self.data[h]:
      if key == i[0]:
        item = i[1]
    return item

  def remove_by_key(self, key):
    h = self.hash(key)
    item = 'Error: could not found the item!'
    for i in self.data[h]:
      if key == i[0]:
        self.data[h].remove(i)
        item = 'Success: item removed!'
    return item


if __name__ == '__main__':
  import unittest
  h = Hashtable()
  print h.insert('Teste 1', 10.4)
  print h.insert('Teste 2', 300)
  print h.insert('Teste 3', {'obj_id': 10, 'name': 'product 1'})
  print h.get_by_key('Teste 1')
  print h.remove_by_key('Teste 1')
  print h.get_data()
  print h.get_by_key('Teste 3')