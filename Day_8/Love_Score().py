from tqdm import tqdm_pandas


def calculate_love_score(name1,name2):
    check_love_1="true"
    check_love_2="love"
    score=""
    count_for_true=0
    count_for_love=0
    total_love_score=""
    combinedName=(name1+name2).lower()

    for idx,char in enumerate(check_love_1):
        true_count=combinedName.count(char)
        count_for_true+=true_count


    for idx,char in enumerate(check_love_2):
        love_count=combinedName.count(char)
        count_for_love+=love_count

    total_love_score=f"{count_for_true}{count_for_love}"
    print(total_love_score)













calculate_love_score("Angela Yu","Jack Bauer")
