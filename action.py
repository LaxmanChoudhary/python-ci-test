from datetime import datetime

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(f"Running the action at {datetime.now()}")