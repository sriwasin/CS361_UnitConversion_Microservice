# Author: sriwasin
# Convert Unit Microservice

import time
from fractions import Fraction

# Global var
CONVERT_MICRO_PIPE = 'convert_micro_pipe.txt'

# Data
convert_table = {
    "currency": {
        "JPY": {
            "USD": 0.0063,
            "EUR": 0.0055,
            "CNY": 0.043
        },
        "EUR": {
            "USD": 1.15,
            "JPY": 182.60,
            "CNY": 7.89
        },
        "CNY": {
            "USD": 0.15,
            "JPY": 23.15,
            "EUR": 0.13
        },
    "time": {
        "seconds": {
            "minutes": Fraction(1, 60)
        },
        "minutes": {
            "hours": Fraction(1, 60)
        },
        "hours": {
            "1_day": Fraction(1, 24),
            "30_days": Fraction(1, 720),
            "31_days": Fraction(1, 744)
        }
        }
    }
}


def clean_pipes():
    with open(CONVERT_MICRO_PIPE, "w") as bus:
        pass


def convert_unit(conversion_type, original_unit, target_unit, original_val):
    new_value = original_val * convert_table[conversion_type][original_unit][target_unit]
    return new_value


def main():
    print("-----------------------------------------")
    print("UnitConversion Microservice: ACTIVE (Polling)")
    print("-----------------------------------------")
    while True:
        try:
            with open(CONVERT_MICRO_PIPE, "r+") as bus:
                bus.seek(0)
                request = bus.read().strip()

                if not request:
                    time.sleep(0.1)
                    continue

                request_decon = request.split(",")
                if len(request) >= 6:
                    if request_decon[0] == "request" and request_decon[5] == "pending":
                        # Read request
                        conversion_type = request_decon[1]
                        original_unit = request_decon[2]
                        target_unit = request_decon[3]
                        original_val = float(request_decon[4])
                        new_value = convert_unit(conversion_type, original_unit, target_unit, original_val)

                        # Write response
                        bus.seek(0)
                        bus.truncate(0)
                        bus.write(f"response,{new_value},complete")
        except (OSError, IOError):
            time.sleep(0.1)
            continue

        time.sleep(0.1)


if __name__ == "__main__":
    clean_pipes()
    main()
