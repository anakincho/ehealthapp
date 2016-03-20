__author__ = 'Nikolay'

from textstat.textstat import textstat
from textblob import TextBlob

def fleschScore(data):

    # For some reason the textstat works for sentences or strings
    # longer than 3 words and if its less it gives that error
    # but the documents are quite large in text so it wont be a problem
    # but for safety reasons we catch the error and give 0
    try:
        readingScore = textstat.flesch_reading_ease(data)
    except TypeError:
        readingScore = 0.0
    return readingScore

def subjectivityScore(data):

    #Create a textblob with the given text
    blob = TextBlob(data)

    #fetch the subjectivity score for that text
    subScore = blob.sentiment.subjectivity

    return subScore

def polarityScore(data):

    #Create a textblob with the given text
    blob = TextBlob(data)

    #fetch the polarity score for that text
    polScore = blob.sentiment.polarity

    return polScore
