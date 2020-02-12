# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
  def __init__(self, player_room, inventory=[]):
    self.player_room = player_room
    self.inventory = inventory
  def __str__(self):
    return (f"{self.player_room} ")  

