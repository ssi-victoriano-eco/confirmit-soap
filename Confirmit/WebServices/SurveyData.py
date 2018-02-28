import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class SurveyData(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['surveydata']

  def ConstructWhereClause(self, projectId=None, dbType=None, expressionVariableType=None, expression=None):
    """Parse string expression to where clause.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        Project id.
      dbType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database type.
      expressionVariableType
        Type: ExpressionVariableType
        Source of variables.
      expression
        Type: System.String
        String expression.
    Return Value
      Type: WhereClause
      Parsed where clause.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if dbType is None:
      raise Exception('Please specify dbType')
    
    if expressionVariableType is None:
      raise Exception('Please specify expressionVariableType')
    
    if expression is None:
      raise Exception('Please specify expression')
    
    return self.GetClient().ConstructWhereClause(self.key, projectId, dbType, expressionVariableType, expression)
    
  def DeleteAllRespondents(self, projectId=None):
    """Delete all respondents
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
    Return Value
      Type: Int32
      Number of respondents deleted.
    """
    return None   # prevent method from deleting respondents

    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().DeleteAllRespondents(self.key, projectId)
    
  def DeleteData(self, transferDef=None):
    """Deletes data in the database according to the given TransferDef. The data will be deleted in reversed nesting level order. Rows appurtenant in underlying levels will also be deleted.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        DataTransfer.
    Return Value
      Type: Int32
      Number of affected rows.
    """
    return None     # prevent method from deleting data

    if transferDef is None:
      raise Exception('Please specify transferDef')
    
    return self.GetClient().DeleteData(self.key, transferDef)
    
  def DeleteRespondents(self, projectId=None, keyName=None, keyValues=None):
    """Deletes a set of respondent based on a unique key.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      keyName
        Type: System.String
        The name of the unique key.
      keyValues
        Type:System.String[]
        The key values that identifies the respondents to delete.
    Return Value
      Type: Int32
      The number of respondents deleted.
    """
    return None     # prevent method from deleting repsondents

    if projectId is None:
      raise Exception('Please specify projectId')
    
    if keyName is None:
      raise Exception('Please specify keyName')
    
    if keyValues is None:
      raise Exception('Please specify keyValues')
    
    return self.GetClient().DeleteRespondents(self.key, projectId, keyName, keyValues)
    
  def Dispose(self):
    """"""
    
  def ExecuteQuery(self, query=None):
    """Execute a query in the database and get the result back as dataset
    Parameters
      key
        Type: System.String
        Key to validate user.
      query
        Type: Firmglobal.Confirmit.SurveyData.Querying.SurveyQuery
        Query
    Return Value
      Type: DataSet
      A DataSet with the result from the query.
    """
    if query is None:
      raise Exception('Please specify query')
    
    return self.GetClient().ExecuteQuery(self.key, query)
    
  def ExecuteQueryGeneral(self, query=None):
    """Execute a query in the database and get the result back as ConfirmitData
    Parameters
      key
        Type: System.String
        Key to validate user.
      query
        Type: Firmglobal.Confirmit.SurveyData.Querying.SurveyQuery
        Query
    Return Value
      Type: ConfirmitData
      A ConfirmitData with the result from the query.
    """
    if query is None:
      raise Exception('Please specify query')
    
    return self.GetClient().ExecuteQueryGeneral(self.key, query)
    
  def GetChangedData(self, transferDef=None, token=None, lastSynchronizedVersion=None):
    """Returns a TransferResult containing the response data.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        The transfer definition object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
      lastSynchronizedVersion
        Type: System.Int64
        The last synchronized version.
    Return Value
      Type: ChangedDataResult
      The transfer result. See ChangedDataResult
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    
    if token is None:
      raise Exception('Please specify token')
    
    if lastSynchronizedVersion is None:
      raise Exception('Please specify lastSynchronizedVersion')
    
    return self.GetClient().GetChangedData(self.key, transferDef, token, lastSynchronizedVersion)
    
  def GetData(self, transferDef=None, token=None):
    """Returns a TransferResult containing the response data. All levels in the project will be returned.
    Parameters
      key
        Type: System.String
        Key to validate user.
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
    
  def GetDataByProject(self, projectId=None, includeSystemVariables=None, databaseType=None, token=None):
    """Returns a TransferResult containing the response data. All levels in the project will be returned.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      includeSystemVariables
        Type: System.Boolean
        True will include all the system variables in the result, false will exclude them.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which database to use.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: TransferResult
      The transfer result. See TransferResult
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if includeSystemVariables is None:
      raise Exception('Please specify includeSystemVariables')
    
    if databaseType is None:
      raise Exception('Please specify databaseType')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetDataByProject(self.key, projectId, includeSystemVariables, databaseType, token)
    
  def GetDataByProjectGeneral(self, projectId=None, includeSystemVariables=None, databaseType=None, token=None):
    """Returns a ConfirmitDataResult containing the response data. All levels in the project will be returned.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      includeSystemVariables
        Type: System.Boolean
        True will include all the system variables in the result, false will exclude them.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which database to use.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: ConfirmitDataResult
      The transfer result. See ConfirmitDataResult
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if includeSystemVariables is None:
      raise Exception('Please specify includeSystemVariables')
    
    if databaseType is None:
      raise Exception('Please specify databaseType')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetDataByProjectGeneral(self.key, projectId, includeSystemVariables, databaseType, token)
    
  def GetDataGeneral(self, transferDef=None, token=None):
    """Returns a ConfirmitDataResult containing the response data. All levels in the project will be returned.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDefBase
        The transfer definition object. It can be a SimpleTransferDef or a TransferDef object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: ConfirmitDataResult
      The transfer result. See ConfirmitDataResult
    """
    if transferDef is None:
      raise Exception('Please specify transferDef')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetDataGeneral(self.key, transferDef, token)
    
  def GetInterviewProgressStats(self, projectId=None):
    """Get interview progress stats based on aggregated counts
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
    Return Value
      Type:InterviewProgressStats[]
      Aggregated counts for each survey status
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetInterviewProgressStats(self.key, projectId)
    
  def GetLevelByName(self, projectId=None, levelNames=None, includeSystemVariables=None, databaseType=None, token=None):
    """Returns a TransferResult containing the response data of one specified level for a project.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      levelNames
        Type:System.String[]
        The names of the levels to return.
      includeSystemVariables
        Type: System.Boolean
        True will include all the system variables in the result, false will exclude them.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which database to use.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: TransferResult
      The transfer result. See TransferResult.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if levelNames is None:
      raise Exception('Please specify levelNames')
    
    if includeSystemVariables is None:
      raise Exception('Please specify includeSystemVariables')
    
    if databaseType is None:
      raise Exception('Please specify databaseType')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetLevelByName(self.key, projectId, levelNames, includeSystemVariables, databaseType, token)
    
  def GetLevelByNameGeneral(self, projectId=None, levelNames=None, includeSystemVariables=None, databaseType=None, token=None):
    """Returns a ConfirmitDataResult containing the response data of one specified level for a project.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      levelNames
        Type:System.String[]
        The names of the levels to return.
      includeSystemVariables
        Type: System.Boolean
        True will include all the system variables in the result, false will exclude them.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which database to use.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: ConfirmitDataResult
      The transfer result. See ConfirmitDataResult.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if levelNames is None:
      raise Exception('Please specify levelNames')
    
    if includeSystemVariables is None:
      raise Exception('Please specify includeSystemVariables')
    
    if databaseType is None:
      raise Exception('Please specify databaseType')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetLevelByNameGeneral(self.key, projectId, levelNames, includeSystemVariables, databaseType, token)
    
  def GetRespondentEmailLogByTask(self, projectId=None, fieldNames=None, taskId=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on the task id.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      taskId
        Type: System.Int64
        The task id to get log entried for.
    Return Value
      Type: DataSet
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if taskId is None:
      raise Exception('Please specify taskId')
    
    return self.GetClient().GetRespondentEmailLogByTask(self.key, projectId, fieldNames, taskId)
    
  def GetRespondentEmailLogByTaskGeneral(self, projectId=None, fieldNames=None, taskId=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on the task id.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      taskId
        Type: System.Int64
        The task id to get log entried for.
    Return Value
      Type: ConfirmitData
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if taskId is None:
      raise Exception('Please specify taskId')
    
    return self.GetClient().GetRespondentEmailLogByTaskGeneral(self.key, projectId, fieldNames, taskId)
    
  def GetRespondentEmailLogByTime(self, projectId=None, fieldNames=None, _from_=None, to=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on time lag.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      from
        Type: System.DateTime
        The start date/time of the log entries selection.
      to
        Type: System.DateTime
        The end date/time of the log entries selection.
    Return Value
      Type: DataSet
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if _from_ is None:
      raise Exception('Please specify from')
    
    if to is None:
      raise Exception('Please specify to')
    
    return self.GetClient().GetRespondentEmailLogByTime(self.key, projectId, fieldNames, _from_, to)
    
  def GetRespondentEmailLogByTimeGeneral(self, projectId=None, fieldNames=None, _from_=None, to=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on time lag.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      from
        Type: System.DateTime
        The start date/time of the log entries selection.
      to
        Type: System.DateTime
        The end date/time of the log entries selection.
    Return Value
      Type: ConfirmitData
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if _from_ is None:
      raise Exception('Please specify from')
    
    if to is None:
      raise Exception('Please specify to')
    
    return self.GetClient().GetRespondentEmailLogByTimeGeneral(self.key, projectId, fieldNames, _from_, to)
    
  def GetRespondentEmailLogByUniqueKey(self, projectId=None, fieldNames=None, keyName=None, keyValues=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on a user defined unique key.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      keyName
        Type: System.String
        The name of the unique key to get log entries for.
      keyValues
        Type:System.String[]
        Unique key values to get log entries for.
    Return Value
      Type: DataSet
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if keyName is None:
      raise Exception('Please specify keyName')
    
    if keyValues is None:
      raise Exception('Please specify keyValues')
    
    return self.GetClient().GetRespondentEmailLogByUniqueKey(self.key, projectId, fieldNames, keyName, keyValues)
    
  def GetRespondentEmailLogByUniqueKeyGeneral(self, projectId=None, fieldNames=None, keyName=None, keyValues=None):
    """Gets the email log entries, that are logged during a respondent emailing task, based on a user defined unique key.
    Parameters
      key
        Type: System.String
        Key to authenticate the user.
      projectId
        Type: System.String
        The project id.
      fieldNames
        Type:System.String[]
        The respondent field names that should be in the returned result.
      keyName
        Type: System.String
        The name of the unique key to get log entries for.
      keyValues
        Type:System.String[]
        Unique key values to get log entries for.
    Return Value
      Type: ConfirmitData
      The email log entries.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    
    if keyName is None:
      raise Exception('Please specify keyName')
    
    if keyValues is None:
      raise Exception('Please specify keyValues')
    
    return self.GetClient().GetRespondentEmailLogByUniqueKeyGeneral(self.key, projectId, fieldNames, keyName, keyValues)
    
  def GetRespondents(self, respondentTransferDef=None):
    """Gets a DataSet with a DataTable that is populated according to the filter (respondentTransferDef), with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      respondentTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentTransferDef
        Definition of what to retrieve.
    Return Value
      Type: DataSet
      A DataSet with the requested information.
    """
    if respondentTransferDef is None:
      raise Exception('Please specify respondentTransferDef')
    
    return self.GetClient().GetRespondents(self.key, respondentTransferDef)
    
  def GetRespondentsGeneral(self, respondentTransferDef=None):
    """Gets a ConfirmitData object with data that is populated according to the filter (respondentTransferDef), with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      respondentTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentTransferDef
        Definition of what to retrieve.
    Return Value
      Type: ConfirmitData
      A ConfirmitData with the requested information.
    """
    if respondentTransferDef is None:
      raise Exception('Please specify respondentTransferDef')
    
    return self.GetClient().GetRespondentsGeneral(self.key, respondentTransferDef)
    
  def GetRespondentsTokenized(self, respondentTransferDef=None, token=None):
    """Gets a DataSet with a DataTable that is populated according to the filter (respondentTransferDef), with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      respondentTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentTransferDef
        Definition of what to retrieve.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentToken
        The RespondentToken.
    Return Value
      Type: RespondentTransferResult
      A DataSet with the requested information.
    """
    if respondentTransferDef is None:
      raise Exception('Please specify respondentTransferDef')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetRespondentsTokenized(self.key, respondentTransferDef, token)
    
  def GetRespondentsTokenizedGeneral(self, respondentTransferDef=None, token=None):
    """Gets a ConfirmitData object with data that is populated according to the filter (respondentTransferDef), with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      respondentTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentTransferDef
        Definition of what to retrieve.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentToken
        The RespondentToken.
    Return Value
      Type: RespondentConfirmitDataResult
      A RespondentConfirmitDataResult with the data and an updated token.
    """
    if respondentTransferDef is None:
      raise Exception('Please specify respondentTransferDef')
    
    if token is None:
      raise Exception('Please specify token')
    
    return self.GetClient().GetRespondentsTokenizedGeneral(self.key, respondentTransferDef, token)
    
  def GetTransactionStatus(self, transactionKey=None):
    """Returns a set of transaction status rows based on a transaction key.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transactionKey
        Type: System.Int32
        Transaction key.
    Return Value
      Type: DataSet
      Data set with transaction log rows.
    """
    if transactionKey is None:
      raise Exception('Please specify transactionKey')
    
    return self.GetClient().GetTransactionStatus(self.key, transactionKey)
    
  def IsRespondentUniqueKey(self, projectId=None, uniqueKey=None):
    """Checks if a respondent field is set to be a unique key.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      uniqueKey
        Type: System.String
        The name of the unique key to check.
    Return Value
      Type: Boolean
      True if it is unique, else false.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    return self.GetClient().IsRespondentUniqueKey(self.key, projectId, uniqueKey)
    
  def RemoveRespondentUniqueKey(self, projectId=None, uniqueKey=None):
    """Removes the definition of uniqueness for a key.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      uniqueKey
        Type: System.String
        The name og the unique key.
    """
    return None     # prevent method from removing unique key
    
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    return self.GetClient().RemoveRespondentUniqueKey(self.key, projectId, uniqueKey)
    
  def ResetConfigSettings(self):
    """"""
    return None     # prevent method from resetting config settings
    # return self.GetClient().ResetConfigSettings(self.key)
    
  def SetRespondentUniqueKey(self, projectId=None, uniqueKey=None):
    """Sets the key that should be unique for the respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      uniqueKey
        Type: System.String
        The name of the unique key.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    return self.GetClient().SetRespondentUniqueKey(self.key, projectId, uniqueKey)
    
  def UpdateData(self, transferDef=None, ds=None, applyRules=None, inTransaction=None, transactionKey=None):
    """Updates the database with the data in the filled DataSet.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        TransferDefintion
      ds
        Type: System.Data.DataSet
        DataSet to be Updated.
      applyRules
        Type: System.Boolean
        Indicates if data in the update should be verified against constraints in the survey. For instance that data updated for a single match a code from the answer list of the single.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
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
    """Updates the database with the data filled in the ConfirmitData.
    Parameters
      key
        Type: System.String
        Key to validate user.
      transferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.TransferDef
        TransferDefintion
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData to be Updated.
      applyRules
        Type: System.Boolean
        Indicates if data in the update should be verified against constraints in the survey. For instance that data updated for a single match a code from the answer list of the single.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
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
    
  def UpdateExistingRespondents(self, projectId=None, ds=None, validate=None, uniqueKey=None, inTransaction=None, transactionKey=None):
    """Updates the existing respondents only. Missing respondents will not be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      ds
        Type: System.Data.DataSet
        DataSet containing a DataTable with the respondent rows to be updated.
      validate
        Type: System.Boolean
        Validation of the content of the respondents.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if ds is None:
      raise Exception('Please specify ds')
    
    if validate is None:
      raise Exception('Please specify validate')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    
    if transactionKey is None:
      raise Exception('Please specify transactionKey')
    
    return self.GetClient().UpdateExistingRespondents(self.key, projectId, ds, validate, uniqueKey, inTransaction, transactionKey)
    
  def UpdateExistingRespondentsGeneral(self, projectId=None, data=None, validate=None, uniqueKey=None, inTransaction=None, transactionKey=None):
    """Updates the existing respondents only. Missing respondents will not be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData containing the respondent rows to be updated.
      validate
        Type: System.Boolean
        Validation of the content of the respondents.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if data is None:
      raise Exception('Please specify data')
    
    if validate is None:
      raise Exception('Please specify validate')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    
    if transactionKey is None:
      raise Exception('Please specify transactionKey')
    
    return self.GetClient().UpdateExistingRespondentsGeneral(self.key, projectId, data, validate, uniqueKey, inTransaction, transactionKey)
    
  def UpdateRespondents(self, projectId=None, ds=None, validate=None, merge=None, uniqueKey=None, inTransaction=None, transactionKey=None):
    """Updates the respondents. Missing respondents will be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      ds
        Type: System.Data.DataSet
        DataSet containing a DataTable with the respondent rows to be updated.
      validate
        Type: System.Boolean
        Validation of the content of the respondents.
      merge
        Type: System.Boolean
        Update existing rows when possible.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false does not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if ds is None:
      raise Exception('Please specify ds')
    
    if validate is None:
      raise Exception('Please specify validate')
    
    if merge is None:
      raise Exception('Please specify merge')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    
    if transactionKey is None:
      raise Exception('Please specify transactionKey')
    
    return self.GetClient().UpdateRespondents(self.key, projectId, ds, validate, merge, uniqueKey, inTransaction, transactionKey)
    
  def UpdateRespondentsGeneral(self, projectId=None, data=None, validate=None, merge=None, uniqueKey=None, inTransaction=None, transactionKey=None):
    """Updates the respondents. Missing respondents will be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData containing the respondent rows to be updated.
      validate
        Type: System.Boolean
        Validation of the content of the respondents.
      merge
        Type: System.Boolean
        Update existing rows when possible.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false does not.
      transactionKey
        Type: System.Int32
        A key, defined by the user to be able to track if the transaction succeeded or not (cannot be a negative number). See GetTransactionStatus(String, Int32).
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    if data is None:
      raise Exception('Please specify data')
    
    if validate is None:
      raise Exception('Please specify validate')
    
    if merge is None:
      raise Exception('Please specify merge')
    
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    
    if inTransaction is None:
      raise Exception('Please specify inTransaction')
    
    if transactionKey is None:
      raise Exception('Please specify transactionKey')
    
    return self.GetClient().UpdateRespondentsGeneral(self.key, projectId, data, validate, merge, uniqueKey, inTransaction, transactionKey)
