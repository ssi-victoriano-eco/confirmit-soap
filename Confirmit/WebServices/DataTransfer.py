import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class DataTransfer(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['datatransfer']

  def DeleteData(self, dataTransferDef=None):
    """Deletes data in the database according to the given TransferDef. The data will be deleted in reversed nesting level order. Rows appurtenant in underlying levels will also be deleted.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.SurveyDataTransferDefBase
        dataTransferDef.
    Return Value
      Type: Int32
      Number of affected rows.
    """
    if dataTransferDef is None:
      raise Exception('Please specify dataTransferDef')

    return self.GetClient().DeleteData(self.key, dataTransferDef)

  def DeleteRespondents(self, projectId=None, filterExpression=None):
    """Deletes a set of respondent by filter.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        Project id.
      filterExpression
        Type: System.String
        Filtering expression.
    Return Value
      Type: Int32
      The number of respondents deleted.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if filterExpression is None:
      raise Exception('Please specify filterExpression')

    return self.GetClient().DeleteRespondents(self.key, projectId, filterExpression)

  def GetChangedData(self, dataTransferDef=None, token=None, lastSynchronizedVersion=None):
    """Returns a ChangedDataResult containing the response data.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.SurveyDataTransferDef
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
    if dataTransferDef is None:
      raise expression('Please specify dataTransferDef')
    if token is None:
      raise expression('Please specify token')
    if lastSynchronizedVersion is None:
      raise expression('Please specify lastSynchronizedVersion')

    return self.GetClient().GetChangedData(self.key, dataTransferDef, token, lastSynchronizedVersion)

  def GetData(self, dataTransferDef=None, token=None):
    """Returns a TransferResult containing the response data.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.SurveyDataTransferDefBase
        The transfer definition object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: TransferResult
      The transfer result. See TransferResult
    """
    if dataTransferDef is None:
      raise Exception('Please specify dataTransferDef')
    if token is None:
      raise Exception('Please specify token')

    return self.GetClient().GetData(self.key, dataTransferDef, token)

  def GetDataGeneral(self, dataTransferDef=None, token=None):
    """Returns a ConfirmitDataResult containing the response data.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.SurveyDataTransferDefBase
        The transfer definition object.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ResponseToken
        The response token.
    Return Value
      Type: ConfirmitDataResult
      The transfer result. See ConfirmitDataResult
    """
    if dataTransferDef is None:
      raise Exception('Please specify dataTransferDef')
    if token is None:
      raise Exception('Please specify token')

    return self.GetClient().GetDataGeneral(self.key, dataTransferDef, token)

  def GetRespondents(self, dataTransferDef=None, token=None):
    """Gets a DataSet with a DataTable that is populated according to the filter (dataTransferDef), with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentDataTransferDefBase
        Definition of what to retrieve.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentToken
        The respondent token.
    Return Value
      Type: RespondentTransferResult
      A DataSet with the requested information.
    """
    if dataTransferDef is None:
      raise Exception('Please specify dataTransferDef')
    if token is None:
      raise Exception('Please specify token')

    return self.GetClient().GetRespondents(self.key, dataTransferDef, token)

  def GetRespondentsGeneral(self, dataTransferDef=None, token):
    """Gets a ConfirmitData object with data that is populated according to the filter, with respondents.
    Parameters
      key
        Type: System.String
        Key to validate user.
      dataTransferDef
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentDataTransferDefBase
        Definition of what to retrieve.
      token
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.RespondentToken
        The respondent token.
    Return Value
      Type: RespondentConfirmitDataResult
      A ConfirmitData with the requested information.
    """
    if dataTransferDef is None:
      raise Exception('Please specify dataTransferDef')
    if token is None:
      raise Exception('Please specify token')

    return self.GetClient().GetRespondentsGeneral(self.key, dataTransferDef, token)

  def UpdateData(self, projectId=None, databaseType=None, uniqueKey=None, dataSet=None, inTransaction=None):
    """Updates the database with the data in the filled DataSet.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        Project Id.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database type.
      uniqueKey
        Type: System.String
        Custom key used during transfer. This key is used instead of responseid.
      dataSet
        Type: System.Data.DataSet
        DataSet to be Updated.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
    Return Value
      Type:ErrorMessage[]
      ErrorMessage (Datatype: Array of strings).
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    if dataSet is None:
      raise Exception('Please specify dataSet')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')

    return self.GetClient().UpdateData(self.key, projectId, databaseType, uniqueKey, dataSet, inTransaction)

  def UpdateDataGeneral(self, projectId=None, databaseType=None, uniqueKey=None, data=None, inTransaction=None):
    """Updates the database with the data filled in the ConfirmitData.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        Project Id.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database type.
      uniqueKey
        Type: System.String
        Custom key used during transfer. This key is used instead of responseid.
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData to be Updated.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false do not.
    Return Value
      Type:ErrorMessage[]
      ErrorMessage (Datatype: Array of strings).
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    if data is None:
      raise Exception('Please specify data')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')

    return self.GetClient().UpdateDataGeneral(self.key, projectId, databaseType, uniqueKey, data, inTransaction)

  def UpdateRespondents(self, projectId=None, uniqueKey=None, ds=None, inTransaction=None):
    """Updates the respondents. Missing respondents will be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      ds
        Type: System.Data.DataSet
        DataSet containing a DataTable with the respondent rows to be updated.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false does not.
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    if ds is None:
      raise Exception('Please specify ds')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')

    return self.GetClient().UpdateRespondents(self.key, projectId, uniqueKey, ds, inTransaction)

  def UpdateRespondentsGeneral(self, projectId=None, uniqueKey=None, data=None, inTransaction=None):
    """Updates the respondents. Missing respondents will be added.
    Parameters
      key
        Type: System.String
        Key to validate user.
      projectId
        Type: System.String
        The project id.
      uniqueKey
        Type: System.String
        The name of the unique key to use when updating the respondents. If set to null or an empry string, the internal id (respid) for respondents will be used.
      data
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.ConfirmitData
        ConfirmitData containing the respondent rows to be updated.
      inTransaction
        Type: System.Boolean
        True runs the update in a transaction, false does not.
    Return Value
      Type:ErrorMessage[]
      Array of error-messages.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if uniqueKey is None:
      raise Exception('Please specify uniqueKey')
    if data is None:
      raise Exception('Please specify data')
    if inTransaction is None:
      raise Exception('Please specify inTransaction')

    return self.GetClient().UpdateRespondentsGeneral(self.key, projectId, uniqueKey, data, inTransaction)
