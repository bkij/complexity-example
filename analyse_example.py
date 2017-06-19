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
    print("Estimated maximum number of elems sorted in 30 seconds: ", complexity_info.estimate_max_n(30))
    print("Estimated time needed to sort 10000 elements: ", complexity_info.estimate_time(10000))
    
if __name__ == '__main__':
    main()
