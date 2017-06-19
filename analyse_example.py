#!/usr/bin/env python3
import argparse
from complexity import ComplexityAnalyser

def parse_args():
    parser = argparse.ArgumentParser(description="Analyse countingSort time complexity")
    parser.add_argument('--timeout', dest='timeout', type=int, default=30)
    parser.add_argument('--log-file', dest='log_file', type=str, default=None)
    return parser.parse_args()

def main():
    args = parse_args()
    analyser = ComplexityAnalyser(
        "data.py", "algo.py", "cleanup.py",
        timeout=args.timeout,
        log_file=args.log_file
    )
    complexity_info = analyser.get_complexity_info()
    print("Time class: ", complexity_info.complexity_class)
    
if __name__ == '__main__':
    main()
