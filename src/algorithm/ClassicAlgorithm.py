#
# klasyczny algorytm O(N) zwracajacy poprawny wynik
#


def run_linear_algorithm(grades):
    cookies = []
    if len(grades) == 1:
        cookies.append(1)
        return cookies

    cookies_count = 0
    empty_values = []
    for index in range(len(grades)):
        if index == 0:
            if grades[index] <= grades[index + 1]:
                cookies.append(1)
            else:
                # value cannot be found in this iteration
                cookies.append(0)
                empty_values.append(index)
        elif index == len(grades) - 1:
            if grades[index] > grades[index - 1]:
                cookies.append(cookies[index - 1] + 1)
            else:
                cookies.append(1)
        else:
            if (grades[index] <= grades[index - 1]) and (grades[index] <= grades[index + 1]):
                cookies.append(1)
            elif (grades[index] > grades[index - 1]) and (grades[index] <= grades[index + 1]):
                cookies.append(cookies[index - 1] + 1)
            else:
                # value cannot be found in this iteration
                cookies.append(0)
                empty_values.append(index)
        cookies_count += cookies[index]

    for index in range(len(empty_values) - 1, -1, -1):
        val = empty_values[index]

        if val == 0:
            cookies[val] = cookies[val + 1] + 1
        else:
            if (grades[val] > grades[val + 1]) and (grades[val] > grades[val - 1]):
                cookies[val] = (cookies[val - 1] + 1) if (cookies[val - 1] > cookies[val + 1]) \
                    else (cookies[val + 1] + 1)
            else:
                cookies[val] = cookies[val + 1] + 1
        cookies_count += cookies[val]

    return cookies_count
