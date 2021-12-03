def runner(func, sample, expected, input, answer=None):
    assert func(sample) == expected
    ans = func(input)
    print(ans)
    if answer:
        assert ans == answer