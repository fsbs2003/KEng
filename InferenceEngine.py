from Candidates import StockModels, OptionsModels
from KnowledgeBase import KnowledgeBaseTreeNode, getFirstAttribute, printTreeFromCurrentLocation


# ***********************INFERENCE ENGINE***************************** #
#                                                                      #
# This InferenceEngine.py represents the Inference engine which        #
# will Base its inferences on the knowledge base which is defined      #
# in  KnowledgeBase.py.   The specific inference steps are defined as  #
# Functions which will be called according to the Inference            #
# Model Defined in the project materials. The Logic is defined below   #
# the function definitions.                                            #
# ******************************************************************** #


def specify(current_node: KnowledgeBaseTreeNode, given_answer):
    """Specify Step

    :param current_node: the current concept in the knowledge base
    :param given_answer: the answer given from the previous iteration of the
                   specify->obtain loop
    :return:
    """

    # Find the Children for this particular node
    children_tuple = current_node.children

    # Return the Child that corresponds to the answer given in the
    #     previous obtain step
    if children_tuple.__len__() > 0:
        for var in children_tuple:
            # In order to select the correct child, make sure that it corresponds with
            #    the User's previous answer
            if var.requiredAnswer == given_answer:
                return var

    # If no Children are left, then there are no more attributes to
    #    Be collected
    else:
        return None


def obtain(Attribute: KnowledgeBaseTreeNode):
    """Obtain Step

    Obtains the value for the attribute given in the Specify Step
    :param Attribute:
    :return:
    """

    collected_answer = "No Answer"

    # Print the Question and collect an answer until a valid answer is given
    while collected_answer not in Attribute.answers:
        # 1) Print the question
        print(Attribute.question)
        # 2) Print the set of possible answers
        for answer in Attribute.answers:
            print("%s-%s" % (answer, Attribute.answers[answer]))
        collected_answer = input("Please enter a Valid input:")

    return collected_answer


def generate(current_attribute: KnowledgeBaseTreeNode, feature):
    """Generate Step

    Generates the set of possible candidates based on the initial feature given
    (where feature is an Attribute: Value Pair)
    :param current_attribute:
    :param feature:
    :return:
    """

    if current_attribute.answers[feature] == "Stocks":
        candidates = StockModels.getStockCandidatesFeatures()

    else:
        candidates = OptionsModels.getOptionCandidatesFeature()

    return candidates


def match(current_feature, candidate_set):
    """ Match Step

    Matches candidates to those that contain the given feature
    :param current_feature:  A key-value pair, where the key is the attribute, and the value is the given value
    :param candidate_set: Current Set of Valid Candidates
    :return:
    """

    # Get the key for the provided feature
    key = next(iter(current_feature))
    new_candidate_set = set()

    # TRUTH VALUE: Make sure the keys both exist and that the values correspond
    for candidate in candidate_set:
        if key in candidate.Attributes and candidate.Attributes[key] == current_feature[key]:
            new_candidate_set.add(candidate)

        elif key not in candidate.Attributes:
            new_candidate_set.add(candidate)

    return new_candidate_set


# ***************************** LOGIC ************************** #
#                                                                #
# The logic is based on the pruning based classification task    #
# type where initially, all candidates are considered, and the   #
# Range of possible candidates becomes smaller as more features  #
# are obtained.  The attributes of the candidates are compared   #
# with the attribute set collected from the user, and candidates #
# are pruned as the process goes further.  The candidates and    #
# Their attributes are defined in the Candicates Package.        #
# ************************************************************** #

# Defining the first relevant attribute to be considered
current_attribute = getFirstAttribute()

# DEBUG: Print the Knowledge Base Tree in its entirety
printTreeFromCurrentLocation(current_attribute)

# OBTAIN CRITERIA: Obtain the value for the attribute  in order to define a new feature
value_obtainted = obtain(current_attribute)
# GENERATE: generate the set of candidates based on the initial feature acquired
candidates = generate(current_attribute, value_obtainted)
feature_set = set()

while current_attribute is not None:
    # DEBUG: Print Candidates as you go
    print("*******************************************************************\n")
    print("\nGiven your previous answers, your potential candidates are:")
    if len(candidates) > 0:
        for candidate in candidates:
            print("* %s" % candidate.ModelName)

    else:
        print("*No Candidates fit the Criteria*")
    print("-------------------------------------------------------------------\n")

    # SPECIFY: Specify the next attribute to be considered based on the knowledge Base Tree
    current_attribute = specify(current_attribute, value_obtainted)

    if current_attribute is not None:
        # DEBUG: Print the Knowledge Base Tree from the current node
        printTreeFromCurrentLocation(current_attribute)
        # OBTAIN: Obtain the value of the selected attribute in order to form a feature
        value_obtainted = obtain(current_attribute)
        current_feature = {current_attribute.attributeName: current_attribute.answers[value_obtainted]}
        feature_set = feature_set.union(current_feature)
        # MATCH: Match the candidates to those that contain the current feature
        candidates = match(current_feature, candidates)

print("Your Model set is:")
if len(candidates) > 0:
    for candidate in candidates:
        print("* %s" % candidate.ModelName)

else:
    print("*No candidates fulfill the criteria*")
