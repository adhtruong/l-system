from enum import Enum
from typing import Dict, List, Type, TypeVar


Alphabet = TypeVar("Alphabet", bound=Enum)


class LSystem:
    def __init__(
        self,
        alphabet: Type[Alphabet],
        rules: Dict[Alphabet, List[Alphabet]],
        allow_constants: bool = True,
    ) -> None:
        self._alphabet = alphabet
        self._rules = rules
        for symbol in list(self._alphabet):
            if symbol in self._rules:
                continue

            if not allow_constants:
                raise ValueError(f"Rule for {symbol} not defined")

            self._rules[symbol] = [symbol]

    def iterate(self, current: List[Alphabet]) -> List[Alphabet]:
        output = []
        for symbol in current:
            try:
                successor = self._rules[symbol]
            except KeyError:
                raise ValueError(f"{symbol} is not valid")
            output.extend(successor)
        return output
