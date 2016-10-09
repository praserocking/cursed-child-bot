from chatterbot import ChatBot
import sys

chatbot = ChatBot(
    'Prasanna',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    silence_performance_warning=True
)

print "Started training!"
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")


# Get a response to an input statement
print "done"

print chatbot.get_response("harry potter")

