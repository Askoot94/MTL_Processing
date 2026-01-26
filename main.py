import tools
import tests

# Line to translate
translate = str("　クロウは原作主人公ことシロウと瓜二つの容姿をしている。\nシロウの肌を褐色にして髪色を銀にすればまんま俺だ。")

# Storage for replaced Text
send = str()

# Create Glossary
glossary = tools.glossary.createGlossary("./Example Files/glossary.txt")

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

