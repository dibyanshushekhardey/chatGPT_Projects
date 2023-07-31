def mad_libs():
    # Story template with placeholders
    story = '''
    Once upon a time, there was a {adj} {noun} who loved to {verb}.
    One day, while {verb} in the {noun2}, the {noun} found a {adj2} {noun3}.
    The {noun} decided to {verb2} the {noun3} and it was {adv} {adj3}!
    '''

    # Prompt the user to enter various inputs
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")
    noun3 = input("Enter a third noun: ")
    verb2 = input("Enter another verb: ")
    adv = input("Enter an adverb: ")
    adj3 = input("Enter one more adjective: ")

    # Replace the placeholders with user inputs
    story = story.replace('{adj}', adj)
    story = story.replace('{noun}', noun)
    story = story.replace('{verb}', verb)
    story = story.replace('{noun2}', noun2)
    story = story.replace('{adj2}', adj2)
    story = story.replace('{noun3}', noun3)
    story = story.replace('{verb2}', verb2)
    story = story.replace('{adv}', adv)
    story = story.replace('{adj3}', adj3)

    # Display the generated story
    print("\nHere's your funny story:\n")
    print(story)

def main():
    print("Welcome to Mad Libs!")
    mad_libs()

if __name__ == '__main__':
    main()
