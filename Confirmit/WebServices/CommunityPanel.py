import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class CommunityPanel(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['communitypanel']

  def CreatePanelist(self, panelProjectId=None, fieldNames=None, fieldValues=None):
    """Create a new panelist in a panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelProjectId
        Type: System.String
        The project id of the panel.
      fieldNames
        Type:System.String[]
        The field names that will be set for the new panelist.
      fieldValues
        Type:System.String[]
        The values that will be set in the corresponding field names.
    Return Value
      Type: Int32
      The id of panelist that has been added.
    """
    if panelProjectId is None:
      raise Exception('Please specify panelProjectId')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    if fieldValues is None:
      raise Exception('Please specify fieldValues')

    return self.GetClient().CreatePanelist(self.key, panelProjectId, fieldNames, fieldValues)

  def DeleteData(self, transferDef=None):
    """Deletes data in the database according to the given TransferDef. The data will be deleted in reversed nesting level order. Rows appurtenant in underlying levels will also be deleted.
    Parameters
      key
        Type: System.String
        Key for authentication.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        DataTransfer.
    Return Value
      Type: Int32
      Number of affected rows.
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    
    return self.GetClient().DeleteData(self.key, transferDef)

  def DeletePanelist(self, projectId=None, panelistId=None):
    """Deletes a panelist from a community panel
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id for the survey
      panelistId
        Type: System.Int32
    Return Value
      Type: Int32
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    
    return self.GetClient().DeletePanelist(self.key, projectId, panelistId)

  def GetAllJobs(self, panelId=None):
    """Gets a XML definition for all jobs in a Professional or Standard panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
    Return Value
      Type:String[]
      String array with XML representing all jobs defined in the panel.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    
    return self.GetClient().GetAllJobs(self.key, panelId)

  def GetAllMatrices(self, panelId=None):
    """Gets an XML definition for all matrices in a Professional or Standard panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
    Return Value
      Type:String[]
      String array with XML representing all matrices in the panel.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    
    return self.GetClient().GetAllMatrices(self.key, panelId)

  def GetAllPanelRules(self, panelId=None):
    """Panel rule export
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
    Return Value
      Type:String[]
      String array with XML representing all panel rules
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    
    return self.GetClient().GetAllPanelRules(self.key, panelId)

  def GetAllPortals(self, panelId=None):
    """Gets a XML definition for all panel portals in a panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
    Return Value
      Type:String[]
      String array with XML representing all portals set up in the panel.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    
    return self.GetClient().GetAllPortals(self.key, panelId)

  def GetData(self, transferDef=None, token=None):
    """Returns a TransferResult containing the response data.
    Parameters
      key
        Type: System.String
        Key for authentication.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDefBase
        The transfer definition object. It can be a SimpleTransferDef or a TransferDef object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: TransferResult
      The transfer result. See TransferResult
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetData(self.key, transferDef, token)

  def GetDataGeneral(self, transferDef=None, token=None):
    """Returns a ConfirmitData containing the panelist data.
    Parameters
      key
        Type: System.String
        Key for authentication.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDefBase
        The transfer definition object. It can be a SimpleTransferDef or a TransferDef object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: ConfirmitDataResult
      The transfer result. See ConfirmitData
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetDataGeneral(self.key, transferDef, token)

  def GetJobs(self, panelId=None, jobIds=None):
    """Gets an XML definition for a list of jobs.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      jobIds
        Type: System.String
        Ids of jobs
    Return Value
      Type:String[]
      String array with XML representing the jobs
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobIds is None:
      raise Exception('Please specify jobIds')
    
    return self.GetClient().GetJobs(self.key, panelId, jobIds)

  def GetLinkedSurveyIds(self, panelId=None):
    """Gets projectIds for projects linked to the panel. This is all profile surveys and all surveys the panel has sampled respondents to.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
    Return Value
      Type:String[]
      String array with the linked projectIds.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    
    return self.GetClient().GetLinkedSurveyIds(self.key, panelId)

  def GetMatrices(self, panelId=None, matrixIds=None):
    """Gets an XML definition for a list of matrices.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      matrixIds
        Type: System.String
        Ids of matrices
    Return Value
      Type:String[]
      String array with XML representing the matrices
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrixIds is None:
      raise Exception('Please specify matrixIds')
    
    return self.GetClient().GetMatrices(self.key, panelId, matrixIds)

  def GetPanelistId(self, panelProjectId=None, fieldNames=None, fieldValues=None):
    """Gets the panelist id for a panelist by querying using the provided field names and values.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelProjectId
        Type: System.String
        The project id of the panel.
      fieldNames
        Type:System.String[]
        The field names that will be checked to find the panelist.
      fieldValues
        Type:System.String[]
        The values to check for the corresponding field names.
    Return Value
      Type: Int32
      The id of the panelist matching the field names and values. If multiple panelists match the quyery the first one is returned.
    """
    if panelProjectId is None:
      raise Exception('Please specify panelProjectId')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    if fieldValues is None:
      raise Exception('Please specify fieldValues')

    return self.GetClient().GetPanelistId(self.key, panelProjectId, fieldNames, fieldValues)

  def GetPanelRules(self, panelId=None, ruleIds=None):
    """Panel rule export
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      ruleIds
        Type: System.String
        Ids of rules to get
    Return Value
      Type:String[]
      String array with XML representing the panel rules
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if ruleIds is None:
      raise Exception('Please specify ruleIds')
    
    return self.GetClient().GetPanelRules(self.key, panelId, ruleIds)

  def GetPanelVariables(self, panelProjectId=None, userId=None, fieldNames=None):
    """Gets the panel variable values for a provided panelist in a panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelProjectId
        Type: System.String
        The project id of the panel.
      userId
        Type: System.Int32
        The userid for the panelist to get panel variables from.
      fieldNames
        Type:System.String[]
        The field names that willbe returned for the panelist.
    Return Value
      Type:String[]
      An array of field values based on the given field names.
    """
    if panelProjectId is None:
      raise Exception('Please specify panelProjectId')
    if userId is None:
      raise Exception('Please specify userId')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')

    return self.GetClient().GetPanelVariables(self.key, panelProjectId, userId, fieldNames)

  def GetRuleSets(self, panelId=None, ruleSetIds=None):
    """Panel rule set export
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      ruleSetIds
        Type: System.String
        Ids of rule sets to get
    Return Value
      Type:String[]
      String array with XML representing the panel rule sets
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if ruleSetIds is None:
      raise Exception('Please specify ruleSetIds')
        
    return self.GetClient().GetRuleSets(self.key, panelId, ruleSetIds)

  def GetSurveyList(self, parameters=None, panelId=None, panelistId=None):
    """Gets a DataTable with a list of the surveys a panelist has access to. Does not return Url for these surveys. Use GetSurveyUrl to get the Urls.
    Parameters
      key
        Type: System.String
        Key for authentication.
      parameters
        Type: Firmglobal.Confirmit.Panel.SurveyListParameters
        A SurveyListParameters object used to define what will be returned in the survey list.
      panelId
        Type: System.String
        The project id of the panel.
      panelistId
        Type: System.Int32
        The id the panelist has in the panel.
    Return Value
      Type: DataTable
      A DataTable with a list of surveys.
    """
    if parameters is None:
      raise Exception('Please specify parameters')
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')

    return self.GetClient().GetSurveyList(self.key, parameters, panelId, panelistId)

  def GetSurveyListGeneral(self, parameters=None, panelId=None, panelistId=None):
    """Gets a ConfirmitData object with a list of the surveys a panelist has access to. Does not return Url for these surveys. Use GetSurveyUrl to get the Urls.
    Parameters
      key
        Type: System.String
        Key for authentication.
      parameters
        Type: Firmglobal.Confirmit.Panel.SurveyListParameters
        A SurveyListParameters object used to define what will be returned in the survey list.
      panelId
        Type: System.String
        The project id of the panel.
      panelistId
        Type: System.Int32
        The id the panelist has in the panel.
    Return Value
      Type: ConfirmitData
      A ConfirmitData object with a list of surveys.
    """
    if parameters is None:
      raise Exception('Please specify parameters')
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')

    return self.GetClient().GetSurveyListGeneral(self.key, parameters, panelId, panelistId)

  def GetSurveyUrl(self, databaseType=None, surveyId=None, panelId=None, panelistId=None, respId=None, isEnterprisePanel=None):
    """Gets the unique survey url for a given panelist in a given survey.
    Parameters
      key
        Type: System.String
        Key for authentication.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test). One of the ConfirmitConstants.DatabaseType values.
      surveyId
        Type: System.String
        The id of the survey to get the url for.
      panelId
        Type: System.String
        The id of the panel the panelist is a member of.
      panelistId
        Type: System.Int32
        The id the panelist has in the panel.
      respId
        Type: System.Int32
        The respid the respondent has in the survey.
      isEnterprisePanel
        Type: System.Boolean
        True if the panel is a Professional or Standard panel.
    Return Value
      Type: String
      The unique survey url.
    """
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if respId is None:
      raise Exception('Please specify respId')
    if isEnterprisePanel is None:
      raise Exception('Please specify isEnterprisePanel')

    return self.GetClient().GetSurveyUrl(self.key, databaseType, surveyId, panelId, panelistId, respId, isEnterprisePanel)

  def GetUpdateProfileSurveyUrl(self, panelId=None, updateProfileProjectid=None, panelistId=None, language=None, returnUrl=None):
    """Returns an update profile url for specified project. Url is valid for 60 sec, and just one time.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      updateProfileProjectid
        Type: System.String
      panelistId
        Type: System.Int32
        The id the panelist has in the panel.
      language
        Type: System.Int32
      returnUrl
        Type: System.String
        Url to where the browser should redirect when update profile is finished
    Return Value
      Type: String
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if updateProfileProjectid is None:
      raise Exception('Please specify updateProfileProjectid')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if language is None:
      raise Exception('Please specify language')
    if returnUrl is None:
      raise Exception('Please specify returnUrl')

    return self.GetClient().GetUpdateProfileSurveyUrl(self.key, panelId, updateProfileProjectid, panelistId, language, returnUrl)

  def ImportMatrix(self, panelId=None, matrixXml=None):
    """Imports an XML defintion of a matrix to a panel as a new matrix.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelId
        Type: System.String
        The project id of the panel.
      matrixXml
        Type: System.String
        String with XML representing the matrix.
    Return Value
      Type: Int32
      The id of the new matrix.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrixXml is None:
      raise Exception('Please specify matrixXml')
    
    return self.GetClient().ImportMatrix(self.key, panelId, matrixXml)

  def UpdateData(self, transferDef=None, ds=None, applyRules=None, inTransaction=None, transactionKey=None):
    """Updates the database with the data in the filled DataSet.
    Parameters
      key
        Type: System.String
        Key for authentication.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        TransferDefintion
      ds
        Type: System.Data.DataSet
        DataSet to be Updated.
      applyRules
        Type: System.Boolean
        Indicates if data in the update should be verified against constraints in the panel. For instance that data updated for a single match a code from the answer list of the single.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number).
    Return Value
      Type:ErrorMessage[]
      ErrorMessage (Datatype: Array of strings).
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    if ds is None:
      raise Exception('Please specify ds')
    if applyRules is None:
      raise Exception('Please specify applyRules')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    if transactionKey is None:
      raise Exception('Please specify transactionKey')

    return self.GetClient().UpdateData(self.key, transferDef, ds, applyRules, inTransaction, transactionKey)

  def UpdateDataGeneral(self, transferDef=None, data=None, applyRules=None, inTransaction=None, transactionKey=None):
    """Updates the database with the data in the filled DataSet.
    Parameters
      key
        Type: System.String
        Key for authentication.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        TransferDefintion
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData to be Updated.
      applyRules
        Type: System.Boolean
        Indicates if data in the update should be verified against constraints in the panel. For instance that data updated for a single match a code from the answer list of the single.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number).
    Return Value
      Type:ErrorMessage[]
      ErrorMessage (Datatype: Array of strings).
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    if data is None:
      raise Exception('Please specify data')
    if applyRules is None:
      raise Exception('Please specify applyRules')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    if transactionKey is None:
      raise Exception('Please specify transactionKey')

    return self.GetClient().UpdateDataGeneral(self.key, transferDef, data, applyRules, inTransaction, transactionKey)

  def UpdatePanelVariables(self, panelProjectId=None, userId=None, fieldNames=None, fieldValues=None):
    """Updates the panel variables for a panelist with the provided values.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelProjectId
        Type: System.String
        The project id of the panel.
      userId
        Type: System.Int32
        The userid for the panelist that will be updated.
      fieldNames
        Type:System.String[]
        The field names that will updated for the panelist.
      fieldValues
        Type:System.String[]
        The values that will be set in the corresponding field names.
    Return Value
      Type: Int32
      0: Update successful.
      -1: Error on the client end, for example not being able to connect to the panel database etc.
      -2: The unique constraint is violated, i.e. another panelist already exists with the provided value(s) you are trying to set for (one of) the unique field(s) (email + any user provided unique fields).
      -3: Other database errors when updating the panelist.
      -4: The panelist does not exist.
      -5: The password failed on one or more of the password complexity rules, according to the Panel settings for password complexity.
    """
    if panelProjectId is None:
      raise Exception('Please specify panelProjectId')
    if userId is None:
      raise Exception('Please specify userId')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    if fieldValues is None:
      raise Exception('Please specify fieldValues')

    return self.GetClient().UpdatePanelVariables(self.key, panelProjectId, userId, fieldNames, fieldValues)

  def UpdateSurveyHistoryVariables(self, panelProjectId=None, userId=None, jobNumber=None, fieldNames=None, fieldValues=None):
    """Updates the survey history variables for a panelist with the provided values.
    Parameters
      key
        Type: System.String
        Key for authentication.
      panelProjectId
        Type: System.String
        The project id of the panel.
      userId
        Type: System.Int32
        The userid for the panelist that will be updated.
      jobNumber
        Type: System.String
        The job number of the job that will be updated.
      fieldNames
        Type:System.String[]
        The field names in the SurveyHistory loop that will updated for the panelist.
      fieldValues
        Type:System.String[]
        The values that will be set in the corresponding field names.
    Return Value
      Type: Int32
      0: Update successful.
      -1: Error on the client end, for example not being able to connect to the panel database etc.
      -2: The unique constraint is violated, i.e. another panelist already exists with the provided value(s) you are trying to set for (one of) the unique field(s) (email + any user provided unique fields).
      -3: Other database errors when updating the panelist.
      -4: The panelist does not exist.
      -5: The password failed on one or more of the password complexity rules, according to the Panel settings for password complexity.
    """
    if panelProjectId is None:
      raise Exception('Please specify panelProjectId')
    if userId is None:
      raise Exception('Please specify userId')
    if jobNumber is None:
      raise Exception('Please specify jobNumber')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    if fieldValues is None:
      raise Exception('Please specify fieldValues')

    return self.GetClient().UpdateSurveyHistoryVariables(self.key, panelProjectId, userId, jobNumber, fieldNames, fieldValues)

