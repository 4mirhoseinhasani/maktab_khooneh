candidates = range(10,91)
candidate = int(input())

while candidate not in candidates:
    candidate = int(input('Error! Candidate,s age must be between 10 and 90 years.\n'))
oldest_candidate = candidate

while True:
    candidate = int(input())
    if candidate == -1:
        break
    if candidate not in candidates:
        print('Error! Candidate,s age must be between 10 and 90 years.')
        continue
    if candidate >= oldest_candidate:
        oldest_candidate = candidate
        
print(oldest_candidate)
    