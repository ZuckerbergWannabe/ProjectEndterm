import matplotlib.pyplot as plt
import pandas as pd
from database import DatabaseManager

def plot_sales_report():
    """Displays a sales report"""
    db = DatabaseManager()
    sales = db.fetch_all("SELECT date, total_price FROM sales")

    df = pd.DataFrame(sales, columns=["Date", "Total Sales"])
    df.groupby("Date")["Total Sales"].sum().plot(kind="bar")
    plt.xlabel("Date")
    plt.ylabel("Total Sales ($)")
    plt.title("Sales Report")
    plt.show()
