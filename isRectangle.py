def rectangle(value):
    if len(value) > 4:
        raise ValueError(
            "It\'s not a rectangle because it has more than 4 sides")
    if len(value) < 4:
        raise ValueError(
            "It\'s not a rectangle because it\'s less than 4 sides")
    if (value[0] == value[2]) and (value[1] == value[3]):
        return "Form a rectangle"
    else:
        raise ValueError("Cannot form a rectangle")


if __name__ == "__main__":
    try:
        print("**Enter numbers in order of top, right, bottom and left with a comma separator**")
        value = [int(x) for x in input("Enter value: ").split(",")]
        isRectangle = rectangle(value)
        print("\n",isRectangle)
    except ValueError as err:
        print("\n",err)
