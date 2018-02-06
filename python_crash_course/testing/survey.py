from collections import Counter


class AnonymousSurvey():
    """Collect anonymous answers to survey questions"""

    def __init__(self, question):
        """Store questions and prepare to store responses"""
        self.question = question
        self.responses = list()

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the reponses that have been given"""
        print("Survey Results: \n")
        responses_counter = Counter(self.responses)
        for response, count in responses_counter.items():
                print('- ' + response + ' : ' + str(count))