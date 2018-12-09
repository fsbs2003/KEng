QUESTION_PRODUCT = "Product"

class obtainCriteria:

    def __init__(self):
        self.type = type(self).__name__

    def nextQuestion(currentQuestion, answer):

        if currentQuestion == QUESTION_PRODUCT:
            nextQuestion = "End"
        else:
            nextQuestion = "Unknown"

        return nextQuestion

    def get_answer(currentQuestion, answer):

        switcherProduct = {
            1: "Stocks",
            2: "Options"
        }

        switcherQuestion = {
            "Product": switcherProduct.get(answer)
        }

        return switcherQuestion.get(currentQuestion)
