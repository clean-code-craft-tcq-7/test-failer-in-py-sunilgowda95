from colorCode import printColorCodeManual, getColorCodeIndex, getMaxLengthOfColours, spaceAlignedString

assert getMaxLengthOfColours() == 6, "max colour length is not 6"
assert len(spaceAlignedString("Red")) == 6, "String is not space aligned"
assert int(getColorCodeIndex("White","Blue")) == 1, "color code index is not matching with given pair of colors"
assert getColorCodeIndex("White","Blue") == "01", "color code index should be of 2 digits for proper alignment"
result = printColorCodeManual()
assert result == 25, "color-code manual does not have 25 pairs"
print("All is well!!")