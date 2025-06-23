# Here begins a new world ...

# Функція, яка обчислює число Фібоначчі.

def caching_fibonacci():
    # Це наш кеш — словник, який зберігатиме вже обчислені значення
    cache = {}

    def fibonacci(n):
        # Базові випадки: F(0) = 0, F(1) = 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Якщо результат уже є в кеші — повертаємо його
        if n in cache:
            return cache[n]

        # Якщо значення відсутнє — рекурсивно обчислюємо і зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(8))  
print(fib(18))  