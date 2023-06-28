from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja_model import Ninja

# ------------   CONSTRUCTOR   ------------
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

# -------------   CLASS METHODS   -----------

# --------- READ ALL - SHOW ALL DOJOS   --------
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

# ----  CREATE - POST ROUTE - ADDS NEW DOJO  ----
    @classmethod
    def add_dojo(cls, data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

# ------  GET ALL NINJAS FOR ONE DOJO ---------
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = """
            SELECT * FROM dojos
            JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(dojo_id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        print(results)

        dojo = cls( results[0] )

        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id" : row_from_db["dojo_id"],
            }
            ninja_instance = Ninja(ninja_data)
            dojo.ninjas.append(ninja_instance)
        return dojo