#Библиотека SmartMath

#Деление! Привет
def div(dividendin, divisorin, size):
    if dividendin.count('.') == 0:
        dividendin += '.'
    if divisorin.count('.') == 0:
        divisorin += '.'
    divisorin.strip('0')
    dividendin.strip('0')
    if dividendin.strip('0') == '.':
        return '0.0'
    else:
        if dividendin[-1] == '.':
            dividendin += '0'
        if divisorin[-1] == '.':
            divisorin += '0'
        dividendin = dividendin.split('.')
        divisorin = divisorin.split('.')
        full = abs(len(dividendin[1])-len(divisorin[1]))
        dividend = ''.join(dividendin) + size*'0'
        divisor = ''.join(divisorin)
        answer = []
        mod = 0
        for i in range(0, size + full):
            intdiv = int(dividend[i]) + mod * 10
            answer.append(str(intdiv // int(divisor)))
            mod = intdiv % int(divisor)
            if i == full - 1 and mod == 0:
                answer.append('.0')
                break
            elif i == full - 1:
                answer.append('.')
            elif mod == 0 and i >= full:
                break
        stranswer = ''.join(answer)
        if stranswer.rstrip('0')[-1] != '.':
            stranswer = stranswer.rstrip('0')
        else:
            stranswer = stranswer.rstrip('0') + '0'
        if stranswer.lstrip('0')[0] != '.':
            stranswer = stranswer.lstrip('0')
        else:
            stranswer = '0' + stranswer.lstrip('0')
        return stranswer
#Сложение!
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


print(div(str(input()),str(input()),int(input())))