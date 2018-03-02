import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class Capi(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['capi']

  def AssignInterviewersToProject(self, userIds=None, projectId=None):
    """Assign interviewers to a project.
    Parameters
      key
        Type: System.String
        Key for authentication.
      userIds
        Type:System.String[]
        The interviewer user ids to assign.
      projectId
        Type: System.String
        The project id that the interviewers will be assigned to.
    Return Value
      Type:String[]
      An array with the user ids that do not exist. A successful assignment will return an empty array.
    """
    if userIds is None:
      raise Exception('Please specify userIds')
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().AssignInterviewersToProject(self.key, userIds, projectId)

  def AssignInterviewerToProjects(self, userId=None, projectIds=None):
    """Assign an interviewer to multiple projects.
    Parameters
      key
        Type: System.String
        Key for authentication
      userId
        Type: System.String
        The interviewer user id to assign.
      projectIds
        Type:System.String[]
        The project ids that the interviewer will be assigned to.
    Return Value
      Type:String[]
      An array with the project ids that do not exist. A successful assignment will return an empty array.
    """
    if userId is None:
      raise Exception('Please specify userId')
    if projectIds is None:
      raise Exception('Please specify projectIds')
    
    return self.GetClient().AssignInterviewerToProjects(self.key, userId, projectIds)

  def DeleteInterviewer(self, userId=None):
    """Delete an interviewer by user id.
    Parameters
      key
        Type: System.String
        Key for authentication
      userId
        Type: System.String
        The interviewer's user id.
    Return Value
      Type: Int32
      The interviewer id if the deletion is successful; -1 if the user id does not exist.
    """
    if userId is None:
      raise Exception('Please specify userId')
    
    return self.GetClient().DeleteInterviewer(self.key, userId)

  def GetAllInterviewerUserIds(self):
    """Get all the interviewer user ids.
    Parameters
      key
        Type: System.String
        Key for authentication
    Return Value
      Type:String[]
      An array with all the interviewer user ids.
    """
    return self.GetClient().GetAllInterviewerUserIds(self.key)

  def GetAssignedInterviewerUserIds(self, projectId=None):
    """Get the interviewer user ids that have been assign to a specified project.
    Parameters
      key
        Type: System.String
        Key for authentication.
      projectId
        Type: System.String
        The project id.
    Return Value
      Type:String[]
      An array with all the interviewer user ids that are assigned to the specified project.
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    
    return self.GetClient().GetAssignedInterviewerUserIds(self.key, projectId)

  def GetSynchronizationLog(self, pageSize=None, lastPageId=None, pagingForward=None, orderAscending=None, columnFilters=None):
    """GetSynchronizationScheduleLog
    Parameters
      key
        Type: System.String
        Key for authentication
      pageSize
        Type: System.Int32
        Number of rows in a page
      lastPageId
        Type: System.Int32
        Last page id
      pagingForward
        Type: System.Boolean
        Is forward or not
      orderAscending
        Type: System.Boolean
        Is ascending or not
      columnFilters
        Type: Firmglobal.Confirmit.Authoring.Capi.ColumnFilters
        Search criteria
    Return Value
      Type:SynchronizationLog[]
    """
    if pageSize is None:
      raise Exception('Please specify pageSize')
    if lastPageId is None:
      raise Exception('Please specify lastPageId')
    if pagingForward is None:
      raise Exception('Please specify pagingForward')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if columnFilters is None:
      raise Exception('Please specify columnFilters')

    return self.GetClient().GetSynchronizationLog(self.key, pageSize, lastPageId, pagingForward, orderAscending, columnFilters)

  def InsertInterviewer(self, userId=None, password=None, lastName=None, firstName=None):
    """Adds a new interviewer.
    Parameters
      key
        Type: System.String
        Key for authentication
      userId
        Type: System.String
        The interviewer's user id.
      password
        Type: System.String
        The interviewer's password.
      lastName
        Type: System.String
        The interviewer's last name.
      firstName
        Type: System.String
        The interviewer's first name.
    Return Value
      Type: Int32
      The (internal) interviewerId if the insert is successful; -1 if the user id already exists.
    """
    if userId is None:
      raise Exception('Please specify userId')
    if password is None:
      raise Exception('Please specify password')
    if lastName is None:
      raise Exception('Please specify lastName')
    if firstName is None:
      raise Exception('Please specify firstName')

    return self.GetClient().InsertInterviewer(self.key, userId, password, lastName, firstName)

  def SendIndividualMessages(self, messageList=None):
    """Send individual messages to interviewers. The message will appear in the CAPI console.
    Parameters
      key
        Type: System.String
        Key for authentication
      messageList
        Type:Firmglobal.Confirmit.Authoring.Capi.MessageToInterviewer[]
        An array of MessageToInterviewer.
    Return Value
      Type:String[]
      An array containing any interviewer user ids that could not be found in the database. If the sendout is successful, this method will return an empty array.
    """
    if messageList is None:
      raise Exception('Please specify messageList')
    
    return self.GetClient().SendIndividualMessages(self.key, messageList)

  def SendMessageToAllInterviewers(self, messageContent=None):
    """Send a message to the all interviewers. The message will appear in the CAPI console.
    Parameters
      key
        Type: System.String
        Key for authentication
      messageContent
        Type: Firmglobal.Confirmit.Authoring.Capi.MessageContent
        The message content. See MessageContent.
    """
    if messageContent is None:
      raise Exception('Please specify messageContent')
    
    return self.GetClient().SendMessageToAllInterviewers(self.key, messageContent)

  def SendMessageToInterviewers(self, userIds=None, messageContent=None):
    """Sends a message to the provided interviewers. The message will appear in the CAPI console.
    Parameters
      key
        Type: System.String
        Key for authentication.
      userIds
        Type:System.String[]
        The interviewer user ids the message will be sent to.
      messageContent
        Type: Firmglobal.Confirmit.Authoring.Capi.MessageContent
        The content of the message. See MessageContent.
    Return Value
      Type:String[]
      An array containing any interviewer user ids that could not be found in the database. If the sendout is successful, this method will return an empty array.
    """
    if userIds is None:
      raise Exception('Please specify userIds')
    if messageContent is None:
      raise Exception('Please specify messageContent')
    
    return self.GetClient().SendMessageToInterviewers(self.key, userIds, messageContent)

  def UpdateInterviewer(self, userId=None, password=None, lastName=None, firstName=None):
    """Updates an interviewer with the supplied information.
    Parameters
      key
        Type: System.String
        Key for authentication
      userId
        Type: System.String
        The interviewer's user id.
      password
        Type: System.String
        The new password.
      lastName
        Type: System.String
        The new last name.
      firstName
        Type: System.String
        The new first name.
    Return Value
      Type: Int32
      The internal interviewer id if the update is successful; -1 if the user id does not exist.
    """
    if userId is None:
      raise Exception('Please specify userId')
    if password is None:
      raise Exception('Please specify password')
    if lastName is None:
      raise Exception('Please specify lastName')
    if firstName is None:
      raise Exception('Please specify firstName')

    return self.GetClient().UpdateInterviewer(self.key, userId, password, lastName, firstName)
