#
# Represents Candidate's base class, which associates a candidate
#   with the given attributes.
#

class Model(object):
    ModelID = "The Model's ID"
    ModelName = "The Name of the Model"
    Attributes = {"AttributeID": "Value"}

    def __init__(self, ModelID, ModelName, Attributes):
        self.ModelID = ModelID
        self.ModelName = ModelName
        self.Attributes = Attributes

