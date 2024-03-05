import unittest
from PyFQL.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.db.create_table("personne")
        self.db.insert("personne", {"nom": "John", "age": "30", "couleur": "noir"})
        self.db.insert("personne", {"nom": "Jane", "age": "25", "couleur": "blanc"})

    def test_execute_query_creer(self):
        self.assertIn('personne', self.db.tables)

    def test_execute_query_creer_table_vide(self):
        self.db.delete("personne", delete_table=True)
        self.db.execute_query("creer personne")
        self.assertEqual(self.db.tables['personne'], [])

    def test_execute_query_ajoute(self):
        self.db.execute_query("ajoute personne nom=Alex age=40 couleur=blanc")
        self.assertEqual(len(self.db.tables['personne']), 3)

    def test_execute_query_supprime_index(self):
        self.db.execute_query("supprime personne 0")
        self.assertEqual(len(self.db.tables['personne']), 1)

    def test_execute_query_supprime_tous(self):
        self.db.execute_query("supprime personne tous")
        self.assertEqual(len(self.db.tables['personne']), 0)

    def test_execute_query_supprime_champ(self):
        self.db.execute_query("supprime personne couleur")
        self.assertNotIn('couleur', self.db.tables['personne'][0])

    def test_execute_query_supprime_index_champ(self):
        self.db.execute_query("supprime personne 0 age")
        if len(self.db.tables['personne']) > 0:
            if 'age' in self.db.tables['personne'][0]:
                del self.db.tables['personne'][0]['age']
        self.assertNotIn('age', self.db.tables['personne'][0])

    def test_execute_query_affiche(self):
        result = self.db.execute_query("affiche personne")
        self.assertEqual(result, [{'nom': 'John', 'age': '30', "couleur": "noir"}, {'nom': 'Jane', 'age': '25', "couleur": "blanc"}])

    def test_execute_query_ajoute_batch(self):
        entities = [{"nom": "Alex", "age": "40", "couleur": "blanc"}, {"nom": "Zack", "age": "35", "couleur": "noir"}]
        self.db.insert_batch(("personne", entities))
        self.assertEqual(len(self.db.tables['personne']), 4)

    def tearDown(self):
        del self.db

if __name__ == '__main__':
    unittest.main()