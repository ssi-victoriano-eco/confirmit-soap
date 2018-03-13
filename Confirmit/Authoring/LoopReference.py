from NamedEntityIdReference import NamedEntityIdReference

class LoopReference(NamedEntityIdReference):
  
  def __init__(self):
    
    self.EntityId = NamedEntityIdReference().EntityId
    self.Name = NamedEntityIdReference().Name