#textblob library
#create a sample text
#let import TextBlob over here in the app
from textblob import TextBlob

texts = [
    "I love NLP, It's work great and I'm very satisfied.",
    "This my first experence on doing sentiment analysis , I am little bit disappointed",
    "The NLP sentiment analysis is quiet intreseting it is neither good  or bad"
]

# Create function to do the sentiment analysis
def analyse_sentiment(text):
    analysis = TextBlob(text)
    #-1.0 - 1.0 polarity score
    polarity = analysis.sentiment.polarity
    if polarity>0:
        sentiment= "Positive"
    elif polarity<0:
        sentiment= "Negative"
    else:
        sentiment= "Neutral"
    return sentiment

for text in texts:
    sentiment = analyse_sentiment(text)
    print(f"Text:{text}")
    print(f"Sentiment:{sentiment}\n")