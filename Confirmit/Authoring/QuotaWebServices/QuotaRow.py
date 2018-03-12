class QuotaRow:
    ''' Represents a row in the quota list '''

    def __init__(self):	
        # The counter
        self.Counter = 0
        # The field precodes
        self.FieldPrecodes = []
        self.LiveCounter = 0
        self.LiveTarget = 0
        # The quota row id
        self.QuotaRowId = 0
        # The target
        self.Target = 0
    
    def GetObjectData(self, info=None, context=None):
        ''' Parameters
        info
            Type: System.Runtime.Serialization.SerializationInfo

        context
            Type: System.Runtime.Serialization.StreamingContext
         '''

        if info is None:
            raise Exception('Please specify info')

        if context is None:
            raise Exception('Please specify context')
    
        return self.GetObjectData(info, context)