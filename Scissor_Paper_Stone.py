def num_conversion(sign):
    if sign.lower() == "paper":
        return 0
    elif sign.lower() == "stone":
        return 1
    elif sign.lower() == "scissor":
        return 2
    else:
        print "Invalid input. Enter again."
        main()

def continue_decide():
    quit = raw_input("Enter \"quit\" to leave the game. Other key to play again.\n")
    if quit == "quit":
        return
    else:
        main()

def main():
    print "scissor-paper-stone game."
    user1 = raw_input("User 1's choice: ")
    user1_num = num_conversion(user1)
    user2 = raw_input("User 2's choice: ")
    user2_num = num_conversion(user2)
    
    if user2_num == (user1_num+1)%3:
        print "User 1 wins!"
    else:
        print "User 2 wins!"
    continue_decide()
    
main()
    