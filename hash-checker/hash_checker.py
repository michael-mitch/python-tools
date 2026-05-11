import hashlib
import os

# ===========================
#     HASH CHECKER TOOL
# ===========================

def print_header():
    """Display the main header for the tool."""
    print("\n===========================")
    print("     HASH CHECKER TOOL")
    print("===========================\n")

def list_algorithms():
    """Return a dictionary mapping menu choices to hashlib algorithm names."""
    return {
        "1": "md5",
        "2": "sha1",
        "3": "sha224",
        "4": "sha256",
        "5": "sha384",
        "6": "sha512",
        "7": "sha3_256",
        "8": "shake_128",
        "9": "shake_256"
    }

def print_algorithms():
    """Print the list of supported hashing algorithms."""
    print("\nSelect a hashing algorithm:\n")
    print(" 1) MD5")
    print(" 2) SHA‑1")
    print(" 3) SHA‑224")
    print(" 4) SHA‑256")
    print(" 5) SHA‑384")
    print(" 6) SHA‑512")
    print(" 7) SHA‑3 (256)")
    print(" 8) SHAKE‑128 (variable length)")
    print(" 9) SHAKE‑256 (variable length)\n")

def compute_hash(file_path, algorithm):
    """
    Compute the hash of a file using the selected algorithm.
    Handles SHAKE algorithms separately because they require an output length.
    """
    try:
        hash_obj = hashlib.new(algorithm)
    except ValueError:
        return None, "Unsupported algorithm."

    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to support large files
            while chunk := f.read(8192):
                hash_obj.update(chunk)
    except FileNotFoundError:
        return None, "File not found."
    except PermissionError:
        return None, "Permission denied."

    # SHAKE algorithms require a user‑provided output length
    if algorithm.startswith("shake"):
        length = input("Enter SHAKE output length (in bytes): ").strip()
        if not length.isdigit():
            return None, "Invalid length for SHAKE output."
        return hash_obj.hexdigest(int(length)), None

    # Standard algorithms return a fixed-length digest
    return hash_obj.hexdigest(), None

def main_menu():
    """Display the main menu and return the user's choice."""
    print_header()
    print("1) Hash a File")
    print("2) Exit\n")
    return input("Select an option: ").strip()

def main():
    """Main program loop."""
    while True:
        choice = main_menu()

        if choice == "1":
            print_algorithms()
            alg_choice = input("Select algorithm: ").strip()

            algorithms = list_algorithms()
            if alg_choice not in algorithms:
                print("\nInvalid selection.\n")
                continue

            algorithm = algorithms[alg_choice]
            file_path = input("\nEnter file path: ").strip()

            print("\nHashing file... please wait.\n")
            result, error = compute_hash(file_path, algorithm)

            if error:
                print(f"Error: {error}\n")
                continue

            print(f"Computed Hash ({algorithm}):\n{result}\n")

            # Optional known-hash comparison
            known = input("Enter known hash to compare (or press Enter to skip): ").strip()
            if known:
                if known.lower() == result.lower():
                    print("\n✔ Hashes match!\n")
                else:
                    print("\n✘ Hashes do NOT match.\n")

        elif choice == "2":
            print("\nExiting... Goodbye!\n")
            break

        else:
            print("\nInvalid option.\n")

if __name__ == "__main__":
    main()
