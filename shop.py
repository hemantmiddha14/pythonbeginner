def shop(kind, *arguments, **keywords):
    print ("Do you have any",kind,"?")
    print ("Yes we have lots of",kind)
    for arg in arguments:
         print(arg)
    print("-"*10)
    keys = sorted(keywords.keys())
    for kw in keys:
         print(kw,":",keywords[kw])

