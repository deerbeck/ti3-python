from abc import ABC, abstractmethod

class Handler(ABC):
    
    def __init__(self, name_) -> None:
        self.__name = name_
    
    @property
    def name(self):
        return self.__name
    
    @abstractmethod
    def emit(self, message):
        pass

class FileHandler(Handler):

    def __init__(self, name_, fname_) -> None:
        super().__init__(name_)
        self.__fname = fname_

    def emit(self, message):
        with open(self.__fname, "a") as ffile:
            ffile.write(f"{self.name}: {message}\n")

class ConsoleHandler(Handler):

    def __init__(self, name_) -> None:
        super().__init__(name_)
    
    def emit(self, message):
        print(f"{self.name}: {message}\n")

class Logger():
    __id : int = 1


    def __init__(self) -> None:
        self.__handler = []
        self.__oid = Logger.__id
        Logger.__id +=1
    
    def addhandler(self, handler: Handler) -> None:
        self.__handler.append(handler)
    
    def log(self, message:str):
        for handler in self.__handler:
            handler.emit(message)
    def __str__(self):
        return f"Logger: {self.__oid}"
    
if __name__ == "__main__":
    logger = Logger()
    console = ConsoleHandler('stdout')
    file = FileHandler('local', 'AUFGABE05.log')
    logger.addhandler(console)
    logger.addhandler(file)

    logger.log("Das ist ein Test")