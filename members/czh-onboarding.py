#!/usr/bin/env python3
"""CZH local onboarding menu. Does not collect or transmit personal data."""

def main():
    print("\n=== CZH MEMBER CENTER ===")
    print("1. Learn about joining")
    print("2. Show local member count")
    print("3. Exit")

    try:
        choice = input("Select: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        return

    if choice == "1":
        print("CZH membership information:")
        print("Use the official project documentation to join.")
        print("This starter release does not submit registration.")
    elif choice == "2":
        print("No public member registry is configured in this release.")
    elif choice == "3":
        print("Member Center closed.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
