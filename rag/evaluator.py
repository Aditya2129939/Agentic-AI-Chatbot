def evaluate_response(question, answer, context):

    """
    Temporary evaluator
    Always returns high score
    """

    print("\n Evaluating Response...\n")

    return {
        "faithfulness": 1.0,
        "relevancy": 1.0
    }