from anytree import NodeMixin, AnyNode, RenderTree
from Candidates.ModelBaseClass import ModelBaseClass
from Candidates import StockModels, OptionsModels


#
# This is a definition of a knowledge Attribute.  It contains the
#       Relevant output to be given during the obtain step and the
#       Valid answers for this question.
#
class KnowledgeAttributeBase(object):
    attributeName = "AttributeID"
    question = "Question to be asked on the Obtain Step"
    answers = {"key": "answer value"}
    requiredAnswer = "Answer at Parent node that is necessary to reach this node"


class KnowledgeAttributeNode(KnowledgeAttributeBase, NodeMixin):
    def __init__(self, attributeName, question, answers, requiredAnswer="Root", isLeaf=False, parent=None):
        super(KnowledgeAttributeBase, self).__init__()
        self.attributeName = attributeName
        self.question = question
        self.answers = answers
        self.requiredAnswer = requiredAnswer
        self.parent = parent
        self.isLeaf = isLeaf


ProductType = KnowledgeAttributeNode(
    attributeName="ProductType",
    question="What type of product do you want to model?",
    answers={"a": "Stocks", "b": "Options"})

HistoricalUnderlyingAssetPriceAvailable = KnowledgeAttributeNode(
    parent=ProductType,
    requiredAnswer="b",
    attributeName="HistoricalUnderlyingAssetPriceAvailable",
    question="Are the historical Underlying Asset Prices available?",
    answers={"a": "Yes", "b": "No"})

Risk_FreeRateInfoAvailable = KnowledgeAttributeNode(
    parent=HistoricalUnderlyingAssetPriceAvailable,
    requiredAnswer="a",
    attributeName="Risk_FreeRateInfoAvailable",
    question="Is the risk free rate available?",
    answers={"a": "Yes", "b": "No"})

UnderlyingAsset = KnowledgeAttributeNode(
    parent=Risk_FreeRateInfoAvailable,
    requiredAnswer="a",
    attributeName="UnderlyingAsset",
    question="What is the underlying asset?",
    answers={"a": "Stocks", "b": "Bonds or Swaps"})

AdditionalUncertantiesStocks = KnowledgeAttributeNode(
    parent=UnderlyingAsset,
    requiredAnswer="a",
    attributeName="AdditionalUncertanties",
    question="Are there additional uncertanties?",
    answers={"a": "Yes", "b": "No"})

AdditionalUncertantiesBondsOrSwaps = KnowledgeAttributeNode(
    parent=UnderlyingAsset,
    requiredAnswer="b",
    attributeName="AdditionalUncertanties",
    question="Are there additional uncertanties?",
    answers={"a": "Yes", "b": "No"})

OptionTypeStock = KnowledgeAttributeNode(
    parent=AdditionalUncertantiesStocks,
    requiredAnswer="b",
    attributeName="OptionType",
    question="What is the option type ?",
    answers={"a": "European", "b": "American"})

OptionTypeBondsOrSwaps = KnowledgeAttributeNode(
    parent=AdditionalUncertantiesBondsOrSwaps,
    requiredAnswer="b",
    attributeName="OptionType",
    question="What is the option type ?",
    answers={"a": "European", "b": "American"})

AssumeDividendsAreNotPaid = KnowledgeAttributeNode(
    parent=OptionTypeStock,
    requiredAnswer="a",
    attributeName="AssumeDividendsAreNotPaid",
    question="Is it assumed that Dividends are not paid ?",
    answers={"a": "Yes", "b": "No"})



DemandsDiscountRate = KnowledgeAttributeNode(
    attributeName="DemandsDiscountRate",
    parent=ProductType,
    requiredAnswer="a",
    question="Do you have a discount rate calculated?",
    answers={"a": "Yes", "b": "No"})

CashFlowDataAvailable = KnowledgeAttributeNode(
    attributeName="CashFlowDataAvailable", parent=DemandsDiscountRate,
    requiredAnswer="a",
    question="Is there cash flow data available?",
    answers={"a": "Yes", "b": "No"})

DistributesUnregularDividends = KnowledgeAttributeNode(
    attributeName="DistributesUnregularDividends", parent=DemandsDiscountRate,
    requiredAnswer="b",
    question="Does the company Pay Out Dividends Unregularly?",
    answers={"a": "Yes", "b": "No"})

FirmHasStableLeverage = KnowledgeAttributeNode(
    attributeName="FirmHasStableLeverage",
    parent=CashFlowDataAvailable,
    requiredAnswer="a",
    question="Does the company have a stable/ moderate amount of leverage?",
    answers={"a": "Yes", "b": "No"}
)

DemandsDividendPayoutToGrow = KnowledgeAttributeNode(
    attributeName="DemandsDividendPayoutToGrow",
    parent=CashFlowDataAvailable,
    requiredAnswer="b",
    question="Is the company expected to grow at some period "
             "in the future?",
    answers={"a": "Yes", "b": "No"})

DemandsDividendPayoutToGrowAtConstantRate = KnowledgeAttributeNode(
    attributeName="DemandsDividendPayoutToGrowAtConstantRate",
    parent=DemandsDividendPayoutToGrow,
    requiredAnswer="a",
    question="Is it safe to assume that the company's growth will remain constant?",
    answers={"a": "Yes", "b": "No"})

DemandsMoreThanTwoGrowthStages = KnowledgeAttributeNode(
    attributeName="DemandsMoreThanTwoGrowthStages",
    parent=DemandsDividendPayoutToGrowAtConstantRate,
    requiredAnswer="b",
    question="Are there more than 2 stages of growth for the dividend payout in this company?",
    answers={"a": "Yes", "b": "No"})


def specify(current_node: KnowledgeAttributeNode, given_answer):
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
            if var.requiredAnswer == given_answer:
                return var

    # If no Children are left, then there are no more attributes to
    #    Be collected
    else:
        return None


def obtain(Attribute: KnowledgeAttributeNode):
    """Obtain Step

    Obtains the value for the attribute given in the Specify Step
    :param Attribute:
    :return:
    """

    collected_answer = "No Answer"

    # Print the Question and collect an answer until a valid answer is given
    while collected_answer not in Attribute.answers:
        print(Attribute.question)
        for answer in Attribute.answers:
            print("%s-%s" % (answer, Attribute.answers[answer]))
        collected_answer = input("Please enter a Valid input:")

    # Return the User's Given Answer
    feature = {Attribute.attributeName: Attribute.answers[collected_answer]}

    return collected_answer


def generate(current_attribute: KnowledgeAttributeNode, feature):
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


# DEBUG: Print the Knowledge Base Tree
# for pre, _, node in RenderTree(ProductType):
#     if node.isLeaf is True:
#         print("%s(%s) [Leaf] %s with answers: %s " % (pre, node.requiredAnswer, node.attributeName, node.answers))
#     else:
#         print("%s(%s) %s with answers: %s" % (pre, node.requiredAnswer, node.attributeName, node.answers))
#
# print("You are currently in ProductType: {Stock, Options}")

# Defining the first attribute
current_attribute = ProductType
# Obtain the value for the Attribute
value_obtainted = obtain(current_attribute)
# Generate Step
candidates = generate(current_attribute, value_obtainted)
feature_set = set()

while current_attribute is not None:
    # SPECIFY the current attribute based on the knowledge Base
    current_attribute = specify(current_attribute, value_obtainted)

    if current_attribute is not None:
        # OBTAIN the value of the attribute in order to form a feature
        value_obtainted = obtain(current_attribute)
        current_feature = {current_attribute.attributeName: current_attribute.answers[value_obtainted]}
        feature_set = feature_set.union(current_feature)
        # MATCH the candidates to those that contain the current feature
        candidates = match(current_feature, candidates)


print("Your Model set is:")
for candidate in candidates:
    print(candidate.ModelName)
