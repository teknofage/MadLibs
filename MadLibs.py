def MadLibs():
    print ("Welcome to the Maddest of MadLibs, Burning Man Edition")
    player_name = input("What's your name? ")
    print('')
    print("Hello, "+player_name+". You are going to play a MadLib game, and this is the Burning Man Edition.")

    noun1 = input("Please Enter a noun: ")
    print(noun1)
    noun2 = input("Please Enter a noun: ")
    print(noun2)
    past_tense_verb3 = input("Please Enter a past tense verb: ")
    print(past_tense_verb3)
    adjective4 = input("Please Enter an adjective: ")
    print(adjective4)
    adjective5 = input("Please Enter an adjective: ")
    print(adjective5)
    adjective6 = input("Please Enter an adjective: ")
    print(adjective6)
    plural_noun7 = input("Please Enter a plural noun: ")
    print(plural_noun7)
    past_tense_verb8 = input("Please Enter a past tense verb: ")
    print(past_tense_verb8)
    noun9 = input("Please Enter a noun: ")
    print(noun9)
    past_tense_verb10 = input("Please Enter a past tense verb: ")
    print(past_tense_verb10)
    plural_noun11 = input("Please Enter a plural noun: ")
    print(plural_noun11)
    past_tense_verb12 = input("Please Enter a past tense verb: ")
    print(past_tense_verb12)
    band_name13 = input("Please Enter a band name: ")
    print(band_name13)
    famous_person14 = input("Please Enter a famous person's name: ")
    print(famous_person14)
    story = f"""This one time at Burning Man, I built a 60 foot long, 40 foot high {noun1}. 
    And the next day I rode my {noun2} by a crew taking wedding pictures, but my skirt was down 
    and my ass made a bullseye in their wedding photo. 
    So I {past_tense_verb3} in a {adjective4} parade from my camp to the Man for the burn. 
    Just at the moment I got tired of riding my {adjective5} bike through the {adjective6} playa, 
    I found a park bench with white writing all over the {plural_noun7}, so I sat down and {past_tense_verb8} 
    the copy of The Brothers Karamozov chained to it. 
    And then I met a {noun9} who told me she’d gotten married earlier in the day 
    and her vows were “0100111000101000101”. 
    And we {past_tense_verb10} a gigantic copper dragon rolling by, chased by 
    hundreds of {plural_noun11}, so I {past_tense_verb12} and found myself in deep playa at 
    a {band_name13} album release party hosted by {famous_person14}. """ # use string values for user input
    print(story)
    
MadLibs()

print ("Would you like to play again?")
while input() == "yes": MadLibs()
    
        
    