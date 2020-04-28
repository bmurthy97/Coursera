#Create a list called emotions that contains the first word of every line in emotion_words.txt.

filw = open("emotion_words.txt","r")
emotions = []
for i in filw.readlines():
    word = i.split()
    emotions.append(word[0])
print(emotions)
