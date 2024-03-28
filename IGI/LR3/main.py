from start_tasks import start_task1, start_task2, start_task3, start_task4, start_task5

# Lab3. Standard data types, collections, functions, modules.
# Performed by a student of group 253502, Krasyov Pavel.
# Fulfillment date: 21.03.2024


def main():
    task = -1
    while (True):
        print("Enter the number of task from 1 to 5, or 0 to exit:")
        try:
            task = int(input())
            if task < 0 or task > 5:
                raise Exception
        except:
            print(
                'Incorrect input, try again! Input only one number between 1 and 5, or 0 to exit\n')
            continue
        if task == 1:
            print('Task 1')
            start_task1()
            continue
        elif task == 2:
            print('Task 2')
            start_task2()
            continue
        elif task == 3:
            print('Task 3')
            start_task3()
            continue
        elif task == 4:
            print('Task 4')
            help(start_task4)
            start_task4()
            continue
        elif task == 5:
            print('Task 5')
            start_task5()
            continue
        elif task == 0:
            break
    print('Program finished!')


if __name__ == '__main__':
    main()
