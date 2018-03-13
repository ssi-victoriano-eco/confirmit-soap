from enum import Enum

class SurveyStatusType(Enum):
    """ This is an enumerator for the various types of statuses a project can have. """

    Production = 0
    Closed = 1
    NotYetStarted = 2