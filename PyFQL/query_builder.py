from .pattern import Pattern
from .execption.custom_execption import InvalideQueryPattern

class QueryBuilder:
    def __init__(self, database_instance):
        self.pattern_handler = Pattern()
        self.query = ""
        self.database_instance = database_instance

    def build_query(self, query):
        self.query = query
        mots = query.split()
        mots_et_categories = [(mot, self.pattern_handler.identify_mot(mot)) for mot in mots]
        #print("mots_et_categories: ", mots_et_categories)
        if self.pattern_handler.is_allowed(mots_et_categories):
            mots_et_categories_filtered = [(mot, categorie) for mot, categorie in mots_et_categories if categorie != 'IGNORE']
            #print("mots_et_categories_filtered: ", mots_et_categories_filtered)
            return mots_et_categories_filtered
        else:
            raise InvalideQueryPattern()

    def execute(self):
        mots_et_categories = self.build_query(self.query)
        print("execute mots_et_categories: ", mots_et_categories)
        actions = []
        reserves = []
        variables = []
        for mot, categorie in mots_et_categories:
            if categorie == "ACTION":
                actions.append(mot)
            elif categorie == "RESERVER":
                reserves.append(mot)
            elif categorie == "VARIABLE":
                variables.append(mot)
        action_str = "_".join(actions) #recupere le mot brute et ajoute un _
        
        action_str = self.pattern_handler.formes_conjuguees_lemmes.get(action_str) # recupere le lemme mot en (er) a partir du mot brute

        if reserves:
            reserve_str = reserves[0]
        else:
            reserve_str = mots_et_categories[0][0]

        if variables:  # Vérifier si la liste variables n'est pas vide
            variable_str = f'"{variables[-1]}"'
        else:
            variable_str = None
        action_str = self.pattern_handler.lemme_to_english.get(action_str) # recupere le mot en anglais a partir du lemme
        reserve_str = self.pattern_handler.lemme_to_english.get(reserve_str, reserve_str)
        print(f"3 action_str anglais: {action_str}")
        self.execute_db_action(action_str, reserve_str, variable_str)
        #print(f"Query OK !")

    def execute_db_action(self, action_str, reserve_str, variable_str):
        database_methods = {
            "create_db": self.database_instance.create_db,
            "delete_db": self.database_instance.delete_db,
            "use_db": self.database_instance.use_db,
            "show_db": self.database_instance.show_db,
        }

        full_action_str = f"{action_str}_{reserve_str}"
        print(f"full_action_str: {full_action_str}")
        if full_action_str in database_methods:
            # Récupérer la fonction associée à l'action
            action_function = database_methods.get(full_action_str)
            
            if action_function:
                # Vérifier si la méthode prend des arguments
                if variable_str:
                    # Si la méthode prend un argument, s'assurer qu'il est fourni avant de l'appeler
                    action_function(variable_str.strip('"'))
                    #print(f"Exécution de {full_action_str}({variable_str})")
                else:
                    # Si la méthode ne prend pas d'argument, appeler la méthode sans passer de paramètre
                    action_function()
                    #print(f"Exécution de {full_action_str}()")
            else:
                print(f"Aucune méthode associée à l'action {full_action_str}")
        else:
            print("Action non prise en charge.")




