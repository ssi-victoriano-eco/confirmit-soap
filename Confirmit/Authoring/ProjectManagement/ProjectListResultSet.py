from ProjectList import ProjectList
from ProjectListToken import ProjectListToken

class ProjectListResultSet:
    """ Represents the result when getting a project list. """

    def __init__(self):        
        self.List = ProjectList()
        self.Token = ProjectListToken()