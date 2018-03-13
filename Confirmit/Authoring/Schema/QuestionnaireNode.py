from Node import Node
from datetime import datetime

class QuestionnaireNode(Node):
    def __init__(self):
        self.Deleted = False
        self.VersionTimestamp = datetime.today()