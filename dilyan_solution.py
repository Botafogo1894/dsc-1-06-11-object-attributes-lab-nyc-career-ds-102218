class Driver:

#init method
    def __init__(self, first, last, miles_driven, rating):
        self._first = first
        self._last = last
        self._miles_driven = miles_driven
        self._rating = rating

#setters and getters for First

    def get_first(self):
        print("GETTING FIRST NAME")
        return self._first

    def set_first(self, first):
        print("SETTING FIRST NAME")
        self._first = first

    first = property(get_first, set_first)

#setters and getters for Last
    def get_last(self):
        print("GETTING LAST NAME")
        return self._last

    def set_last(self, last):
        print("SETTING LAST NAME")
        self._first = last

    last = property(get_last, set_last)
#setters and getters for miles driven

    def get_miles_driven(self):
        print("GETTING MILES")
        return self._miles_driven

    def set_miles_driven(self, miles_driven):
        print("SETTING MILES")
        self.__miles_driven = miles_driven

    miles_driven = property(get_miles_driven, set_miles_driven)

#setters and getters fro rating

    def get_rating(self):
        print("GETTING RATING")
        return self._rating

    def set_rating(self, rating):
        print("SETTING RATING")
        self._rating = rating

    rating = property(get_rating, set_rating)

    def greet_passenger(self):
        return "Hello! I'll be your driver today. My name is " + self.first + " " + self.last


#2. SAME FOR PASSENGER:

class Passenger:

#init method
    def __init__(self, first, last, email):
        self._first = first
        self._last = last
        self._email = email

#setters and getters for First

    def get_first(self):
        print("GETTING FIRST NAME")
        return self._first

    def set_first(self, first):
        print("SETTING FIRST NAME")
        self._first = first

    first = property(get_first, set_first)

#setters and getters for Last
    def get_last(self):
        print("GETTING LAST NAME")
        return self._last

    def set_last(self, last):
        print("SETTING LAST NAME")
        self._first = last

    last = property(get_last, set_last)
#setters and getters for email

    def get_email(self):
        print("GETTING MILES")
        return self._email

    def set_email(self, email):
        print("SETTING EMAIL")
        self._email = email

    email = property(get_email, set_email)

#define Yell name

    def yell_name(self):
            return f"{self.first.upper()} {self.last.upper()}!"

# Testing

passenger = Passenger("Ron", "Burgundy", "ron.burgundy1984@gmail.com")
print(passenger.first) # "Ron"
print(passenger.last) # "Burgundy"
print(passenger.email) # "ron.burgundy1984@gmail.com"
passenger.yell_name() # "RON BURGUNDY"
