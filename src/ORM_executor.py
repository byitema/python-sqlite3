from pony import orm
from datetime import datetime

class ORM_executor:
    db = orm.Database()

    def __init__(self, dbname: str):
        self.db.bind('sqlite', dbname, create_db=True)
        self.db.generate_mapping(create_tables=False)

    class Cars(db.Entity):
        ID = orm.PrimaryKey(int)
        brand = orm.Required(str)
        color = orm.Required(str)
        serial_number = orm.Required(str)
        registration_number = orm.Required(str)
        year_of_issue = orm.Required(datetime)
        year_of_inspection = orm.Required(datetime)
        price = orm.Required(float)
        vendor_id = orm.Required(int)

    class Vendor(db.Entity):
        ID = orm.PrimaryKey(int)
        ven_name = orm.Required(str)
        ven_description = orm.Required(str)

    @orm.db_session
    def query1(self):
        orm.select(car for car in self.Cars if car.year_of_issue < datetime.fromisoformat('2019-03-06'))[:].show()

    @orm.db_session
    def query2(self):
        orm.select(orm.count() for car in self.Cars if car.price > 16000.0)[:].show()

    @orm.db_session
    def query3(self):
        orm.select(orm.sum(car.price) for car in self.Cars if (car.year_of_issue > datetime.fromisoformat('2016-01-01') and
            car.year_of_issue < datetime.fromisoformat('2016-12-31')))[:].show()

    @orm.db_session
    def query4(self):
        orm.select((orm.max(car.price), orm.min(car.price)) for car in self.Cars)[:].show()

    @orm.db_session
    def query5(self):
        orm.select((car.ID, car.brand, car.year_of_issue, vendor.ven_name) for car in self.Cars
                                                                            for vendor in self.Vendor
                                                                            if (car.vendor_id == vendor.ID))[:].show()

    @orm.db_session
    def query6(self):
        orm.select((car, vendor) for car in self.Cars
                                            for vendor in self.Vendor
                                             if (car.vendor_id == vendor.ID and car.vendor_id == 3))[:].show()