"""Examples of importing python."""


from lessons import helpers

# alias a module / importanted name as another name
from lessons import helpers as hp

# import names defined globally in a module
from lessons.helpers import powerful


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()