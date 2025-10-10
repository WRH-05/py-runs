def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    azara_coordinate= tuple(azara_record[1])
    return azara_coordinate==rui_record[1]

def create_record(azara_record, rui_record):
    azara_coordinate= tuple(azara_record[1])
    if azara_coordinate==rui_record[1]:
        return azara_record+rui_record
    return "not a match"

def clean_up(combined_record_group):
    cleaned_records = []
    for item in combined_record_group:
        cleaned_record = (item[0], item[2], item[3], item[4])
        cleaned_records.append(cleaned_record)
    return "\n".join(str(record) for record in cleaned_records) + "\n"
