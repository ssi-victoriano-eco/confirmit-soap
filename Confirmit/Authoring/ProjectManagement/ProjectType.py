from enum import Enum

class ProjectType(Enum):
    """ Used to specify if panel projects, regular projects or both should be retrieved"""

    ProjectOnly = 0
    PanelOnly = 1
    ProjectAndPanel = 2
    EnterprisePanelOnly = 3
    PollOnly = 4
    ProjectAndPoll = 5
    StandardPanelOnly = 6
    StandardAndProfessionalPanels = 7
    ContactDatabaseOnly = 8