import unittest
from booklover import booklover

class BookLoverTestSuite(unittest.TestCase):
    pass

    def test_1_add_book(self):
        lover = BookLover("Aug", "aug@gmail.com", "romance")
        lover.add_book("The Summer I Turned Pretty", 5)
        self.assertTrue("The Summer I Turned Pretty" in lover.book_list['book_name'].values)

    def test_2_add_book(self):
        lover = BookLover("Mike", "mike@gmail.com", "romance")
        lover.add_book("Wild Robot", 5)
        self.assertEqual(len(lover.book_list[lover.book_list['book_name'] == "Wild Robot"]), 5)

    def test_3_has_read(self):
        lover = BookLover("Charles", "charlie@yahoo.com", "mystery")
        lover.add_book("War of the Worlds", 4)
        self.assertTrue(lover.has_read("War of the Worlds"))

    def test_4_has_read(self):
        lover = BookLover("Chers", "chers@yahoo.com", "romance")
        self.assertFalse(lover.has_read("Romeo and Juliet"))

    def test_5_num_books_read(self):
        lover = BookLover("Steve", "steve@gmail.com", "horror")
        lover.add_book("Monsters", 2)
        lover.add_book("Frankenstein", 3)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Kyle", "kyle@example.com", "adventure")
        lover.add_book("Adventure Kids", 4)
        lover.add_book("Wonder", 5)
        fav_books = lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
