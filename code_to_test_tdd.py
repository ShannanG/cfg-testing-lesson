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


def average_exam_score(student_marks):
    # delete this pass once you start coding
    # pass
    # store the number of results entries we have (how many there are, not the sum of all the marks)
    num_of_results = len(student_marks)

    # create a list to store the marks
    marks_list = []
    # loop through the student marks parameter
    for result in student_marks:

    # try to assign a mark variable for each student_mark in student_marks
        try:
            mark = int(result['mark'])
    # handle a KeyError exception with except
        except KeyError:
    # and set the mark to 5
            mark = 5
    # raise a Value Error if the mark is not in the valid range (less than 10, more than one)
        if not 10 > mark > 1:
            raise ValueError('mark is not in range')
    # add mark to the marks list
        marks_list.append(mark)

    # return the average mark
        return sum(marks) / num_of_results

