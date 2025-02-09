# validator.add_check(lambda x: isinstance(x, int))
#     assert validator.is_valid(5)
#     assert not validator.is_valid("value")

#     validator.add_check(lambda x: x > 10)
#     validator.add_check(lambda x: x % 2 == 0)
#     assert validator.is_valid(12)
#     assert not validator.is_valid(8)
#     assert not validator.is_valid(21)