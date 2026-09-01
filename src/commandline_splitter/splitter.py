from enum import Enum


def splitter(s: str) -> list[str]:
    class Status(Enum):
        SEPARATOR = 0
        NON_QUOTE = 1
        IN_SINGLE_QUOTE = 2
        IN_DOUBLE_QUOTE = 3
        BACKSLASH = 4
        BACKSLASH_IN_DOUBLE_QUOTE = 5

    result: list[str] = []
    token: str = ""
    token_exist: bool = False
    status: Status = Status.SEPARATOR
    for c in list(s):
        match status:
            case Status.SEPARATOR:
                match c:
                    case " ":
                        pass
                    case "\\":
                        token_exist = True
                        status = Status.BACKSLASH
                    case "'":
                        token_exist = True
                        status = Status.IN_SINGLE_QUOTE
                    case '"':
                        token_exist = True
                        status = Status.IN_DOUBLE_QUOTE
                    case _:
                        token += c
                        token_exist = True
                        status = Status.NON_QUOTE
            case Status.NON_QUOTE:
                match c:
                    case " ":
                        if token_exist:
                            result.append(token)
                        token = ""
                        token_exist = False
                        status = Status.SEPARATOR
                    case "\\":
                        status = Status.BACKSLASH
                    case "'":
                        status = Status.IN_SINGLE_QUOTE
                    case '"':
                        status = Status.IN_DOUBLE_QUOTE
                    case _:
                        token += c
            case Status.IN_SINGLE_QUOTE:
                match c:
                    case "'":
                        status = Status.NON_QUOTE
                    case _:
                        token += c
            case Status.IN_DOUBLE_QUOTE:
                match c:
                    case "\\":
                        status = Status.BACKSLASH_IN_DOUBLE_QUOTE
                    case '"':
                        status = Status.NON_QUOTE
                    case _:
                        token += c
                        status = Status.IN_DOUBLE_QUOTE
            case Status.BACKSLASH:
                token += c
                status = Status.NON_QUOTE
            case Status.BACKSLASH_IN_DOUBLE_QUOTE:
                token += c
                status = Status.IN_DOUBLE_QUOTE
    match status:
        case Status.SEPARATOR:
            pass
        case Status.NON_QUOTE:
            if token_exist:
                result.append(token)
        case Status.IN_SINGLE_QUOTE:
            # TODO: warning: No matching single quotation
            if token_exist:
                result.append(token)
        case Status.IN_DOUBLE_QUOTE:
            # TODO: warning: No matching double quotation
            if token_exist:
                result.append(token)
        case Status.BACKSLASH:
            # TODO: warning: No character follows the backslash
            if token_exist:
                result.append(token)
        case Status.BACKSLASH_IN_DOUBLE_QUOTE:
            # TODO: warning: No character follows the backslash
            # TODO: warning: No matching double quotation
            if token_exist:
                result.append(token)
    return result
