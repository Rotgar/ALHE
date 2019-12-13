import unittest

from src.algorithm import GeneticAlgorithm
from src.algorithm.Individual import Individual


class TestGeneticAlgorithmFunctions(unittest.TestCase):
    def test_is_correct_should_return_0(self):
        GeneticAlgorithm.INPUT_GRADE_ARRAY = [2, 3, 5, 2, 1, 4, 6]
        input_array = [1, 4, 6, 3, 2, 5, 6]
        result = GeneticAlgorithm.is_correct(input_array)
        self.assertEqual(0, result)

    def test_is_correct_should_return_1(self):
        GeneticAlgorithm.INPUT_GRADE_ARRAY = [2, 3, 5, 2, 1, 4, 6]
        input_array = [1, 4, 3, 3, 2, 5, 6]
        result = GeneticAlgorithm.is_correct(input_array)
        self.assertEqual(1, result)

    def test_select_best_for_next_generation_omit_repetition(self):
        GeneticAlgorithm.POPULATION_SIZE = 30
        GeneticAlgorithm.INPUT_GRADE_ARRAY = [2, 3, 5, 2, 1, 4, 6]
        actual_array = [Individual([3, 4, 5, 2, 1, 5, 6]),
                        Individual([3, 4, 5, 2, 1, 2, 3]),
                        Individual([3, 4, 5, 2, 1, 2, 3]),
                        Individual([3, 4, 5, 2, 1, 3, 4])]
        new_array = []
        GeneticAlgorithm.select_best_for_next_generation(new_array, actual_array)
        self.assertEqual(3, len(new_array))

    def test_select_best_for_next_generation_add_only_required_amount(self):
        GeneticAlgorithm.POPULATION_SIZE = 30
        GeneticAlgorithm.INPUT_GRADE_ARRAY = [2, 3, 5, 2, 1, 4, 6]
        actual_array = [Individual([3, 4, 5, 2, 1, 5, 6]),
                        Individual([3, 4, 5, 2, 1, 2, 3]),
                        Individual([3, 4, 5, 2, 1, 3, 4]),
                        Individual([3, 4, 5, 2, 1, 5, 6])]
        new_array = []
        GeneticAlgorithm.select_best_for_next_generation(new_array, actual_array)
        self.assertEqual(3, len(new_array))


if __name__ == "__main__":
    unittest.main()
