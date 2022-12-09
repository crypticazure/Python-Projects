"""This program is used to create clickbait-style headlines from a Mad Libs-style template."""

import random

#Set up the constants
OBJECT_PRONOUNS = ["Her", "His", "Their"]
POSSESSIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
STATES = ["California", "Texas", "Hawaii", "Utah", "Arizona", "Colorado", "Florida", "Indiana", "Alaska", "Montana", "Pennsylvania", "Louisiana", "Connecticut", "New Mexico", "Wyoming", "Oregon", "Delaware", "Nevada", "Massachusetts", "Arkansas", "Virginia", "South Dakota", "Georgia", "Nebraska", "North Dakota", "Maryland", "Maine", "Minnesota", "Michigan", "Wisconsin", "Kentucky", "Oklahoma", "Rhode Island", "Alabama", "New Jersey", "New Hampshire", "Washington", "Kansas", "North Carolina", "South Carolina", "Tennessee", "Illinois", "Iowa", "Idaho", "Vermont", "Missouri", "Mississippi", "Ohio", "West Virginia", "New York"]
NOUNS = ["Nintendo Game", "Doctor", "Parent", "Diet Fad", "Robot", "Chicken", "Pork", "Noodles", "Child", "Sibling", "Cat", "Dog", "Fish", "Computer", "Bed", "Anime", "Book", "Desk", "Television Show", "Movie", "Clown", "Bodybuilder", "Shovel", "Screwdriver", "Beverage", "Drag Queen"]
PLACES = ["House", "Bar", "Club", "Attic", "Library", "Hospital", "Restaurant", "School", "Office", "Bookstore", "Grocery Store", "Basement"]
WHEN = ["Soon", "Later Today", "Next Week", "Later This Month", "Sooner Than You Think", "Tomorrow", "Next Month", "Sometime Next Year"]

def main():
    print("Clickbait Headline Generator")
    print()
    while True:
        print("Enter the number of headlines to generate:")
        response = input('> ')
        if not response.isdecimal():
            print("Please enter a number")
        else:
            num_headlines = int(response)
            break #Exit the loop once a valid number is entered

    for i in range(num_headlines):
        clickbait_type = random.randint(1, 8)
        
        if clickbait_type == 1:
            headline = generateMillenials()
        elif clickbait_type == 2:
            headline = generateWhatYouDontKnow()
        elif clickbait_type == 3:
            headline = generateCompaniesHateHer()
        elif clickbait_type == 4:
            headline = generateYouWontBelieve()
        elif clickbait_type == 5:
            headline = generateDontWantYouToKnow()
        elif clickbait_type == 6:
            headline = generateGiftIdea()
        elif clickbait_type == 7:
            headline = generateReasonsWhy()
        elif clickbait_type == 8:
            headline = generateJobAutomated()
    
    print(headline)
print()

#Each of these functions returns a different type of headline
def generateMillenials():
    noun = random.choice(NOUNS)
    return "Are Millennials Killing the {} Industry?".format(noun)

def generateWhatYouDontKnow():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return "Without This {}, {} Could Kill You {}".format(noun, pluralNoun, when)

def generateCompaniesHateHer():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return "Big Companies Hate {}! See How This {} {} Invented a Cheaper {}".format(pronoun, state, noun1, noun2)

def generateYouWontBelieve():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return "You Won't Believe What This {} {} Found in {} {}".format(state, noun, pronoun, place)

def generateDontWantYouToKnow():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return "What {} Don't Want You to Know About {}".format(pluralNoun1, pluralNoun2)

def generateGiftIdea():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return "{} Gift Ideas to Give Your {} From {}".format(number, noun, state)

def generateReasonsWhy():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1) #number2 should not be larger than number1
    return "{} Reasons Why {} Are More Intersting Than You Think (Number {} Will Surprise You!)".format(number1, pluralNoun, number2)

def generateJobAutomated():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    return "THis {} {} Didn't Think Robots Would Take {} Job"

main()