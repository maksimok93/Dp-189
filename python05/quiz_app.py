"""This questionnaire asks user to write answers in the command line.
The program will ask three questions from each section. Answers can be viewed in a file
quiz_answers.txt and timing statistics in timing.txt."""
from context_manager import FileManager
import functools
import time


def timer(func):
    """Prints the runtime of the decorated function."""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        with FileManager('timing.txt', 'a') as timing_file:
            timing_file.write(f"Finished section in {end_time - start_time:.4f} secs\n")
        return value

    return wrapper_timer


def create_questions_list(questions_from_section) -> list:
    """This function creates the list of questions after opening the file with questions
    data in the main block."""
    questions = []
    for line in questions_from_section.read().splitlines():
        questions.append(line)
    return questions


@timer
def start_quiz(questions) -> list:
    """
    After the user answers, function creates the list which will contain data with each
    question and user answers.
    """
    answers_list = []
    for question in questions:
        answer = input(question + ' ')
        answers_list.append(f'{question} : {answer}')
    return answers_list


if __name__ == '__main__':
    start_time_quiz = time.perf_counter()
    section_files = ['section1.txt', 'section2.txt']

    for file in section_files:
        with FileManager(file, 'r') as questions_from_section:
            answers_output = start_quiz(create_questions_list(questions_from_section))
            with FileManager('quiz_answers.txt', 'a') as answers_file:
                for record in answers_output:
                    answers_file.write(record + "\n")
    end_time_quiz = time.perf_counter()

    with FileManager('timing.txt', 'a') as timing_file:
        timing_file.write(f"Finished quiz in {end_time_quiz - start_time_quiz:.4f} secs\n")
