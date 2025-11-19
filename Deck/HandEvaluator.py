from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand):

    rank_count = {}

    for card in hand:

        rank = card.rank.value

        rank_count[rank] = rank_count.get(rank, 0) + 1

    suit_count = {}

    for card in hand:

        suit = card.suit

        suit_count[suit] = suit_count.get(suit, 0) + 1

    is_flush = any(count >= 5 for count in suit_count.values())

    unique_ranks = sorted(set(rank_count.keys()))

    is_straight = False

    for i in range(len(unique_ranks) - 4):
        if (unique_ranks[i] + 1 == unique_ranks[i+1] and
            unique_ranks[i] + 2 == unique_ranks[i+2] and
            unique_ranks[i] + 3 == unique_ranks[i+3] and
            unique_ranks[i] + 4 == unique_ranks[i+4]):
            is_straight = True

    if set([14, 2, 3, 4, 5]).issubset(unique_ranks):
        is_straight = True

    counts = sorted(rank_count.values(), reverse=True)

    if 4 in counts:
        return "Four of a Kind"

    if 3 in counts and 2 in counts:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if 3 in counts:
        return "Three of a Kind"

    if counts.count(2) >= 2:
        return "Two Pair"

    if 2 in counts:
        return "One Pair"

    return "High Card"

