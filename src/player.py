

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
  def __init__(self, player_room, inventory=[]):
    self.player_room = player_room
    self.inventory = inventory
    
  def get_item(self, item):
    #i want player to grab item from entered room
    #item in room is taken away and item is added to player inventory
    #compare input string to items in current room 
    #if input string matches item in room, set item_obj = item
    item_obj = ''
    for index, element in enumerate(self.player_room.items):
      if item == element.name:
        item_obj = element
    if item_obj:
      self.inventory.append(item_obj)
      self.player_room.items.remove(item_obj)
    else:
      print('that item is not in the room')
        
      #print('spri',self.player_room.items)
      #print('si',self.inventory)
  def drop_item(self, item):
    pass  
  
  def __str__(self):
    return (f"{self.player_room}\n{self.inventory} ")  

