current_score = 100



def lose_points(old_score):
    new_score = old_score - 10
    if new_score < 0:
        new_score = 0
        print("CPU: You can keep guessing..\n")
        print("CPU: If you want.\n")
        print("CPU: But your points are low. Very low...\n")
        print("CPU: I suggest you restart...\n")
    return new_score

def score_rating(new_score):
    if new_score >= 80:
        print("SCORE RATING:\n")
        print("CPU: Excellent job! You are a great guesser!")
    elif new_score >= 50:
        print("SCORE RATING:\n")
        print("CPU: You did a great job, but I believe you can do better!")
    else:
        print("SCORE RATING:\n")
        print("CPU: Yikes. Keep practicing, you'll get better with time.")