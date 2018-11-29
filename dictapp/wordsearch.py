import json

from difflib import get_close_matches

def wordcheck():
    word = input("Enter a word: ")
    w = word.lower() or w = word.upper()
    data = json.load(open("dictapp/data.json", 'r'))
    if w in data:
        a = data[w]
        return a
    # elif w.title() in data:
    #     return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input( "Did you mean {} instead? Enter Y if yes, or N if no".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Please double check entry"
        else:
            return "This is nonsense"
    else:
        return word + " does not exist"


output = wordcheck()

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

# my_string = "hello world"
#
# k = [(i.upper(), len(i)) for i in my_string]
#
# print(k)
