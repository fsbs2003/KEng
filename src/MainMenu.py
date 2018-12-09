from src import obtainCriteria

if __name__ == "__main__":



    print("Please answer the questions:")

    print("What is the product type ?")
    print("1 - Stocks")
    print("2 - Options")

    reply = input('Enter your input:')

    ans = obtainCriteria.get_answer(obtainCriteria.QUESTION_PRODUCT, reply)
    nextQuestion = obtainCriteria.nextQuestion(obtainCriteria.QUESTION_PRODUCT, ans)

    while nextQuestion != "End":
        nextQuestion = obtainCriteria.nextQuestion(nextQuestion, ans)




