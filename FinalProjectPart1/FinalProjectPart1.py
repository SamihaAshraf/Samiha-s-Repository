#Samiha Ashraf
#1884227

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

def load_manufacturer_data(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        items_dic = {}
        for row in reader:
            if len(row) > 0:
                item_id = row[0]
                manufacturer = row[1]
                item_type = row[2]
                damaged = row[3]
                items_dic[item_id] = [manufacturer, item_type, damaged]
        return items_dic

def load_price_list(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        prices = {}
        for row in reader:
            if len(row) > 0:
                item_id = row[0]
                price = row[1]
                prices[item_id] = price
        return prices

def load_service_dates_data(filename):
     with open(filename, "r") as csvfile:
         reader = csv.reader(csvfile, delimiter=",")
         service_dates = {}
         for row in reader:
             if len(row) > 0:
                 item_id = row[0]
                 service_date = row[1]
                 service_dates[item_id] = service_date
         return service_dates

def generate_full_inventory_report(items):
    with open("FullInventoryReport.csv", "w") as csvfile:
        items = sorted(items, key=lambda item: item.manufacturer)
        writer = csv.writer(csvfile, delimiter=",")
        for item in items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def generate_item_type_inventory_report(items):
    items = sorted(items, key=lambda item: item.item_id)
    item_types = list(set(item.item_type for item in items))

    for item_type in item_types:
        with open(f"{item_type}InventoryReport.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for item in items:
                if item.item_type == item_type:
                    writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.damaged])

def generate_past_service_date_inventory_report(items):
    with open("PastServiceDateInventoryReport.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        today = datetime.datetime.today()
        items = sorted(items, key=lambda item: datetime.datetime.strptime(item.service_date, '%m/%d/%Y'), reverse=True)
        for item in items:
            date = datetime.datetime.strptime(item.service_date, '%m/%d/%Y')
            if date < today:
                writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

def generate_damaged_inventory_report(items):
    with open("DamagedInventoryReport.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        damaged_items = sorted(items, key=lambda item: item.price, reverse=True)
        for item in damaged_items:
            if item.damaged:
                writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

if __name__ == "__main__":
    inventory_items = []
    price_list_dic = load_price_list('PriceList.csv')
    service_dates_dic = load_service_dates_data('ServiceDatesList.csv')
    manufacturer_dic = load_manufacturer_data('ManufacturerList.csv')

    for item_id, data in manufacturer_dic.items():
        manufacturer, item_type, damaged = data
        price = ""
        service_date = ""
        if item_id in price_list_dic.keys():
            price = price_list_dic[item_id]
        if item_id in service_dates_dic.keys():
            service_date = service_dates_dic[item_id]
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