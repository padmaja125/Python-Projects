class Error(BaseException):
    def __str__(self):
        return "Error"


class EnteredValueError(Error) :
    def __str__(self):
        return "Incorrect Password"


class TypedWrong(Error):
    def __str__(self):
        return "no character allowed"


class SomethingWrong(Error):
    def __str__(self):
        return "Something went wrong"

