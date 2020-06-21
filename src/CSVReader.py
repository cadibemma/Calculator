import csv


def class_factory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CSVReader:
    data = []

    def __init__(self, filepath):
        with open(filepath, 'r') as test_data:
            csv_reader = csv.DictReader(test_data, delimiter=',')
            for row in csv_reader:
                self.data.append(row)
        pass

    def return_data_as_object(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects
