introvert_points=0 
extrovert_points=0
ambivert_points=0

answer1 = input("Do you prefer A being alone, B being in an big group of people, C with only people you are comfortable around")
if answer1 == "A":
    introvert_points += 1
elif answer1 == "B":
    extrovert_points
elif answer1 == "C":
    ambivert_points

answer2 = input("After several hours of social activity how do you typically feel? A Energized and ready for more,B Drained and needing quiet time alone to recharge,C Somewhere in the middle, or it depends on the situation/people.")
if answer2 == "A":
    extrovert_points += 1
elif answer2 == "B":
    introvert_points += 1
elif answer2 == "C":
    ambivert_points += 1

answer3 = input("How do you prefer to make plans for the weekend? A plan an active weekend full of social events and group outings, B  I prefer a quiet weekend at home, C A good weekend involves a mix of both  ")
if answer3 == "A":
     extrovert_points += 1
elif answer3 == "B":
    ambivert_points += 1
elif answer3 == "C":
    introvert_points += 1

answer4 = input("Do you play A team sport, B individual sport, C you excel in both")
if answer4 == "A":
    extrovert_points += 1
elif answer4 == "B":
    introvert_points += 1
elif answer4 == "C":
    ambivert_points += 1

answer5 = input("Do you A work in a library, B loud classroom, C cafe")
if answer5 == "A":
    introvert_points += 1
elif answer5 == "B":
    extrovert_points += 1
elif answer5 == "C":
    ambivert_points += 1

if ambivert_points >= introvert_points and ambivert_points >= extrovert_points:
    print("looks like your a person whose personality has a balance of extrovert and introvert features, a ambivert!.")
if introvert_points >= extrovert_points and introvert_points >= ambivert_points:
    print("you are a typically reserved or quiet person who tends to enjoys spending time alone introverts gain energy through solitude and quiet, a introvert!")
if extrovert_points >= ambivert_points and extrovert_points >= introvert_points:
    print("your personality is  a friendly person who enjoys talking to and being with other people, talking on the phone, and meeting new people. a extrovert!")