import tools

# Line to translate
base_text = str("　クロウは原作主人公ことシロウと瓜二つの容姿をしている。\nシロウの肌を褐色にして髪色を銀にすればまんま俺だ。")

# Create Glossary
glossary = tools.glossary.createGlossary("./Example Files/glossary.txt")

# Start Replacement
replaced = tools.glossary.replaceTerms(base_text, glossary)

# Replacement for Translation
print(replaced)

