# products/management/commands/import_products.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Product
import json

UserModel = get_user_model()

ADMIN_ID = "gui"
ADMIN_PASSWORD = "guiguigui"


class Command(BaseCommand):
    help = "Import initial products data from JSON file"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Product.objects.all().delete()

        with open("front/src/assets/products.json", "r") as file:
            data = json.load(file)
            for item in data["data"]:
                Product.objects.create(
                    code=item["code"],
                    name=item["name"],
                    description=item["description"],
                    price=item["price"],
                    quantity=item["quantity"],
                    inventory_status=item["inventoryStatus"],
                    category=item["category"],
                    image=item.get("image", ""),
                    rating=item.get("rating", None),
                )
        self.stdout.write(self.style.SUCCESS("Products imported successfully"))

        UserModel.objects.create_superuser(ADMIN_ID, "admin@gui.gui", ADMIN_PASSWORD)
