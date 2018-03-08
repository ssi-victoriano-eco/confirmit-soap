import sys, os
sys.path.append(os.path.abspath('../'))

from Confirmit.DatabaseType import DatabaseType
from Confirmit.SurveyData.DataTransfer.TransferDef import TransferDef
from Confirmit.SurveyData.DataTransfer.TransferForm import TransferForm
from Confirmit.SurveyData.DataTransfer.TransferLevel import TransferLevel
from Confirmit.SurveyData.Querying.WhereClause import WhereClause

class SurveyDataUtil:

  RespondentTableName = 'respondent'

  @staticmethod
  def NewTransferDef(projectId=None, allChildLevels=True, dbType=DatabaseType.Production, levelsForms=[], where=None, systemVariables=None, includeRecodedVariables=False):
    transferDef = TransferDef(
      ProjectId = projectId,
      AllChildrenLevels = allChildLevels,
      DbType = dbType,
      Key = "responseid",
      IncludeRecodedVariables = includeRecodedVariables,
      SystemVariables = systemVariables
    )

    levelsList = []
    for level in levelsForms:
      transferLevel = TransferLevel(LoopId = level[0])
      if len(level) == 1:
        transferLevel.AllChildrenForms = True
      else:
        transferLevel.AllChildrenForms = False
        transferLevel.Forms = list(level.Select(lambda formName: TransferForm(
          AllChildrenFields = True,
          Name = formName
        )).Skip(1))
      
      levelsList.append(transferLevel)
    
    transferDef.Levels = list(levelsList)

    return transferDef
