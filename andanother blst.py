def add(term1,term2):
    if term1.count('.') == 0:
        term1 += '.0'
    if term2.count('.') == 0:
        term2 += '.0'
    termlist1 = term1.split('.')
    termlist2 = term2.split('.')
    maximod = max(len(termlist1[1]), len(termlist2[1]))
    termlist1[1] = termlist1[1].ljust(maximod,'0')
    termlist2[1] = termlist2[1].ljust(maximod,'0')
    term1n = int(''.join(termlist1).lstrip('0'))
    term2n = int(''.join(termlist2).lstrip('0'))
    answer = list(str(term1n + term2n))
    answer.insert(-maximod,'.')
    answer = ''.join(answer)
    if answer.rstrip('0')[-1] != '.':
        answer = answer.rstrip('0')
    else:
        answer = answer.rstrip('0') + '0'
    if answer.lstrip('0')[0] != '.':
        answer = answer.lstrip('0')
    else:
        answer = '0' + answer.lstrip('0')
    return answer

print(add(str(input()),str(input())))
