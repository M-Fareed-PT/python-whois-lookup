import whois

def menu():
    print("\n====== PYTHON WHOIS LOOKUP TOOL ======")
    print("1. Perform WHOIS Lookup")
    print("2. Exit")
    print("=====================================")

def whois_lookup():
    print("\n--- WHOIS LOOKUP MODE ---")
    domain = input("Enter domain (e.g. google.com): ").strip()

    if not domain:
        print("\n❌ Domain cannot be empty.")
        input("\nPress Enter to return to menu...")
        return

    try:
        data = whois.whois(domain)

        print("\n========== WHOIS RESULT ==========")
        print(f"Domain Name      : {data.domain_name}")
        print(f"Registrar        : {data.registrar}")
        print(f"Creation Date    : {data.creation_date}")
        print(f"Expiration Date : {data.expiration_date}")
        print(f"Name Servers     : {data.name_servers}")
        print(f"Country          : {data.country}")
        print("==================================")

    except Exception as e:
        print("\n❌ WHOIS Lookup Failed.")
        print("Error:", e)

    input("\nPress Enter to return to menu...")

def main():
    while True:
        menu()
        choice = input("Select option (1-2): ").strip()

        if choice == "1":
            whois_lookup()

        elif choice == "2":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid selection. Try again.")

if __name__ == "__main__":
    main()
