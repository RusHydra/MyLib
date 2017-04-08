def div(dividendin,divisorin,size):
    if dividendin.count('.') == 0:
        dividendin += '.'
    if divisorin.count('.') == 0:
        divisorin += '.'
    dividendin = dividendin.strip('0')
    divisorin = divisorin.strip('0')
    if dividendin == '.':
        return '0.0'
    else:
        if dividendin[-1] == '.':
            dividendin += '0'
        if divisorin[-1] == '.':
            divisorin += '0'
        dividendin = dividendin.split('.')
        divisorin = divisorin.split('.')
        full = abs(len(dividendin[1])-len(divisorin[1])) + size
        dividendin = ''.join(dividendin) + size*'0'
        divisorin = ''.join(divisorin)
        answer = str(int(dividendin)//int(divisorin))
        answer = list('0'*abs(full-len(answer))+answer)
        answer.insert(-full,'.')
        answer = ''.join(answer).strip('0')
        if answer[-1] == '.':
            answer += '0'
        if answer[0] == '.':
            answer = '0'+answer
        return ''.join(answer)


print(div(str(input()),str(input()),int(input())))


