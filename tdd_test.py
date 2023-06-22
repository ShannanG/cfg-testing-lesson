"""
Let's write a test for our function first and then will write an actual code to ensure that
all tests pass.

Task
Given a list of dictionaries where keys are student's  name and student's mark.
calculate the average score for the exam.

If mark is not within the range 1 to 10, raise an error
Some mark values can be integers and some are strings, we need to process both
If mark is missing, use value 5

"""


from code_to_test_tdd import average_exam_score
# Do the two files (code to test and test) need to be in the same folder for the import to work?
class TestAverageExamScore(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': '8'},
        ]
        expected = 7.25  # (8+8+6+7) / 4

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_missing_mark(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha',},
            {'name': 'Zac', 'mark': '8'},
        ]
        expected = 6.5  # (8+5+6+7) / 4 --> use 5 if mark is missing

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_error_raised(self):
        my_input = [
            {'name': 'Jane', 'mark': 15},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', },
            {'name': 'Zac', 'mark': '8'},
        ]
        with self.assertRaises(ValueError):
            average_exam_score(my_input)


if __name__ == '__main__':
    main()
