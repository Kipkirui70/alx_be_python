def safe_divide(numerator, denominator):
    """Performs safe division with error handling for invalid inputs and zero division."""

    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try dividing
        try:
            result = num / den
