import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('2wvOXhkMg7NRUGq1EGk9dAoQCU4UO804uJoI46ZLwfo')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self, text):
        paralleldots.ner(text)

    def emotion_prediction(self, text):
        paralleldots.emotion(text)