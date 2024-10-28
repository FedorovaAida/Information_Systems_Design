import re

class Patient:
    def __init__(self, first_name, last_name, date_of_birth, email, gender, phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__gender = gender
        self.__phone = phone

    # Геттеры
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_phone(self):
        return self.__phone

    # Сеттеры с валидацией
    def set_first_name(self, first_name):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        self.__first_name = first_name

    def set_last_name(self, last_name):
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Фамилия должна быть непустой строкой.")
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        # Простая проверка на наличие данных
        if not date_of_birth:
            raise ValueError("Дата рождения не может быть пустой.")
        self.__date_of_birth = date_of_birth

    def set_email(self, email):
        if "@" not in email:
            raise ValueError("Некорректный формат email.")
        self.__email = email

    def set_gender(self, gender):
        if not isinstance(gender, str) or not gender.strip():
            raise ValueError("Пол не может быть пустым.")
        self.__gender = gender

    def set_phone(self, phone):
        if not phone.isdigit() or len(phone) < 10:
            raise ValueError("Неверный формат номера телефона.")
        self.__phone = phone
