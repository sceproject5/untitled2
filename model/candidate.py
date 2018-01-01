from model import jsonLoad
import json


def import_json_file(file):
    json_data = jsonLoad.import_json(file)
    insert_candidate_information(json_data)


def empty_json_template():
    return {'notes': {'1': {'description': ''}, '2': {'description': ''}}, 'image': 'https://imagelocation', 'expAndSkill': {'specillaztion': {'1': {'description': 'field description', 'date': '2015'}, '3': {'description': 'field description', 'date': '2013'}, '2': {'description': 'field description', 'date': '2014'}}, 'previousCareer': {'1': {'description': 'field description', 'date': '2015'}, '3': {'description': 'field description', 'date': '2013'}, '2': {'description': 'field description', 'date': '2014'}}}, 'sortAcademic': {'1': {'post_doctoral': 1}, '4': {'fellowship_grants': 0}, '3': {'high_level_research': 0}, '2': {'teaching_in_postscenodry': 0}}, 'phoneNumber': '', 'AcadmicHistory': {'education': {'1': {'description': 'field description', 'date': '2015'}, '3': {'description': 'field description', 'date': '2013'}, '2': {'description': 'field description', 'date': '2014'}}, 'researchersAndProject': {'1': {'description': 'field description', 'date': '2015'}, '3': {'description': 'field description', 'date': '2013'}, '2': {'description': 'field description', 'date': '2014'}}}, 'status': {'1': {'hired': 0}, '3': {'onhold': 1}, '2': {'rejected': 0}}, 'email': 'youreEmail@gmail.com', 'name': 'YoureFullName'}


def write_json_file(data,filename):
    with open((filename+'.json'), 'w') as outfile:
        json.dump(data, outfile, indent=2)
    print("template file saves as template.json fill the template and import the file.")


def insert_candidate_information(data):
    query = "INSERT INTO `candidateInformation`(`id`,`name`,`email`,`phoneNumber`," \
            "`sortAcademic`,`AcadmicHistory`,`expAndSkill`,`status`,`notes`,`mid`) " \
            "VALUES (NULL ,{0},{1},{2},{3},{4},{5},{6},{7},{8});".format(data['name'],
                                                                         data['email'],
                                                                         data['phoneNumber'],
                                                                         data['name'],
                                                                         data['name'],
                                                                         data['name'],
                                                                         data['name'],
                                                                         data['name'],
                                                                         data['name'],)
    print(query)
