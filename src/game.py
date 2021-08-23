#Improved Hackerrank challenge solution by Michał Wiliński
#Main loop definition
def main():
    print(minion_game(input("Enter word:")))

#Game function loop
def minion_game(string):
    #setting up variables
    string=string.upper()
    scoreboard={
    "Kevin" : 0,
    "Stuart" : 0
    }
    vowels="AEIOU"

    #main loop for scoring
    for i in range(len(string)):
        points=len(string)-i
        if string[i] in vowels:
            scoreboard["Kevin"]+=points
        else:
            scoreboard["Stuart"]+=points
    
    #returning values
    if len(set(scoreboard.values()))==1:
        return "Draw"
    else:
        winner=max(scoreboard,key=scoreboard.get)
        score=scoreboard[winner]
        return (f"{winner} is the winner with score {score}.")
if __name__=='__main__':
    main()