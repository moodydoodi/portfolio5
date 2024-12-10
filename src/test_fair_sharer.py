from fair_sharer import fair_sharer

def test_fair_sharer():
    # Test 1: Single iteration
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    # Test 2: Two iterations
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    # Test 3: No iterations
    assert fair_sharer([1, 2, 3], 0) == [1, 2, 3]
    # Test 4: all values equal
    assert fair_sharer([100, 100, 100], 1) == [100, 100, 100]