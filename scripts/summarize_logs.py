# summarize_logs.py
import sys

def extract_errors(log_lines):
    errors = []
    capture = False
    for line in log_lines:
        if "ERROR" in line or "Exception" in line or "FAILURE" in line:
            capture = True
        if capture:
            errors.append(line)
            if line.strip() == "":
                capture = False
    return errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 summarize_logs.py build.log")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as f:
            log = f.readlines()

        errors = extract_errors(log)
        if not errors:
            print("❗ No specific error patterns found in logs.")
        else:
            print("🔴 Build Failed Summary (AI-Free):")
            for line in errors[-10:]:
                print(line.strip())
    except Exception as e:
        print(f"Failed to summarize logs: {e}")
