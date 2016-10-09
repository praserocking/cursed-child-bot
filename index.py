from chatterbot import ChatBot
import sys
import time

chatbot = ChatBot(
    'Prasanna',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    silence_performance_warning=True
)

start = int(round(time.time() * 1000))
print "Started training!"
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")


# Get a response to an input statement
end = int(round(time.time() * 1000))
print "done"
print "time taken = " + str((end-start)/1000) + " secs"

while True:
	print "enter your chat: "
	inp = sys.stdin.readline()
	print "starting to search"
	start = int(round(time.time() * 1000))
	print chatbot.get_response(inp)
	end = int(round(time.time() * 1000))
	print "time taken = " + str((end-start)/1000) + " secs"

