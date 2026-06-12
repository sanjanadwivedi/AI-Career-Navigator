def calculate_score(skills,
                    education,
                    projects,
                    experience):

    score = 0

    score += min(len(skills) * 5, 40)

    if education:
        score += 20

    score += min(len(projects) * 5, 20)

    score += min(len(experience) * 10, 20)

    return min(score, 100)