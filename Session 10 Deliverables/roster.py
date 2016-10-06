#professor. I don't know why my list doesn't append and remove the called students. 

roster = ["Beshansky",
          "Collins",
          "Fischer",
          "Giovanucci",
          "Jain",
          "Kim",
          "Lauture",
          "Lee",
          "Maddox",
          "Martinez",
          "Mendez",
          "Oh",
          "Petrone",
          "Posada",
          "Rule",
          "Schilb",
          "Tariq",
          "Wang",
          "Wolf"]
roster_completed =[]
import random

def call_three(roster):
    """
    print three names randomly
    roster: a list of strings
    """
    number_list = random.sample(range(1,len(roster)), 3)
    for number in number_list:
        print(roster[number])
        roster_completed.append(roster[number])
        roster.remove(roster[number])


call_three(roster)

