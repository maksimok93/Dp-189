"""
In three-point estimation of project, you need to set three variables for each
required task based on previous experience or best assumptions, where:
a = the best-case estimate;
m = the most likely estimate;
b = the worst-case estimate.
"""
import math


class Task:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def get_task_estimate(self):
        """
        Estimate is a weighted average which takes into account both the most optimistic
        and most pessimistic estimates provided.
        """
        return round((self.a + 4 * self.m + self.b) / 6, 0)

    def get_task_sd(self):
        """Task Standard Deviation (SD) measures the variability or uncertainty in the estimate."""
        return round((self.b - self.a) / 6, 0)


class Project:
    def __init__(self, estimates, task_sd):
        self.estimates = estimates
        self.task_sd = task_sd

    def get_total_estimate(self):
        """Getting total estimate of our project."""
        return sum(self.estimates)

    def get_standard_error(self):
        """Getting standard error of project in this way: SE(project) = sqrt( sum(squared SD (tasks)) )."""
        return round(math.sqrt(sum([i ** 2 for i in self.task_sd])), 0)

    def get_ci_project_(self):
        """Confidence interval calculates in this way: CI(project) = E(project) ± 2 × SE(project)."""
        min = (Project.get_total_estimate(self) - 2 * Project.get_standard_error(self))
        max = (Project.get_total_estimate(self) + 2 * Project.get_standard_error(self))
        return str(f'Projects 95% confidence interval: {round(min)} ... {round(max)} points')


def main():
    n = input("How many tasks will be involved to your project? ")
    while True:
        try:
            n = int(n)
            break
        except:
            print("Please, input the correct integer value! ")
            n = input("How many tasks will be involved to your project? ")
    tasks = [list(map(int, input("Enter a, m, b using space: ").split())) for i in range(n)]
    estimates = []
    task_sd = []
    for task in tasks:
        task = Task(task[0], task[1], task[2])
        estimates.append(task.get_task_estimate())
        task_sd.append(task.get_task_sd())
        print("E(task) = ", task.get_task_estimate(), "SD(task) = ", task.get_task_sd())

    project = Project(estimates, task_sd)
    print(project.get_ci_project_())


if __name__ == '__main__':
    main()
