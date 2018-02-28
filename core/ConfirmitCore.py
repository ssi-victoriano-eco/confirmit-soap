import sys, os
sys.path.append(os.path.abspath('../'))

import zeep

class ConfirmitCore:
  VERSION = '22.0.89'
  USERNAME = os.environ['CONFIRMIT_API_USERNAME']
  PASSWORD = os.environ['CONFIRMIT_API_PASSWORD']
  WSDL = {
    'authoring'        : os.path.abspath('wsdl/{}/authoring.wsdl'.format(VERSION)),
    'capi'             : os.path.abspath('wsdl/{}/capi.wsdl'.format(VERSION)),
    'communitypanel'   : os.path.abspath('wsdl/{}/communitypanel.wsdl'.format(VERSION)),
    'databasedesigner' : os.path.abspath('wsdl/{}/databasedesigner.wsdl'.format(VERSION)),
    'datatransfer'     : os.path.abspath('wsdl/{}/datatransfer.wsdl'.format(VERSION)),
    'logon'            : os.path.abspath('wsdl/{}/logon.wsdl'.format(VERSION)),
    'panelcredit'      : os.path.abspath('wsdl/{}/panelcredit.wsdl'.format(VERSION)),
    'quotamanagement'  : os.path.abspath('wsdl/{}/quotamanagement.wsdl'.format(VERSION)),
    'reporting'        : os.path.abspath('wsdl/{}/reporting.wsdl'.format(VERSION)),
    'samplemanagement' : os.path.abspath('wsdl/{}/samplemanagement.wsdl'.format(VERSION)),
    'surveydata'       : os.path.abspath('wsdl/{}/surveydata.wsdl'.format(VERSION)),
    'surveydeployer'   : os.path.abspath('wsdl/{}/surveydeployer.wsdl'.format(VERSION)),
    'taskmanagement'   : os.path.abspath('wsdl/{}/taskmanagement.wsdl'.format(VERSION)),
  }

  def __init__(self):
    self.key = None
    self.soap_client = None
    self.wsdl = None

  def GetClient(self):
    self.soap_client = zeep.Client(wsdl=self.wsdl)
    return self.soap_client.service
