import sys, os
sys.path.append(os.path.abspath('../'))

from Confirmit.DatabaseType import DatabaseType
from Confirmit.WebServices.Authoring import Authoring
from Confirmit.WebServices.SurveyData import SurveyData

import zeep

def GetConfirmitData(projectId):
  token = None
  result = None

  confirmit_data = []

  while True:
    result = surveydata.GetDataByProject(
      projectId = projectId,
      includeSystemVariables = True,
      databaseType = DatabaseType.Production,
      token = token
    )
    token = result.ResponseToken
    dataset = result.Result._value_1
    records = dataset.xpath('NewDataSet/responseid')
    
    for record in records:
      children = record.iterchildren()
      response = {}
      for child in children:
        key = child.tag
        value = child.text
        response[key] = value
      confirmit_data.append(response)
    
    print(confirmit_data)

    if bool(token.LastDataSet):
      break
  
  return confirmit_data

if __name__ == '__main__':
  projectId = 'p1590365'

  authoring = Authoring()
  surveydata = SurveyData()

  exists = authoring.ProjectExists(projectId)

  if exists:
    data = GetConfirmitData(projectId)
    print(data)
  else:
    print('cannot find {}'.format(projectId))

