from enum import Enum
from unittest import TestCase

from grammar import LSystem
from manager import LSystemManager


class Alphabet(Enum):
    A = "A"
    B = "B"


RULES = {Alphabet.A: [Alphabet.A, Alphabet.B], Alphabet.B: [Alphabet.A]}


class TestLSystem(TestCase):
    def test_algae(self):
        lsystem = LSystem(Alphabet, RULES)
        current = [Alphabet.A]
        for expected in (
            [Alphabet.A, Alphabet.B],
            [Alphabet.A, Alphabet.B, Alphabet.A],
            [Alphabet.A, Alphabet.B, Alphabet.A, Alphabet.A, Alphabet.B],
        ):
            current = lsystem.iterate(current)
            self.assertEqual(expected, current)

    def test_constants(self):
        with self.assertRaises(ValueError):
            LSystem(Alphabet, {}, allow_constants=False)

        lsystem = LSystem(Alphabet, {})
        self.assertEqual([Alphabet.A], lsystem.iterate([Alphabet.A]))
        self.assertEqual([Alphabet.A, Alphabet.B], lsystem.iterate([Alphabet.A, Alphabet.B]))


class TestManager(TestCase):
    def test_render(self):
        class Renderer:
            def __init__(self):
                self.output = []

            def add(self, symbol: Alphabet):
                self.output.append(symbol)

            def reset(self):
                self.output = []

        renderer = Renderer()
        render_methods = {Alphabet.A: lambda: renderer.add(Alphabet.A), Alphabet.B: lambda: renderer.add(Alphabet.B)}

        lsystem = LSystem(Alphabet, RULES)
        lsystem_manager = LSystemManager(
            axiom=[Alphabet.A], lsystem=lsystem, reset_method=renderer.reset, render_methods=render_methods
        )
        lsystem_manager.iterate(2)
        expected = [Alphabet.A, Alphabet.B, Alphabet.A]
        self.assertEqual(expected, lsystem_manager.state)
        lsystem_manager.render()
        self.assertEqual(expected, renderer.output)

        lsystem_manager.reset()
        self.assertEqual([], renderer.output)
        self.assertEqual([Alphabet.A], lsystem_manager.state)
