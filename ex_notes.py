def moyenne(notes):
    return sum(notes)/len(notes)

def note_max(notes):
    return max(notes)

def note_min(notes):
    return min(notes)

def mediane(notes):
    tri = sorted(notes)
    n = len(tri)
    return tri[n // 2]

#programme principale
notes=[10,15,8,18]
print("Moyenne:",moyenne(notes))
print("Note maximale:",note_max(notes))
print("Note minimale:",note_min(notes))
print("Médiane :", mediane(notes))