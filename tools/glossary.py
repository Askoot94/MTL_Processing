def createGlossary(filename:str):
    # Need to grab Glossary of replacement terms from a file. And store in preprocess
    
    # Identify List of terms to replace
    terms = list(dict())
    
    # try to open file
    try:
        # with statement will handle opening and closing the file.
        with open(filename, "rt", encoding="UTF-8") as glossaryFile:

            # Grab a line from the file
            for Line in glossaryFile:
                # remove trailing newline on right side
                Line = Line.rstrip()
                
                # find '='
                delim = Line.find("=")
 
                # Identify and Store character(s) to remove and insert
                split = dict(find =Line[:delim], replace =Line[delim+1:])
                
                # add the new dictionary to list
                terms.append(split)
        return terms
    except FileNotFoundError as e:
        e.add_note("Requested file was not found.")
        return terms

def replaceTerms(text: str, glossary:list):
    if glossary != [] and text != "":
        send = str()
        for line in text.split("\n"):
            for term in glossary:
                # Check for find and replace terms in given dict
                if "find" and "replace" in term:    
                    line = line.replace(term["find"],term["replace"])
                    send = send + '\n' + line
                else:
                    print("Bad Dict recieved")
                    print(term)
                    
        return send
    else:
        return text