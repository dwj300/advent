def runner(func, sample, expected, input, answer=None):
    assert func(sample) == expected
    print(func(input))
    if answer:
        assert func(input) == answer