from pathlib import Path
from textatistic import Textatistic
from nltk.tokenize import word_tokenize, sent_tokenize

ap = Path('apArt.txt')
reuters = Path('reutersArt.txt')
npr = Path('nprArt.txt')
fox = Path('foxArt.txt')

apRead = ap.read_text()
reutersRead = reuters.read_text()
nprRead = reuters.read_text()
foxRead = fox.read_text()

apReadability = Textatistic(apRead)
reutersReadability = Textatistic(reutersRead)
nprReadability = Textatistic(nprRead)
foxReadability = Textatistic(foxRead)

def avgGradeLevel(text):
    fks = text.fleschkincaid_score
    gfs = text.gunningfog_score
    ds = text.dalechall_score 
    avg = (fks + gfs + ds)/3
    print(f'\tFlesch-Kincaid Score: {fks:.2f}')
    print(f'\tGunning Fox Index Value: {gfs:.2f}')
    print(f'\tDale-Chall Score: {ds:.2f}')
    print(f'\tAverage Reading Grade Level: {avg:.2f}')

def wordStats(text, processedText):
    sentToken = len(sent_tokenize(text))
    wordToken = len(word_tokenize(text))
    charCount = processedText.char_count
    syblCount = processedText.sybl_count
    charAvg = charCount/wordToken
    syblAvg = syblCount/wordToken
    wps = wordToken/sentToken
    print(f'\tAverage Number of Words per Sentence: {wps:.2f}')
    print(f'\tAverage Number of Characters per Word: {charAvg:.2f}')
    print(f'\tAverage Number of Syllables per Word: {syblAvg:.2f}')

print('\nThis program demonstrates the use of NLP libraries to analyze news articles from various sources in terms of readability.')    
print('\nAP READABILITY')
avgGradeLevel(apReadability)
wordStats(apRead, apReadability)

print('\nREUTERS READABILITY')
avgGradeLevel(reutersReadability)
wordStats(reutersRead, reutersReadability)

print('\nNPR READABILITY')
avgGradeLevel(nprReadability)
wordStats(nprRead, nprReadability)

print('\nFOX NEWS READABILITY')
avgGradeLevel(foxReadability)
wordStats(foxRead, foxReadability)
