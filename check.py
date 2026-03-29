import argparse

import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inp", required = True)
    args = parser.parse_args()

    try:
        feat = json.loads(args.inp)
    except Exception as e:
        raise e("unable to")
    
    print(args.inp)
    print(feat)
    
if __name__ == "__main__":
    main()
