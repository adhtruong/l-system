from typing import Callable, Dict, List, Type, Union

from lsystem.grammar import Alphabet, LSystem, Rules


class LSystemManager:
    def __init__(
        self,
        axiom: Union[Alphabet, List[Alphabet]],
        lsystem: LSystem,
        reset_method: Callable[[], None],
        render_methods: Dict[Alphabet, Callable[[], None]],
    ):
        self._axiom = axiom if isinstance(axiom, list) else [axiom]
        self._state = self._axiom
        self._lsystem = lsystem
        self._reset_method = reset_method
        self._render_methods = render_methods
        for symbol in self._lsystem.alphabet:
            if symbol in render_methods:
                continue

            raise ValueError(f"No render method for {symbol}")

    @property
    def state(self):
        return self._state

    def reset(self):
        self._state = self._axiom
        self._reset_method()

    def _iterate_state(self) -> None:
        self._state = self._lsystem.iterate(self._state)

    def iterate(self, n: int = 1) -> None:
        for _ in range(n):
            self._iterate_state()

    def render(self) -> None:
        for symbol in self._state:
            self._render_methods[symbol]()
