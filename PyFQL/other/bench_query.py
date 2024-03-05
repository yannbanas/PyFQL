import pytest
from PyFQL.database import Database

# Fonction de test pour mesurer les performances de la fonction create_table
@pytest.mark.benchmark(min_rounds=10)
def test_create_table_performance(benchmark):
    db = Database()
    # Définir la fonction que vous souhaitez tester
    def create_table():
        db.create_table("test_table")
    # Mesurer les performances de la fonction
    benchmark(create_table)

# Ajoutez des fonctions de test similaires pour chaque fonction de votre classe Database

# Exemple avec la fonction insert
@pytest.mark.benchmark(min_rounds=10)
def test_insert_performance(benchmark):
    db = Database()
    def insert():
        db.create_table("test_table")
        for i in range(1000):
            db.insert("test_table", {"id": i, "name": f"Entity {i}"})
    benchmark(insert)


# Exemple avec la fonction insert_batch
@pytest.mark.benchmark(min_rounds=10)
def test_insert_batch_performance(benchmark):
    db = Database()
    def insert_batch():
        db.create_table("test_table")
        entities = [{"id": i, "name": f"Entity {i}"} for i in range(100)]
        db.insert_batch(("test_table", entities))
    benchmark(insert_batch)

# Exemple avec la fonction delete
@pytest.mark.benchmark(min_rounds=10)
def test_delete_performance(benchmark):
    db = Database()
    # Supposons que vous avez des données préexistantes dans la table "test_table"
    def delete():
        db.delete("test_table", index=0)
    benchmark(delete)

# Exécutez pytest pour exécuter les tests
# Assurez-vous d'avoir pytest-benchmark installé
# Utilisez la commande: pytest -v
