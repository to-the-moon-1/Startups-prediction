from django.db import models


class Customer(models.Model):
    CITY_CHOICES = (
        ('is_CA', 'California'), ('is_NY', 'New York'), ('is_MA', 'Massachusetts'), ('is_TX', 'Texas'),
        ('is_otherstate', 'Other state'))
    city = models.CharField(max_length=13, choices=CITY_CHOICES, default=1)

    CATEGORY_CHOICES = (
        ('is_software', 'Software'), ('is_web', 'Web-development'), ('is_mobile', 'Mobile development'),
        ('is_enterprise', 'Enterprise'), ('is_advertising', 'Advertising'), ('is_gamesvideo', 'Video games'),
        ('is_ecommerce', 'Ecommerce'), ('is_biotech', 'Biotech'), ('is_consulting', 'Consulting'),
        ('is_othercategory', 'Other category'))
    category = models.CharField(max_length=18, choices=CATEGORY_CHOICES, default=1)

    avg_members = models.IntegerField(default=0)
    relationships = models.IntegerField(default=0)

    milestones = models.IntegerField(default=0)

    funding_rounds = models.IntegerField(default=0)

    # ROUND_CHOICES = (
    #     (True, 'on'), (False, 'off')
    # )

    round_a = models.BooleanField(max_length=7, default=False)
    round_b = models.BooleanField(max_length=7, default=False)

    def __str__(self):
        return self.city, self.category
