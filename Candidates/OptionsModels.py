from Candidates.Model import Model

# (Root) ProductType with answers: {'a': 'Stocks', 'b': 'Options'}
# ├── (b) HistoricalUnderlyingAssetPriceAvailable with answers: {'a': 'Yes', 'b': 'No'}
# │   └── (a) Risk_FreeRateInfoAvailable with answers: {'a': 'Yes', 'b': 'No'}
# │       └── (a) UnderlyingAsset with answers: {'a': 'Stocks', 'b': 'Bonds or Swaps'}
# │           ├── (a) AdditionalUncertanties with answers: {'a': 'Yes', 'b': 'No'}      <---- This part is problematic
# │           │   └── (b) OptionType with answers: {'a': 'European', 'b': 'American'}
# │           │       └── (a) AssumeDividendsAreNotPaid with answers: {'a': 'Yes', 'b': 'No'}
# │           └── (b) AdditionalUncertanties with answers: {'a': 'Yes', 'b': 'No'}
# │               └── (b) OptionType with answers: {'a': 'European', 'b': 'American'}


MonteCarlo = Model(
    ModelID="MonteCarlo",
    ModelName="Monte Carlo Simulations",
    Attributes={"ProductType": "Options",
                "HistoricalUnderlyingAssetPriceAvailable": "Yes",
                "Risk_FreeRateInfoAvailable": "Yes",
                "FirmHasStableLeverage": "Yes"})

Lattice = Model(
    ModelID="Lattice",
    ModelName="Lattice models",
    Attributes={"ProductType": "Options",
                "HistoricalUnderlyingAssetPriceAvailable": "Yes",
                "Risk_FreeRateInfoAvailable": "Yes",
                "FirmHasStableLeverage": "Yes",
                "AdditionalUncertanties": "No",
                "OptionType": "American"})

B_n_SClassical = Model(
    ModelID="B_n_SClassical",
    ModelName="Black and Scholes Classical Models",
    Attributes={"ProductType": "Options",
                "HistoricalUnderlyingAssetPriceAvailable": "Yes",
                "Risk_FreeRateInfoAvailable": "Yes",
                "FirmHasStableLeverage": "Yes",
                "UnderlyingAsset": "Stocks",
                "AdditionalUncertanties": "No",
                "AssumeDividendsAreNotPaid": "Yes"})

B_n_SDivYield = Model(
    ModelID="B_n_SDivYield",
    ModelName="Black and Scholes Dividend Yield Models",
    Attributes={"ProductType": "Options",
                "HistoricalUnderlyingAssetPriceAvailable": "Yes",
                "Risk_FreeRateInfoAvailable": "Yes",
                "FirmHasStableLeverage": "Yes",
                "UnderlyingAsset": "Stocks",
                "AdditionalUncertanties": "No",
                "AssumeDividendsAreNotPaid": "No"})


def getOptionCandidatesFeature():
    return {MonteCarlo,
            Lattice,
            B_n_SClassical,
            B_n_SDivYield}
