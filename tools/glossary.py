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
