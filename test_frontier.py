import unittest
import frontier


class TestFrontier(unittest.TestCase):
    def test_create_maze_all_blockers(self):
        expect = [
            list("Sxxxx"),
            list("xxxxx"),
            list("xxxxx"),
            list("xxxxx"),
            list("xxxxG")]

        maze = frontier.Maze(5, 5, 1)
        self.assertEqual(expect, maze.cells)

    def test_create_maze_no_blockers(self):
        expect = [
            list("S    "),
            list("     "),
            list("     "),
            list("     "),
            list("    G")]

        maze = frontier.Maze(5, 5, 0.0)
        self.assertEqual(expect, maze.cells)


class TestLocation(unittest.TestCase):
    def test_location_compare_true(self):
        a = frontier.Location(0, 5)
        b = frontier.Location(0, 5)
        self.assertTrue(a == b)

    def test_location_compare_false(self):
        a = frontier.Location(0, 3)
        b = frontier.Location(1, 1)
        self.assertFalse(a == b)


if __name__ == "__main__":
    unittest.main()
