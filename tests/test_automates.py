import importlib.util
from pathlib import Path
import unittest


def _load_function(file_path: Path, func_name: str):
    """Load a function from a standalone Python file."""
    spec = importlib.util.spec_from_file_location(func_name, file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return getattr(module, func_name)


ROOT = Path(__file__).resolve().parent.parent
LIRELETTRE_PATH = ROOT / "1.3_automates" / "lirelettre.py"
LIREMOT_PATH = ROOT / "1.3_automates" / "liremot.py"

lirelettre = _load_function(LIRELETTRE_PATH, "lirelettre")
liremot = _load_function(LIREMOT_PATH, "liremot")


class AutomateTests(unittest.TestCase):
    def setUp(self):
        # Automate where every letter has a defined transition to avoid infinite loops.
        self.transitions = [
            [0, "a", 1],
            [0, "b", 0],
            [1, "a", 1],
            [1, "b", 2],
            [2, "a", 2],
            [2, "b", 0],
        ]
        self.states = [0, 1, 2]

    def test_lirelettre_collects_reachable_states(self):
        reachable = lirelettre(self.transitions, [0, 1], "a")
        self.assertCountEqual(reachable, [1, 1])  # 0->1 and 1->1

    def test_lirelettre_returns_empty_when_no_match(self):
        reachable = lirelettre(self.transitions, [2], "c")
        self.assertEqual(reachable, [])

    def test_liremot_reads_word_from_initial_states(self):
        end_states = liremot(self.transitions, [0], "aba")
        self.assertEqual(end_states, [2])

    def test_liremot_handles_multiple_initial_states(self):
        end_states = liremot(self.transitions, [0, 1], "ba")
        # From 0 with "ba": 0 -b-> 0 -a-> 1
        # From 1 with "ba": 1 -b-> 2 -a-> 2
        self.assertCountEqual(end_states, [1, 2])


if __name__ == "__main__":
    unittest.main()
