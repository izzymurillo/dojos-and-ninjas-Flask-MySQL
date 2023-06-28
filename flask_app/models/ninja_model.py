from flask_app.config.mysqlconnection import connectToMySQL

# ------------   CONSTRUCTOR   ------------
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

# --------- READ ALL - SHOW ALL NINJAS   ---------
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

# -----  CREATE - POST ROUTE - ADDS A NINJA  -----
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)