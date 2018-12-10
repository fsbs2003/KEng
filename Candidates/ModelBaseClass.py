class ModelBaseClass(object):
    ModelID = "The Model's ID"
    ModelName = "The Name of the Model"
    Attributes = {"AttributeID": "Value"}

    def __init__(self, ModelID, ModelName, Attributes):
        self.ModelID = ModelID
        self.ModelName = ModelName
        self.Attributes = Attributes

