def solution(args):
    string = []
    start = None
    end = None
    sw = True

    for i in range(0, len(args)):
        if sw and (i+2) < len(args):
            if args[i+1] == args[i]+1 and args[i+2] == args[i]+2:
                start = args[i]
                sw = False
                continue

        if not sw and (i+1) < len(args):
            if args[i+1] == args[i]+1:
                continue
            if args[i-1] == args[i]-1 and args[i+1] != args[i]+1:
                end = args[i]
                sw = True

        if not sw and (i+1) == len(args):
            if args[i-1] == args[i]-1:
                end = args[i]
                sw = True

        if start and end:
            string.append('{}-{}'.format(start, end))
            start = None
            end = None
        else:
            string.append(str(args[i]))
    return ','.join(string)
