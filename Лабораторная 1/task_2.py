# условие задачи
disk_volume_megabytes = 1.44
pages_in_book = 100
strings_on_page = 50
symbols_in_string = 25
bytes_on_symbol = 4

# явный перевод объёма дискеты из мегабайтов в байты
bytes_in_kilobyte = 1024
kilobytes_in_megabyte = 1024
disk_volume_bytes = disk_volume_megabytes * kilobytes_in_megabyte * bytes_in_kilobyte

# вычисление объёма одной книги
book_volume_bytes = pages_in_book * strings_on_page * symbols_in_string * bytes_on_symbol

# вычисление количества книг на одной дискете
books_on_disk = int(disk_volume_bytes // book_volume_bytes)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_on_disk)
