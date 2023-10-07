# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024

pages = 100
lines = 50
chars = 25

book_size = pages * lines * chars * 4
num_books = int(disk_size // book_size)

print("Количество книг, помещающихся на дискету:", num_books)
