from django.test import TestCase

from .models import Restaurant, Menu, Employee
from django.utils import timezone
import datetime

# Try vote after lunch began!!!
class EmployeeModelTests(TestCase):

    def test_vote_after_lunch_began(self):
        e = Employee(first_name="Name", last_name="Surname")
        def had_been_lunch_time_already():
            return True
        e.had_been_lunch_time_already = had_been_lunch_time_already
        menu = Menu(menu_text="Menu text", day=timezone.now().date())
        e.vote_lunch_menu(menu)

        self.assertIs(menu.votes, 0)
    
    def test_vote_for_future_menu(self):
        e = Employee(first_name="Name", last_name="Surname")
        def had_been_lunch_time_already():
            return False
        e.had_been_lunch_time_already = had_been_lunch_time_already
        menu = Menu(menu_text="Menu text", day=timezone.now().date()+datetime.timedelta(days=1))
        e.vote_lunch_menu(menu)

        self.assertIs(menu.votes, 0)
    

class RestaurantModelTests(TestCase):

    def test_no_today_menu(self):
        r = Restaurant(restaurant_name="Restaurant")
        r.save()
        today_menu = r.get_today_menu()

        self.assertIs(today_menu, None)