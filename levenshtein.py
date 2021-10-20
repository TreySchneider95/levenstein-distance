"""
Assignment to create a function that calculates the levenshtein distance between
two words.
"""

CACHE_DICT = {}

def sentence_in(stmnt1, stmnt2, space_removal = False, case_sensitive = False):
    if not case_sensitive:
        stmnt1 = stmnt1.lower()
        stmnt2 = stmnt2.lower()
    if not space_removal:
        return levenshtein_distance(stmnt1, stmnt2)
    else:
        lst1 = stmnt1.split()
        lst2 = stmnt2.split()
        counter = 0
        diff_num = len(lst1) - len(lst2)
        for word in range(len(lst1)):
            if diff_num <= 0 and word == len(lst1)-1:
                counter += levenshtein_distance(lst1[word], lst2[word])
                for remainder in lst2[len(lst1):]:
                    counter += levenshtein_distance('', remainder)
            elif diff_num > 0 and word == len(lst2):
                for remainder in lst1[len(lst2):]:
                    counter += levenshtein_distance(remainder, '')
                break
            else:
                counter += levenshtein_distance(lst1[word], lst2[word])
        return counter

def levenshtein_distance(wrd1, wrd2):
    """
    Calculates the levenshtein distance between two words and prints the steps
    """
    counter = 0
    if wrd1 + '|' + wrd2 in CACHE_DICT:
        for x in CACHE_DICT[wrd1+wrd2]:
            print('CACHE:' + ' ' + x)
            counter += int(x[-1:])
        return counter
    steps_list = []
    wrd1_dict = {key:value for key, value in enumerate(wrd1)}
    for k,v in wrd1_dict.items():
        # check if index in range
        if k < len(wrd2):
            # replace logic
            if k < len(wrd1) - 1:
                if v != wrd2[k]:
                    print(f'replace "{wrd1[k]}" with "{wrd2[k]}" - 1')
                    steps_list.append(f'replace "{wrd1[k]}" with "{wrd2[k]}" - 1')
                    counter += 1
            # insert logic
            elif k == len(wrd1) - 1:
                if v != wrd2[k]:
                    print(f'replace "{wrd1[k]}" with "{wrd2[k]}" - 1')
                    counter += 1
                if len(wrd2[len(wrd1):]) > 0:
                    print(f'insert "{wrd2[len(wrd1):]}" - {len(wrd2[len(wrd1):])}')
                    steps_list.append(f'insert "{wrd2[len(wrd1):]}" - {len(wrd2[len(wrd1):])}')
                counter += len(wrd2[len(wrd1):])
                CACHE_DICT[wrd1 + '|' + wrd2] = steps_list
                return counter
        # remove logic
        else:
            if len(wrd1[len(wrd2):]) > 0:
                print(f'remove "{wrd1[len(wrd2):]}" - {len(wrd1[len(wrd2):])}')
                steps_list.append(f'remove "{wrd1[len(wrd2):]}" - {len(wrd1[len(wrd2):])}')
            counter += len(wrd1[len(wrd2):])
            CACHE_DICT[wrd1 + '|' + wrd2] = steps_list
            return counter
    if not wrd1_dict:
        if len(wrd2[len(wrd1):]) > 0:
            print(f'insert "{wrd2[len(wrd1):]}" - {len(wrd2[len(wrd1):])}')
            steps_list.append(f'insert "{wrd2[len(wrd1):]}" - {len(wrd2[len(wrd1):])}')
        counter += len(wrd2[len(wrd1):])
        CACHE_DICT[wrd1 + '|' + wrd2] = steps_list
        return counter

# print(levenshtein_distance('', 'test'))
print(sentence_in('this is not a little test', 'this is a an test', space_removal=True))
