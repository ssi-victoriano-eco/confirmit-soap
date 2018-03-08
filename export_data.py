from Confirmit.DatabaseType import DatabaseType
from Confirmit.WebServices.Authoring import Authoring
from Confirmit.WebServices.SurveyData import SurveyData

import time, json

def GetConfirmitData(surveydata, projectId):
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

    if bool(token.LastDataSet):
      break

  return confirmit_data

if __name__ == '__main__':
  projectId = 'p1590365'

  start = time.time()
  surveydata = SurveyData()

  data = GetConfirmitData(surveydata, projectId)
  print('elapsed: ', time.time() - start)

  # write to file
  json_file = './.exports/{}.json'.format(projectId)
  with open(json_file, 'w') as f:
    f.write(json.dumps(data))
