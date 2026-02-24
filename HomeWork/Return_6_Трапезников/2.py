def boundares(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit

low_limit, high_limit = boundares(100, 20)
print(f"Нижний предел {low_limit}, верхний предел: {high_limit}")
