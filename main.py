from PyFQL import Database, QueryBuilder

db_instance = Database("D:\\test_db\\")
query_builder_instance = QueryBuilder(db_instance)


while True:
    phrase = input("(PyFQL)>>> ")
    query_builder_instance.query = phrase
    query_builder_instance.execute()
    if phrase in ["quit", "exit", "q", "bye"]:
        break
