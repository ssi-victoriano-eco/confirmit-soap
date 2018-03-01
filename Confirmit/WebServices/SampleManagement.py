import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class SampleManagement(ConfirmitCore):
  """
  Summary description for SampleManagement
  """
  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['samplemanagement'] 

  def AddExternalSurveyLinks(self, panelId=None, jobId=None, surveyLinks=None):
    """Adds external survey links to a job
    Parameters
      key
        Type: System.String
        Security key.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
      surveyLinks
        Type:System.String[]
        Array of the external survey links.
    Return Value
      Type: Int32
      Amount of links added.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if surveyLinks is None:
      raise Exception('Please specify surveyLinks')

    return self.GetClient().AddExternalSurveyLinks(self.key, panelId, jobId, surveyLinks)

  def AddMatrix(self, panelId=None, matrix=None):
    """Add a new matrix to a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that matrix will be added to (Example: p0000001).
      matrix
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.SamplingMatrix
        SamplingMatrix representing the matrix you want to add.
    Return Value
      Type: Int32
      Id for the added matrix.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrix is None:
      raise Exception('Please specify matrix')
    
    return self.GetClient().AddMatrix(self.key, panelId, matrix)

  def AddSamplingJob(self, panelId=None, job=None):
    """Add a sampling job to a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel the job will be added to (Example: p0000001).
      job
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.SamplingJob
        SamplingJob representing the job you want to add.
      Return Value
        Type: Int32
        Id of the added job.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if job is None:
      raise Exception('Please specify job')
    
    return self.GetClient().AddSamplingJob(self.key, panelId, job)

  def DeleteMatrix(self, panelId=None, matrixId=None):
    """Remove a matrix from a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel the matrix belongs to (Example: p0000001).
      matrixId
        Type: System.Int32
        Id of the matrix you want to remove.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrixId is None:
      raise Exception('Please specify matrixId')
    
    return self.GetClient().DeleteMatrix(self.key, panelId, matrixId)

  def DeleteSamplingJob(self, panelId=None, jobId=None):
    """Remove a sampling job from a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel the job belongs to (Example: p0000001).
      jobId
        Type: System.Int32
        Id of the job you want to remove.
    Return Value
      Type: Boolean
      True if the operation succeeds, false if the matrix could not be removed.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    
    return self.GetClient().DeleteSamplingJob(self.key, panelId, jobId)

  def DeleteSamplingJobRun(self, panelId=None, jobId=None, runNumber=None):
    """Deletes the specified run.
    Parameters
      key
        Type: System.String
        Security key.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
      runNumber
        Type: System.Int32
        Number that specifies the concrete job run.
    Return Value
      Type: Boolean
      If the operation succeed.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if runNumber is None:
      raise Exception('Please specify runNumber')

    return self.GetClient().DeleteSamplingJobRun(self.key, panelId, jobId, runNumber)

  def ExecuteJob(self, settings=None):
    """Execute a sampling job.
    Parameters
      key
        Type: System.String
        Key to validate user.
      settings
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.ExecutionSettings
        ExecutionSettings holding the settings for the execution of the sampling job. These settings include
    Return Value
      Type: Int64
      Id of the task that executes the job.
    """
    if settings is None:
      raise Exception('Please specify settings')
    
    return self.GetClient().ExecuteJob(self.key, settings)

  def GetLastSamplingJobRun(self, panelId=None, jobId=None):
    """Return the last run of the specified job.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
    Return Value
      Type: SamplingJobRunReport
      SamplingJobRunReport report on the last job run.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    
    return self.GetClient().GetLastSamplingJobRun(self.key, panelId, jobId)

  def GetMatrix(self, panelId=None, matrixId=None):
    """Return a SamplingMatrix from a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel the matrix belongs to (Example: p0000001).
      matrixId
        Type: System.Int32
        Id of the matrix you want to receive.
    Return Value
      Type: SamplingMatrix
      Object representing the matrix.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrixId is None:
      raise Exception('Please specify matrixId')
    
    return self.GetClient().GetMatrix(self.key, panelId, matrixId)

  def GetSamplingJob(self, panelId=None, jobId=None):
    """Return a SamplingJob from a panel based on the jobs id.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to (Example: p0000001).
      jobId
        Type: System.Int32
        Id of the job you want to get.
    Return Value
      Type: SamplingJob
      Object representing the job.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    
    return self.GetClient().GetSamplingJob(self.key, panelId, jobId)

  def GetSamplingJobByJobNumber(self, panelId=None, jobNumber=None):
    """Return a sampling job from a panel based on the jobs job number.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to (Example: p0000001).
      jobNumber
        Type: System.String
        Job Number of the job you want to get.
    Return Value
      Type: SamplingJob
      Object representing the job.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobNumber is None:
      raise Exception('Please specify jobNumber')
    
    return self.GetClient().GetSamplingJobByJobNumber(self.key, panelId, jobNumber)

  def GetSamplingJobRun(self, panelId=None, jobId=None, runNumber=None):
    """Return the specified run of the job.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
      runNumber
        Type: System.Int32
        Number tat specifies the concrete job run.
    Return Value
      Type: SamplingJobRunReport
      SamplingJobRunReport report on the specified job run.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if runNumber is None:
      raise Exception('Please specify runNumber')

    return self.GetClient().GetSamplingJobRun(self.key, panelId, jobId, runNumber)

  def GetSamplingJobRunNumberByTaskId(self, panelId=None, jobId=None, taskId=None):
    """Returns run number by specified task id.
    Parameters
      key
        Type: System.String
        Security key.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
      taskId
        Type: System.Int64
        Id of the task that was capable of the job execution.
    Return Value
      Type: Int32
      Run number.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if taskId is None:
      raise Exception('Please specify taskId')

    return self.GetClient().GetSamplingJobRunNumberByTaskId(self.key, panelId, jobId, taskId)

  def GetSurveyLinksStatus(self, panelId=None, jobId=None):
    """Returns external survey links of a job
    Parameters
      key
        Type: System.String
        Security key.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
    Return Value
      Type: SurveyLinksStatus
      An object representing links status (total links and available links).
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    
    return self.GetClient().GetSurveyLinksStatus(self.key, panelId, jobId)

  def RemoveSamplingJobRunFromPanel(self, panelId=None, jobId=None, runNumber=None):
    """Removes the specified run from the specified job.
    Parameters
      key
        Type: System.String
        Security key.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job.
      runNumber
        Type: System.Int32
        Number that specifies the concrete job run.
    Return Value
      Type: Int64
      Number of the task that proceeds removal of the panel
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if runNumber is None:
      raise Exception('Please specify runNumber')

    return self.GetClient().RemoveSamplingJobRunFromPanel(self.key, panelId, jobId, runNumber)

  def UpdateMatrix(self, panelId=None, matrix=None):
    """Update an existing matrix in a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel the matrix belongs to (Example: p0000001).
      matrix
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.SamplingMatrix
        SamplingMatrix representing the matrix you want to update.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if matrix is None:
      raise Exception('Please specify matrix')
    
    return self.GetClient().UpdateMatrix(self.key, panelId, matrix)

  def UpdateSamplingJob(self, panelId=None, job=None):
    """Update an existing sampling job in a panel.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to (Example: p0000001).
      job
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.SamplingJob
        SamplingJob representing the job you want to update.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if job is None:
      raise Exception('Please specify job')
    
    return self.GetClient().UpdateSamplingJob(self.key, panelId, job)

  def UploadSamplingJobRun(self, panelId=None, jobId=None, runNumber=None, settings=None):
    """Upload a sampling job run.
    Parameters
      key
        Type: System.String
        Key to validate user.
      panelId
        Type: System.String
        Id of the panel that job belongs to. (example: p1111111)
      jobId
        Type: System.Int32
        Id of the job you want to upload.
      runNumber
        Type: System.Int32
        Number of the run to be uploaded.
      settings
        Type: Firmglobal.Confirmit.Sampling.DataTransfer.UploadSettings
        UploadSettings holding the settings for the upload of the sampling job.
    Return Value
      Type: Int64
      Id of the Task that runs the job's upload.
    """
    if panelId is None:
      raise Exception('Please specify panelId')
    if jobId is None:
      raise Exception('Please specify jobId')
    if runNumber is None:
      raise Exception('Please specify runNumber')
    if settings is None:
      raise Exception('Please specify settings')

    return self.GetClient().UploadSamplingJobRun(self.key, panelId, jobId, runNumber, settings)
