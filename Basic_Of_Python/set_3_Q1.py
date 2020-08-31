dict_for_Antonmy={"Destroy":"Create","Powerful":"Weak","Upset":"Relaxed","Divide":"Unite","Praise":"Criticism","Urge":"Deter","Drunk":"Sober","Private":"Public","Vacant":"Occupied","Expand":"Contract","Problem":"Solution","Vague":"Definite"}
def Antonomy(word1):
    #dict_for_Antonmy={"Destroy":"Create","Powerful":"Weak","Upset":"Relaxed","Divide":"Unite","Praise":"Criticism","Urge":"Deter","Drunk":"Sober","Private":"Public","Vacant":"Occupied","Expand":"Contract","Problem":"Solution","Vague":"Definite"}
    if word1 in dict_for_Antonmy.keys():
        for i in dict_for_Antonmy.keys():
            if word1==i:
                return dict_for_Antonmy[i]
    else:
        return 0

def main():
    print("In My Mind I have the Antonmy For these Words:",dict_for_Antonmy.keys())
    word=input("Give the Word So that I can Give U antonomy of that: ")
    print(word,"Antonomy of this word is:",Antonomy(word))
main()    