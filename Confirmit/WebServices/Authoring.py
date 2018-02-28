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
      raise Exception('Please specify isPanel')
    
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
  
  def GetFilteredQuestionnaire(self, projectId=None, projectSpecific=None, filter=None):
    """Get Questionnaire (Routing, PredefinedLists and Quotas). Allows caller to filter out unwanted information (Script nodes)
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.t
      projectSpecific
        Type: System.Boolean
        True means that the questionnaire should be linked to the project and can be updated, False means that the questionnaire should not be linked to the project and can be used to update other projects
      filter
        Type: PoetReadFilter
        Filter specifying what information is to be filtered out
    Return Value
      Type: SurveySchema
      ObjectStructure containing Questionnaire
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if projectSpecific is None:
      raise Exception('Please specify projectSpecific')
    
    if filter is None:
      raise Exception('Please specify filter')
    
    return self.GetClient().GetFilteredQuestionnaire(self.key, projectId, projectSpecific, filter)
  
  def GetForm(self, projectId=None, form=None, readFilterSimple=None, schemaSource=None):
    """Get Form (Info, Single, Multi, Grid, Grid3D, Open or Loop) from the form Should be used designtime. Typically this function is called to get a heavy-weight Form having already retrieved a light-weight Form.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      form
        Type: FormBase
        Form to be retrieved
      readFilterSimple
        Type: ReadFilterSimple
        Filter used to specify the target
      schemaSource
        Type: SchemaSourceType
        Designtime/RuntimeProduction/RuntimeTest
    Return Value
      Type: SurveySchema
      ObjectStructure containing Form
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if form is None:
      raise Exception('Please specify form')
    
    if readFilterSimple is None:
      raise Exception('Please specify readFilterSimple')
    
    if schemaSource is None:
      raise Exception('Please specify schemaSource')
    
    return self.GetClient().GetForm(self.key, projectId, form, readFilterSimple, schemaSource)
  
  def GetFormByName(self, projectId=None, name=None, readFilterSimple=None, schemaSource=None):
    """Get Form (Info, Single, Multi, Grid, Grid3D, Open or Loop) from name Should NOT be used designtime as it is very resource-demanding Well suited and fast realtime
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      name
        Type: System.String
        Name of form
      readFilterSimple
        Type: ReadFilterSimple
        Filter used to specify the target
      schemaSource
        Type: SchemaSourceType
        Designtime/RuntimeProduction/RuntimeTest
    Return Value
      Type: SurveySchema
      ObjectStructure containing Form
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if name is None:
      raise Exception('Please specify name')
    
    if readFilterSimple is None:
      raise Exception('Please specify readFilterSimple')
    
    if schemaSource is None:
      raise Exception('Please specify schemaSource')
    
    return self.GetClient().GetForm(self.key, projectId, name, readFilterSimple, schemaSource)
    
  def GetFormsInLoop(self, projectId=None, parent=None, readFilter=None, schemaSource=None):
    """Get Forms within a given Loop If a parent (Loop) is specified all forms within that Loop-level is retrieved (IncludeAllForms in ReadFilter will be set to true) If parent is an object of type Root all forms that are not within any Loop is retrieved. If parent is NULL the search will be performed on all forms no matter loop-levels. In that case IncludeAllForms in ReadFilter will not be automatically set to true and it will be possible to specify form-names as a filter.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      parent
        Type: Node
        The parent loop node.
      readFilter
        Type: ReadFilter
        Filter used to specify the target
      schemaSource
        Type: SchemaSourceType
        Designtime/RuntimeProduction/RuntimeTest
    Return Value
      Type: SurveySchema
      ObjectStructure containing forms
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if parent is None:
      raise Exception('Please specify parent')
    
    if readFilter is None:
      raise Exception('Please specify readFilter')
    
    if schemaSource is None:
      raise Exception('Please specify schemaSource')
    
    return self.GetClient().GetFormsInLoop(self.key, projectId, parent, readFilter, schemaSource)
  
  def GetHashCode(self):
    """(inherited from Object) Select the method name to go to the Microsoft documentation."""
  
  def GetLoopStructure(self, projectId=None, schemaSource=None):
    """Get LoopStructure (Only Loops)
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      schemaSource
        Type: SchemaSourceType
        Designtime/RuntimeProduction/RuntimeTest
    Return Value
      Type: SurveySchema
      ObjectStructure containing loops
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if schemaSource is None:
      raise Exception('Please specify schemaSource')
    
    return self.GetClient().GetLoopStructure(self.key, projectId, schemaSource)
  
  def GetNode(self, projectId=None, node=None, poetReadFilter=None):
    """Get Node (any node). Typically this function is called to get a heavy-weight Node having already retrieved a light-weight Node.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      node
        Type: Node
        Node to be retrieved
      poetReadFilter
        Type: PoetReadFilter
        Filter used to specify the target
    Return Value
      Type: SurveySchema
      ObjectStructure containing Node
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if node is None:
      raise Exception('Please specify node')
    
    if poetReadFilter is None:
      raise Exception('Please specify poetReadFilter')
    
    return self.GetClient().GetNode(self.key, projectId, node, poetReadFilter)
  
  def GetNodes(self, projectId=None, parent=None, poetReadFilter=None):
    """Get Nodes
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      parent
        Type: Node
        The parent node.
      poetReadFilter
        Type: PoetReadFilter
        Filter used to specify the target
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
    
    return self.GetClient().GetNodes(self.key, projectId, parent, poetReadFilter)
  
  def GetPredefinedList(self, projectId=None, name=None, readFilterSimple=None):
    """Get a single Predefined List
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      name
        Type: System.String
        Name of the Predefined list
      readFilterSimple
        Type: ReadFilterSimple
        Filter used to specify the target
    Return Value
      Type: SurveySchema
      ObjectStructure containing PredefinedList
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if name is None:
      raise Exception('Please specify name')
    
    if readFilterSimple is None:
      raise Exception('Please specify readFilterSimple')
    
    return self.GetClient().GetPredefinedList(self.key, projectId, name, readFilterSimple)
  
  def GetPredefinedLists(self, projectId=None, readFilterSimple=None):
    """Get all PredefinedLists
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      readFilterSimple
        Type: ReadFilterSimple
        Filter used to specify the target
    Return Value
      Type: SurveySchema
      ObjectStructure containing PredefinedLists
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if readFilterSimple is None:
      raise Exception('Please specify readFilterSimple')
    
    return self.GetClient().GetPredefinedLists(self.key, projectId, readFilterSimple)
  
  def GetProjectEmailObjects(self, projectId=None):
    """Gets EmailObjects for all email nodes that project contains
    Parameters
      key
        Type: System.String
        The authentication key
      projectId
        Type: System.String
        The id of the project
    Return Value
      Type:EmailObject[]
      A collection of EmailObjects
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetProjectEmailObjects(self.key, projectId)
  
  def GetProjectInfo(self, projectId=None):
    """Get project-info from a project
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
    Return Value
      Type: SurveySchema
      ObjectStructure containing ProjectInfo
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetProjectInfo(self.key, projectId)
  
  def GetProjectList(self, projectType=None, allProjects=None, token=None):
    """Get info about your projects. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectType
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectType
        Projecttype (panel/project/both)
      allProjects
        Type: System.Boolean
        true means all your projects, false means favorites
      token
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectListToken
        Token
    Return Value
      Type: ProjectListResultSet
      ProjectList-object
    """
    if projectType is None:
      raise Exception('Please specify projectType')
    
    if allProjects is None:
      raise Exception('Please specify allProjects')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetProjectList(self.key, projectType, allProjects, token)
  
  def GetProjectListByCreatedDate(self, projectType=None, allProjects=None, token=None, topN=None, createdFrom=None, createdTo=None):
    """Get info about your projects by created date. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectType
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectType
        Projecttype (panel/project/both)
      allProjects
        Type: System.Boolean
        true means all your projects, false means favorites
      token
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectListToken
        Token
      topN
        Type: System.Int32
        Will return the top N results. If token.LastId is set, the results will be relative to that id.
      createdFrom
        Type: System.DateTime
        Created from date. Inclusive.
      createdTo
        Type: System.DateTime
        Created to date. Inclusive.
    Return Value
      Type: ProjectListResultSet
      ProjectList-object
    """
    if projectType is None:
      raise Exception('Please specify projectType')
    
    if allProjects is None:
      raise Exception('Please specify allProjects')
    
    if token is None:
      raise Exception('Please specify token')
    
    if topN is None:
      raise Exception('Please specify topN')
    
    if createdFrom is None:
      raise Exception('Please specify createdFrom')
    
    if createdTo is None:
      raise Exception('Please specify createdTo')
    
    return self.GetClient().GetProjectListByCreatedDate(self.key, projectType, allProjects, token, topN, createdFrom, createdTo)
  
  def GetProjectListByCreator(self, projectType=None, allProjects=None, token=None, topN=None, createdByLastName=None):
    """Get info about your projects by creator. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectType
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectType
        Projecttype (panel/project/both)
      allProjects
        Type: System.Boolean
        true means all your projects, false means favorites
      token
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectListToken
        Token
      topN
        Type: System.Int32
        Will return the top N results. If token.LastId is set, the results will be relative to that id.
      createdByLastName
        Type: System.String
        Last name of the creator. Case sensitive
    Return Value
      Type: ProjectListResultSet
      ProjectList-object
    """
    if projectType is None:
      raise Exception('Please specify projectType')
    
    if allProjects is None:
      raise Exception('Please specify allProjects')
    
    if token is None:
      raise Exception('Please specify token')
    
    if topN is None:
      raise Exception('Please specify topN')
    
    if createdByLastName is None:
      raise Exception('Please specify createdByLastName')
    
    return self.GetClient().GetProjectListByCreator(self.key, projectType, allProjects, token, topN, createdByLastName)
  
  def GetProjectListByKeywords(self, projectType=None, allProjects=None, token=None, topN=None, keywords=None):
    """Get info about your projects by keywords. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectType
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectType
        Projecttype (panel/project/both)
      allProjects
        Type: System.Boolean
        true means all your projects, false means favorites
      token
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectListToken
        Token
      topN
        Type: System.Int32
        Will return the top N results. If token.LastId is set, the results will be relative to that id.
      keywords
        Type:System.String[]
        Keywords to search for.
    Return Value
      Type: ProjectListResultSet
      ProjectList-object
    """
    if projectType is None:
      raise Exception('Please specify projectType')
    
    if allProjects is None:
      raise Exception('Please specify allProjects')
    
    if token is None:
      raise Exception('Please specify token')
    
    if topN is None:
      raise Exception('Please specify topN')
    
    if keywords is None:
      raise Exception('Please specify keywords')
    
    return self.GetClient().GetProjectListByKeywords(self.key, projectType, allProjects, token, topN, keywords)
  
  def GetProjectListByProjectName(self, projectType=None, allProjects=None, token=None, topN=None, projectName=None):
    """Get info about your projects by project name. Token-based, ie. you get pages of projects at a time along with a token that can be sent in the nest request to get the next projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectType
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectType
        Projecttype (panel/project/both)
      allProjects
        Type: System.Boolean
        true means all your projects, false means favorites
      token
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.ProjectListToken
        Token
      topN
        Type: System.Int32
        Will return the top N results. If token.LastId is set, the results will be relative to that id.
      projectName
        Type: System.String
        Name of the project to search for. Use '*' to match not exact names.
    Return Value
    Type: ProjectListResultSet
    ProjectList-object
    """
    if projectType is None:
      raise Exception('Please specify projectType')
    
    if allProjects is None:
      raise Exception('Please specify allProjects')
    
    if token is None:
      raise Exception('Please specify token')
    
    if topN is None:
      raise Exception('Please specify topN')
    
    if projectName is None:
      raise Exception('Please specify projectName')
    
    return self.GetClient().GetProjectListByProjectName(self.key, projectType, allProjects, token, topN, projectName)
  
  def GetQuestionnaire(self, projectId=None, projectSpecific=False):
    """Get Questionnaire (Routing, PredefinedLists and Quotas). Note that all information about a survey is retrieved. If not all that information is needed, please use a different function that is suited to retrieve a subset of a survey schema.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.t
      projectSpecific
        Type: System.Boolean
        True means that the questionnaire should be linked to the project and can be updated, False means that the questionnaire should not be linked to the project and can be used to update other projects
    Return Value
      Type: SurveySchema
      ObjectStructure containing Questionnaire
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if projectSpecific is None:
      raise Exception('Please specify projectSpecific')
    
    return self.GetClient().GetQuestionnaire(self.key, projectId, projectSpecific)
  
  def GetQuota(self, projectId=None, name=None, projectSpecific=False):
    """Get single Quota
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      name
        Type: System.String
        Name of Quota
      projectSpecific
        Type: System.Boolean
        True means that the questionnaire should be linked to the project and can be updated, False means that the questionnaire should not be linked to the project and can be used to update other projects
    Return Value
      Type: SurveySchema
      ObjectStructure containing Quota
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if name is None:
      raise Exception('Please specify name')
    
    if projectSpecific is None:
      raise Exception('Please specify projectSpecific')
    
    return self.GetClient().GetQuota(self.key, projectId, name, projectSpecific)
  
  def GetQuotas(self, projectId=None, projectSpecific=False):
    """Get all Quotas
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      projectSpecific
        Type: System.Boolean
        True means that the questionnaire should be linked to the project and can be updated, False means that the questionnaire should not be linked to the project and can be used to update other projects
    Return Value
      Type: SurveySchema
      ObjectStructure containing Quotas
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if projectSpecific is None:
      raise Exception('Please specify projectSpecific')
    
    return self.GetClient().GetQuotas(self.key, projectId, projectSpecific)
  
  def GetRouting(self, projectId=None, projectSpecific=False):
    """Get Routing
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id.
      projectSpecific
        Type: System.Boolean
        True means that the questionnaire should be linked to the project and can be updated, False means that the questionnaire should not be linked to the project and can be used to update other projects
    Return Value
      Type: SurveySchema
      ObjectStructure containing nodes
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if projectSpecific is None:
      raise Exception('Please specify projectSpecific')
    
    return self.GetClient().GetRouting(self.key, projectId, projectSpecific)
  
  def GetService(self):
    """(inherited from MarshalByValueComponent) Select the method name to go to the Microsoft documentation."""
  
  def GetSurveyStatus(self, projectId=None):
    """Get the status of a project.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Id of the project
    Return Value
      Type: SurveyStatusType
      SurveyStatusType
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetSurveyStatus(self.key, projectId)
  
  def GetType(self):
    """(inherited from Object) Select the method name to go to the Microsoft documentation."""
  
  def ImportRemoteProject(self, remoteSite=None, remoteUserName=None, remotePassword=None, useSsl=True, remoteProjectId=None, newProjectName=None, includeData=False):
    """Imports a specified project from a remote Confirmit site to this site.
    Parameters
      key
        Type: System.String
        The authentication key
      remoteSite
        Type: System.String
        The hostname of the remote Confirmit site you want to import the project from
      remoteUserName
        Type: System.String
        Your Confirmit username at the remote site
      remotePassword
        Type: System.String
        The password associated with your Confirmit user at the remote site
      useSsl
        Type: System.Boolean
        Whether SSL should be used for the communication (remote site needs to have a certificate installed)
      remoteProjectId
        Type: System.String
        The project code of the project you want to import from the remote site
      newProjectName
        Type: System.String
        The name that the imported project should be given
      includeData (Optional)
        Type: System.Boolean
        Whether survey data should be included in the import
    Return Value
      Type: String
      The project code of the imported project
    """
    if remoteSite is None:
      raise Exception('Please specify remoteSite')
    
    if remoteUserName is None:
      raise Exception('Please specify remoteUserName')
    
    if remotePassword is None:
      raise Exception('Please specify remotePassword')
    
    if useSsl is None:
      raise Exception('Please specify useSsl')
    
    if remoteProjectId is None:
      raise Exception('Please specify remoteProjectId')
    
    if newProjectName is None:
      raise Exception('Please specify newProjectName')
    
    if includeData is None:
      raise Exception('Please specify includeData')
    
    return self.GetClient().ImportRemoteProject(self.key, remoteSite, remoteUserName, remotePassword, useSsl, remoteProjectId, newProjectName, includeData)
  
  def ImportSurvey(self, surveyXml=None):
    """Make a surveyimport
    Parameters
      key
        Type: System.String
        Key for authentication
      surveyXml
        Type: System.String
        XML representing the whole Survey
    Return Value
      Type: String
      Project-ID of the new survey
    """
    if surveyXml is None:
      raise Exception('Please specify surveyXml')
    
    return self.GetClient().ImportSurvey(self.key, surveyXml)
  
  def ImportTranslation(self, projectId=None, translationXml=None):
    """Import a translated TranslationXML and merge it into the specified survey
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The id of the survey to be updated with the translation changes
      translationXml
        Type: System.String
        TranslationXML document
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if translationXml is None:
      raise Exception('Please specify translationXml')
    
    return self.GetClient().ImportTranslation(self.key, projectId, translationXml)
  
  def ProjectExists(self, projectId=None):
    """Check if project exists
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The survey project id
    Return Value
      Type: Boolean
      A boolean if project exists
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().ProjectExists(self.key, projectId)
  
  def SetCustomProjectInfoField(self, projectId=None, status=None):
    """Set a value of a custom info field for a project
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
      fieldValue
        Type: System.String
        Value of the field
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldId is None:
      raise Exception('Please specify fieldId')
    
    if fieldValue is None:
      raise Exception('Please specify fieldValue')
    
    return self.GetClient().SetCustomProjectInfoField(self.key, projectId, fieldId, fieldValue)
  
  def SetSurveyStatus(self, projectId=None, status=None):
    """Set the status of a project Status 'NotYetStarted' will be converted to 'Closed'
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Id of the project
      status
        Type: Firmglobal.Confirmit.Authoring.ProjectManagement.SurveyStatusType
        The new status of the project
    Return Value
      Type: 
      void
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if status is None:
      raise Exception('Please specify status')
    
    return self.GetClient().SetSurveyStatus(self.key, projectId, status)
  
  def ToString(self):
    """(inherited from MarshalByValueComponent) Select the method name to go to the Microsoft documentation."""
  
  def Update(self, projectId=None, schema=None):
    """Update the datacarrier
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project-ID
      schema
        Type: SurveySchema
        The structure that has been obtained and changed
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if schema is None:
      raise Exception('Please specify schema')
    
    return self.GetClient().Update(self.key, projectId, schema)
  
