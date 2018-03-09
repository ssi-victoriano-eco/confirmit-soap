from datetime import datetime

class DateTimeFilter:
  '''Used by ColumnFilter for synchronization log to specify a filter on a date value.'''
  
  def __init__(self):
    # The filter value
    self.Value = datetime.today()