import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class PanelCredit(ConfirmitCore):
  
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['panelcredit']
    
  def AddCreditToPanelist(self, panelId=None, panelistId=None, credit=None, comment=None, databaseType=None):
    """Add one credit to a panelist.
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      credit
        Type: System.Int32
        The credit to be added to the panelist. The credit can be a positive or negative integer.
      comment
        Type: System.String
        Open text field (255 char) to add a comment. Can be null or ""
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if credit is None:
      raise Exception('Please specify credit')
    if comment is None:
      raise Exception('Please specify comment')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().AddCreditToPanelist(self.key, panelId, panelistId, credit, comment, databaseType)

  def DeleteAllCreditsFromPanelist(self, panelId=None,panelistId=None,databaseType=None):
    """Delete all credits from a panelist
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: Int32
      Number of rows deleted
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeleteAllCreditsFromPanelist(self.key, panelId, panelistId, databaseType)

  def DeleteAllCreditsFromPanelistPerSurvey(self, panelId=None, panelistId=None, surveyId=None, databaseType=None):
    """Delete all panelist credits obtained from a given survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        SurveyId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: Int32
      Number of rows deleted
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeleteAllCreditsFromPanelistPerSurvey(self.key, panelId, panelistId, surveyId, databaseType)

  def DeleteAllCreditsFromSurvey(self, panelId=None, surveyId=None, databaseType=None):
    """Delete all credits from a survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      surveyId
        Type: System.String
        SurveyId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: Int32
      Number of rows deleted
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeleteAllCreditsFromSurvey(self.key, panelId, surveyId, databaseType)

  def DeleteCreditFromPanelist(self, panelId=None, panelistId=None, creditId=None, databaseType=None):
    """Delete one credit from a panelist.
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelistId
      panelistId
        Type: System.Int32
        PanelistId
      creditId
        Type: System.Int32
        The unique creditId to delete
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: Int32
      Number of rows deleted
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if creditId is None:
      raise Exception('Please specify creditId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().DeleteCreditFromPanelist(self.key, panelId, panelistId, creditId, databaseType)

  def GetAllCreditsFromPanel(self, panelId=None, databaseType=None):
    """Gets all credits for a given panel
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if databaseType is None:
      raise Exception('Please specify databaseType')
    
    return self.GetClient().GetAllCreditsFromPanel(self.key, panelId, databaseType)

  def GetAllCreditsFromPanelBetween(self, panelId=None, fromDate=None, toDate=None, databaseType=None):
    """Gets all credits for a panel to/from/between dates
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      fromDate
        Type: System.DateTime
        Specifies the from DateTime (including) when the credit was added. If you do not want to use from date, use MinValue. The parameter will then be ignored in the whereclause
      toDate
        Type: System.DateTime
        Specifies the to DateTime (including) when the credit was added. If you do not want to use to date, use MaxValue. The parameter will then be ignored in the whereclause
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if fromDate is None:
      raise Exception('Please specify fromDate')
    if toDate is None:
      raise Exception('Please specify toDate')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromPanelBetween(self.key, panelId, fromDate, toDate, databaseType)

  def GetAllCreditsFromPanelist(self, panelId=None, panelistId=None, databaseType=None):
    """Gets all credits for a panelist
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromPanelist(self.key, panelId, panelistId, databaseType)

  def GetAllCreditsFromPanelistBetween(self, panelId=None, panelistId=None, fromDate=None, toDate=None, databaseType=None):
    """Gets all credits for a panelist to/from/between dates
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      fromDate
        Type: System.DateTime
        Specifies the from DateTime (including) when the credit was added. If you do not want to use from date, use MinValue. The parameter will then be ignored in the whereclause
      toDate
        Type: System.DateTime
        Specifies the to DateTime (including) when the credit was added. If you do not want to use to date, use MaxValue. The parameter will then be ignored in the whereclause
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if fromDate is None:
      raise Exception('Please specify fromDate')
    if toDate is None:
      raise Exception('Please specify toDate')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromPanelistBetween(self.key, panelId, panelistId, fromDate, toDate, databaseType)

  def GetAllCreditsFromPanelistPerSurvey(self, panelId=None, panelistId=None, surveyId=None, databaseType=None):
    """Gets all credits for a panelist, where the credits are obtained from a given survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        SurveyId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromPanelistPerSurvey(self.key, panelId, panelistId, surveyId, databaseType)

  def GetAllCreditsFromSurvey(self, panelId=None, surveyId=None, databaseType=None):
    """Gets all credits for a survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      surveyId
        Type: System.String
        SurveyId
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromSurvey(self.key, panelId, surveyId, databaseType)

  def GetAllCreditsFromSurveyBetween(self, panelId=None, surveyId=None, fromDate=None, toDate=None, databaseType=None):
    """Gets all credits for a survey to/from/between dates
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      surveyId
        Type: System.String
        SurveyId
      fromDate
        Type: System.DateTime
        Specifies the from DateTime (including) when the credit was added. If you do not want to use from date, use MinValue. The parameter will then be ignored in the whereclause
      toDate
        Type: System.DateTime
        Specifies the to DateTime (including) when the credit was added. If you do not want to use to date, use MaxValue. The parameter will then be ignored in the whereclause
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if fromDate is None:
      raise Exception('Please specify fromDate')
    if toDate is None:
      raise Exception('Please specify toDate')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetAllCreditsFromSurveyBetween(self.key, panelId, surveyId, fromDate, toDate, databaseType)

  def GetCreditBalanceFromPanelist(self, panelId=None, panelistId=None, databaseType=None):
    """Gets the creditbalance for a given panelist
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        The unique Id for the panelist
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: Int32
      The balance for the given user
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetCreditBalanceFromPanelist(self.key, panelId, panelistId, databaseType)

  def GetCredits(self, panelId=None, panelistId=None, surveyId=None, topN=None, startPosition=None, orderAscending=None, fromDate=None, toDate=None, databaseType=None):
    """Get credits
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        SurveyId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      fromDate
        Type: System.DateTime
        Specifies the from DateTime (including) when the credit was added. If you do not want to use from date, use MinValue. The parameter will then be ignored in the whereclause
      toDate
        Type: System.DateTime
        Specifies the to DateTime (including) when the credit was added. If you do not want to use to date, use MaxValue. The parameter will then be ignored in the whereclause
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if fromDate is None:
      raise Exception('Please specify fromDate')
    if toDate is None:
      raise Exception('Please specify toDate')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetCredits(self.key, panelId, panelistId, surveyId, topN, startPosition, orderAscending, fromDate, toDate, databaseType)

  def GetCreditsWithCustomVariables(self, panelId=None, panelistId=None, surveyId=None, topN=None, startPosition=None, orderAscending=None, fromDate=None, toDate=None, customFieldNames=None):
    """Get credits with custom variables
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        SurveyId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      fromDate
        Type: System.DateTime
        Specifies the from DateTime (including) when the credit was added. If you do not want to use from date, use MinValue. The parameter will then be ignored in the whereclause
      toDate
        Type: System.DateTime
        Specifies the to DateTime (including) when the credit was added. If you do not want to use to date, use MaxValue. The parameter will then be ignored in the whereclause
      customFieldNames
        Type:System.String[]
        The names of the variables to retrieve
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if fromDate is None:
      raise Exception('Please specify fromDate')
    if toDate is None:
      raise Exception('Please specify toDate')
    if customFieldNames is None:
      raise Exception('Please specify customFieldNames')

    return self.GetClient().GetCreditsWithCustomVariables(self.key, panelId, panelistId, surveyId, topN, startPosition, orderAscending, fromDate, toDate, customFieldNames)

  def GetTopNCreditsFromPanel(self, panelId=None, topN=None, startPosition=None, orderAscending=None, databaseType=None):
    """Gets top N credits for a panel
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetTopNCreditsFromPanel(self.key, panelId, topN, startPosition, orderAscending, databaseType)

  def GetTopNCreditsFromPanelist(self, panelId=None, panelistId=None, topN=None, startPosition=None, orderAscending=None, databaseType=None):
    """Gets top N credits for a panelist
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetTopNCreditsFromPanelist(self.key, panelId, panelistId, topN, startPosition, orderAscending, databaseType)

  def GetTopNCreditsFromPanelistPerSurvey(self, panelId=None, panelistId=None, surveyId=None, topN=None, startPosition=None, orderAscending=None, databaseType=None):
    """Gets top N credits for a panelist, where the credits are obtained from a given survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        SurveyId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetTopNCreditsFromPanelistPerSurvey(self.key, panelId, panelistId, surveyId, topN, startPosition, orderAscending, databaseType)

  def GetTopNCreditsFromSurvey(self, panelId=None, surveyId=None, topN=None, startPosition=None, orderAscending=None, databaseType=None):
    """Gets top N credits for a survey
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      surveyId
        Type: System.String
        SurveyId
      topN
        Type: System.Int32
        The number of credits to return
      startPosition
        Type: System.Int32
        The creditId from where to start
      orderAscending
        Type: System.Boolean
        true/false
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    Return Value
      Type: PanelistCreditCollection
      A collection of credits
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if topN is None:
      raise Exception('Please specify topN')
    if startPosition is None:
      raise Exception('Please specify startPosition')
    if orderAscending is None:
      raise Exception('Please specify orderAscending')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().GetTopNCreditsFromSurvey(self.key, panelId, surveyId, topN, startPosition, orderAscending, databaseType)

  def SetCreditToPanelist(self, panelId=None, panelistId=None, surveyId=None, sectionId=None, credit=None, comment=None, databaseType=None):
    """Set one credit to a panelist. If combination of surveyId, panelistId and sectionId exists, update row. Else add row
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId for panelist to receive credits
      surveyId
        Type: System.String
        SurveyId
      sectionId
        Type: System.String
        Add credits to a section within a survey. Specified sectionId is added to surveyId. E.g p999999.section1. Default value is surveyId
      credit
        Type: System.Int32
        The credit to be added to the panelist. The credit can be a positive or negative integer.
      comment
        Type: System.String
        Open text field (255 char) to add a comment. Can be null.
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if sectionId is None:
      raise Exception('Please specify sectionId')
    if credit is None:
      raise Exception('Please specify credit')
    if comment is None:
      raise Exception('Please specify comment')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().SetCreditToPanelist(self.key, panelId, panelistId, surveyId, sectionId, credit, comment, databaseType)

  def SetCreditToPanelistWithCustomVariables(self, panelId=None, panelistId=None, surveyId=None, sectionId=None, credit=None, comment=None, fieldNames=None, fieldValues=None):
    """Add credit to a panelist with custom variables.
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      panelistId
        Type: System.Int32
        PanelistId
      surveyId
        Type: System.String
        The surveyId which the credit is added from.
      sectionId
        Type: System.String
        Add credits to a section within a survey. Specified sectionId is added to surveyId. E.g p999999.section1. Default value is surveyId
      credit
        Type: System.Int32
        The credit to be added to the panelist. The credit can be a positive or negative integer.
      comment
        Type: System.String
        Open text field (255 char) to add a comment. Can be null or ""
      fieldNames
        Type:System.String[]
        The names of the custom variables
      fieldValues
        Type:System.String[]
        The values of the custom variables
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if panelistId is None:
      raise Exception('Please specify panelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if sectionId is None:
      raise Exception('Please specify sectionId')
    if credit is None:
      raise Exception('Please specify credit')
    if comment is None:
      raise Exception('Please specify comment')
    if fieldNames is None:
      raise Exception('Please specify fieldNames')
    if fieldValues       is None:
      raise Exception('Please specify fieldValues')

    return self.GetClient().SetCreditToPanelistWithCustomVariables(self.key, panelId, panelistId, surveyId, sectionId, credit, comment, fieldNames, fieldValues)

  def SetCreditToSecondaryPanelist(self, panelId=None, receivingPanelistId=None, referrerPanelistId=None, surveyId=None, sectionId=None, credit=None, comment=None, databaseType=None):
    """Set one credit to a secondary panelist. If combination of surveyId, panelistId and sectionId exists, update row. Else add row
    Parameters
      key
        Type: System.String
        Key to validate user
      panelId
        Type: System.String
        PanelId
      receivingPanelistId
        Type: System.Int32
        PanelistId for panelist to receive credits
      referrerPanelistId
        Type: System.Int32
        Used when adding credits to another panelist. Referrer is the panelist giving credits
      surveyId
        Type: System.String
        SurveyId
      sectionId
        Type: System.String
        Add credits to a section within a survey. Specified sectionId is added to surveyId. E.g p999999.section1. Default value is surveyId
      credit
        Type: System.Int32
        The credit to be added to the panelist. The credit can be a positive or negative integer.
      comment
        Type: System.String
        Open text field (255 char) to add a comment. Can be null or ""
      databaseType
        Type: Firmglobal.Confirmit.ConfirmitConstants.DatabaseType
        Enumeration for which ConfirmitConstants.DatabaseType to use: Production or Test
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if receivingPanelistId is None:
      raise Exception('Please specify receivingPanelistId')
    if referrerPanelistId is None:
      raise Exception('Please specify referrerPanelistId')
    if surveyId is None:
      raise Exception('Please specify surveyId')
    if sectionId is None:
      raise Exception('Please specify sectionId')
    if credit is None:
      raise Exception('Please specify credit')
    if comment is None:
      raise Exception('Please specify comment')
    if databaseType is None:
      raise Exception('Please specify databaseType')

    return self.GetClient().SetCreditToSecondaryPanelist(self.key, panelId, receivingPanelistId, referrerPanelistId, surveyId, sectionId, credit, comment, databaseType)

