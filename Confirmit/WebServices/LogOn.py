import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore

class LogOn(ConfirmitCore):
  
  def __init__(self):
    self.wsdl = ConfirmitCore.WSDL['logon']
  
  def LogOnUser(self, username=None, password=None):
    """Log on to confirmit web-services
    Parameters
      username
        Type: System.String
        Username of account with sufficient access to all operations that are to be performed
      password
        Type: System.String
        Password for the account
    Return Value
      Type: String
      Key that must be provided in each call to a confirmit web-service function
    """
    if username is None:
      raise Exception('Please specify username')
    
    if password is None:
      raise Exception('Please specify password')
    
    return self.GetClient().LogOnUser(username, password)
