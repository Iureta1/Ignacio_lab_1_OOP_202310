from parse_options import ParseOptions
from csv_reader import CsvReader
from tables_by_region_exporter import TablesByRegionExporter
from general_results_exporter import GeneralResultsExporter
from results_by_region_exporter import ResultsByLocalExporter

ParseOptions.display_menu()
option = ParseOptions.get_option()

CsvReader.__init__("data.csv")
datos = CsvReader.read_file()

if option == str(1):
    tables_exporter = TablesByRegionExporter(datos, "mesas_por_region.csv")
    tables_exporter.export()
if option == str(2):
    general_results = GeneralResultsExporter(datos,"Resultados_generales.csv")
    general_results.export()
if option == str(3):
    local = input("Ingrese el local a analizar: ")
    results_by_region = ResultsByLocalExporter(datos,f"Resultados_en_local_{local}.csv",local)
    results_by_region.export()

    


