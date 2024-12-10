candidates = range(10,91)
candidate = int(input())

while candidate not in candidates:
    candidate = int(input('Error! Candidate,s age must be between 10 and 90 years.\n'))
candidate_list = []
oldest_candidate = candidate
candidate_list.append(candidate)


while True:        
        candidate = int(input())
        candidate_list.append(candidate)
        if candidate == -1:
            candidate_list.remove(candidate)
            break
        if candidate not in candidates:
            print('Error! Candidate,s age must be between 10 and 90 years.')
            candidate_list.remove(candidate)
            continue
        if candidate >= oldest_candidate:
            oldest_candidate = candidate
            
candidate_list.sort(reverse=True)
print(candidate_list[0],candidate_list[1])
    