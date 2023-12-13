from django.db import models


class RatingChoice(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=RatingChoice.choices,
        default=RatingChoice.G
    )
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies")

    movie_order = models.ManyToManyField(
        "users.User",
        related_name="movieOrder",
        through="movies_orders.MovieOrder"
    )
