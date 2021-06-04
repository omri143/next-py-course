def is_funny(string):
    return isinstance(string, str) and [True for i in range(0, len(string) - 1)
                                        if not ((string[i] == 'a' or string[i] == 'h') and
                                                (string[i + 1] == 'a' or string[i + 1] == 'h'))] == []


print(is_funny("ahaha"))
