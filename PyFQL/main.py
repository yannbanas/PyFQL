from pattern import Pattern
from execption.custom_execption import InvalideQueryPattern
from database import Database
from query_builder import QueryBuilder

db_instance = Database()
query_builder_instance = QueryBuilder(db_instance)

while True:
    phrase = input("(PyFQL)>>> ")
    query_builder_instance.query = phrase
    query_builder_instance.execute()
    if phrase in ["quit", "exit", "q", "bye"]:
        break
