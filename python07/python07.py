"""
Program filters a given file or annotates its lines according
to certain rules (see README).
"""
from abc import ABC, abstractmethod
import sys
from manager import FileManager
from enum import Enum
import re


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass


class Ends_With_A_Dot(Filter):
    def name(self) -> str:
        return 'FP001'

    def matches(self, line: str) -> bool:
        """"Check if line ends with '.' """
        return line.endswith('.')


class Less_Than_100_Characters(Filter):
    def name(self) -> str:
        return 'FP002'

    def matches(self, line: str) -> bool:
        """"Check if line has less than 100 characters """
        return len(line) < 100


class Five_A_Letters(Filter):
    def name(self) -> str:
        return 'FP003'

    def matches(self, line: str) -> bool:
        """"Check if line contains at least 5 'a' letters """
        return line.count('a') >= 5


class Three_Z_Letters(Filter):
    def name(self) -> str:
        return 'FN201'

    def matches(self, line: str) -> bool:
        """"Check if line has more then 3 'z' letters """
        return line.count('z') > 3


class Check_For_Empty_Line(Filter):
    def name(self) -> str:
        return 'FN202'

    def matches(self, line: str) -> bool:
        """"Check if line is empty"""
        return len(line.rstrip()) == 0


class Only_Non_Letter_Characters(Filter):
    def name(self) -> str:
        return 'FN203'

    def matches(self, line: str) -> bool:
        """Check if line consists only from non-letter characters"""
        return len(line.strip()) > 0 and not re.search("[A-Za-z]", line.rstrip())


class Display_Rules(Enum):
    """Collect all display rules into one class using Enum module."""
    FP001 = Ends_With_A_Dot()
    FP002 = Less_Than_100_Characters()
    FP003 = Five_A_Letters()


class Dont_Display_Rules(Enum):
    """Collect all non-display rules into one class using Enum module."""
    FN201 = Three_Z_Letters()
    FN202 = Check_For_Empty_Line()
    FN203 = Only_Non_Letter_Characters()


class Option(ABC):
    """Depending on user choice, each rule implements by extending the following abstraction"""

    @abstractmethod
    def get_lines_from_file(self, file):
        pass

    @staticmethod
    def get_option(choice: str):
        if choice == "filter":
            return Display_Filter()
        if choice == "annotate":
            return Display_Annotate()
        else:
            raise ValueError


class Display_Filter(Option):
    """
    Using 'filter' method, the program will display lines according to the rules.
    In addition, the 'display' rules have a priority over the 'non-display' rules.
    """

    def __init__(self):
        self.lines_from_file = []

    def get_lines_from_file(self, file) -> list:
        with FileManager(file, 'r') as f:
            data = f.read().splitlines()
            for line in data:
                self.lines_from_file.append(line)
        return self.lines_from_file

    def use_filter(self):
        for line in self.lines_from_file:
            display_lines = 0
            not_display_lines = 0

            for rule in Display_Rules:
                if rule.value.matches(line):
                    display_lines += 1

            for rule in Dont_Display_Rules:
                if rule.value.matches(line):
                    not_display_lines += 1

            if display_lines >= not_display_lines:
                print(line)


class Display_Annotate(Option):
    """
    Using 'annotate' method, the program will display information about which rules
    are applicable for each line as follows: <line number>: [rule].
    """

    def __init__(self):
        self.lines_from_file = []

    def get_lines_from_file(self, file) -> list:
        with FileManager(file, 'r') as f:
            data = f.read().splitlines()
            for line in data:
                self.lines_from_file.append(line)
        return self.lines_from_file

    def use_filter(self):
        num_line = 0
        for line in self.lines_from_file:
            num_line += 1
            rules_in_line = []
            for rule in Display_Rules:
                if rule.value.matches(line):
                    rules_in_line.append(rule.value.name())

            for rule in Dont_Display_Rules:
                if rule.value.matches(line):
                    rules_in_line.append(rule.value.name())

            print(f"{num_line} : {' '.join(rules_in_line)}")


if __name__ == '__main__':
    start = Option.get_option(sys.argv[1])
    path = sys.argv[2]
    start.get_lines_from_file(path)
    start.use_filter()
