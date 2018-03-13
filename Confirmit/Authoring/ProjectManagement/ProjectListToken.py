class ProjectListToken:    
    """ This class contains the status of each round trip when getting the project list. """

    def __init__(self):
        self.AtEnd = False
        self.HasError = False
        self.LastId = ''