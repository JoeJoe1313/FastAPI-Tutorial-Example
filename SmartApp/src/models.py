# contains the domain classes for the application,  such as Company and Configuration
from enum import Enum
from pydantic import BaseModel


# generate an exception handler for it in workflow_runner.py
class MyException(Exception):
    pass


# represent each constituent of the index
class Company:
    def __init__(self, symbol):
        self.name = None
        self.symbol = symbol
        self.sector = None
        self.industry = None


class Index(str, Enum):
    FTSE100 = 'FTSE100'
    SNP500 = 'SNP500'
    DOWJONE = 'Dow Jones'


# This class contains the name of the index as an Enum.
# The enum members will be displayed in the API documentation and in the Swagger UI as a drop down.
# Note that the Configuration class inherits from the pydantic BaseModel.
# This will enable us to generate automatic data schema documentation.
# The configuration class contains a dictionary named index_map.
# Each index map item has its key as the index enum member and
# the value as the URL of the webpage which has the companies information.
class Configuration(BaseModel):
    index: str = None
    index_map = {
        Index.FTSE100: 'https://en.wikipedia.org/wiki/FTSE_100_Index',
        Index.SNP500: 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    }

    # return the url for the chosen index
    def get_url(self):
        return self.index_map[self.index]
