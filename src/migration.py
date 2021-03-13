def upgrade(connection, cursor):
    sql = """CREATE TABLE cars
    (
	id INT PRIMARY KEY,
  	brand TEXT,
  	color TEXT,
  	serial_number TEXT,
  	registration_number TEXT,
  	year_of_issue DATE,
  	year_of_inspection DATE,
  	price REAL
    );"""
    cursor.execute(sql)
    
    cars = [(1, 'KIA', 'Grey', '7792TE-7', '892B5A87', '2020-01-08', '2020-05-13', 20000),
            (2, 'BMW', 'Black', 'A33JAK-1', '8K2B512D', '2013-08-24', '2016-10-18', 34300), 
            (3, 'Hyundai', 'White', '567AG8-4', 'JKLAS', '2017-12-20', '2019-11-09', 12653),
            (4, 'Lexus', 'Red', '134HJ3-3', 'J1423SS', '2016-03-02', '2021-01-16', 23500),
            (5, 'Volvo', 'White', '123BSN-6', 'ASDJKJ2', '2016-11-26', '2020-7-08', 12653)
            ]
    sql = 'INSERT INTO cars VALUES (:1, :2, :3, :4, :5, :6, :7, :8)'
    for ID, brand, color, serial_number, registration_number, year_of_issue, year_of_inspection, price in cars:
        cursor.execute(sql, [ID, brand, color, serial_number, registration_number, year_of_issue, year_of_inspection, price])

    connection.commit()

def downgrade(connectin, cursor):
    cursor.execute('DROP TABLE cars')
    connectin.commit()