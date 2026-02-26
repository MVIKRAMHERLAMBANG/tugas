class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self, member_name):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"✓ Buku '{self.title}' dipinjam oleh {member_name}")
        else:
            print(f"✗ Buku '{self.title}' sedang dipinjam")

    def return_book(self, member_name):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"✓ Buku '{self.title}' dikembalikan oleh {member_name}")
        else:
            print(f"✗ Buku '{self.title}' tidak sedang dipinjam")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id


class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff

    def borrow_book(self):
        if not self.book.is_borrowed:
            self.book.borrow(self.member.name)
            self.member.borrowed_books.append(self.book.title)
            print(f"  Diproses oleh Staff : {self.staff.name}")
        else:
            print("  Transaksi gagal!")

    def return_book(self):
        if self.book.is_borrowed:
            self.book.return_book(self.member.name)
            print(f"  Diproses oleh Staff : {self.staff.name}")
        else:
            print("  Buku tidak sedang dipinjam")


# PROGRAM UTAMA

print("=" * 50)
print("        SISTEM PEMINJAMAN PERPUSTAKAAN")
print("=" * 50)

# 3 Buku
book1 = Book("Pemrograman Python", "Andi", "978-602-1234-01-1")
book2 = Book("Struktur Data", "Budi", "978-602-1234-02-8")
book3 = Book("Basis Data", "Citra", "978-602-1234-03-5")

# 3 Peminjam
member1 = Member("Sandi", "12550112934")
member2 = Member("Dani", "125305849")
member3 = Member("Ahmed", "32148492")

# Staff
staff1 = Staff("Admin Perpustakaan", "S001")

# TAMPILKAN DAFTAR BUKU
print("\nDAFTAR BUKU")
print("-" * 50)
for book in [book1, book2, book3]:
    status = "Dipinjam" if book.is_borrowed else "Tersedia"
    print(f"Judul  : {book.title}")
    print(f"Author : {book.author}")
    print(f"ISBN   : {book.isbn}")
    print(f"Status : {status}")
    print("-" * 50)

# PROSES PEMINJAMAN
print("\nPROSES PEMINJAMAN")
print("-" * 50)

transaction1 = BorrowTransaction(book1, member1, staff1)
transaction1.borrow_book()

transaction2 = BorrowTransaction(book2, member2, staff1)
transaction2.borrow_book()

transaction3 = BorrowTransaction(book3, member3, staff1)
transaction3.borrow_book()

# STATUS SETELAH DIPINJAM
print("\nSTATUS BUKU SETELAH DIPINJAM")
print("-" * 50)
for book in [book1, book2, book3]:
    status = "Dipinjam" if book.is_borrowed else "Tersedia"
    print(f"{book.title:<25} : {status}")

# DATA PEMINJAM
print("\nDATA PEMINJAM")
print("-" * 50)
for member in [member1, member2, member3]:
    print(f"Nama          : {member.name}")
    print(f"ID Member     : {member.member_id}")
    print(f"Buku Dipinjam : {member.borrowed_books}")
    print("-" * 50)