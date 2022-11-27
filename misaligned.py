from colorCode import printColorCodeManual, getColorCodeIndex

result = printColorCodeManual()
assert result == 25, "color-code manual does not have 25 pairs"
assert getColorCodeIndex("White","Blue") == 1, "color code index is not matching with given pair of colors"
