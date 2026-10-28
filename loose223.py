"""Odds and ends."""

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(list(chunks(range(28), 3)))

# works for now
