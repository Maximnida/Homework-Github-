def find_top_voters(votes):
    
    count_1 = sum(1 for v in votes.values() if v == 1)
    count_0 = sum(1 for v in votes.values() if v == 0)
    
    if count_1 > count_0:
        top_vote_value = 1
    elif count_0 > count_1:
        top_vote_value = 0
    else:
        top_vote_value = "Durrang"
    
    top_voters = [name for name, vote in votes.items() if vote == top_vote_value]
    
    if top_vote_value == "Durrang":
        print(top_vote_value)
        print("Teng.")
    else:
        print(top_vote_value)
        print(" ".join(top_voters))
    

votes = {'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}
find_top_voters(votes)