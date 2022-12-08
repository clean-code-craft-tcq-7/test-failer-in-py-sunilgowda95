major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def getMaxLengthOfColours():
    maxLength = 0
    for eachColorGourp in [major_colors, minor_colors]:
        maxLength = len(max(eachColorGourp, key=len)) if len(max(eachColorGourp, key=len)) > maxLength else maxLength
    return maxLength
maxLengthColorString = 0
maxLengthColorString = getMaxLengthOfColours()

def spaceAlignedString(inStr):
    return inStr.ljust(maxLengthColorString)

def getColorCodeIndex(majorColor, minorColor):
    return str(major_colors.index(majorColor) * 5 + minor_colors.index(minorColor)+1).zfill(2)

def printColorCodeManual():
    for indexMajor, majorColor in enumerate(major_colors):
        for indexMinor, minorColor in enumerate(minor_colors):
            print(f' {getColorCodeIndex(majorColor, minorColor)} | {spaceAlignedString(majorColor)} | {spaceAlignedString(minorColor)}')
    return len(major_colors) * len(minor_colors)