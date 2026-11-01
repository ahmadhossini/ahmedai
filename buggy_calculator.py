"""Small demo module containing one intentional bug.

Expected behavior:
    apply_discount(200, 10) == 180
"""


def apply_discount(price: float, discount_percent: float) -> float:
    """Return the price after applying a percentage discount."""
    # Intentional bug: subtracts the percentage number, not the percentage amount.
    return price - discount_percent


if __name__ == "__main__":
    print(apply_discount(200, 10))  # Expected: 180.0
