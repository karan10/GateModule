def is_int_or_float(num: str):
    try:
        a = int(num)
        return a
    except:
        try:
            a = float(num)
            return a
        except:
            raise Exception('not an int or float')


def convert_in_format(val: str):
    if isinstance(val, (bool,int, float)):
        return val

    val = val.strip('"').strip("'")
    try:
        a = int(val)
        return a
    except:
        try:
            a = float(val)
            return a
        except:
            try:
                a = bool(a)
                return a
            except:
                return val