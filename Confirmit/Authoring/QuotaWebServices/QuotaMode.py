from enum import Enum

class QuotaMode(Enum):
    ''' Represents the mode (source) for the quota '''
    # Quota in production mode
    Production = 0
    # Quota in test mode
    Test = 1
    # Quota in design mode with counters from production mode
    DesignWithProductionCounter = 2
    # Quota in design mode with counters from test mode
    DesignWithTestCounter = 3