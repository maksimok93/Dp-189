"""
In three-point estimation of project, you need to set three variables for each
required task based on previous experience or best assumptions, where:
a = the best-case estimate;
m = the most likely estimate;
b = the worst-case estimate.
"""
import math


class Task:
    """For each single task of project these values are used to calculate an E value for the estimate
    and the standard deviation (SD)."""

    def __init__(self, best_case, most_likely_case, worst_case):
        self.best_case = best_case
        self.most_likely_case = most_likely_case
        self.worst_case = worst_case

    def get_task_estimate(self):
        """
        Estimate is a weighted average which takes into account both the most optimistic
        and most pessimistic estimates provided.
        """
        return round((self.best_case + 4 * self.most_likely_case + self.worst_case) / 6, 0)

    def get_task_sd(self):
        """Task Standard Deviation (SD) measures the variability or uncertainty in the estimate."""
        return round((self.worst_case - self.best_case) / 6, 0)


class Project:
    """The Project class consists of estimable tasks, i.e. of the work breakdown structure. Estimates the expected
    value E(task) and the standard error SE(task) of this estimate for each task time."""

    def __init__(self, task_estimates, task_sd):
        self.task_estimates = task_estimates
        self.task_sd = task_sd

    def get_total_estimate(self):
        """Getting total estimate of our project."""
        return sum(self.task_estimates)

    def get_standard_error(self):
        """Getting standard error of project in this way: SE(project) = sqrt( sum(squared SD (tasks)) )."""
        return round(math.sqrt(sum([i ** 2 for i in self.task_sd])), 0)

    def get_confidence_interval(self):
        """Confidence interval calculates in this way: CI(project) = E(project) ± 2 × SE(project)."""
        min = (self.get_total_estimate() - 2 * self.get_standard_error())
        max = (self.get_total_estimate() + 2 * self.get_standard_error())
        return str(f'Projects 95% confidence interval: {round(min)} ... {round(max)} points')


def main_menu():
    while True:
        try:
            n = int(input("How many tasks will be involved to your project? "))
            break
        except:
            print("Please, input the correct integer value! ")
    tasks = [list(map(int, input("Enter best-case, most-case and worst-case using space: ").split())) for i in range(n)]
    task_estimates = []
    task_sd = []
    for task in tasks:
        best_case = task[0]
        most_case = task[1]
        worst_case = task[2]
        task = Task(best_case, most_case, worst_case)
        task_estimates.append(task.get_task_estimate())
        task_sd.append(task.get_task_sd())
        print("E(task) = ", task.get_task_estimate(), "SD(task) = ", task.get_task_sd())

    project = Project(task_estimates, task_sd)
    print(project.get_confidence_interval())


if __name__ == '__main__':
    main_menu()
