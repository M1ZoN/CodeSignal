# Problem Link: https://app.codesignal.com/company-challenges/godaddy/RjJwsTCiF663krgSP

def domainType(domains):
    res = []
    for i in domains:
        temp = i[i.rfind('.')+1:]
        if temp == 'com':
            res.append('commercial')
        elif temp == 'org':
            res.append('organization')
        elif temp == 'net':
            res.append('network')
        elif temp == 'info':
            res.append('information')
    return res
