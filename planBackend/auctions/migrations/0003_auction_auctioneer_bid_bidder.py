<<<<<<< HEAD
# Generated by Django 5.1.7 on 2025-04-13 12:07
=======
# Generated by Django 5.2 on 2025-04-13 08:10
>>>>>>> main

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("auctions", "0002_remove_bid_bidder"),
=======
        ('auctions', '0002_remove_bid_bidder'),
>>>>>>> main
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
<<<<<<< HEAD
            model_name="auction",
            name="auctioneer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="auctions",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bid",
            name="bidder",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
=======
            model_name='auction',
            name='auctioneer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
>>>>>>> main
        ),
    ]
