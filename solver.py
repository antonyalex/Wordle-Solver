from data import total_words
import math
from data import all_word_colour_possibilities
def word_filter(word_details,wordlist): 
    filtered_list=list(wordlist) 
    for i in range(5):
        if word_details[i]['Colour']=="Grey":
            filtered_list=[word for word in filtered_list if word_details[i]['Letter'] not in word]
        if word_details[i]['Colour']=="Yellow":
            filtered_list=[x for x in filtered_list if word_details[i]["Letter"] in x and word_details[i]["Letter"] not in x[i]]
        if word_details[i]['Colour']=="Green":
            filtered_list=[x for x in filtered_list if word_details[i]["Letter"] in x[i]]

    return(filtered_list)

def all_colour_possibilities(word):
    word_letters=[i for i in word]
    possibilities=[]
    for j in range(len(all_word_colour_possibilities)):
        linked_word_colour={}
        for i in range(5):
            linked_word_colour[i]={"Letter":word_letters[i],"Colour":all_word_colour_possibilities[j][i]}
        possibilities.append(linked_word_colour)
    return possibilities

def entropy_calc(word,wordlist):
    entropy=0
    all_possibilities=all_colour_possibilities(word)
    for i in all_possibilities:
        probability=len(word_filter(i,wordlist))/len(wordlist)
        if probability==0:
            continue
        else:
            I=math.log2(1/probability)
            entropy=entropy+(probability*I)
    return(entropy)


word_list=total_words
for i in range(5):
    a=dict()
    b=input("Enter Word")
    c=input("Enter Colours(G for Green,Y for Yellow,B for Black)")
    if c=="GGGGG":
        print("Success")
        break
    print("Please Wait,this takes a few moments:")
    d=list(b)
    e=list(c)
    for j in range(len(d)):
        if e[j].lower()=="G":
            a[j]={'Letter': d[j], 'Colour': "Green"}
        elif e[j].lower()=="Y":
            a[j]={'Letter': d[j], 'Colour': "Yellow"}
        else:
            a[j]={'Letter': d[j], 'Colour': "Grey"}
    f=word_filter(a,word_list)
    word_list=f
    g=[]
    for i in f:
        g.append(entropy_calc(i,f))
    h=f[g.index(max(g))]
    print("Ideal Word is:",h)








