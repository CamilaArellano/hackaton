
def generar_alias(contectName):
    cont = 0
    for item in contectName:
        if cont < 1:
            firstName = item
        if cont < 2:
            MiddleName = item
        if cont < 3:
            lastName = item
        cont = cont + 1

    if firstName is not None:
       aliasFirstName = firstName[:4]
    else:
        aliasFirstName = ""

    if MiddleName is not None:
        aliasMiddleName = MiddleName[:3]+'ey'
    else:
        aliasMiddleName = ""

    if lastName is not None:
        aliasLastname = lastName[:2]+'ie'
    else:
        aliasLastname = ""
        

    alias = []
    alias.append(aliasFirstName)
    alias.append(aliasMiddleName)
    alias.append(aliasLastname)

    return alias
 

