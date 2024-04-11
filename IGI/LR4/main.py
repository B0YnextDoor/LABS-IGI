from start_tasks import TasksStarter

# Lab4. Working with files, classes, serializers, regular expressions and standard libraries.
# Performed by a student of group 253502, Krasyov Pavel.
# Fulfillment date: 25.03.2024


def main():
    starter = TasksStarter()
    while True:
        try:
            task = int(input(
                'Enter number of task from 1 to 5, or 6 to perform data analysis, or 0 to exit: '))
            if task < 0 or task > 6:
                raise Exception
        except:
            print(
                'Incorrect input, try again! Input only integer numbers between 0 and 6!\n')
            continue
        if task == 1:
            starter.runTask1()
            continue
        elif task == 2:
            starter.runTask2()
            continue
        elif task == 3:
            starter.runTask3()
            continue
        elif task == 4:
            starter.runTask4()
            continue
        elif task == 5:
            starter.runTask5()
            continue
        elif task == 6:
            starter.runAnalisys()
            continue
        elif task == 0:
            break
    print('Program finished!')


if __name__ == '__main__':
    main()
