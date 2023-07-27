#Samiha Ashraf
#1884227

#Project Part 1
#Code starts here

import csv
import datetime

class InventoryItem:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged):
        item_info = {
            "item_id" : item_id,
            "manufacturer" : manufacturer,
            "item_type" : item_type,
            "price" : price,
            "service_date" : service_date,
            "damaged" : damaged,
        }
        self.__dict__.update(item_info)

def load_data(filename):
    data = {}
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if len(row) > 0:
                item_id = row[0]
                if len(row) >= 4:
                    manufacturer, item_type, damaged = row[1:4]
                else:
                    manufacturer, item_type, damaged = "", "", ""
                service_date = row[4] if len(row) > 4 else ""
                data[item_id] = [manufacturer, item_type, damaged, service_date]
    return data


def get_price(item):
    return item.price

def generate_full_inventory_report(items):
    with open("FullInventoryReport.csv", "w", newline='') as csvfile:
        items.sort(key=get_manufacturer)
        writer = csv.writer(csvfile, delimiter=",")
        for item in items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def generate_item_type_inventory_report(items):
    items.sort(key=get_item_id)
    item_types = set(item.item_type for item in items)

    for item_type in item_types:
        filename = f"{item_type}InventoryReport.csv"
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for item in items:
                if item.item_type == item_type:
                    writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.damaged])

def generate_past_service_date_inventory_report(items):
    with open("PastServiceDateInventoryReport.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        today = datetime.datetime.today()
        for item in items:
            date = datetime.datetime.strptime(item.service_date, '%m/%d/%Y') if item.service_date else None
            if date and date < today:
                writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def generate_damaged_inventory_report(items):
    damaged_items = sorted(items, key=get_price, reverse=True)
    with open("DamagedInventoryReport.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for item in damaged_items:
            if item.damaged:
                writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def get_manufacturer(item):
    return item.manufacturer

def get_item_id(item):
    return item.item_id

if __name__ == "__main__":
    inventory_items = []
    price_list_dic = load_data('PriceList.csv')
    service_dates_dic = load_data('ServiceDatesList.csv')
    manufacturer_dic = load_data('ManufacturerList.csv')

    for item_id, data in manufacturer_dic.items():
        manufacturer, item_type, damaged, service_date = data
        price = price_list_dic.get(item_id, "")
        item = InventoryItem(item_id, manufacturer, item_type, price, service_date, damaged)
        inventory_items.append(item)

    generate_full_inventory_report(inventory_items)
    generate_damaged_inventory_report(inventory_items)
    generate_past_service_date_inventory_report(inventory_items)
    generate_item_type_inventory_report(inventory_items)

    print('Full Inventory report written to file FullInventoryReport.csv')
    print('Damaged Inventory report written to file DamagedInventoryReport.csv')
    print('Past Service Date report written to file PastServiceDateInventoryReport.csv')
    print('Generated item type report for every item')
