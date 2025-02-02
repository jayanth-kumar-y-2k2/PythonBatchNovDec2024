"""
Purpose:

| Network        | IIN (Prefix) | Length |
+----------------+--------------+--------+
|American Express| 34, 37       | 15     |
|Diners Club     | 38, 39       | 14     |

"""

import unittest


def detect_network(card_number: str) -> str | None:
    """Return the card network for card_number"""
    if len(card_number) == 15 and card_number[:2] in ("34", "37"):
        return "American Express"
    elif len(card_number) == 14 and card_number[:2] in ("38", "39"):
        return "Diners Club"
    return None


# Table driven test cases
class TestDetectNetwork(unittest.TestCase):
    TEST_CASES = [
        ("341234567890123", "American Express"),
        ("371234567832423", "American Express"),
        ("38123456789123", "Diners Club"),
        ("39123456787567", "Diners Club"),
        ("3412345678901", None),
        ("37123456789015", None),
    ]

    def test_cases(self):
        for card_number, expected in self.TEST_CASES:
            actual = detect_network(card_number)
            error_msg = (
                f"Card number {card_number} should be {expected} but was {actual}"
            )
            self.assertEqual(actual, expected, error_msg)



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=3)