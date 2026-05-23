from src.sample.sampler import reservoir_sample

def test_sampler():
    rows = [[str(i)] for i in range(100)]
    sampled = reservoir_sample(rows, k=5)
    assert len(sampled) == 5
