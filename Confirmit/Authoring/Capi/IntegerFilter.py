class IntegerFilter:
  '''Used by ColumnFilter for synchronization log to specify a filter on an integer value.'''
  
  def __init__(self):
    # The operator for this filter
    self.Operator = None
    # The filter value
    self.Value = 0