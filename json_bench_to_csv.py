import json
import sys
import csv
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("benchmark_json") if isfile(join("benchmark_json", f))]

# with open("data.csv", 'w', encoding='utf-8') as outputfile:
#     writer = csv.writer(outputfile)
#     writer.writerow(["e0b9d79758b - initial","","","","","","", "408a28e7676 - sup json","","","","","","", "01b8046c58e - WithName WithValues","","","","","","", "32596ed3ef9 - only v>3","","","","","","", "f7ac1e31be7 - no WithName","","","","","","",])

for index, file in enumerate(onlyfiles):
    with open("data{}.csv".format(index), 'w', encoding='utf-8') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["","Average","Perc50","Perc90","Perc95","Perc99","Unit"])
        with open("{}/{}".format("benchmark_json", file), encoding='utf-8') as inputfile:
            df = json.load(inputfile)
            for item in df["dataItems"]:
                writer.writerow([item["labels"]["Name"],"","","","","",""])
                writer.writerow([item["labels"]["Metric"], item["data"]["Average"], item["data"]["Perc50"], item["data"]["Perc90"],item["data"]["Perc95"],item["data"]["Perc99"],item["unit"]])
            





