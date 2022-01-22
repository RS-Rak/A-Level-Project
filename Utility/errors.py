#this is my class for custom error messages 

class Error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NonExistentEntity(Error):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.message = "This entity does not exist!"