from Candidates.ModelBaseClass import ModelBaseClass

# (Root) ProductType with answers: {'a': 'Stocks', 'b': 'Options'}
# └── (a) DemandsDiscountRate with answers: {'a': 'Yes', 'b': 'No'}
#     ├── (a) CashFlowDataAvailable with answers: {'a': 'Yes', 'b': 'No'}
#     │   ├── (a) FirmHasStableLeverage with answers: {'a': 'Yes', 'b': 'No'}
#     │   └── (b) DemandsDividendPayoutToGrow with answers: {'a': 'Yes', 'b': 'No'}
#     │       └── (a) DemandsDividendPayoutToGrowAtConstantRate with answers: {'a': 'Yes', 'b': 'No'}
#     │           └── (b) DemandsMoreThanTwoGrowthStages with answers: {'a': 'Yes', 'b': 'No'}
#     └── (b) DistributesUnregularDividends with answers: {'a': 'Yes', 'b': 'No'}


# Stock Candidate Attributes
FreeCashFlowToEquityModels = ModelBaseClass(ModelID="FreeCashFlowToEquityModels",
                                            ModelName="Free Cash Flow To Equity Model Types",
                                            Attributes={"ProductType": "Stocks",
                                                        "DemandsDiscountRate": "Yes",
                                                        "CashFlowDataAvailable": "Yes",
                                                        "FirmHasStableLeverage": "Yes"})

CashFlowToTheFirmModels = ModelBaseClass(ModelID="CashFlowToTheFirmModels",
                                         ModelName="Cash Flow to the Firm Models",
                                         Attributes={"ProductType": "Stocks",
                                                     "DemandsDiscountRate": "Yes",
                                                     "CashFlowDataAvailable": "Yes",
                                                     "FirmHasStableLeverage": "No"})

ZeroGrowthModel = ModelBaseClass(ModelID="ZeroGrowthModel",
                                 ModelName="Zero Growth Model",
                                 Attributes={"ProductType": "Stocks",
                                             "DemandsDiscountRate": "Yes",
                                             "CashFlowDataAvailable": "No",
                                             "DemandsDividendPayoutToGrow": "No"})

GordonGrowthModel = ModelBaseClass(ModelID="GordonGrowthModel",
                                   ModelName="Gordon Growth Model",
                                   Attributes={"ProductType": "Stocks",
                                               "DemandsDiscountRate": "Yes",
                                               "CashFlowDataAvailable": "No",
                                               "DemandsDividendPayoutToGrow": "Yes",
                                               "DemandsDividendPayoutToGrowAtConstantRate": "Yes"})

ThreeStageDividendDiscountModel = ModelBaseClass(ModelID="ThreeStageDividendDiscountModel",
                                                 ModelName="Three Stage Dividend Discount Model",
                                                 Attributes={"ProductType": "Stocks",
                                                             "DemandsDiscountRate": "Yes",
                                                             "CashFlowDataAvailable": "No",
                                                             "DemandsDividendPayoutToGrow": "Yes",
                                                             "DemandsDividendPayoutToGrowAtConstantRate": "No",
                                                             "DemandsMoreThanTwoGrowthStages": "Yes"})

TwoStageDividendDiscountModel = ModelBaseClass(ModelID="TwoStageDividendDiscountModel",
                                               ModelName="Two Stage Dividend Discount Model",
                                               Attributes={"ProductType": "Stocks",
                                                           "DemandsDiscountRate": "Yes",
                                                           "CashFlowDataAvailable": "No",
                                                           "DemandsDividendPayoutToGrow": "Yes",
                                                           "DemandsDividendPayoutToGrowAtConstantRate": "No",
                                                           "DemandsMoreThanTwoGrowthStages": "No"})

DiscountedResidualIncomeModel = ModelBaseClass(ModelID="DiscountedResidualIncomeModel",
                                               ModelName="Discounted Residual Income Model",
                                               Attributes={"ProductType": "Stocks",
                                                           "DemandsDiscountRate": "No",
                                                           "DistributesUnregularDividends": "Yes"})

DiscountedAssetModel = ModelBaseClass(ModelID="DiscountedAssetModel",
                                      ModelName="Discounted Asset Model",
                                      Attributes={"ProductType": "Stocks",
                                                  "DemandsDiscountRate": "No",
                                                  "DistributesUnregularDividends": "No"})


def getStockCandidatesFeatures():
    return {FreeCashFlowToEquityModels,
            CashFlowToTheFirmModels,
            ZeroGrowthModel,
            GordonGrowthModel,
            ThreeStageDividendDiscountModel,
            TwoStageDividendDiscountModel,
            DiscountedResidualIncomeModel,
            DiscountedAssetModel}
