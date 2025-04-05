import argparse
from conversions.temperature import c_to_f, f_to_c
from conversions.distance import km_to_miles, miles_to_km

def main():
    parser = argparse.ArgumentParser(description="Multi-Unit Converter CLI")
    subparsers = parser.add_subparsers(dest='command', help='Conversion command')

    # Temperature conversion parser
    temp_parser = subparsers.add_parser('temp', help='Temperature conversion')
    temp_parser.add_argument('--mode', choices=['c2f', 'f2c'], required=True,
                             help='Conversion mode: c2f (Celsius to Fahrenheit) or f2c (Fahrenheit to Celsius)')
    temp_parser.add_argument('value', type=float, help='Temperature value to convert')

    distance = subparsers.add_parser('distance', help='Distance conversion')
    distance.add_argument('--mode', choices=['k2m','m2k'], required=True,
                          help='Conversion mode: k2m (Kilometers to Miles) or m2k (Miles to Kilometers)')
    args = parser.parse_args()

    if args.command == 'temp':
        if args.mode == 'c2f':
            result = c_to_f(args.value)
            print(f"{args.value}°C is {result:.2f}°F")
        elif args.mode == 'f2c':
            result = f_to_c(args.value)
            print(f"{args.value}°F is {result:.2f}°C")
    elif args.command == 'distance':
        if args.mode == "k2m":
            result = km_to_miles(args.value)
            print(f"{args.value} km is {result:.2f} miles")
        elif args.mode == "m2k":
            result = miles_to_km(args.value)
            print(f"{args.value} miles is {result:.2f} km")

if __name__ == "__main__":
    main()
