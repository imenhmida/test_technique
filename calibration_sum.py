import os

# Étape 1 : Fonction pour extraire la valeur d'étalonnage d'une ligne
def extract_calibration_value(line):
    """
    Prend une ligne en entrée et retourne la valeur d'étalonnage en combinant
    le premier et le dernier chiffre de la ligne.
    """
    # Trouver le premier chiffre
    first_digit = next((char for char in line if char.isdigit()), None)
    # Trouver le dernier chiffre
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    # Si les deux chiffres existent, les combiner pour former un nombre
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    return 0  # Retourne 0 si aucun chiffre n'est trouvé

# Étape 2 : Calculer la somme totale
def calculate_total_calibration_sum(file_path):
    """
    Lit un fichier ligne par ligne et calcule la somme des valeurs d'étalonnage.
    """
    total_calibration_value = 0
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return 0
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Lire toutes les lignes
        # Calculer la somme des valeurs d'étalonnage pour chaque ligne
        total_calibration_value = sum(extract_calibration_value(line) for line in lines)
    return total_calibration_value

# Étape 3 : Exécution principale
if __name__ == "__main__":
    # Spécifier le chemin du fichier d'entrée
    file_path = "document.txt" 
    # Vérifier l'existence du fichier
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas dans le dossier courant : {os.getcwd()}")
    else:
        # Calculer et afficher le résultat
        result = calculate_total_calibration_sum(file_path)
        print(f"La somme totale des valeurs d'étalonnage est : {result}")
