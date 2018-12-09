from src import Obtain
from src.models.stocks.GordonModel import GordonModel

NO_MORE_QUESTIONS = "No more questions"

def generate(product):
    if product == "Stocks":
        list_candidates = [GordonModel()]

    return list_candidates


def presentQuestionAnswers(presented_question):

    if presented_question == Obtain.QUESTION_DIVIDEND_DISCOUNT_RATE:
            print(Obtain.QUESTION_DIVIDEND_DISCOUNT_RATE)
            print("1 - Yes")
            print("2 - No")


def obtain_answer(curr_question):
    user_input = input('Enter your input:')
    reply_user = Obtain.translate_input_user2answer(curr_question, user_input)

    return reply_user


def specify(current_question, answer_given):

    next_question = NO_MORE_QUESTIONS

    if current_question == Obtain.QUESTION_PRODUCT:
        if answer_given == "Stocks":
            next_question = Obtain.QUESTION_DIVIDEND_DISCOUNT_RATE

    return next_question


def match(remCandidates, criteria, value):

    if criteria == Obtain.QUESTION_DIVIDEND_DISCOUNT_RATE:
        if value == "No":
            for candidate in remCandidates:
                if candidate.get_demands_discount_rate() == "Yes":
                    remCandidates.remove(candidate)


if __name__ == "__main__":

    # This is a list of key value pairs containing the values defined by the user for each relevant feature.
    features = {}

    currentQuestion = Obtain.QUESTION_PRODUCT

    print("Please answer the questions:")

    print(Obtain.QUESTION_PRODUCT)
    print("1 - Stocks")
    print("2 - Options")

    reply = input('Enter your input:')

    answer = Obtain.translate_input_user2answer(Obtain.QUESTION_PRODUCT, reply)

    features["productType"] = answer

    listOfCandidates = generate(features.get("productType"))

    remainingCandidates = listOfCandidates

    nextQuestion = specify(currentQuestion, answer)

    while nextQuestion != NO_MORE_QUESTIONS and len(remainingCandidates) > 0:
        question = nextQuestion
        presentQuestionAnswers(question)
        answer = obtain_answer(question)
        match(remainingCandidates, question, answer)
        nextQuestion = specify(question, answer)

    print("These are the suggested models:")

    for selected_candidate in remainingCandidates:
        print(selected_candidate.get_name())



