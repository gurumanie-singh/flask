# script.py
import argparse, calendar


def main():
    parser = argparse.ArgumentParser(description="CLI Tool to run inside the container")
    parser.add_argument(
        "--name","-name","-n",
        type=str, 
        help="Enter your name.", 
        required=True
    )
    parser.add_argument(
        "--date","-date","-d",
        type=int,
        help="Enter your birth date (1-31).",
        choices=range(1,31),
        default=1,
        required=True
    )
    parser.add_argument(
        "--month","-m",
        type=int,
        help="Enter your birth month (1-12)",
        choices=range(1,12),
        default=1,
        required=True
    )
    parser.add_argument(
        "--year","-y",
        type=int,
        help="Enter your birth year.",
        choices=range(1925,2025),
        default=1,
        required=True
    )

    args = parser.parse_args()

    print(f"Your name is {args.name} and you were born on {args.date} {calendar.month_name[args.month]}, {args.year}!")

if __name__ == "__main__":
    main()