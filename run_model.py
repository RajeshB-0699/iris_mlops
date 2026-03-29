import argparse
import json
from pathlib import Path
import numpy as np
import joblib

MODEL_PATH = Path("artifacts/model.pkl")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",required = True, help = "Feature list as json string")
    args = parser.parse_args()

    try:
        features = json.loads(args.input)
    except json.JSONDecodeError:
        raise ValueError("invalid Input. Use JSON list")

    x = np.array(features).reshape(1,-1)

    model = load_model()
    pred = model.predict(x)

    print(json.dumps({"prediction": pred.tolist()}))
    
if __name__ == "__main__":
    main()


