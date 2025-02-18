def create_structure(catalog):
    catalog['Electronics']['Smartphone']['Items'] = []
    catalog['Electronics']['Smartphone']['Items'].append('Apple iPhone 15')
    catalog['Electronics']['Smartphone']['Items'].append('Samsung Galaxy S23')
    catalog['Electronics']['Smartphone']['Items'].append('Google Pixel 8')

    catalog['Electronics']['Laptops']['Gaming']['Items'] = []
    catalog['Electronics']['Laptops']['Gaming']['Items'].append('Alienware X17')
    catalog['Electronics']['Laptops']['Gaming']['Items'].append('Razer Blade 15')

    catalog['Electronics']['Laptops']['Ultrabook']['Items'] = []
    catalog['Electronics']['Laptops']['Ultrabook']['Items'].append('MacBook Air M2')
    catalog['Electronics']['Laptops']['Ultrabook']['Items'].append('Dell XPS 13')

    catalog['Electronics']['Tablets']['Items'] = []
    catalog['Electronics']['Tablets']['Items'].append('Samsung Galaxy Tab S9')
    catalog['Electronics']['Tablets']['Items'].append('Microsoft Surface Pro 9')

    catalog['Electronics']['Wearables']['Smartwatches']['Items'] = []
    catalog['Electronics']['Wearables']['Smartwatches']['Items'].append('Apple Watch Ultra')
    catalog['Electronics']['Wearables']['Smartwatches']['Items'].append('Garmin Fenix 7')

    catalog['Electronics']['Audio']['Headphones']['Items'] = []
    catalog['Electronics']['Audio']['Headphones']['Items'].append('Sony WH-1000XM5')
    catalog['Electronics']['Audio']['Headphones']['Items'].append('Bose QuietComfort 45')

    catalog['Electronics']['Audio']['Speakers']['Bluetooth']['Items'] = []
    catalog['Electronics']['Audio']['Speakers']['Bluetooth']['Items'].append('JBL Flip 6')
    catalog['Electronics']['Audio']['Speakers']['Bluetooth']['Items'].append('Sonos Roam')

    catalog['Electronics']['Gaming']['Consoles']['Items'] = []
    catalog['Electronics']['Gaming']['Consoles']['Items'].append('PS5 Digital Edition')
    catalog['Electronics']['Gaming']['Consoles']['Items'].append('Xbox Series X')

    catalog['Electronics']['TV']['OLED']['Items'] = []
    catalog['Electronics']['TV']['OLED']['Items'].append('LG C3 OLED TV')
    catalog['Electronics']['TV']['OLED']['Items'].append('Sony A95K OLED')

    catalog['Electronics']['Storage']['SSD']['Items'] = []
    catalog['Electronics']['Storage']['SSD']['Items'].append('Samsung 990 PRO')
    catalog['Electronics']['Storage']['SSD']['Items'].append('Crucial P5 Plus')

    catalog['Home Appliances']['Kitchen']['Microwave']['Items'] = []
    catalog['Home Appliances']['Kitchen']['Microwave']['Items'].append('Panasonic Genius')
    catalog['Home Appliances']['Kitchen']['Microwave']['Items'].append('Toshiba Countertop Microwave')

    catalog['Home Appliances']['Kitchen']['Refrigerators']['Items'] = []
    catalog['Home Appliances']['Kitchen']['Refrigerators']['Items'].append('LG InstaView')
    catalog['Home Appliances']['Kitchen']['Refrigerators']['Items'].append('Samsung Family Hub')

    catalog['Home Appliances']['Laundry']['Washing Machines']['Items'] = []
    catalog['Home Appliances']['Laundry']['Washing Machines']['Items'].append('Samsung WF45B')
    catalog['Home Appliances']['Laundry']['Washing Machines']['Items'].append('Whirlpool Front Load')

    catalog['Home Appliances']['Cleaning']['Vacuum Cleaners']['Items'] = []
    catalog['Home Appliances']['Cleaning']['Vacuum Cleaners']['Items'].append('Dyson V15 Detect')
    catalog['Home Appliances']['Cleaning']['Vacuum Cleaners']['Items'].append('Roomba j7+')

    catalog['Furniture']['Living Room']['Sofas']['Items'] = []
    catalog['Furniture']['Living Room']['Sofas']['Items'].append('IKEA Landskrona')
    catalog['Furniture']['Living Room']['Sofas']['Items'].append('West Elm Harmony Sofa')

    catalog['Furniture']['Office']['Desks']['Items'] = []
    catalog['Furniture']['Office']['Desks']['Items'].append('Autonomous SmartDesk Pro')
    catalog['Furniture']['Office']['Desks']['Items'].append('Uplift V2 Standing Desk')

    catalog['Furniture']['Office']['Chairs']['Items'] = []
    catalog['Furniture']['Office']['Chairs']['Items'].append('Herman Miller Embody')
    catalog['Furniture']['Office']['Chairs']['Items'].append('Steelcase Leap')

    catalog['Automotive']['Vehicles']['Cars']['Items'] = []
    catalog['Automotive']['Vehicles']['Cars']['Items'].append('Toyota Camry Hybrid')
    catalog['Automotive']['Vehicles']['Cars']['Items'].append('Honda Accord')

    catalog['Automotive']['Bikes']['Mountain']['Items'] = []
    catalog['Automotive']['Bikes']['Mountain']['Items'].append('Trek Marlin 7')
    catalog['Automotive']['Bikes']['Mountain']['Items'].append('Giant Talon 2')

    catalog['Sports']['Outdoor']['Tents']['Items'] = []
    catalog['Sports']['Outdoor']['Tents']['Items'].append('REI Half Dome 2 Plus')
    catalog['Sports']['Outdoor']['Tents']['Items'].append('Big Agnes Copper Spur HV UL2')

    catalog['Sports']['Fitness']['Dumbbells']['Items'] = []
    catalog['Sports']['Fitness']['Dumbbells']['Items'].append('Bowflex SelectTech 552')
    catalog['Sports']['Fitness']['Dumbbells']['Items'].append('PowerBlock Elite EXP')

    catalog['Toys']['Building Sets']['LEGO']['Items'] = []
    catalog['Toys']['Building Sets']['LEGO']['Items'].append('LEGO Ferrari Daytona SP3')
    catalog['Toys']['Building Sets']['LEGO']['Items'].append('LEGO Star Wars Millennium Falcon')

    catalog['Books']['Fiction']['Sci-Fi']['Items'] = []
    catalog['Books']['Fiction']['Sci-Fi']['Items'].append('Dune by Frank Herbert')
    catalog['Books']['Fiction']['Sci-Fi']['Items'].append('The Three-Body Problem by Cixin Liu')

    catalog['Books']['Self-Help']['Productivity']['Items'] = []
    catalog['Books']['Self-Help']['Productivity']['Items'].append('Atomic Habits by James Clear')
    catalog['Books']['Self-Help']['Productivity']['Items'].append('Deep Work by Cal Newport')

    return catalog

