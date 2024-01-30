# Get input scores for players and pillars
score_player = list(map(int, input().split()))
pillar_score = list(map(int, input().split()))

# Print the input scores for verification
print(score_player, pillar_score)

# Define a function to determine the winners
def winners(score_player, pillar_score):
    winner = 0
    
    # Iterate through each player's score
    for i in score_player:
        # Iterate through each pillar's score
        for k in range(len(pillar_score)):
            # Check if the pillar's score is divisible by the player's score
            if pillar_score[k] % i == 0:
                winner += 1
    
    # Print the total number of winners
    print(winner)

# Call the winners function with the input scores
winners(score_player, pillar_score)
