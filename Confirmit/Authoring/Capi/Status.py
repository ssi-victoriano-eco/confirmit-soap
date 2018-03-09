from enum import Enum

class Status(Enum):
    ''' Used by ColumnFilter to specify a synchronization status '''
    # No filtering
    All = 0
    # Include only failed synchronizations
    Failed = 1
    # Include only successful synchronizations
    Success = 2
    # Include only currently running synchronizations
    Running = 3