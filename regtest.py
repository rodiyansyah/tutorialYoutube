import re
def Main():
    line = "I think I understand regular expression"
    matchResult = re.match('think', line, re.M|re.I)
    if matchResult:
        print(matchResult.group())
    else:
        print("not found")

    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print(searchResult.group())
    else:
        print("not found")

if __name__ == "__main__":
    Main()