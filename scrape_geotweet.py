import twython
import random

words = []
joined = " "

#access_codes
api_key = #put yours
api_secret = #put yours
access_token = #put yours
token_secret = #put yours
twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

#search parameters
choice = raw_input("default or new radius or new: ")
if choice == "default":
    lat = str(37.799506)
    lon = str(-122.266104)
    radius = str(2)
    tweet_type = "recent"
if choice == "new radius":
    lat = str(37.799506)
    lon = str(-122.266104)
    radius = raw_input("radius in miles: ")
    tweet_type = "recent"
if choice == "new":
    lat = raw_input("lat: ")
    lon = raw_input("lon: ")
    radius = raw_input("radius in miles: ")
    tweet_type = raw_input("popular or recent: ")
geocount = raw_input("count (<100): ")

#extractor functions:
#geo-search general
def geo_search_gen():
    response = twitter.search(result_type=tweet_type, count=geocount, geocode=lat+','+lon+','+radius+'mi')
    print "\n".join([r['text'] for r in response['statuses']])
#geo-search w/specific term
def geo_search_spef(term):
    response = twitter.search(q=term, result_type=tweet_type, count=geocount, geocode=lat+','+lon+','+radius+'mi')
    print "\n".join([r['text'] for r in response['statuses']])

#loop
loop = 1
while loop == 1:

    #input system
    input = raw_input("analyze: ")

    #analyzer
    if input == "":
        geo_search_gen()
    if input != "":
        geo_search_spef(input)

    #adder
    final_input = raw_input("select: ")
    words.append(final_input)

    #shower
    print words

    #exiter
    if input == "  ":
        print " "
        print " ".join(words)
        print " "
        loop = 0
