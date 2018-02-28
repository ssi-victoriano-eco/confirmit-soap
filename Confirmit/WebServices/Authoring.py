import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class Authoring(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['authoring']
  
  def AddProject(self, isPanel=None):
    """Add a project (no content)
    Parameters
      key
        Type: System.String
        Key for authentication
      isPanel
        Type: System.Boolean
        True means that the survey is to become a panel
    Return Value
      Type: String
      Project-ID for the new project
    """
    if isPanel is None:
      raise Exception('isPanel missing')
    
    return self.GetClient().AddProject(self.key, isPanel)
  
  def AddProjectFromTripleS(self, schema=None, language=None):
    """Add new project based on TripleS schema Note that this is only a BETA and does not support all datatypes
    Parameters
      key
        Type: System.String
        Key for authentication
      schema
        Type: SssSchema
        Schema object-structure
      language
        Type: System.Int32
        Language for the project
    Return Value
      Type: String
      ProjectId for new project
    """
    if schema is None:
      raise Exception('Please specify schema')
    
    if language is None:
      raise Exception('Please specify language')
    
    return self.GetClient().AddProjectFromTripleS(self.key, schema, language)
  
  def DeleteProject(self, projectId=None):
    """Deletes a project
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project-ID of the project
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().DeleteProject(self.key, projectId)
  
  def DeleteQuestionnaire(self, projectId=None):
    """Delete Questionnaire Will delete Routing, Quotas and PredefinedLists
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().DeleteQuestionnaire(self.key, projectId)
  
  def DeleteRouting(self, projectId=None):
    """Delete Routing. Will also delete quotas Will NOT delete predefined lists
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().DeleteRouting(self.key, projectId)
  
  def Dispose(self):
    """(inherited from MarshalByValueComponent) Select the method name to go to the Microsoft documentation."""
  
  def DuplicateProject(self, projectId=None, newProjectName=None):
    """Duplicates a project
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project-ID of the project
      newProjectName
        Type: System.String
        Name for the new project
    Return Value
      Type: String
      Project-ID for the new project
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if newProjectName is None:
      raise Exception('Please specify newProjectName')
    
    return self.GetClient().DuplicateProject(self.key, projectId, newProjectName)
  
  def Equals(self):
    """(inherited from Object) Select the method name to go to the Microsoft documentation."""
  
  def ExportSurvey(self, projectId=None):
    """Make a surveyexport
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
    Return Value
      Type: String
      XML representing the whole Survey
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().ExportSurvey(self.key, projectId)
  
  def ExportSurveyLayout(self, surveyLayoutId=None):
    """Export a survey layout
    Parameters
      key
        Type: System.String
        Key for authentication
      surveyLayoutId
        Type: System.String
        The id of the survey layout you want to export
    Return Value
      Type: String
      XML representing the survey layout
    """
    if surveyLayoutId is None:
      raise Exception('Please specify surveyLayoutId')
    
    return self.GetClient().ExportSurveyLayout(self.key, surveyLayoutId)
  
  def ExportSurveyWithHTMLRemoved(self, projectId=None):
    """Make a surveyexport. XML tags that can contain encoded HTML are processed and unwanted coding is removed.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
    Return Value
      Type: String
      XML representing the whole Survey (where encoded HTML is converted to plain text).
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().ExportSurveyWithHTMLRemoved(self.key, projectId)

  def ExportTranslation(
      self, 
      projectId=None, 
      targetLanguage=None, 
      baseLanguage=None, 
      useFallbackLanguage=None, 
      fallbackLanguage=None
    ):
    """Export TranslationXML from a given survey
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The id of the survey to extract a TranslationXML from
      targetLanguage
        Type: System.Int32
        The target language, i.e. the language this survey will be translated to
      baseLanguage
        Type: System.Int32
        The base language, i.e. the language this survey will be translated from
      useFallbackLanguage
        Type: System.Boolean
        Whether to use texts from a fallback language if some texts do not exist for the base language
      fallbackLanguage
        Type: System.Int32
        If fallback is enabled, the fallback language to use
    Return Value
      Type: String
      TranslationXML document
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if targetLanguage is None:
      raise Exception('Please specify targetLanguage')
    
    if baseLanguage is None:
      raise Exception('Please specify baseLanguage')
    
    if useFallbackLanguage is None:
      raise Exception('Please specify useFallbackLanguage')
    
    if fallbackLanguage is None:
      raise Exception('Please specify fallbackLanguage')
    
    return self.GetClient().ExportTranslation(self.key, projectId, targetLanguage, baseLanguage, useFallbackLanguage, fallbackLanguage)
  
  def GetBenchmarkProjectIds(self, projectId=None):
    """Gets the ids of all benchmarkprojects associated with the given projectId
    Parameters
      key
        Type: System.String
        The authentication key
      projectId
        Type: System.String
        The id of the project we want to retrieve benchmarkprojects for
    Return Value
      Type:String[]
      A string collection of the ids of the benchmark projects associated with the given projectId. If no benchmark projects are found, an empty array will be returned
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetBenchmarkProjectIds(self.key, projectId)
  
  def GetConditionBranch(self, projectId=None, parent=None, poetReadFilter=None, trueBranch=None):
    """Get nodes within a condition
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      parent
        Type: Condition
        Condition
      poetReadFilter
        Type: PoetReadFilter
        Filter used to specify the target
      trueBranch
        Type: System.Boolean
        True: Truebranch False: FalseBranch
    Return Value
      Type: SurveySchema
      ObjectStructure containing nodes
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if parent is None:
      raise Exception('Please specify parent')
    
    if poetReadFilter is None:
      raise Exception('Please specify poetReadFilter')
    
    if trueBranch is None:
      raise Exception('Please specify trueBranch')
    
    return self.GetClient().GetConditionBranch(self.key, projectId, parent, poetReadFilter, trueBranch)
  
  def GetCustomProjectInfoField(self, projectId=None, fieldId=None):
    """Get a value of a custom info field for a project
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project-ID of the project
      fieldId
        Type: System.String
        ID of the field (not to be confused with NAME of field)
    Return Value
      Type: String
      Value of the field
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldId is None:
      raise Exception('Please specify fieldId')
    
    return self.GetClient().GetCustomProjectInfoField(self.key, projectId, fieldId)
  
  def GetDatabaseLastCompiled(self, projectId=None, dbType=None):
    """Returns the timestamp of the last time the given database was compiled. If not compiled ever DateTime.MinValue is returned
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      dbType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Production or Test
    Return Value
      Type: DateTime
      Timestamp of last compilation
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if dbType is None:
      raise Exception('Please specify dbType')
    
    return self.GetClient().GetDatabaseLastCompiled(self.key, projectId, dbType)
  
  def GetExternalAnswers(self, projectId=None, name=None):
    """Gets the external answers for a single question
    Parameters
      key
        Type: System.String
        Key for authentication.
      projectId
        Type: System.String
        The survey project id
      name
        Type: System.String
        The name of the single question
    Return Value
      Type:AnswerBase[]
      An array of AnswerBase
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if name is None:
      raise Exception('Please specify name')
    
    return self.GetClient().GetExternalAnswers(self.key, projectId, name)
  
  def GetFilteredQuestionnaire(self):
    """Get Questionnaire (Routing, PredefinedLists and Quotas). Allows caller to filter out unwanted information (Script nodes)"""
  
  def GetForm(self):
    """Get Form (Info, Single, Multi, Grid, Grid3D, Open or Loop) from the form Should be used designtime. Typically this function is called to get a heavy-weight Form having already retrieved a light-weight Form."""
  
  def GetFormByName(self):
    """Get Form (Info, Single, Multi, Grid, Grid3D, Open or Loop) from name Should NOT be used designtime as it is very resource-demanding Well suited and fast realtime"""
  
  def GetFormsInLoop(self):
    """Get Forms within a given Loop If a parent (Loop) is specified all forms within that Loop-level is retrieved (IncludeAllForms in ReadFilter will be set to true) If parent is an object of type Root all forms that are not within any Loop is retrieved. If parent is NULL the search will be performed on all forms no matter loop-levels. In that case IncludeAllForms in ReadFilter will not be automatically set to true and it will be possible to specify form-names as a filter."""
  
  def GetHashCode(self):
    """(inherited from Object) Select the method name to go to the Microsoft documentation."""
  
  def GetLoopStructure(self):
    """Get LoopStructure (Only Loops)"""
  
  def GetNode(self):
    """Get Node (any node). Typically this function is called to get a heavy-weight Node having already retrieved a light-weight Node."""
  
  def GetNodes(self):
    """Get Nodes"""
  
  def GetPredefinedList(self):
    """Get a single Predefined List"""
  
  def GetPredefinedLists(self):
    """Get all PredefinedLists"""
  
  def GetProjectInfo(self):
    """Get project-info from a project"""
  
  def GetProjectList(self):
    """Get info about your projects. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects."""
  
  def GetProjectListByCreatedDate(self):
    """Get info about your projects by created date. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects."""
  
  def GetProjectListByCreator(self):
    """Get info about your projects by creator. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects."""
  
  def GetProjectListByKeywords(self):
    """Get info about your projects by keywords. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects."""
  
  def GetProjectListByProjectName(self):
    """Get info about your projects by project name. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects."""
  
  def GetQuestionnaire(self):
    """Get Questionnaire (Routing, PredefinedLists and Quotas). Note that all information about a survey is retrieved. If not all that information is needed, please use a different function that is suited to retrieve a subset of a survey schema."""
  
  def GetQuota(self):
    """Get single Quota"""
  
  def GetQuotas(self):
    """Get all Quotas"""
  
  def GetRouting(self):
    """Get Routing"""
  
  def GetService(self):
    """(inherited from MarshalByValueComponent) Select the method name to go to the Microsoft documentation."""
  
  def GetSurveyStatus(self):
    """Get the status of a project."""
  
  def GetType(self):
    """(inherited from Object) Select the method name to go to the Microsoft documentation."""
  
  def ImportSurvey(self):
    """Make a surveyimport"""
  
  def ImportTranslation(self):
    """Import a translated TranslationXML and merge it into the specified survey"""
  
  def ProjectExists(self):
    """Check if project exists"""
  
  def SetCustomProjectInfoField(self):
    """Set a value of a custom info field for a project"""
  
  def SetSurveyStatus(self):
    """Set the status of a project Status 'NotYetStarted' will be converted to 'Closed'"""
  
  def ToString(self):
    """(inherited from MarshalByValueComponent) Select the method name to go to the Microsoft documentation."""
  
  def Update(self):
    """Update the datacarrier"""
  
