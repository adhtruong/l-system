from enum import Enum
from typing import Dict, List, Type, TypeVar

Alphabet = TypeVar("Alphabet", bound=Enum)
Rules = Dict[Alphabet, List[Alphabet]]


def iterate(current: List[Alphabet], rules: Rules, allow_constants: bool = True) -> List[Alphabet]:
    output = []
    for symbol in current:
        try:
            successor = rules[symbol]
        except KeyError:
            if allow_constants:
                output.append(symbol)
                continue
            raise ValueError(f"{symbol} is not valid")
        output.extend(successor)
    return output


class LSystem:
    def __init__(
        self, alphabet: Type[Alphabet], rules: Dict[Alphabet, List[Alphabet]], allow_constants: bool = True
    ) -> None:
        self._alphabet = alphabet
        self._rules = rules
        for symbol in list(self._alphabet):
            if symbol in self._rules:
                continue

            if not allow_constants:
                raise ValueError(f"Rule for {symbol} not defined")

            self._rules[symbol] = [symbol]

    @property
    def alphabet(self) -> Type[Alphabet]:
        return self._alphabet

    @property
    def rules(self) -> Rules:
        return self._rules

    def iterate(self, current: List[Alphabet]) -> List[Alphabet]:
        output = []
        for symbol in current:
            try:
                successor = self._rules[symbol]
            except KeyError:
                raise ValueError(f"{symbol} is not valid")
            output.extend(successor)
        return output
