"""Happy Independence Day Jamaica
culture lowered force
Red impact affected brilliant
happy love counting

Happy Independence Day Jamaica
culture conceived force
Red impact affected trending
able see dance


"""




import twitter
import private
import nltk	
from nltk.corpus import wordnet
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import random
import subprocess
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
import sys


#11 hours


# Set access variables from private.py
api = twitter.Api(consumer_key=private.consumer_key,
        consumer_secret=private.consumer_secret,
        access_token_key = private.access_token,
        access_token_secret = private.access_token_secret)

# Location code
woeid = 23424977 # United States

# Get the first trend for location code
trends = api.GetTrendsWoeid(woeid)

for trend in trends[0:1]:
  a=trend.name
  print "--------------------------"
  print "The top trend:"+a	
  print "--------------------------"
  
print "THE HAIKU\n"

#Getting the tweets
words=[] 
#result=api.GetSearch(a, count=100)
result=api.GetSearch(a, count=50)

string=""
for r in result:
  string=string+" "+r.text
raw_data=nltk.word_tokenize(string)


#Filtering English words from the tweets
meaningful_words=[]

single_letters=["i","I"]
for i in raw_data:
  if (wordnet.synsets(i)):
    meaningful_words.append(i)

for i in meaningful_words:
  if len(i)==1 and (i not in single_letters):
    meaningful_words.remove(i)
  



#part of speech
text=word_tokenize(' '.join(meaningful_words))
text_grammar=nltk.pos_tag(text)
part_of_speech={}
for i in text_grammar:
  part_of_speech[i[0]]=i[1]



#get_syllable function
d = cmudict.dict() 
def get_syllable(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

#Creating data structure(dictionary)
data_structure={}

for i in meaningful_words:
  try:
    if i not in data_structure and i.isalpha():
      data_structure[i]=get_syllable(i)[0]
  except:
    a="error"


#print data_structure

#Making haiku

haiku=""
one_syllable=[]
two_syllable=[]
three_syllable=[]
four_syllable=[]
five_syllable=[]
six_syllable=[]
seven_syllable=[]
for i in data_structure:
    if data_structure[i]==1:
      one_syllable.append(i)    
    if data_structure[i]==2:
      two_syllable.append(i)
    if data_structure[i]==3:
      three_syllable.append(i)
    if data_structure[i]==4:
      four_syllable.append(i)
    if data_structure[i]==5:
      five_syllable.append(i)
    if data_structure[i]==6:
      six_syllable.append(i)
    if data_structure[i]==7:
      seven_syllable.append(i)
    
    
def random_number(syllable):
    return random.randint(0,len(syllable)-1)
    

"""
#randomize and print haikus


first=two_syllable[random_number(two_syllable)]+" "+two_syllable[random_number(two_syllable)]+" "+one_syllable[random_number(one_syllable)]
second=two_syllable[random_number(two_syllable)]+" "+three_syllable[random_number(three_syllable)]+" "+two_syllable[random_number(two_syllable)]
third=one_syllable[random_number(one_syllable)]+" "+three_syllable[random_number(three_syllable)]+" "+one_syllable[random_number(one_syllable)]
"""

#synonyms
#print all the synset element of an element
def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names:
            syn_set.append(item)
    return syn_set

#haiku

#1
try:
  first_1=[x for x in two_syllable if (part_of_speech[x]=="NN")][0]
  two_syllable.remove(first_1)
except:
  first_1="Harry"

try:
  first_2=[x for x in two_syllable if (part_of_speech[x]=="VBN")][0]
  two_syllable.remove(first_2)
except:
  first_2="lowered"

try:
  first_3=[x for x in one_syllable if part_of_speech[x]=="NN"][0]
  one_syllable.remove(first_3)
except:
  first_3="hat"

print first_1+" "+first_2+" "+first_3

#2
try:
  second_1=[x for x in one_syllable if part_of_speech[x]=="JJ"][0]
  one_syllable.remove(second_1)
except:
  second_1="Red"

try:
  second_2=[x for x in two_syllable if part_of_speech[x]=="NN"][0]
  two_syllable.remove(second_2)
except:
  second_2="Influence"

try:
  second_3=[x for x in two_syllable if part_of_speech[x]=="VBP"][0]
  two_syllable.remove(second_3)
except:
  second_3="affected"

try:
  second_4=[x for x in two_syllable if part_of_speech[x]=="NN"][0]
  two_syllable.remove(second_4)
except:
  second_4="rapidly"

print second_1+" "+second_2+" "+second_3+" "+second_4


#3
try:
  third_1=[x for x in two_syllable if part_of_speech[x]=="NN"][0]
  two_syllable.remove(third_1)
except:
  third_1="Music"

try:
  third_2=[x for x in one_syllable if part_of_speech[x]=="VBG"][0]
  one_syllable.remove(third_2)
except:
  third_2="caused"

try:
  third_3=[x for x in two_syllable if part_of_speech[x]=="NN"][0]
  two_syllable.remove(third_3)
except:
  third_3="harmony"

print third_1+" "+third_2+" "+third_3

#print +"marries"+

haiku= first_1+" "+first_2+" "+first_3+" "+second_1+" "+second_2+" "+second_3+" "+second_4+" "+third_1+" "+third_2+" "+third_3
#print haiku


#speaking
def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

print "\n"

a = haiku
b = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a
execute_unix(b)



