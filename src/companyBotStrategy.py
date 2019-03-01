# Company Problem for CodeSignal
# Problem Link: https://app.codesignal.com/company-challenges/codesignal/gJMBmTwHHMF8mbQvH

def companyBotStrategy(trainingData):
    total = 0
    count = 0
    for i in trainingData:
        if i[1] == 1:
            total += i[0]
            count += 1
    return (total/count if count != 0 else 0)
