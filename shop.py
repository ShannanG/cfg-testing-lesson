retro_playground_toys = {
  'Ventriloquist Doll': 150,
  'Cloudmobile': 15,
  'Magic Roundabout': 95
}

customer_wallet = 100

choose_toy = input(
        'Welcome to Retro Playground, your one stop shop for toys from your past! \nMay I dray your attention to today\'s specials: \n' + '\n'.join(
            [f'This {toy} can be yours for just £{price}' for toy, price in
             retro_playground_toys.items()]) + '\nEnter the toy you would like to buy or exit to leave?: ').title()
chosen_toy = choose_toy

ask_for_more_money = ['That\'s still not enough, look again!', 'Check all your pockets, do you have any more?']


def goodbye():
    print('Goodbye, please come again!')


class PurchaseAttemptedThreeTimesError(ValueError):
    pass


def buy_toy(customer_wallet, chosen_toy):

    try:
        if chosen_toy == 'Exit':
            left_shop = f'I\'m sorry we didn\'t have anything for you today'
            print(left_shop)
            return left_shop

        elif chosen_toy not in retro_playground_toys and chosen_toy != 'Exit':
            raise ValueError

        elif chosen_toy in retro_playground_toys:
            price = retro_playground_toys[chosen_toy]

            if price <= customer_wallet:
                paid_for_toy = f'Here’s your {chosen_toy}!'
                print(paid_for_toy)
                return paid_for_toy

            elif price >= customer_wallet:
                add_more_money = input(f'You can\'t afford the {chosen_toy}. Do you have any more money? Enter the extra amount you have or 0 if not: ').lower()
                extra_money = int(add_more_money)
                total_money = customer_wallet + extra_money
                print(f'I have £{total_money} in total.')

                if total_money >= price:
                    enough_money = f'Glad you have enough money, here is your {chosen_toy}'
                    print(enough_money)
                    return enough_money

                elif total_money < price:
                    counter = 0

                    while total_money < price and counter < len(ask_for_more_money):

                        ask_for_more_again = input(ask_for_more_money[counter] + ' Enter the amount of extra money you\'ve found, or 0 for none: ')
                        add_more_money = int(ask_for_more_again)
                        total_money += add_more_money
                        print(f'I can give you £{total_money}.')

                        if total_money >= price and counter < len(ask_for_more_money):

                            print(f'Glad you have enough money, here is your {chosen_toy}')
                            break
                        counter += 1
                        if total_money < price and counter == len(ask_for_more_money):
                            raise PurchaseAttemptedThreeTimesError

                return add_more_money

    except PurchaseAttemptedThreeTimesError:
        message = 'You need to save up some more.'
        print(message)
        return message

    except ValueError:
        print('You did not choose correctly.')

    finally:
        goodbye()


buy_toy(customer_wallet, chosen_toy)
