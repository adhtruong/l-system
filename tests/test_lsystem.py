from enum import Enum
from unittest import TestCase

from lsystem import LSystem


class Alphabet(Enum):
    A = "A"
    B = "B"


class TestLSystem(TestCase):
    def test_algae(self):
        lsystem = LSystem(Alphabet, {Alphabet.A: [Alphabet.A, Alphabet.B], Alphabet.B: [Alphabet.A]})
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
