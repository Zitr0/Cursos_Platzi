

def binarySearch(numbers: object, numberToFind: object, low: object, high: object) -> object:

    if low > high:
        return False

    mid = int((low + high) / 2)

    if numbers[mid] == numberToFind:
        return True

    elif numbers[mid] > numberToFind:
        return binarySearch(numbers, numberToFind, low, mid - 1)

    else:
        return binarySearch(numbers, numberToFind, mid + 1, high)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numberToFind = int(input('Ingresa un número: '))

    result = binarySearch(numbers, numberToFind, 0, len(numbers) - 1)

    if result is True:
        print('El número SI esta en la lista.')
    else:
        print('El número NO esta en la lista')
