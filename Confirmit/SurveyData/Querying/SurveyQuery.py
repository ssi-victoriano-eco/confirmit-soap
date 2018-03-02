from DayOfWeekType import DayOfWeekType
from QueryProject import QueryProject

class SurveyQuery:
  """Represents a query towards the survey response data."""

  def __init__(self):
    # Gets or sets the alias. Alias is required when the query is used as a sub-query.  
    self.Alias = None
    # Applicable for HitList query  
    self.CommandTimeout = 0
    # The day of week setting to be used towards the database.  
    self.DayOfWeek = DayOfWeekType.Default
    # Gets or sets the default project.  
    self.DefaultProject = None
    # Gets or sets the delete statement.  
    self.DeleteStatement = None
    #  
    self.IsMultiProjUnion = None
    # Gets the select statement of this query.  
    self.SelectStatements = None
    # Projects part of a UNION.  
    self.UnionProjects = None
    # Gets or sets the update statement.  
    self.UpdateStatement = None
    # Not applicable for SQL queries. Only valid when translating Survey Query to BitStream query.  
    self.WeekRule = None

