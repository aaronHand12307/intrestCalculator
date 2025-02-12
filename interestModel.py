import plotly.express as px
import pandas as pd

def main(principal, rate, deposits, time, amount):
    indexlist = []  # Fixed: Moved initialization outside

    def fn(principal, rate, deposits, time, amount):
        for i in range(time):
            principal = principal * (1 + rate)
            principal = principal + deposits
            amount.append(principal)
            indexlist.append(i + 1)  # Fixed: Index list should be populated here

        principal = round(principal)

    fn(principal, rate, deposits, time, amount)

    df = pd.DataFrame({'Year': indexlist, 'Amount': amount})  # Fixed: Correct DataFrame format

    fig = px.line(df, x="Year", y="Amount", markers=True,
                  labels={"Year": "Year",
                           "Amount": "Amount of Money (€)"
                           })           


    fig.update_layout(title_text='Compound Interest Modeling', title_x=0.5, template='plotly_dark')

    return fig  # Fixed: Return fig instead of showing it
