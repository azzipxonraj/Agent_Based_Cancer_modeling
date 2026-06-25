import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        prog="tumor_sim",
        description="Tumor growth simulation with customizable grid and dynamics.",
        epilog="Example: python3 main.py -rows 50 -cols 50 -t 100"
    )

    parser.add_argument("-r", "--rows", type=int, help="number of rows", default=50)
    parser.add_argument("-c", "--cols", type=int, help="number of columns", default=50)
    parser.add_argument("-t", "--max-steps", type=int, help="maximum number of steps", default=100)

    # add in maybe later. depending on what type of cancer.
    # parser.add_argument("-b", type=int, help="gompertz b", default=100)
    # parser.add_argument("-c", type=int, help="gompertz b", default=100)

    parser.add_argument("-tgc", "--tumor-growth-chance", type=float, help="the chance per day that the"
                                                                          "tumor will grow in size", default=0.001)
    parser.add_argument("-cdt", "--c-doubling-time", type=float, help="the chance per day that the")

    args = parser.parse_args()

    if args.rows <= 1 or args.cols <= 1:
        parser.error("number of rows and columns must be positive and more then 1")

    return args