import random
def gussing_game():
    print("Game is started!!!")
    random_number=random.randint(1,100)
    user_gusse=0
    while random_number!=user_gusse :
       user_gusse=int(input(("Enter your gusse(1-100):-")))
       if user_gusse==random_number:
           print("YOU WON!!!!")
           break
       elif user_gusse<random_number:
           print("HINT:-Your gusse is less!")
           
       elif user_gusse>random_number:
           print("HINT:-Your gusse is large!")
gussing_game()           
        

