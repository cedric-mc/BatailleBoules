# Ce programme permet d'exporter en format csv, les noms de fonctions et nombre d'appels d'un fichier .stats généré par cProfile
import pstats
import csv
import sys


def main(fileName):
	# Charger le profil
	p = pstats.Stats(fileName)

	# Trier les statistiques
	p.sort_stats("ncalls")

	# Extraire les données pour le CSV
	stats_data = []
	header = ["Fonction", "ncalls"]
	for data in p.stats.items():
		# Extraire le nom de la fonction et le nombre d'appels
		func_name = f"{data[0][0]}:{data[0][1]}:{data[0][2]}"  # Module:Ligne:Nom de fonction
		ncalls = data[1][0]
		stats_data.append([func_name, ncalls])

	# Trier les données du plus grand au plus petit nombre d'appels
	stats_data.sort(key=lambda x: x[1], reverse=True)

	# Exporter vers un fichier CSV
	with open("profiling_results.csv", "w", newline="") as csvfile:
		# Séparer les valeurs par des points-virgules
		writer = csv.writer(csvfile, delimiter=";")
		writer.writerow(header)  # Écrire l'en-tête
		writer.writerows(stats_data)  # Écrire les données

	print("Les statistiques ont été exportées dans le fichier profiling_results.csv")

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		print("Veuillez spécifier le fichier .stats à exporter en argument.")
