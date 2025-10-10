"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first, second, *rest = each_wagons_id    
    reordered_wagons = [*rest, first, second]
    loco_index = reordered_wagons.index(1)
    before_loco, loco, after_loco = reordered_wagons[:loco_index], reordered_wagons[loco_index], reordered_wagons[loco_index + 1:]
    result = [*before_loco, loco, *missing_wagons, *after_loco]
    
    return result

def add_missing_stops(routing, **kwargs):
    stops = [city for key, city in sorted(kwargs.items()) if key.startswith("stop_")]
    routing["stops"] = stops
    
    return routing
    
def extend_route_information(route, more_route_information):
    final= {**route, **more_route_information}
    return final


def fix_wagon_depot(wagons_rows):
    row1, row2, row3 = wagons_rows
    column1, column2, column3 = zip(*wagons_rows)
    
    return [list(column1), list(column2), list(column3)]