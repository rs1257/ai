from math import inf

STAMP_DUTY_BANDS = (
    (125_000, 0.00),
    (725_000, 0.05),
    (inf, 0.15),
)


def stamp_duty_calculator(property_price: float) -> float:
    if not isinstance(property_price, (int, float)):
        raise ValueError("property_price must be a number")

    if property_price < 0:
        raise ValueError("property_price must be a positive number")

    if property_price == 0:
        return 0.0

    total_stamp_duty = 0.0
    previous_threshold = 0

    for band_limit, rate in STAMP_DUTY_BANDS:
        if property_price <= previous_threshold:
            break

        taxable_amount = min(property_price, band_limit) - previous_threshold
        total_stamp_duty += taxable_amount * rate
        previous_threshold = band_limit

    return total_stamp_duty


if __name__ == "__main__":
    stamp_duty = stamp_duty_calculator(1_000_000)
    print(f"£{stamp_duty:,.2f}")