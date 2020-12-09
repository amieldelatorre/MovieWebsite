class Actor:
    def __init__(self, full_name: str):
        if full_name == "" or type(full_name) is not str:
            self.__full_name = None
        else:
            self.__full_name = full_name.strip()

    @property
    def full_name(self) -> str:
        return self.__full_name

    def __repr__(self):
        return f"<Actor {self.__full_name}>"

    def __eq__(self, other):
        if self.__full_name == other.full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__full_name < other.full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__full_name)

