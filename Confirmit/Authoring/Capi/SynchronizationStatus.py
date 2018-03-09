from enum import Enum

class SynchronizationStatus(Enum):
    ''' The synchronization status '''
    Success = 0
    Running = 1
    Fail = 2