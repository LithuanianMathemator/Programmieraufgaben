
def evaluate(string):

    if "-" in string:
        raise Exception("syntaktisch inkorrekt")
        # if negative term in string, raise error

    if "++" in string or "+*" in string:
        raise Exception("syntaktisch inkorrekt")
        # if two operations in a row, raise error

    if "**" in string or "*+" in string:
        raise Exception("syntaktisch inkorrekt")
        # if two operations in a row, raise error

    openbrackets = ["(", "[", "{"]
    closedbrackets = [")", "]", "}"]
    # brackets to test wether or not brackets fit to each other and to test
    # if they are even there

    bracketstack = []
    # list for current newest opened bracket at last index

    for i in string:
        if i in openbrackets:
            bracketstack.append(i)
            # append open bracket to list
        elif i in closedbrackets:
            bracketindex = closedbrackets.index(i)
            # index of closed bracket
            if len(bracketstack) > 0 and openbrackets[bracketindex] ==\
                    bracketstack[len(bracketstack)-1]:
                # if stack has open bracket, compare last item in stack
                # to closing bracket
                bracketstack.pop()
                # tried brackets make room for still opened brackets
            else:
                raise Exception("syntaktisch inkorrekt")
                # if closed bracket without opened bracket, raise error

    if len(bracketstack) == 0:
        pass
    else:
        raise Exception("syntaktisch inkorrekt")
        # if opened bracket has no closing bracket

    evalstring = string.replace("[", "(")
    evalstring = evalstring.replace("{", "(")
    evalstring = evalstring.replace("}", ")")
    evalstring = evalstring.replace("]", ")")
    # all brackets made "(" or ")"

    depth = 0
    maxdepth = 0

    for i in evalstring:
        if i == "(":
            depth += 1
            # for open bracket raise depth
            if depth > maxdepth:
                maxdepth = depth
                # update depth if depth newest maximum

        elif i == ")":
            depth -= 1
            # each closing bracket lowers depth

    if any(i.isdigit() for i in evalstring):
        # number needs to be in string
        try:
            return(eval(evalstring), maxdepth)
            # return evaluation of string and maximum depth
        except TypeError:
            raise Exception("syntaktisch inkorrekt") from None
            # if TypeError, for example ()()()()
        except SyntaxError:
            raise Exception("syntaktisch inkorrekt") from None
            # if SyntaxError, for example (+)
        except NameError:
            raise Exception("syntaktisch inkorrekt") from None
            # if NameError
    else:
        raise Exception("syntaktisch inkorrekt") from None
