import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class TaskManagement(ConfirmitCore):
  """
  """
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['taskmanagement']
  
  def GetTaskLogEntries(self, taskId=None):
    """Gets the log of a task
    Parameters
      key
        Type: System.String
        Key for authentication
      taskId
        Type: System.Int64
        Id for batch-task
    Return Value
      Type:TaskLogEntry[]
      Array of log-entries of the batch-task
    """
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetTaskLogEntries(self.key, taskId)

  def GetTaskPercentageCompleted(self, taskId=None):
    """Gets the percentage completed of a task
    Parameters
      key
        Type: System.String
        Key for authentication
      taskId
        Type: System.Int64
        Id for batch-task
    Return Value
      Type: Int16
      Percentage complete of the task
    """
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetTaskPercentageCompleted(self.key, taskId)

  def GetTaskStatus(self, taskId=None):
    """Gets the status of a task
    Parameters
      key
        Type: System.String
        Key for authentication
      taskId
        Type: System.Int64
        Id for batch-task
    Return Value
      Type: TaskStatus
      Status of the batch-task
    """
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetTaskStatus(self.key, taskId)

  def SetRecurrencePattern(self, recurrencePattern=None, taskId=None):
    """Set recurrence pattern on an existing task
    Parameters
      key
        Type: System.String
        Key for authentication
      recurrencePattern
        Type: TaskRecurrencePattern
        Recurrence pattern parameters in TaskRecurrencePattern
      taskId
        Type: System.Int64
        Id for batch-task to set recurrenct pattern on
    """
    if recurrencePattern is None:
      raise Exception('Please specify recurrencePattern')
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().SetRecurrencePattern(self.key, recurrencePattern, taskId)

  def SurveyDataExport(self, projectId=None, dataExportParams=None):
    """Start a Survey Data Export for a given project using parameters in the DataExportParameters object.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id
      dataExportParams
        Type: Firmglobal.Confirmit.SurveyData.DataTransfer.DataExportParameters
        Survey Data Export parameters in DataExportParameters
    Return Value
      Type: Int64
      Id for batch-task
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if dataExportParams is None:
      raise Exception('Please specify dataExportParams')

    return self.GetClient().SurveyDataExport(self.key, projectId, dataExportParams)

  def SurveyDataExportDefault(self, projectId=None):
    """Start a Survey Data Export for a given project. Default values of DataExportParameters will be used.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id
    Return Value
      Type: Int64
      Id for batch-task
    """
    if projectId is None:
      raise Exception('Please specify projectId')

    return self.GetClient().SurveyDataExportDefault(self.key, projectId)

