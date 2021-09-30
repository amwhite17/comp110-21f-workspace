"""Example of Writing a Function to Process a List."""


def main() -> None: 
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """return true iff needle is found in the haystack, False otherwise.""" 
        #move through each item inlist untill needle found
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1

    return False
    

if __name__ == "__main__":
    main()