def upgrade(connection, cursor):
    sql = """CREATE TABLE Cars
    (
	id INT PRIMARY KEY,
  	brand TEXT,
  	color TEXT,
  	serial_number TEXT,
  	registration_number TEXT,
  	year_of_issue DATE,
  	year_of_inspection DATE,
  	price REAL,
    vendor_id INT
    );"""
    cursor.execute(sql)
    
    cars = [(1, 'KIA', 'Grey', '7792TE-7', '892B5A87', '2020-01-08', '2020-05-13', 20000, 1),
            (2, 'BMW', 'Black', 'A33JAK-1', '8K2B512D', '2013-08-24', '2016-10-18', 34300, 3), 
            (3, 'Hyundai', 'White', '567AG8-4', 'JKLAS', '2017-12-20', '2019-11-09', 12653, 2),
            (4, 'Lexus', 'Red', '134HJ3-3', 'J1423SS', '2016-03-02', '2021-01-16', 23500, 1),
            (5, 'Volvo', 'White', '123BSN-6', 'ASDJKJ2', '2016-11-26', '2020-7-08', 12653, 3)
            ]
    sql = 'INSERT INTO Cars VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)'
    for ID, brand, color, serial_number, registration_number, year_of_issue, year_of_inspection, price, vendor_id in cars:
        cursor.execute(sql, [ID, brand, color, serial_number, registration_number, year_of_issue, year_of_inspection, price, vendor_id])
    
    sql = """CREATE TABLE Vendor
    (
        id INT PRIMARY KEY,
        ven_name TEXT,
        ven_description TEXT
    );"""
    cursor.execute(sql)

    vendors = [(1, 'LK Transport', 'Some text in here...'),
            (2, 'Hyundai Company', 'South Korea Company.'), 
            (3, 'Germany Auto', 'Best cars in the world!')
            ]
    sql = 'INSERT INTO Vendor VALUES (:1, :2, :3)'
    for ID, ven_name, ven_description in vendors:
        cursor.execute(sql, [ID, ven_name, ven_description])

    connection.commit()

def downgrade(connection, cursor):
    cursor.execute('DROP TABLE Cars')
    cursor.execute('DROP TABLE Vendor')
    connection.commit()
