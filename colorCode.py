major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def getColorCodeIndex(majorColor, minorColor):
    return major_colors.index(majorColor) * 5 + minor_colors.index(minorColor)

def printColorCodeManual():
    for indexMajor, majorColor in enumerate(major_colors):
        for indexMinor, minorColor in enumerate(minor_colors):
            print(f' {getColorCodeIndex(majorColor, minorColor)} | {majorColor} | {minorColor}')
    return len(major_colors) * len(minor_colors)