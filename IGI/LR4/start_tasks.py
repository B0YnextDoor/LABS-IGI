from decorators import RunTask
from task1.task1 import Task1, CsvDictionary, PickleDictionary
from task2.task2 import Task2
from task3.task3 import Task3
from task4.task4 import Task4
from task5.task5 import Task5
from analysis.analysis import DataAnalisys
from utils import validateNumberInput


class TasksStarter():

    @RunTask(Task1)
    def runTask1(self, task: Task1) -> str | None:
        ''' Task1\nA dictionary consisting of words arranged in pairs is given. Each word is a synonym for its paired word. All words in the dictionary are different. For the last word in the dictionary, determine its synonym. Display information about the word entered from the keyboard. '''
        var = validateNumberInput('type (1 -> csv file | 2 -> pickle module | 0 -> Exit function)',
                                  '1 -> csv file | 2 -> pickle module | 0 -> Exit function', int,
                                  condition=lambda x: x != 0 and x != 1 and x != 2)
        if var == 1:
            dictionary = CsvDictionary(f'{task.path}csv')
        elif var == 2:
            dictionary = PickleDictionary(f'{task.path}pkl')
        else:
            return 'stop'
        task(dictionary)

    @RunTask(Task2)
    def runTask2(self, task: Task2) -> None:
        ''' Task2\nRead text from the source file. Using regular expressions, obtain the required information display it on the screen and save it to another file. Archive the result file using the zipfile module and ensure that information about the file is retrieved in the archive. '''
        task()

    @RunTask(Task3)
    def runTask3(self, task: Task3) -> str | None:
        ''' Task3\nWith a given accuracy calculate the value of a function using Tailor's row. Determine additional parameters: arithmetic mean, median, mode, dispersion, standard deviation of the sequence. Using the `matplotlib` library, draw charts of different colors on the same coordinate axis'''
        return task()

    @RunTask(Task4)
    def runTask4(self, task: Task4) -> str | None:
        ''' Task4\nConstruct a square, on one side of which, as a base, an equilateral triangle with side a is built. '''
        return task()

    @RunTask(Task5)
    def runTask5(self, task: Task5) -> str | None:
        ''' Task5\nGenerate an integer matrix A[n,m] using a random number generator.Find all elements that exceed the specified number B in absolute value. Count the number of such elements and write them to array C. Calculate the median value for this array C. '''
        return task()

    def runAnalisys(self) -> None:
        ''' Additional task\nDataset -> different car models with main characteristics. '''
        print(self.runAnalisys.__doc__)
        analiser = DataAnalisys('./analysis/data.csv')
        analiser()
