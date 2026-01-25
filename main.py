def createGlossary(filename):
    # Need to grab Glossary of replacement terms from a file. And store in preprocess
    
    # Identify List of terms to replace
    terms = list(dict())
    
    # with statement will handle opening and closing the file.
    with open(filename, "rt", encoding="UTF-8") as glossaryFile:

        # Grab a line from the file
        for Line in glossaryFile:
            Line = Line.strip()
            # find '='
            delim = Line.find("=")
            split = dict(find =Line[:delim], replace =Line[delim+1:])
            terms.append(split)
    return terms

# Line to translate
translate = str("　クロウは原作主人公ことシロウと瓜二つの容姿をしている。\nシロウの肌を褐色にして髪色を銀にすればまんま俺だ。")

# Storage for replaced Text
send = str()

# Create Glossary
glossary = createGlossary("./TestFiles/glossary.txt")

# Start Replacement
for line in translate.split("\n"):
    # Identify and store character(s) to remove
    # Identify and Store character(s) to insert
    for term in glossary:
        line = line.replace(term["find"],term["replace"])
    send = send + "\n" + line

# Replacement for Translation
print(translate)
print(send)

