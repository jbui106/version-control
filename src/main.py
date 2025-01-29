import datetime

def write_version():
    # Get current date/time
    now = datetime.datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    # Path to version.md file (assuming you want it in docs or whichever folder was "appropriate")
    version_file = "../docs/version.md"

    with open(version_file, "w") as f:
        f.write(f"Current version (date/time): {formatted_now}\n")

if __name__ == "__main__":
    write_version()
    print("version.md updated with current date/time!")

