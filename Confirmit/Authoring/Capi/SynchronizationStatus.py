from enum import Enum

class SynchronizationStatus(Enum):
    ''' The synchronization status '''
    # Success
    Success = 0
    # Running
    Running = 1
    # Failed
    Fail = 2