from datetime import datetime
def get_days_from_today(date):
    try:
        date_1 = datetime.strptime(date, "%Y-%m-%d")
        date_2 = datetime.now()
        difference = date_2.toordinal() - date_1.toordinal()
        print(difference)
    except ValueError:
        print("Дату записано в неправильному форматі")
  

date = input("Введіть дату у форматі YYYY-MM-DD:")  
get_days_from_today(date)