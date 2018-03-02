
class DeleteStatement:

  def __init__(self):
    # A property for retrieving and assigning the name of the logical table to delete
    self.LogicalTable = None
    # A property for deleting top N number of rows
    self.TopN = 0
    # A property for retrieving and assigning the where clause
    self.WhereClause
