"""Practice with using dictionaries"""

__author__: str = "730743185"

"""Inverts the keys and values of a dict"""


def invert(base: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    for key in base:
        if base[key] in new_dict:
            raise KeyError("Cant have identical Keys!")
        new_dict[base[key]] = key
    return new_dict


"""Returns the color that appears most in dictionary"""


def favorite_color(base: dict[str, str]) -> str:
    counter: dict[str, int] = {}
    max: int = 0
    for key in base:
        if not base[key] in counter:
            counter[base[key]] = 1
        else:
            counter[base[key]] += 1
    for key in counter:
        if counter[key] > max:
            max = counter[key]
    for key in counter:
        if counter[key] == max:
            return key
        # ensures empty dictionary will still cause something to be returned
    return ""


"""returns a count of the num of times a value appeared in list"""


def count(database: list[str]) -> dict[str, int]:
    empty_dict: dict[str, int] = {}
    for i in database:
        if i in empty_dict:
            # raises the count by 1 if it is present in the list
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    return empty_dict


"""Produce a dict with each word being placed with its first letter"""


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    final: dict[str, list[str]] = {}
    for word in words:
        if not word[0] in final:
            # creates letter key if letter not already created and assigns space for word to be added
            final[word[0]] = []
        for key in final:
            if word not in final:
                if word[0].lower() == key:
                    # adds word to corresponding letter in list. Hard to find correct syntax with .append and .lower
                    final[key].append(word)
    return final


"""Mutates a dict if needed to add dates or students"""


def update_attendance(data: dict[str, list[str]], day: str, student: str) -> None:
    if day not in data:
        # if the day not in the data, you know the day AND the student needs to be added
        data[day] = []
        data[day].append(student)
    elif student not in data[day]:
        data[day].append(student)
