from django.core.management.base import BaseCommand
from gadgets.models import Gadget

FALLBACK_GADGETS = [
    {
        "name": "iPad Pro 12.9 (2022)",
        "brand": "Apple",
        "price": 112900.00,
        "category": "tablet",
        "specs": {"ram": "8GB", "storage": "128GB", "cpu": "Apple M2"},
        "image_url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-129-2022-1.jpg"
    },
    {
        "name": "Samsung Galaxy Tab S9 Ultra",
        "brand": "Samsung",
        "price": 108999.00,
        "category": "tablet",
        "specs": {"ram": "12GB", "storage": "256GB", "cpu": "Snapdragon 8 Gen 2"},
        "image_url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s9-ultra-1.jpg"
    },
    {
        "name": "Xiaomi Pad 6",
        "brand": "Xiaomi",
        "price": 26999.00,
        "category": "tablet",
        "specs": {"ram": "8GB", "storage": "128GB", "cpu": "Snapdragon 870"},
        "image_url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-pad-6-1.jpg"
    },
    {
        "name": "Lenovo Tab P12 Pro",
        "brand": "Lenovo",
        "price": 69999.00,
        "category": "tablet",
        "specs": {"ram": "8GB", "storage": "256GB", "cpu": "Snapdragon 870"},
        "image_url": "https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-tab-p12-pro-1.jpg"
    },
    {
        "name": "Realme Pad X",
        "brand": "Realme",
        "price": 27999.00,
        "category": "tablet",
        "specs": {"ram": "6GB", "storage": "128GB", "cpu": "Snapdragon 695"},
        "image_url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-pad-x-1.jpg"
    }
    ]
 


class Command(BaseCommand):
    help = 'Populate database with fallback gadget data'

    def handle(self, *args, **kwargs):
        try:
            for item in FALLBACK_GADGETS:
                Gadget.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'brand': item['brand'],
                        'price': item['price'],
                        'category': item['category'],
                        'specs': item['specs'],
                        'image_url': item['image_url']
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'Populated {len(FALLBACK_GADGETS)} gadgets'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))