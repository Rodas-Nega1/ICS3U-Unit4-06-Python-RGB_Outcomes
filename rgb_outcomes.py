# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program outputs 255 ^ 3 RGB outcomes


def main():
    # this function has nested loops that outputs 255 ^ 3 outcomes

    # loop variables
    red_counter = 0
    green_counter = 0
    blue_counter = 0

    for red_counter in range(256):
        for green_counter in range(256):
            for blue_counter in range(256):
                print(
                    "RGB({0}, {1}, {2})".format(
                        red_counter, green_counter, blue_counter
                    )
                )

    print("\nDone.")


if __name__ == "__main__":
    main()
