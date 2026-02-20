def classify_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"

    elif fingers == [1, 0, 0, 0, 0]:
        return "THUMB_UP"

    elif fingers == [0, 0, 0, 0, 1]:
        return "PINKY"

    elif fingers == [1, 1, 1, 1, 1]:
        return "PALM"

    elif fingers == [0, 1, 1, 0, 0]:
        return "TWO_FINGERS"

    else:
        return "UNKNOWN"
