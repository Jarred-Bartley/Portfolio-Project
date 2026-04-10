def read_number(prompt):
    while True:
        try:
            s = input(prompt)
            if s.strip() == "":
                raise ValueError()
            if "." in s or "e" in s.lower():
                return float(s)
            return int(s)
        except ValueError:
            print("Invalid number, please try again.")