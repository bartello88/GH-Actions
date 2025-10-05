from random import randint

class User:

    users_amount = 0
    def __init__(self, name, surname, age, sex, pesel):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.__pesel = pesel
        self.accounts = []
        User.users_amount =+ 1


class Account:

    def __init__(self, user:User):
        self.account_number = randint(10000,99999)
        self.user = user
        self.__saldo = 0
        self.__password = "1234567"

    def __hide__password(self):
        return f"*****{self.__password[::-3]}"
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, enroll):
        if enroll >= 0:
            self._saldo = enroll
        else:
            print("Za mało kasy")
    
    @property
    def password(self):
        self.__password = self.__hide__password()
        return self._password

    @password.setter
    def password(self, new_password):
        raise Exception("Can't set password")

    def __repr__(self):
        return f"Konto: {self.user.name} {self.user.surname[0]}"


class StandardAccount(Account):

    def __init__(self, user:User):
        super().__init__(user)
        self.account_type = "Standard"


class PremiumAccount(Account):

    def __init__(self, user:User):
        super().__init__(user)
        self.account_type = "Premium"


class Bank:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__accounts = []
        self.__users = []
    
    def create_account(self, user:User, account_type):
        if account_type == "Standard":
            account = StandardAccount(user)
        elif account_type == "Premium":
            account = PremiumAccount(user)
        user.accounts.append(account)
        self.__accounts.append(account)
        self.__users.append(user)
        return account
    
    def show_users(self):
        print("[-------------Users------------]")
        for i in self.__users:
            print(f"User: {i.name}.{i.surname[0]}")
    
    def show_accounts(self):
        print("[------------Accounts-----------]")
        for i in self.__accounts:
            print(f"Type: {i.account_type} {i.account_number}")
    
    def delete_account(self, account_number):
        for i in self.__accounts:
            if account_number == i.account_number:
                delete = input("Czy usunac konto? tak/nie")
                if delete == "tak":
                    i.remove(account_number)
            else:
                print("Nie ma takiego konta")


if __name__ == "__main__":

    user1 = User("Arek", "Zdunek", 40, 'man', 134574830)
    user2 = User("Tomek", "Zdunek", 47, 'man', 237237499)
    user3 = User("Bartek", "Zdunek", 49, 'man', 234098088)

    bank = Bank("PKO", "Warszawa")
    bank.create_account(user1, "Standard")
    bank.create_account(user2, "Premium")
    bank.create_account(user3, "Standard")
    bank.show_users()
    bank.show_accounts()
    bank.delete_account(22558)






