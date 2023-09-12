from database.main import create_database_structure

class AppInitializerService:
    def initialize_db(self):
        create_database_structure()