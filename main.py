import argparse
import sys

from util.args import Arguments

def main():
    try:
        parser = Arguments()
        args = parser.parse()

        if args.summary:

            if args.json_path == None:
                raise TypeError('No --json_path argument provided. Use --h for more information.')

            
            if args.month == None:
                raise TypeError('No --month argument provided. Use --h for more information.')
            if args.month not in {'January', 'February', 'March', 'April', 'May', 'June', 
                              'July', 'August', 'September', 'October', 'November', 'December'}:
                raise ValueError('The --month input provided does not exist. Use --h for more information.')
            
            if args.year == None:
                raise TypeError('No --year argument provided. Use --h for more information.')

                


        if not args.summary:
            raise TypeError("No --summary argument provided. Use --h for more information.")


    except (TypeError, ValueError) as exception_info:
        print(exception_info)
        sys.exit(1)

if __name__ == '__main__':
    main()
