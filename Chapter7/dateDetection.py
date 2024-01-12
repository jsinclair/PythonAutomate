import pyperclip, re

def validDates():
    # Date regex
    dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

    text = str(pyperclip.paste())
    print(text)

    dates = []
    for groups in dateRegex.findall(text):
        print(groups)
        day = int(groups[0])
        month = int(groups[1])
        year = int(groups[2])

        if day < 1 or day > 31:
            continue
        if month < 1 or month > 12:
            continue
        if month in [4, 6, 9, 11] and day > 30:
            continue
        if month == 2:
            # if leap year
            if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
                if day > 29:
                    continue
            elif day > 28:
                continue

        dates.append(f'{groups[0]}/{groups[1]}/{groups[2]}')

    print(dates)
    pyperclip.copy('\n'.join(dates))

validDates()