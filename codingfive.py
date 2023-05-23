"""In this section we are going to learn recursvity with simple condiotionals"""

def calif():
    """Howarts Gate"""
    print("You can only enter values between 0 to 100")
    score = int(input("What is the score: ").title())
    if score >= 90 and score <= 100:
        print("Take your sock Dobby, go to Kyoto".title())
    elif score >= 85 and score < 90:
        print("ask Dumbledore if go to Gryffindor to get better".capitalize())
    elif score >= 80 and score < 85:
        print ("9 3/4 is your gate, take another year Dobby".capitalize())
    elif score >= 70 and score < 80:
        print ("you should study".capitalize())
    else:
        print ("wabi sabi")
calif()
        