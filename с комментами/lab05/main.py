#импорт всех наших функций из tablestats. Можно было бы использовать import tablestats, но тогда функции пришлось бы вызывать через tablestats.функция
#Пример: tablestats.total_minutes, что дольше и как будто бесполезно.
from tablestats import *


def main():
    #with open -- альтернатива f.open(), более безопасная и принятая. По условию ввод названия файла должен делать пользователь, поэтому with open(input())
    #encoding указывать необязательно, указывается для совместимости
    with open(input(), encoding="utf-8") as table:
        #вызываем нашу функцию из tablestats (read_rows)
        rows = read_rows(table)
        
    #вызов функций и возвращенных значений из tablestats
    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))

    #записываем в файл summary.csv наши даные, используем to_csv(counts) для формирования строки
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

#Необязательно. Используется для того, чтобы функция запустилась только при прямом запуске, и не работала при import.
#При решении этого задания можно упустить, здесь это как дань качествонному коду, не более
if __name__ == "__main__":
    main()
