from Project import Project

class ProjectList:
    """ ProjectList is only used for READ-ONLY operations. The projectlist contains a number of Project-objects, each representing a project in confirmit. """

    def __init__(self):
        self._Projects_Xml = []
        self.Projects = []
        self.XmlSerializer = None

    def AddProject(self, project=None):
        """ Adds a project to the ProjectList """        

        if project is None:
            raise Exception('Please specify project')

        self.Projects.append(project)

    def GetProject(self, position=None):
         """ Get a project based on its order position """

         if position == None:
            raise Exception('Please specify position')      

         try:
            return self.Projects[position]
         except:
             return None