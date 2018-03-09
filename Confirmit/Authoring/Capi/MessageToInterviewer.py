from MessageContent import MessageContent

class MessageToInterviewer:
    ''' Represents a message to a particular interviewer '''

    def __init__(self):
        # Content of this message
        self.Content = MessageContent()
        # The userid of the interviewer who this message will be sent to
        self.UserId = ''