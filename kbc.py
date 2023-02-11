print("Welcome to the KBC Game Here You Can Earn Money")
questionList = ["1.Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?", "2.Ranthambore, Sariska and Keoladeo Ghana are all names of what?","3. India's official entry to Oscars 2021, 'Jallikattu' is, a film in which language?","4. In terms of production, which of these is the largest train coach manufacturing unit in the world?","5. In 2020, Louise Gluck won the Nobel Prize in which category?","6 .Which of the following companies was originally started as a loom manufacturing unit in 1909?","7. In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?"]
AnswerList = [4,1,4,3,3,1,2]
optionList = ["Virat Kohli","Sunil Gavaskar","VVS laxman","Rahul Dravid","National Parks","Goosebumps","Mountains","Rivers" ,"Hindi","Punjabi","Kannada","Malayalam","Integral Coach Factory, Bangalore"," Integral Coach Factory, Mumbai","Integral Coach Factory, Chennai","Integral Coach Factory, Kolkata","Music","Sports","Literature","Dance","Suzuki","CEAT", "Honda","Mercedes","Udit Narayan"," A. R. Rahman","Lata Mangeshkar","Raj Burman"]
i = 0
priceList = [1000,5000,10000,25000,50000,100000,1000000]
totalwining = 0
allAnswertrue = True
for x in range(len(priceList)):
    print("price of question ",priceList[x])
    print(questionList[x])
    print("option 1 ->" , optionList[i])
    i=i+1
    print("option 2 ->" , optionList[i])
    i=i+1
    print("option 3 ->" , optionList[i])
    i=i+1
    print("option 4 ->" , optionList[i])
    i=i+1
    uservalue = int(input("enter you Answer "))
    if(uservalue==AnswerList[x]):
        print("You Win " , priceList[x])
        totalwining+=priceList[x]
    else:
        print("You Loss")
        print("totla wining is " , totalwining)
        allAnswertrue = False
        break

if(allAnswertrue==True):
     print("totla wining is " , totalwining)


