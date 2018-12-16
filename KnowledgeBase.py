from anytree import NodeMixin, AnyNode, RenderTree
from Candidates.Model import Model



class TreeNodeAttributes(object):
    """
    This is a definition of a knowledge Attribute.  It contains the
    Relevant output to be given during the obtain step and the
    Valid answers for this question.
    """
    attributeName = "AttributeID"
    question = "Question to be asked on the Obtain Step"
    answers = {"key": "answer value"}
    requiredAnswer = "Answer at Parent node that is necessary to reach this node"


class KnowledgeBaseTreeNode(TreeNodeAttributes, NodeMixin):
    def __init__(self, attributeName, question, answers, requiredAnswer="Root", isLeaf=False, parent=None):
        super(TreeNodeAttributes, self).__init__()
        self.attributeName = attributeName
        self.question = question
        self.answers = answers
        self.requiredAnswer = requiredAnswer
        self.parent = parent
        self.isLeaf = isLeaf


ProductType = KnowledgeBaseTreeNode(
    attributeName="ProductType",
    question="What type of product do you want to model?",
    answers={"a": "Stocks", "b": "Options"})

HistoricalUnderlyingAssetPriceAvailable = KnowledgeBaseTreeNode(
    parent=ProductType,
    requiredAnswer="b",
    attributeName="HistoricalUnderlyingAssetPriceAvailable",
    question="Are the historical Underlying Asset Prices available?",
    answers={"a": "Yes", "b": "No"})

Risk_FreeRateInfoAvailable = KnowledgeBaseTreeNode(
    parent=HistoricalUnderlyingAssetPriceAvailable,
    requiredAnswer="a",
    attributeName="Risk_FreeRateInfoAvailable",
    question="Is the risk free rate available?",
    answers={"a": "Yes", "b": "No"})

UnderlyingAsset = KnowledgeBaseTreeNode(
    parent=Risk_FreeRateInfoAvailable,
    requiredAnswer="a",
    attributeName="UnderlyingAsset",
    question="What is the underlying asset?",
    answers={"a": "Stocks", "b": "Bonds or Swaps"})

AdditionalUncertantiesStocks = KnowledgeBaseTreeNode(
    parent=UnderlyingAsset,
    requiredAnswer="a",
    attributeName="AdditionalUncertanties",
    question="Are there additional uncertanties?",
    answers={"a": "Yes", "b": "No"})

AdditionalUncertantiesBondsOrSwaps = KnowledgeBaseTreeNode(
    parent=UnderlyingAsset,
    requiredAnswer="b",
    attributeName="AdditionalUncertanties",
    question="Are there additional uncertanties?",
    answers={"a": "Yes", "b": "No"})

OptionTypeStock = KnowledgeBaseTreeNode(
    parent=AdditionalUncertantiesStocks,
    requiredAnswer="b",
    attributeName="OptionType",
    question="What is the option type ?",
    answers={"a": "European", "b": "American"})

OptionTypeBondsOrSwaps = KnowledgeBaseTreeNode(
    parent=AdditionalUncertantiesBondsOrSwaps,
    requiredAnswer="b",
    attributeName="OptionType",
    question="What is the option type ?",
    answers={"a": "European", "b": "American"})

AssumeDividendsAreNotPaid = KnowledgeBaseTreeNode(
    parent=OptionTypeStock,
    requiredAnswer="a",
    attributeName="AssumeDividendsAreNotPaid",
    question="Is it assumed that Dividends are not paid ?",
    answers={"a": "Yes", "b": "No"})

DemandsDiscountRate = KnowledgeBaseTreeNode(
    attributeName="DemandsDiscountRate",
    parent=ProductType,
    requiredAnswer="a",
    question="Do you have a discount rate calculated?",
    answers={"a": "Yes", "b": "No"})

CashFlowDataAvailable = KnowledgeBaseTreeNode(
    attributeName="CashFlowDataAvailable", parent=DemandsDiscountRate,
    requiredAnswer="a",
    question="Is there cash flow data available?",
    answers={"a": "Yes", "b": "No"})

DistributesUnregularDividends = KnowledgeBaseTreeNode(
    attributeName="DistributesUnregularDividends", parent=DemandsDiscountRate,
    requiredAnswer="b",
    question="Does the company Pay Out Dividends Unregularly?",
    answers={"a": "Yes", "b": "No"})

FirmHasStableLeverage = KnowledgeBaseTreeNode(
    attributeName="FirmHasStableLeverage",
    parent=CashFlowDataAvailable,
    requiredAnswer="a",
    question="Does the company have a stable/ moderate amount of leverage?",
    answers={"a": "Yes", "b": "No"}
)

DemandsDividendPayoutToGrow = KnowledgeBaseTreeNode(
    attributeName="DemandsDividendPayoutToGrow",
    parent=CashFlowDataAvailable,
    requiredAnswer="b",
    question="Is the company expected to grow at some period "
             "in the future?",
    answers={"a": "Yes", "b": "No"})

DemandsDividendPayoutToGrowAtConstantRate = KnowledgeBaseTreeNode(
    attributeName="DemandsDividendPayoutToGrowAtConstantRate",
    parent=DemandsDividendPayoutToGrow,
    requiredAnswer="a",
    question="Is it safe to assume that the company's growth will remain constant?",
    answers={"a": "Yes", "b": "No"})

DemandsMoreThanTwoGrowthStages = KnowledgeBaseTreeNode(
    attributeName="DemandsMoreThanTwoGrowthStages",
    parent=DemandsDividendPayoutToGrowAtConstantRate,
    requiredAnswer="b",
    question="Are there more than 2 stages of growth for the dividend payout in this company?",
    answers={"a": "Yes", "b": "No"})


def getFirstAttribute():
    """
    Function to be called in order to Specify the First relevant Attribute

    :return: First Attribute int the knowledge Base Tree
    """
    return ProductType


def printTreeFromCurrentLocation(target_node):
    """
    Function to print the tree starting from the current Location

    :return:
    """
    print("The Specify Step will be based on this Tree:\n\n")

    for pre, _, node in RenderTree(target_node):
        if node.isLeaf is True:
            print("    %s(%s) [Leaf] %s with answers: %s " % (pre, node.requiredAnswer, node.attributeName, node.answers))
        else:
            print("    %s(%s) %s with answers: %s" % (pre, node.requiredAnswer, node.attributeName, node.answers))

    print("\n\n*******************************************************************\n\n")


