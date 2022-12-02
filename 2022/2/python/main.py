RPS_MAPPING = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

RPS_SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

WIN_MULTIPLIER = 3

with open("../input.txt", "r") as f:
    lines = f.readlines()

score = 0

OUTCOME_MAPPING = {
    "X": {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    },
    "Y": {
        "Rock": "Rock",
        "Paper": "Paper",
        "Scissors": "Scissors",
    },
    "Z": {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock",
    },
}

OUTCOME_SCORE_MULTIPLIER_MAPPING = {
    "X": 0,
    "Y": 1,
    "Z": 2,
}

for line in lines:
    choices = line.split()
    theirs = RPS_MAPPING[choices[0]]
    outcome = choices[1]
    
    base_score = OUTCOME_SCORE_MULTIPLIER_MAPPING[outcome]
    ours = OUTCOME_MAPPING[outcome][theirs]

    score += RPS_SCORE[ours] + base_score*WIN_MULTIPLIER

print(score)
