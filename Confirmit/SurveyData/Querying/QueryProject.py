import sys, os
sys.path.append(os.path.abspath('../../'))

from DatabaseType import DatabaseType

class QueryProject:
  
  def __init__(self):
    # Gets or sets the database type of this project
    self.DBType = DatabaseType.Production
    # Gets or sets the project id.
    self.ProjectId = None
