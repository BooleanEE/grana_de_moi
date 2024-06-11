import argparse

class Arguments:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Command line argument parser")
        self.parser.add_argument('--json_path', type=str, help='Path to the JSON file with the financial information.', default=None)
        self.parser.add_argument('--month', type=str, help='Target month to show the financial summary (e.g. January, February, ...).', default=None)
        self.parser.add_argument('--summary', action='store_true', help='The software functionality to generate the user financial summary.', default=False)
        self.parser.add_argument('--year', type=str, help='Target year to show the financial summary (e.g. 2024).', default=None)

    def parse(self):
        try:
            arguments = self.parser.parse_args()
            return arguments
        except:
            raise TypeError('No valid argument(s) was(were) provided. Use --h for more information.')
