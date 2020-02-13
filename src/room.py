
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.items = items
  def add_item(self, item):
    pass
  
  def drop_item(self, item):
    pass  
  def __str__(self):
    itemz = " ".join([f"{i.name}\n\n-{i.description}\n " for i in self.items ])
    return f"{self.name} \n{self.description}\n\n{itemz}"
  
  
  
  
  