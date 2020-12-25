def runner(func, sample, expected, input, answer=None):
    assert func(sample) == expected
    ans = func(input)
    if answer:
        assert ans == answer