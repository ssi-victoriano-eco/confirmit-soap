import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class SurveyDeployer(ConfirmitCore):
  """
  The web-service SurveyDeployer gives an interface to the task-management system of confirmit.
  It enables programatical start of some common tasks and provides information about running tasks.
  """
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['surveydeployer']

  def CompileDB(self, projectId=None, databaseType=None, rebuild=None, deleteOld=None):
    """This method is obsolete. Please use LaunchSurvey instead. Compiles the database
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test)
      rebuild
        Type: System.Boolean
        Rebuild or Incremental
      deleteOld
        Type: System.Boolean
        Delete old database and create a new database    
    Return Value
      Type: Int64
      TaskID
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if rebuild is None:
      raise Exception('Please specify rebuild')
    if deleteOld is None:
      raise Exception('Please specify deleteOld')
    return self.GetClient().CompileDB(self.key, projectId, databaseType, rebuild, deleteOld)

  def DeployProject(self, projectId=None, databaseType=None):
    """This method is obsolete. Please use LaunchSurvey instead. Compiles the database and generates the web interview.    
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test)
    Return Value
      Type: TaskStatus
      Status of the batch-task
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeployProject(self.key, projectId, databaseType)

  def DeployProjectWithDotNetSurvey(self, projectId=None, databaseType=None):
    """This method is obsolete. Please use LaunchSurvey instead. Compiles the database and generates the .Net web interview
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test)
    Return Value
      Type: Int64
      TaskID
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeployProjectWithDotNetSurvey(self.key, projectId, databaseType)

  def GenerateWI(self, projectId=None, databaseType=None):
    """This method is obsolete. Please use LaunchSurvey instead. Generates Web Interview.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test). One of the ConfirmitConstants.DatabaseType values.
    Return Value
      Type: Int64
      TaskID
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GenerateWI(self.key, projectId, databaseType)
 
  def GenerateWINet(self, projectId=None, databaseType=None):
    """This method is obsolete. Please use LaunchSurvey instead. Generates .Net Web Interview
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        Project ID
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Database Type (Production or Test)
    Return Value
      Type: Int64
      TaskID
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GenerateWINet(self.key, projectId, databaseType)

  def GetTaskLogEntries(self, taskId=None):
    """Gets the log of a task
    Parameters
      key
        Type: System.String
        Key for authentication.
      taskId
        Type: System.Int64
        Id for task.
    Return Value
      Type:TaskLogEntry[]
      Array of log entries of the task.
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
        Id for the task.
    Return Value
      Type: Int16
      Percentage complete of the task.
    """
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetTaskPercentageCompleted(self.key, taskId)

  def GetTaskStatus(self, taskId=None):
    """Gets the status of a task
    Parameters
      key
        Type: System.String
        Key for authentication.
      taskId
        Type: System.Int64
        Id for the task.
    Return Value
      Type: TaskStatus
      Status of the task. One of the TaskStatus values.
    """
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetTaskStatus(self.key, taskId)

  def LaunchSurvey(self, projectId=None, databaseType=None, generateDBOption=None, generateWiOption=None):
    """Launch a survey
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        One of the ConfirmitConstants.DatabaseType values.
      generateDBOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateDbOptions
        One of the ConfirmitConstants.GenerateDbOptions values.
      generateWiOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateWiOptions
        One of the ConfirmitConstants.GenerateWiOptions values.
    Return Value
      Type: Int64
      The id of the launch task.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if generateDBOption is None:
      raise Exception('Please specify generateDBOption')
    if generateWiOption is None:
      raise Exception('Please specify generateWiOption')

    return self.GetClient().LaunchSurvey(self.key, projectId, databaseType, generateDBOption, generateWiOption)

  def LaunchSurveyAt(self, projectId=None, databaseType=None, generateDBOption=None, generateWIOption=None, dateSchedule=None):
    """Launch a survey at a specified time.
    Parameters
      key
        Type: System.String
        Key for authentication
      projectId
        Type: System.String
        The project id
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        One of the ConfirmitConstants.DatabaseType values.
      generateDBOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateDbOptions
        One of the ConfirmitConstants.GenerateDbOptions values.
      generateWIOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateWiOptions
        One of the ConfirmitConstants.GenerateWiOptions values.
      dateSchedule
        Type: System.DateTime
        The DateTime to start the task.
    Return Value
      Type: Int64
      The id of the launch task.
    """

    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if generateDBOption is None:
      raise Exception('Please specify generateDBOption')
    if generateWIOption is None:
      raise Exception('Please specify generateWIOption')
    if dateSchedule is None:
      raise Exception('Please specify dateSchedule')

    return self.GetClient().LaunchSurveyAt(self.key, projectId, databaseType, generateDBOption, generateWIOption, dateSchedule)

  def LaunchSurveyAtWithQA(self, projectId=None, databaseType=None, generateDBOption=None, generateWIOption=None, dateSchedule=None, enableExternalTest=None, isExternalQuicktest=None):
    """
    Parameters
      key
        Type: System.String
      projectId
        Type: System.String
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
      generateDBOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateDbOptions
      generateWIOption
        Type: Firmglobal.Confirmit.ConfirmitConstants.GenerateWiOptions
      dateSchedule
        Type: System.DateTime
      enableExternalTest
        Type: System.Boolean
      isExternalQuicktest
        Type: System.Boolean
    Return Value
      Type: Int64
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    if generateDBOption is None:
      raise Exception('Please specify generateDBOption')
    if generateWIOption is None:
      raise Exception('Please specify generateWIOption')
    if dateSchedule is None:
      raise Exception('Please specify dateSchedule')
    if enableExternalTest is None:
      raise Exception('Please specify enableExternalTest')
    if isExternalQuicktest is None:
      raise Exception('Please specify isExternalQuicktest')

    return self.GetClient().LaunchSurveyAtWithQA(self.key, projectId, databaseType, generateDBOption, generateWIOption, dateSchedule, enableExternalTest, isExternalQuicktest)

  def SendEmails(self, projectId=None, sender=None, subject=None, body=None, includeLink=None, mailFormat=None, bodyFormat=None, customText=None, isPanel=None, encoding=None, respondentFilter=None, activateLogging=None):
    """Sends an email
    Parameters
      key
        Type: System.String
        Key for authentication.
      projectId
        Type: System.String
        The project id.
      sender
        Type: System.String
        The email address from which the email will appear to be sent.
      subject
        Type: System.String
        The subject set on the email
      body
        Type: System.String
        The body of the email
      includeLink
        Type: Firmglobal.Confirmit.LinkType
        The type of link to the survey that should be attached. One of the LinkType values.
      mailFormat
        Type: Firmglobal.Confirmit.MailFormat
        The format of the email. One of the MailFormat values.
      bodyFormat
        Type: Firmglobal.Confirmit.BodyFormat
        the format of the email body. One of the BodyFormat values.
      customText
        Type: System.String
        A custom message that will be added to the confirmation email sent to the sender.
      isPanel
        Type: System.Boolean
        Set to false if the email is sent from a project, or true if the email is sent from a basic panel.
      encoding
        Type: System.String
        The encoding used for the email text (Central European (Windows), Cyrillic (DOS), Chinese Traditional,...)
      respondentFilter
        Type: Firmglobal.Confirmit.Emailing.RespondentFilter
        RespondentFilter object to define which respondents that should receive the email.
      activateLogging
        Type: System.Boolean
        True will log informationon every email sent, false will deactivate logging.
    Return Value
      Type: Int64
      The id of the emailing task.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if sender is None:
      raise Exception('Please specify sender')
    if subject is None:
      raise Exception('Please specify subject')
    if body is None:
      raise Exception('Please specify body')
    if includeLink is None:
      raise Exception('Please specify includeLink')
    if mailFormat is None:
      raise Exception('Please specify mailFormat')
    if bodyFormat is None:
      raise Exception('Please specify bodyFormat')
    if customText is None:
      raise Exception('Please specify customText')
    if isPanel is None:
      raise Exception('Please specify isPanel')
    if encoding is None:
      raise Exception('Please specify encoding')
    if respondentFilter is None:
      raise Exception('Please specify respondentFilter')
    if activateLogging is None:
      raise Exception('Please specify activateLogging')

    return self.GetClient().SendEmails(self.key, projectId, sender, subject, body, includeLink, mailFormat, bodyFormat, customText, isPanel, encoding, respondentFilter, activateLogging)

  def SendEmailsByEmailObject(self, projectId=None, emailObjectId=None, respondentFilter=None, schedulingTime=None):
    """Sends an emails to respondents using an email object defined in the survey.
    Parameters
      key
        Type: System.String
        Key for authentication.
      projectId
        Type: System.String
        The project id.
      emailObjectId
        Type: System.String
        The id of the survey email object that should be sent.
      respondentFilter
        Type: Firmglobal.Confirmit.Emailing.RespondentFilter
        RespondentFilter object to define which respondents that should receive the email.
      schedulingTime
        Type: System.Nullable<DateTime>
        The time to start the emailing task. If null - start immediately.
    Return Value
      Type: Int64
      The id of the emailing task.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if emailObjectId is None:
      raise Exception('Please specify emailObjectId')
    if respondentFilter is None:
      raise Exception('Please specify respondentFilter')
    if schedulingTime is None:
      raise Exception('Please specify schedulingTime')

    return self.GetClient().SendEmailsByEmailObject(self.key, projectId, emailObjectId, respondentFilter, schedulingTime)

  def SendEmailsByPanelEmailObject(self, projectId=None, panelEmailObjectId=None, respondentFilter=None, schedulingTime=None):
    """Sends an emails to respondents using an email object defined in a Professional or Standard panel. This method will only work for surveys connected to a panel.
    Parameters
      key
        Type: System.String
        Key for authentication.
      projectId
        Type: System.String
        The project id.
      panelEmailObjectId
        Type: System.String
        The id of the panel email object that should be sent.
      respondentFilter
        Type: Firmglobal.Confirmit.Emailing.RespondentFilter
        RespondentFilter object to define which respondents that should receive the email.
      schedulingTime
        Type: System.Nullable<DateTime>
        Time to start task. If null - start immediately.
    Return Value
      Type: Int64
      The id of the emailing task
    """
    if temp is None:
      raise Exception('Please specify temp')
    if projectId is None:
      raise Exception('Please specify projectId')
    if panelEmailObjectId is None:
      raise Exception('Please specify panelEmailObjectId')
    if respondentFilter is None:
      raise Exception('Please specify respondentFilter')
    if schedulingTime is None:
      raise Exception('Please specify schedulingTime')

    return self.GetClient().SendEmailsByPanelEmailObject(self.key, projectId, panelEmailObjectId, respondentFilter, schedulingTime)
