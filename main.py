from datetime import time
from algorithm import GeneticAlgorithm
from models import Population,Data

import displaymgr
POPULATION_SIZE = 100

displayMgr = displaymgr.DisplayMgr()
population = Population(POPULATION_SIZE)
population.get_schedules()
displayMgr.print_generation(population)
generation_num = 0
print("\n Generation #" + str(generation_num))
geneticAlgorithm = GeneticAlgorithm()
while (population.get_schedules()[0].get_fitness() != 1.0):
    generation_num += 1
    print("\n Generation #" + str(generation_num))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)

print("\\n")
# print(population.get_schedules()[0].__str__())
final_schedule = population.get_schedules()[0]
sec1S = []
sec2S = []
sec3S = []
sec4S = []
for i in final_schedule.get_classes():
    if (i.get_section().get_name() == "Sec1"):
        sec1S.append(i)
    elif (i.get_section().get_name() == "Sec2"):
        sec2S.append(i)
    elif (i.get_section().get_name() == "Sec3"):
        sec3S.append(i)
    else:
        sec4S.append(i)

displayMgr.get_ics_data(sec1S, "sec1")
displayMgr.get_ics_data(sec2S, "sec2")
displayMgr.get_ics_data(sec3S, "sec3")
displayMgr.get_ics_data(sec4S, "sec4")

displayMgr.json_parser(sec1S, "sec1j.json")
displayMgr.json_parser(sec2S, "sec2j.json")
displayMgr.json_parser(sec3S, "sec3j.json")
displayMgr.json_parser(sec4S, "sec4j.json")
