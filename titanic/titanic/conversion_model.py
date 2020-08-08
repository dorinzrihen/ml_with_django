
def sex(sex):
    result = sex.lower()
    if result=="male":
        return 0
    else:
        return 1


def embarked(emb):
    emb = emb.lower()
    return {
        "s": 0,
        "c": 1,
        "q": 2
    }.get(emb, 0)

def title(title):
    title = title.lower()
    x = title.split()
    title_options= ['mr','mrs','master','dr','rev','officer','royalty']
    for i in title_options:
        for word in x:
            if word == i:
                return title_options.index(i)

    return 0



