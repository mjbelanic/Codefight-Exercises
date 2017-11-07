def checkParticipants(participants):
    return f(participants)

def f(participants):
    checked = []
    for i in range(len(participants)):
        if participants[i] < i:
            checked.append(i)
    return checked