# import nltk
import time
# from spellchecker import SpellChecker

# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))

"""
Suggest will work the following way:
    - Spellcheck 
    - Suggest queries that the user has searched before(personalization)
    - Trending searchs that are relevant to user's search
    - Queries that we can actually answer and have data on
"""

# Levenshtein Distance Algorithm implemented with Dynamic Programming
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]


testArr = ["Heloooo", "Helojaops", "ihaisd", "Helo", "jaoisjdj"]

# Using Edit Distance to show the closest query
def closestQuery(query):
    minDistance = edit_distance(query, testArr[0])
    closestQ = testArr[0]

    for i in range(1, len(testArr) - 1):
        if(edit_distance(query, testArr[i]) < minDistance):
            minDistance = edit_distance(query, testArr[i])
            closestQ = testArr[i]
    
    return closestQ

def trendingSearch():
    return "trending searches"

# Check spellings of queries and suggest corrections

def spellcheck(query):
    tokens = nltk.word_tokenize(query)
    spell = SpellChecker()
    spellQuery = ''
    for word in tokens:
        spellQuery += spell.correction(word) + " "
    return spellQuery



def suggest(query):
    json = {}
    json['spellcheck'] = spellcheck(query)
    json['closest-query'] = closestQuery(query)
    json['trending-searches'] = trendingSearch()
    return json

