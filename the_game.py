# Thank you for taking time to review my code!

from cards import Cards
from cards import true_values
from cards import suites
from cards import values
import random
import time

# define initial variables that need to be created outside of game loop
player_chips = 1000
player_count = []
dealer_count = []
player_card = ()
dealer_card = ()

# main game loop
while True:
    # functions to print cards and totals
    def print_player():
        print("You draw the", player_card.value, "of", player_card.suite)
        time.sleep(1)


    def print_dealer():
        print("The dealer draws the", dealer_card.value, "of", dealer_card.suite)
        time.sleep(1)


    def print_player_total():
        print("Your total count is:", player_total)
        time.sleep(1)


    def print_dealer_total():
        print("The dealer's total count is:", dealer_total)
        time.sleep(1)


    player_count.clear()
    dealer_count.clear()
    player_total = 0
    dealer_total = 0
    check_bet = True
    bet = ()
    side_bet = 0
    game_over = False
    end_of_round = False

    # player bets chips
    while check_bet:
        if player_chips > 0:
            try:
                print("Your current chips stack is:", int(player_chips))
                bet = int(input("How much would you like to bet?: "))
                print("\b")
                if bet > player_chips:
                    you_broke = True
                    while you_broke:
                        print("Oops! You don't have enough chips! Your current chip stack is:", player_chips)
                        bet = int(input("How much would you like to bet?: "))
                        if bet <= player_chips:
                            player_chips -= bet
                            you_broke = False
                            check_bet = False

                elif bet <= player_chips:
                    player_chips -= bet
                    check_bet = False

            except ValueError:
                print("Oops, please enter a numerical value!")

        else:
            time.sleep(2)
            print("You're out of chips! Game over!")
            quit()

    # deals initial cards
    # player card 1
    player_card = Cards(random.choice(suites), random.choice(values))
    player_count.append(true_values[player_card.value])
    print_player()
    if player_card.value == "Ace":
        check_ace = True
        while check_ace:
            ace_choice = input("Would you like your ace to count as a 1 or 11?: ")
            if ace_choice == "1":
                player_card.value = 1
                player_count.remove(11)
                player_count.append(player_card.value)
                check_ace = False
                time.sleep(1)
            elif ace_choice == "11":
                check_ace = False
                time.sleep(1)

    # dealer card 1
    dealer_card = Cards(random.choice(suites), random.choice(values))
    dealer_count.append(true_values[dealer_card.value])
    print_dealer()




# need to create instance where player is paid out on side bet


    # checks for side bet
    if dealer_card.value == "Ace":
        check_insurance = True
        while check_insurance:
            insurance = input("The dealer faced up card is an Ace.\nWould you like to place a side bet? [Y/N: ").upper()
            if insurance == "Y":
                check_bet_value = True
                while check_bet_value:
                    try:
                        time.sleep(1)
                        print("You can place a side bet for up to half of your original bet.")
                        side_bet = int(input("How much would you like to bet?: "))
                        if side_bet <= bet/2:
                            player_chips -= side_bet
                            check_bet_value = False
                            check_insurance = False
                            dealer_card = Cards(random.choice(suites), random.choice(values))
                            dealer_count.append(true_values[dealer_card.value])
                            dealer_total = sum(dealer_count)
                            if dealer_card.value == "Ace":
                                if 11 + dealer_total > 21:
                                    dealer_card.value = 1
                                    dealer_count.remove(11)
                                    dealer_count.append(dealer_card.value)
                                    dealer_total = sum(dealer_count)

                            if dealer_total == 21:
                                print("The dealer turns over their card and it's a", dealer_card.value, "of",
                                      dealer_card.suite)
                                print("The dealer hits a Blackjack, you lose your initial"
                                      "bet but but collect 2x your side bet!")
                                player_chips -= bet
                                player_chips += side_bet * 2
                                game_over = True


                            elif dealer_total != 21:
                                print("The dealer turns over their card and it's a", dealer_card.value, "of",
                                      dealer_card.suite)
                                print("The dealer collects your side bet.")


                        elif side_bet > player_chips:
                            time.sleep(1)
                            print("You can only place a side bet equal to or less than your original bet!")
                            print("Your original bet was: ", bet)

                    except ValueError:
                        time.sleep(1)
                        print("Error! Please enter a numerical value!")

            elif insurance == "N":
                check_insurance = False

    # player card 2
    if not game_over:
        player_card = Cards(random.choice(suites), random.choice(values))
        player_count.append(true_values[player_card.value])
        print_player()
        if player_card.value == "Ace":
            check_ace = True
            while check_ace:
                ace_choice = input("Would you like your ace to count as a 1 or 11?: ")
                if ace_choice == "1":
                    player_card.value = 1
                    player_count.remove(11)
                    player_count.append(player_card.value)
                    check_ace = False

                elif ace_choice == "11":
                    check_ace = False


    player_total = sum(player_count)
    if player_total == 21:
        print("You hit a Blackjack and win!\b")
        player_chips += bet * 2.5
        game_over = True
    # In the event the user draws two aces and chooses them as 11's.
    elif player_total > 21:
        print("You busted! Why did you do that!?\b")
        player_chips -= bet * 2
        game_over = True
        check_player_hit = False


    # dealer card 2
    if not game_over and side_bet == 0:
        dealer_card = Cards(random.choice(suites), random.choice(values))
        dealer_count.append(true_values[dealer_card.value])
        dealer_total = sum(dealer_count)
        if dealer_card.value == "Ace":
            if 11 + dealer_total > 21:
                dealer_card.value = 1
                dealer_count.remove(11)
                dealer_count.append(dealer_card.value)
                dealer_total = sum(dealer_count)
        print("The dealer draws a card faced down.")
        time.sleep(1)


        check_player_hit = True
        while check_player_hit and not game_over:
            print_player_total()
            hit_again = input("Would you like to hit again?: ").upper()
            if hit_again == "Y":
                player_card = Cards(random.choice(suites), random.choice(values))
                player_count.append(true_values[player_card.value])
                player_total = sum(player_count)
                print_player()


                if player_card.value == "Ace":
                    check_ace = True
                    while check_ace:
                        ace_choice = input("Would you like your ace to count as a 1 or 11?: ")
                        if ace_choice == "1":
                            player_card.value = 1
                            player_count.remove(11)
                            player_count.append(player_card.value)
                            player_total = sum(player_count)
                            check_ace = False
                        elif ace_choice == "11":
                            check_ace = False


                if player_total > 21:
                    print("You busted!\b")
                    player_chips -= bet*2
                    game_over = True
                    check_player_hit = False

                elif player_total == 21:
                    print("You hit a Blackjack and win!\b")
                    player_chips += bet*2.5
                    game_over = True
                    check_player_hit = False

            if hit_again == "N":
                check_player_hit = False

            elif hit_again != "Y" and hit_again != "N":
                print("Error, please enter 'Y' or 'N'..")









# Issues with adding dealers total. Seems to be subtracting when it shoulnd't be.

# dealers turn
    dealer_turn = True
    if dealer_turn and not game_over:
        print("The dealer turns over their card and it's a", dealer_card.value, "of", dealer_card.suite)
        print_dealer_total()
        if dealer_total > player_total:
            if dealer_total == 21 and player_total != 21:
                print("The dealer hits a Blackjack, you lose!")
                player_chips -= bet * 2
                dealer_turn = False
            else:
                print("The dealer beats you with a total of", dealer_total)
                player_chips -= bet*2
                game_over = True
                dealer_turn = False


        elif player_total > dealer_total <= 16 and not game_over:
            dealer_hit = True
            while dealer_hit:
                dealer_card = Cards(random.choice(suites), random.choice(values))
                dealer_count.append(true_values[dealer_card.value])
                dealer_total = sum(dealer_count)
                print_dealer()
                print_dealer_total()

                if dealer_card.value == "Ace":
                    if 11 + dealer_total > 21:
                        dealer_card.value = 1
                        dealer_count.remove(11)
                        dealer_count.append(dealer_card.value)
                        dealer_total = sum(dealer_count)

                if dealer_total > 21:
                    print("The dealer busted!\b")
                    player_chips += bet*2
                    dealer_hit = False

                elif dealer_total == 21:
                    print("The dealer hits a Blackjack!\b")
                    player_chips -= bet*2
                    dealer_hit = False

                elif 16 < dealer_total < player_total:
                    print("The dealer stands.")
                    time.sleep(1)
                    print("You beat the dealer with a total of", player_total)
                    player_chips += bet*2
                    dealer_hit = False

                elif dealer_total > player_total:
                    print("The dealer beats you with a", dealer_total)
                    player_chips -= bet*2
                    dealer_hit = False

                elif dealer_total == player_total:
                    print("It's a draw!")
                    dealer_hit = False
                    player_chips += bet


        elif player_total > dealer_total > 16 and not game_over:
            print("The dealer stands.")
            print("You won with a total of", player_total)
            player_chips += bet * 2


        elif player_total == dealer_total:
            print("It's a draw!")
            dealer_hit = False
            player_chips += bet

