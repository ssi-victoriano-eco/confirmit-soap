
class TransferForm:

  def __init__(self):
    #  Gets or sets the allChildrenFields value
    self.AllChildrenFields = None
    #  A property for collapsing the form fields to a bit string format
    self.BitString = None
    #  A property for retrieving and assigning the IsSystemVariable value
    self.IsSystemVariable = None
    #  A property for retrieving the Name of the form
    self.Name = None
    #  A property to specify the field value if all fields to collapse are null
    self.NullPadding = None
    #  A property for collapsing the form fields to a spread format
    self.Spread = None
    #  This property is used to specify the right padding of the output value if selected values are less than spread size (default is no padding)
    self.SpreadOutputPadding = None
    #  The size of the spread
    self.SpreadSize = None
    #  This property is used to specify the (left) padding of values that are less than SpreadWidth (default is ' ')
    self.SpreadValuePadding = None
    #  A property for retrieving the TransferFields
    self.TransferFields = None
