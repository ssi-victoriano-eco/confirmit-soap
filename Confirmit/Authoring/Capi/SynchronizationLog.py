from datetime import datetime
from SynchronizationStatus import SynchronizationStatus
from SynchronizationType import SynchronizationType

class Synchronization:
    ''' Represents a synchronization log item '''

    def __init__(self):
        # The console name
        self.ConsoleName = ''
        # Duration
        self.Duration = ''
        # The end time
        self.EndTime = datetime.today()
        # The interview
        self.Interviewer = ''
        # The log item id
        self.LogId = 0
        # Project ids
        self.Projects = []
        self.ProjectString = ''
        # Number of responses
        self.Responses = 0
        # The start time
        self.StartTime = datetime.today()
        # The synchronization status
        self.SynchronizationStatus = SynchronizationStatus.Running
        # The synchronization type
        self.SynchronizationType = SynchronizationType.Automatic
    
    def GetObjectData(self, info=None, context=None):
        ''' Parameters
        info
            Type: System.Runtime.Serialization.SerializationInfo

        context
            Type: System.Runtime.Serialization.StreamingContext
         '''

        if info is None:
            raise Exception('Please specify info')

        if context is None:
            raise Exception('Please specify context')

        self.info = info
        self.context = context

        # return self.GetObjectData(info, context)