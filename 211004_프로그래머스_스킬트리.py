from itertools import combinations


def solution(skill, skill_trees):
    count = 0

    for skilltree in skill_trees:
        skillsss = "".join(s for s in list(filter(lambda x: x in skill, skilltree)))
        if skill.find(skillsss) == 0:
            count += 1
    return count


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))