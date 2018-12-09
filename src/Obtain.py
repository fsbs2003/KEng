QUESTION_PRODUCT = "What is your product?"
QUESTION_DIVIDEND_DISCOUNT_RATE = "Is the Dividend Discount Rate Available ?"


class Obtain:

    def __init__(self):
        self.type = type(self).__name__

def nextQuestion(currentQuestion, answer):

    if currentQuestion == QUESTION_PRODUCT:
        nextQuestion = "End"
    else:
        nextQuestion = "Unknown"

    return nextQuestion

def translate_input_user2answer(currentQuestion, answer):

    switcherProduct = {
        "1": "Stocks",
        "2": "Options"
    }

    switcherYesNo = {
        "1": "Yes",
        "2": "No"
    }

    switcherQuestion = {
        QUESTION_PRODUCT: switcherProduct.get(answer),
        QUESTION_DIVIDEND_DISCOUNT_RATE: switcherYesNo.get(answer)
    }

    return switcherQuestion.get(currentQuestion)
