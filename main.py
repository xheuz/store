import csv

from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader(searchpath="./"))

WHATSAPP_CONTACT = "18098461452"

def get_inventory():
    content = []
    with open("src/data/inventory.csv") as source_file:
        content += csv.DictReader(source_file)

    ordered_by_category = {}
    for item in content:
        values = item.values()
        count = 0
        for value in values:
            if not value:
                count += 1
                break

        if count > 0 or item["vendido"] != 'N':
            continue

        category = item.pop("categoria")
        if category not in ordered_by_category:
            ordered_by_category[category] = []
        ordered_by_category[category].append(item)
    return ordered_by_category

articles_by_category = get_inventory()

# outputs
with open("public/index.html", "w") as output_file:
    template = template_env.get_template("src/templates/index.html")
    output_file.write(
        template.render(
            title="Tienda Personal",
            shop_title="Articulos Disponibles",
            categories=articles_by_category,
            whatsapp_contact=WHATSAPP_CONTACT
        )
    )

# for category, articles in articles_by_category.items():
#     for product in articles:
#         _id = product["id"]
#         if not _id:
#             continue
#         filename = f"public/products/{_id}.html"
#         with open(filename, "w") as output_file:
#             template = template_env.get_template("src/product.html")
#             output_file.write(
#                 template.render(
#                     product=product,
#                     whatsapp_contact=WHATSAPP_CONTACT
#                 )
#             )

