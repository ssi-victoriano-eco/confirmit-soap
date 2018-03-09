from enum import Enum

class SynchronizationMode(Enum):
    ''' Used by ColumnFilter for synchronization log to filter on synchronization mode.'''

    All = 0
    Auto = 1
    Manual = 2