def urlConvertor(name, year, playerindex, advanced: bool):
    lname = name[1]
    fname = name[0]
    lnamelist = list(lname)
    linitial = lnamelist[0]
    fnamelist = list(fname)
    lname5 = ''
    for x in range(5):
        try:
            lname5 += lnamelist[x]
        except:
            break
    f2i = fnamelist[0] + fnamelist[1]
    if advanced == False:
        url = f'https://www.basketball-reference.com/players/{linitial}/{lname5}{f2i}{playerindex}/gamelog/{year}/'
    else:
        url = f'https://www.basketball-reference.com/players/{linitial}/{lname5}{f2i}{playerindex}/gamelog-advanced/{year}/'
    return url, advanced