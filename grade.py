print("CHECK YOUR SCORE HERE")
username=input("username :")
print("\nwelcome", username)
score=int(input("INPUT YOUR SCORE:"))
if score>=70:
    print(username,"score is", score, "hence", username, "gets A")
elif score>=60 and score<=69:
    print(username, "score is", score, "hence",username, "gets B")
elif score>=55 and score<=59:
    print(username, "score is", score, "hence",username, "gets C")
elif score>=50 and score<=55:
    print(username, "score is", score, "hence",username, "gets D")
elif score>=45 and score<=49:
    print(username,"score is", score, "hence", username, "gets E")
else:

    print(username,"score is", score,"hence", username,"gets F")
          
