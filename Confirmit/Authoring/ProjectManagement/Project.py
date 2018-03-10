from datetime import datetime

class Project:
    """ Project is only used for READ-ONLY operations. When retrieving a project-list each project is represented by a Project-object. """

    def __init__(self):
        
        #Fields in C#
        self.ProductionWI_Timestamp = ''
        self.ProjectLifecycleClosed = ''
        self.ProjectLifecycleNotYetStarted = ''
        self.ProjectLifecycleProduction = ''
        self.TestWI_Timestamp = ''
        self.WILaunchDate = ''
        self.WITemplatePoet = ''

        #Properties in C#
        self._KeyWords_Xml = []
        self._Objid_Xml = ''
        self.Closed = ''
        self.Company = ''
        self.Created = datetime.today()
        self.Creator = ''
        self.Id = ''
        self.IsPanel = False
        self.IsSurveyPoll = False
        self.Keywords = []
        self.Name = []

