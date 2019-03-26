print("hello , what is your name ")
name = input()
question_et_reponse ={'question1':["quelle est la capitale politique de la cote d ivoire ?","yamoussokro"],
'question2':["quelle nombre de point doit on avoir pour etre admin au BAC en Cote d ivoire ?","200"]}
print("good morning {}".format(name))


verification = input("veux tu jour un quiz avec moi O | N: \n ")


while verification=="O":

    print("Allez c\'est parti: premier question")
    reponse =input(question_et_reponse['question1'][0])
    if reponse == question_et_reponse['question1'][1]:
        print("bravoo bonne repose")
    else:
        print("mauvaise reponse!!!\n" + "la bonne reponse etait: " + question_et_reponse['question1'][1] )
    verification = input("veux tu jour un quiz avec moi O | N ")

print("a bientot portez vous bien")
