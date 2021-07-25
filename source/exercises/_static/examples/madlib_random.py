import random


males = ["Rob", "Darius", "Clif", "Dane", "Monty", "Reggie", "Gus",
         "Vernon", "Maynard", "Gavin", "Ward", "Stefan", "Winfred"]	

females = ["Laurene", "Kathy", "Yoko", "Matilda", "Georgette", "Greta",
           "Meg", "Ruby", "Rikki", "Suzanne", "Dorine", "Elaine", "Frederica"]	

nouns = ["moment", "joy", "license", "race", "inertia", "molecule",
         "helicopter", "sweat", "blame", "brush", "art", "song", "liberty"]

 # past-tense verbs
verbs_pt = ["ground", "settled", "gave", "labeled", "restored", "washed",
            "sold", "arranged", "neglected", "accused", "confined"]

adjectives = ["overdue", "collapsed", "jealous", "topical", "naughty", "third", 
              "sharp", "electrical", "bogus", "warm", "cryptic", "hopeful", "alleged"]

adverbs = ["endlessly", "wholly", "mentally", "brightly", "willingly",
           "sweetly", "legitimately", "behind", "instead", "within"]

colors = ["red", "orange", "yellow", "blue", "purple", "green",
          "white", "black", "pink", "brown", "grey", "hazel"]	

numbers = ["one", "two", "three", "four", "five", "six", "seven"]

bodyparts_s = ["nose", "mouth", "ear", "hand", "stomach", "back", "shoulder", "hair", "spleen"]

bodyparts_pl = ["teeth", "legs", "arms", "ears", "eyes", "hands"]	

male = random.choice(males)
female = random.choice(females)
adj1 = random.choice(adjectives)
adj2 = random.choice(adjectives)
verb1 = random.choice(verbs_pt)
noun1 = random.choice(nouns)
number = random.choice(numbers)
color = random.choice(colors)
noun2 = random.choice(nouns)
bodypart = random.choice(bodyparts_pl)
verb2 = random.choice(verbs_pt)

print("One afternoon  {} and  {} were walking down a(n)  {} trail,".format(male, female, adj1))
print("looking for kindling for their campfire. The trees were  {} and".format(adj2))
print("green, and there were colorful wildflowers all around.  {} and  {}".format(male, female))
print("began to pick the wildflowers, and after a while, they  {} so far".format(verb1))
print("that they had wandered away from the trail." )

print("It started to get dark.  {} began to get worried, but  {} seemed".format(male, female))
print("excited to have an adventure. \"Look!\"  {} said. \"Do you see that".format(female))
print(" {}? It looks like a house!\"".format(noun1))

print("\"We're saved!\" cried  {}, who was relieved.".format(male))

print("Once they got closer,  {} felt very uneasy again. It didn't look like".format(male))
print("the cozy little cottage  {} had been imagining, but rather a big, spooky".format(male))
print("tower! It was about  {} feet tall, and it was covered with  {} ivy".format(number, color))
print("and moss. It was the creepiest thing  {} had ever seen!".format(male))

print(" {} said, \" {}, let's keep walking! There's no way I'm going into".format(male, female))
print("that tower! It looks haunted!\"" )

print("\"Don't be such a(n)  {}! We're going in. I think it looks perfectly".format(noun2))
print("un-haunted!\" said  {}.".format(female))

print(" {} was so scared that he could not open his eyes. He felt his  {}".format(male, bodypart))
print("chatter as  {} opened the door. All of a sudden,  {} felt that he was".format(female, male))
print("not alone. He opened his eyes, prepared to see the worst. But instead, he" )
print("saw all his friends and family inside the haunted tower! \"Surprise! Happy" )
print("birthday,  {}!\" they all  {}.".format(male, verb2))
