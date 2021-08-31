from pprint import pprint
from typing import Dict
from collections import defaultdict


from pprint import pprint
from typing import Dict
from collections import defaultdict


def makeTableToDictionary(table):
    jobTable = dict()

    for col in table:
        splited = col.split()
        jobDict = dict()
        for i, lang in enumerate(splited[1:]):
            jobDict[lang] = len(splited[1:]) - i
        jobTable[splited[0]] = jobDict
    return jobTable


def coupleUserLanguageWithPerference(languages, preference):
    retDict = dict()
    for pref, lang in zip(preference, languages):
        retDict[lang] = pref
    return retDict


def scoreByJobType(jobTable, userInfo):
    ret = dict.fromkeys(jobTable.keys(), 0)
    for jobName, languages in jobTable.items():
        print(languages)
        for lang, pref in userInfo.items():
            if languages.get(lang) is not None:
                ret[jobName] += languages.get(lang) * pref
    return ret


def solution(table, languages, preference):
    jobTable = makeTableToDictionary(table)  # 자료구조를 만든다.
    userJobPreference = coupleUserLanguageWithPerference(
        languages, preference
    )  # 언어와 선호도를 묶는다
    userScore = scoreByJobType(jobTable, userJobPreference)
    userScore = sorted(list(userScore.items()), key=lambda x: (-x[1], x[0]))
    return userScore[0][0]

    # 언어를 돌면서 각 직군마다 점수를 산출한다. (점수, 직군)
    # 점수, 언어(string)으로 정렬 후 가장 앞의 원소를 리턴


def main():
    table = [
        "SI JAVA JAVASCRIPT SQL PYTHON C#",
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA",
    ]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    result = "PORTAL"
    solution(table, languages, preference)


if __name__ == "__main__":
    main()
