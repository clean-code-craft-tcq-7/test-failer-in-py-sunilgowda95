from tshirtsCheckSize import checkSize

assert checkSize(37) == 'S', "FAILED : for size == 37. T-Shirt Size should be Small"
assert checkSize(38) == 'M', "FAILED : for size == 38. T-Shirt Size should be Medium"
assert checkSize(40) == 'M', "FAILED : for size == 40. T-Shirt Size should be Medium"
assert checkSize(43) == 'L', "FAILED : for size == 43. T-Shirt Size should be Large"
