import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class QuotaManagement(ConfirmitCore):
  """
  Confirmit QuotaManagementAPI
  """

  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['quotamanagement']

  def AdjustQuotaTarget(self, projectId=None, quotaName=None, quotaRowId=None, deltaTarget=None):
    """
    Adjusts the target for a quota row in design mode by a provided delta value.
    For example, the quota target can be decreased by 10 by providing -10 for deltaTarget.
    Note. This method can only be used if QuotaRowId was included from the GetQuotaList method.
    See note above. 
      string key,
      string projectId,
      string quotaName,
      int quotaRowId,
      int deltaTarget
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if quotaRowId is None:
      raise Exception('Please specify quotaRowId')
    if deltaTarget is None:
      raise Exception('Please specify deltaTarget')
    return self.GetClient().AdjustQuotaTarget(self.key, projectId, quotaName, quotaRowId, deltaTarget)

  def DeleteQuotaRows(self, projectId=None, quotaName=None, quotaList=None):
    """
    Deletes the rows in design mode that are specified in the quotaList propery (the QuotaList has a property called QuotaRows). 
      string key,
      string projectId,
      string quotaName,
      QuotaList quotaList
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if quotaList is None:
      raise Exception('Please specify quotaList')

    return self.GetClient().DeleteQuotaRows(self.key, projectId, quotaName, quotaList)

  def GetQuotaList(self, projectId=None, quotaName=None, quotaMode=None):
    """
    Gets the quota list for a quota.
    The user can specify to get the quota list for either Production, Test, DesignWithProductionCounter, or DesignWithTestCounter by the quotaMode property.
    Note. The QuotaRowId on the QuotaRow object (which is contained by QuotaList) is only set if the quota is synchronized. If not available, it is set to -1. 
      string key,
      string projectId,
      string quotaName,
      QuotaMode quotaMode
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if quotaMode is None:
      raise Exception('Please specify quotaMode')
    return self.GetClient().GetQuotaList(self.key, projectId, quotaName, quotaMode)

  def GetQuotaNames(self, projectId=None, quotaMode=None):
    """
    Gets the quota names for a project.
    The user can specify to get the names for either Production, Test, or design (DesignWithProductionCounter and DesignWithTestCounter will both give design name for this method) by the quotaMode property. 
      string key,
      string projectId,
      QuotaMode quotaMode
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaMode is None:
      raise Exception('Please specify quotaMode')

    return self.GetClient().GetQuotaNames(self.key, projectId, quotaMode)

  def RecalculateQuota(self, projectId=None, quotaName=None, databaseType=None):
    """
    Goes through all the responses for a survey and recalculates the quota counts for a given quota. 
      string key,
      string projectId,
      string quotaName,
      DatabaseType databaseType
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().RecalculateQuota(self.key, projectId, quotaName, databaseType)

  def SynchronizeQuota(self, projectId=None, quotaName=None, databaseType=None):
    """
    Synchronizes the quota from design to either test or production.
      string key,
      string projectId,
      string quotaName,
      DatabaseType databaseType
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().SynchronizeQuota(self.key, projectId, quotaName, databaseType)

  def UpdateQuotaList(self, projectId=None, quotaName=None, quotaList=None):
    """
    Updates the quota list in design mode.
      string key,
      string projectId,
      string quotaName,
      QuotaList quotaList
    """
    if projectId is None:
      raise Exception('Please specify projectId')
    if quotaName is None:
      raise Exception('Please specify quotaName')
    if quotaList is None:
      raise Exception('Please specify quotaList')

    return self.GetClient().UpdateQuotaList(self.key, projectId, quotaName, quotaList)
