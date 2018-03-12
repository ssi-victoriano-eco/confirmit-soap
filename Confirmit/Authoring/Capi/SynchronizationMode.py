from enum import Enum

class SynchronizationMode(Enum):
    ''' Used by ColumnFilter for synchronization log to filter on synchronization mode.'''
    # No filtering
    All = 0
    # Only include scheduled synchronizations
    Auto = 1
    # Only include manual synchronizations
    Manual = 2