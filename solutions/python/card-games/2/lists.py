
def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1+rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    return False

def card_average(hand):
    """Calculate the average value of the cards in the hand.

    :param hand: list of int - The card values.
    :return: float - The average value of the hand.
    """
    return sum(hand)/len(hand)


def approx_average_is_average(hand):   
    """Determine if the approximate average is equal to the actual average.

    :param hand: list of int - The card values.
    :return: bool - True if either approximate average is equal to the actual average.
    """
    actual_average = card_average(hand)
    average_first_last = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]

    return actual_average in (average_first_last, median)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_hand=hand[1::2]
    even_hand=hand[::2]
    odd_hand_average=sum(odd_hand)/len(odd_hand)
    even_hand_average=sum(even_hand)/len(even_hand)
    if even_hand_average==odd_hand_average:
        return True
    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1]*2
    return hand
