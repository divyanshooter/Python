from faker import Faker
import random

faker =Faker()

restaurant_menu = [
    "Margherita Pizza",
    "Cheeseburger",
    "Caesar Salad",
    "Spaghetti Carbonara",
    "Grilled Salmon",
    "Chicken Tikka Masala",
    "Vegetable Stir Fry",
    "Beef Tacos",
    "Pancakes",
    "Shrimp Scampi",
    "Mushroom Risotto",
    "Chocolate Lava Cake",
    "Caprese Salad",
    "Lamb Chops",
    "Fettuccine Alfredo",
    "Tom Yum Soup"]


order=[]
order.extend(random.sample(restaurant_menu, random.randint(1,len(restaurant_menu))))

def get_orders():
    return {
        "order_id":random.randint(1,20000),
        "user_id":faker.email(),
        "name":faker.name(),
        "items":order,
        "cost":len(order)*20,
        "created_at":faker.date(),
    }