from Confirmit.WebServices.Authoring import Authoring
from Confirmit.WebServices.SurveyData import SurveyData

# ## INTERNAL 22070002 | Millenials Bid w/ Data Duplicate (p2506549)
# Survey for testing Confirmit Data API (6442 records)
# * https://online.ssisurveys.com/wix/p2506549.aspx

projectId = 'p2506549'

authoring = Authoring()
surveydata = SurveyData()

exists = authoring.ProjectExists(projectId)

if exists:
  print('{} exists.'.format(projectId))
  stats = surveydata.GetInterviewProgressStats(projectId)
  print(stats)
else:
  print('cannot find {}'.format(projectId))
