from unittest import TestCase
import sqlite3
from migration import upgrade, downgrade
import query_executor
import ORM_executor

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
upgrade(connection, cursor)
connection.close()

class test_executors(TestCase):
    ex = query_executor.query_executor('db.sqlite')
    
    def test_select(self):
        res = self.ex.execute_query('SELECT Cars.color FROM Cars')
        index = 0
        for row in res:
            if index == 0:
                self.assertEqual(row, ('Grey',))
                break
    
    def test_insert(self):
        self.ex.execute_query("INSERT INTO Vendor VALUES (4, 'zavod', 'da-da')")
        res = self.ex.execute_query('SELECT * FROM Vendor')
        index = 0
        for row in res:
            index = index + 1
        self.assertEqual(index, 4)

    def just_to_show_ORM(self):
        executor = ORM_executor.ORM_executor('db.sqlite')
        executor.query1()
        executor.query2()
        executor.query3()
        executor.query4()
        executor.query5()
        executor.query6()

t = test_executors()
t.test_select()
t.test_insert()
t.just_to_show_ORM()