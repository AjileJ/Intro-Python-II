class Item():
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def on_take(self, name):
    pass
  def __str__(self):
    return (f"{self.name}\n <<>> \n {self.description} ")
      