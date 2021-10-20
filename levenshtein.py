"""
Assignment to create a function that calculates the levenshtein distance between
two words.
"""

def levenshtein_distance(wrd1, wrd2):
    """
    Calculates the levenshtein distance between two words and prints the steps
    """
    counter = 0
    wrd1_dict = {key:value for key, value in enumerate(wrd1)}
    for k,v in wrd1_dict.items():
        # check if index in range
        if k < len(wrd2):
            # replace logic
            if k < len(wrd1) - 1:
                if v != wrd2[k]:
                    print(f'replace "{wrd1[k]}" with "{wrd2[k]}" - 1')
                    counter += 1
            # insert logic
            elif k == len(wrd1) - 1:
                if v != wrd2[k]:
                    print(f'replace "{wrd1[k]}" with "{wrd2[k]}" - 1')
                    counter += 1
                print(f'insert "{wrd2[len(wrd1):]}" - {len(wrd2[len(wrd1):])}')
                counter += len(wrd2[len(wrd1):])
                return counter
        # remove logic
        else:
            print(f'remove "{wrd1[len(wrd2):]}" - {len(wrd1[len(wrd2):])}')
            counter += len(wrd1[len(wrd2):])
            return counter


print(levenshtein_distance('kittenooo', 'sitting'))
