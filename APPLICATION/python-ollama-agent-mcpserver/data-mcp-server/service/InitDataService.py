from repository import DataRepository
import logging

class InitDataService:
    __logger = logging.getLogger(__name__)
    __data_repository = DataRepository()

    @staticmethod
    def initialize_data() -> str:
        students =[
            {"name": "John Doe", "age": 30, "city": "New York", "subjects": [{"Math": 85},{ "Biology": 90},{"physics": 88},{"Chemistry": 92},{"Arts": 87}]},
            {"name": "Jane Smith", "age": 25, "city": "Los Angeles", "subjects": [{"Math": 78},{"Biology": 82},{"physics": 80},{"Chemistry": 85},{"Arts": 90}]},
            {"name": "Michael Johnson", "age": 28, "city": "Chicago", "subjects": [{"Math": 92},{"Biology": 88},{"physics": 91},{"Chemistry": 89},{"Arts": 85}]},
            {"name": "Emily Wilson", "age": 26, "city": "Houston", "subjects": [{"Math": 88},{"Biology": 95},{"physics": 87},{"Chemistry": 91},{"Arts": 93}]},
            {"name": "David Brown", "age": 29, "city": "Phoenix", "subjects": [{"Math": 80},{"Biology": 78},{"physics": 82},{"Chemistry": 79},{"Arts": 81}]},
            {"name": "Sarah Davis", "age": 27, "city": "Philadelphia", "subjects": [{"Math": 91},{"Biology": 93},{"physics": 90},{"Chemistry": 94},{"Arts": 88}]},
            {"name": "Robert Miller", "age": 31, "city": "San Antonio", "subjects": [{"Math": 75},{"Biology": 80},{"physics": 78},{"Chemistry": 82},{"Arts": 79}]},
            {"name": "Jessica Taylor", "age": 24, "city": "San Diego", "subjects": [{"Math": 89},{"Biology": 87},{"physics": 85},{"Chemistry": 88},{"Arts": 92}]},
            {"name": "Christopher Anderson", "age": 32, "city": "Dallas", "subjects": [{"Math": 86},{"Biology": 84},{"physics": 89},{"Chemistry": 87},{"Arts": 83}]},
            {"name": "Amanda Martinez", "age": 25, "city": "San Jose", "subjects": [{"Math": 94},{"Biology": 91},{"physics": 93},{"Chemistry": 95},{"Arts": 89}]},
        ]
        InitDataService.__logger.info(f"Initializing data: {students}")
        for student in students:
            InitDataService.__logger.info(f"Inserting student data: {student}")
            InitDataService.__data_repository.insert_data(student)
            
        return "Data initialization completed."