class Link:
  empty = ()
  
  det __init__(self, first, rest=empty):
    assert self.rest is Link.empty or isinstance(self.rest, Link) 
    self.first = first
    self.rest = rest
    
    
    
