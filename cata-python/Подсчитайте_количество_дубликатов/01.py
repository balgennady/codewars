def duplicate_count(text):
    
    seen = ''
    dupes = ''
    result = 0
    
    for x in text_upper:
        x = x.upper()
        if seen.find(x) < 0:
            seen += x
        else:
            if dupes.find(x) < 0:
                dupes += x
                result += 1
    return result

print( duplicate_count('aab') )
