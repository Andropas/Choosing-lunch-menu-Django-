import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=40)

    def __str__(self):
        return self.restaurant_name

    def get_today_menu(self):
        today = timezone.now().date()
        menus = self.menu_set.all()
        todays_menus = menus.filter(day=today)

        if not todays_menus:
            return None
        return todays_menus[0]


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        unique_for_date='day'
    )
    menu_text = models.TextField(max_length=200)
    day = models.DateField("Date")
    votes = models.PositiveIntegerField("Votes", default=0)

    def __str__(self):
        return self.menu_text


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    selected_menu = models.ForeignKey(
        Menu,
        models.SET_NULL,
        null=True,
        blank=True,
    )
    lunch_time = models.TimeField(
        "Lunch time",
        unique=True,
        default=datetime.time(13, 0)
    )

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

    def vote_lunch_menu(self, menu):
        if not self.had_been_lunch_time_already() and menu in self.get_today_menus():
            if self.selected_menu != None:
                old_menu = self.selected_menu
                old_menu.votes -= 1
            
            self.selected_menu = menu
            self.selected_menu.votes += 1

    def had_been_lunch_time_already(self):
        return self.lunch_time > timezone.now().time()

    def get_today_menus(self):
        restaurants = Restaurant.objects.all()
        menus = []
        for r in restaurants:
            menus.append(r.get_today_menu())
        
        return menus
    
    def get_final_menu(self):
        menus = self.get_today_menus()
        sorted_menus = menus[:]
        sorted_menus.sort(reverse=True, key=lambda m: m.votes)
        final_menu = sorted_menus[0]

        return final_menu