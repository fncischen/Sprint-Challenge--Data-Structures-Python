class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  # non growable buffer

  def append(self, item):
    if self.current > self.capacity - 1:
      self.current = 0
      # override oldest element with new item, based on the current counter 
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    list = []
    for item in self.storage:
      if item != None:
        list.append(item)
    return list 