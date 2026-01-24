# Line to translate
translate = str("　クロウは原作主人公ことシロウと瓜二つの容姿をしている。\nシロウの肌を褐色にして髪色を銀にすればまんま俺だ。")

# Storage for replaced Text
send = str()

# Need to grab Glossary of replacement terms from a file. And store in preprocess
glossaryFile = open("./TestFiles/glossary.txt", "rt", encoding="UTF-8")

# Identify List of dictionaries to replace
terms = list(dict())

# Grab a line from the 
for Line in glossaryFile:
    # find '='
    delim = Line.find("=")
    split = dict(find =Line[:delim], replace =Line[delim+1:])
    terms.append(split)

# Close file
glossaryFile.close()


# Start Replacement
for line in translate.split("\n"):
    # Identify and store character(s) to remove
    # Identify and Store character(s) to insert
    for term in terms:
        line = line.replace(term["find"],term["replace"])
    send = send + "\n" + line

# Return output to console
print(translate)
print(send)
