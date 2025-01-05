# Ce programme permet d'exporter en format csv, les données d'un fichier .stats généré par cProfile.
import csv
import pstats
import sys


def main(fileName):
	# Exporter les statistiques
	with open(f"{fileName}_results.csv", "w") as f:
		writer = csv.writer(f, delimiter=";")
		writer.writerow(["Fonction", "ncalls"])

		# Charger le profil
		ps = pstats.Stats(fileName)
		ps.strip_dirs()
		ps.sort_stats('ncalls')

		for func, stats in ps.stats.items():
			ncalls = stats[0]
			# func_name = f"{func[2]} ({func[0]}:{func[1]})"
			# refaire car pour le nom je veux juste : exemples :
			# {method ’getint’ of ’_tkinter.tkapp’ objects}
			# {built-in method builtins.callable}
			# __init__.py(_cnfmerge)

			if "{" in func[2]:
				func_name = func[2]
			elif ".py" in func[0]:
				func_name = f"{func[0]} ({func[2]})"
			elif "<" in func[2]:
				func_name = func[2]
			writer.writerow([func_name, ncalls])

	print(f"Les statistiques ont été exportées dans {fileName}_results.csv.")

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		print("Veuillez spécifier le fichier .stats à exporter en argument.")
