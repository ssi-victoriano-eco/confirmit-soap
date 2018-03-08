from .TransferDefBase import TransferDefBase

class TransferDef(TransferDefBase):
  
  def __init__(self):
    # Indicates if a respondent record should be added (to generate a respid) before adding the response record.  
    self.AddRespondents = False
    # Gets or sets the allChildrenTables value  
    self.AllChildrenLevels = False
    # Indicates whether looplevel answers should be expanded in looplevel of form or reside in looplevel like stored in database  
    self.CollapseLoopReferences = False
    # The command timeout to use on the query, if set  
    self.CommandTimeout = None
    # (inherited from TransferDefBase) Gets or sets the Database type  
    self.DbType = None
    # Gets or sets the IncludeRecodedVariables value  
    self.IncludeRecodedVariables = False
    # Gets or sets the key that is used to join the different datatables containing the responses. Normally the key 'responseid' should be used.  
    self.Key = None
    # (inherited from TransferDefBase)  
    self.OrderBy = None
    # (inherited from TransferDefBase) Gets or sets the ProjectId  
    self.ProjectId = None
    # Systemvariables to be included  
    self.SystemVariables = None
    # A hash value calculated from a serialized object. Used as a cache key  
    self.TransferDefHash = None
    # A property for retrieving and assigning the TransferLevels  
    self.TransferLevels = None
    # (inherited from TransferDefBase) A property for retrieving and assigning the Where clause  
    self.Where = None
