from DateTimeFilter import DateTimeFilter
from Status import Status
from SynchronizationMode import SynchronizationMode

class ColumnFilters:
  ''' Class representing column filter similar to the one you find in synchronization log in Confirmit UI.'''

  def __init__(self):
    # Apply this to filter on completed responses synchronized.
    self.CompletedResponsesFilter = None
    # Apply this to filter on console name.
    self.ConsoleNameFilter = ''
    # Apply this to filter on duration
    self.DurationInSecondsFilter = None
    # Apply this to filter on interviewer user id.
    self.InterviewerUserIDFilter = None
    # Apply this to filter on period from date
    self.PeriodFrom = DateTimeFilter()
    # Apply this to filter on period to date
    self.PeriodTo = DateTimeFilter()
    # Apply this to filter on project
    self.ProjectFilter = ''
    # Apply this to filter on synchronization status
    self.StatusFilter = Status.All
    # Apply this to filter on synchronization mode
    self.SynchronizationMode = SynchronizationMode.All