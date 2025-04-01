def znajdz(wzorzec, tekst):
    d_tekst = len(tekst)
    d_wzorzec = len(wzorzec)
    for i in range(d_tekst - d_wzorzec + 1):
        for j in range(d_wzorzec):
            if tekst[i + j] != wzorzec[j]:
                break
            elif j == d_wzorzec - 1:
                return True
    return False
