
score_player =list(map(int, input().split()))
pillar_score = list(map(int, input().split()))
print(score_player, pillar_score)

def winners(score_player, pillar_score):
    winner = 0
    for i in score_player:
        for k in range(pillar_score):
            if pillar_score[k] % i == 0: 
                winner += 1
    print(winner)

winners(score_player,pillar_score)
