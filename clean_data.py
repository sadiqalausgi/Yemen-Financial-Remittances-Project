
import pandas as pd

def clean_remittance_data(file_path):
    df = pd.read_csv(file_path, skiprows=4) # Skip metadata rows
    df = df[df["Country Code"] == "YEM"] # Filter for Yemen
    # Drop unnecessary columns. The last column might be unnamed and empty, so we'll drop it if it exists.
    cols_to_drop = ["Country Name", "Country Code", "Indicator Name", "Indicator Code"]
    # Check if there's an unnamed column at the end and add it to the list if it exists
    if df.columns[-1].startswith("Unnamed:"):
        cols_to_drop.append(df.columns[-1])
    df = df.drop(columns=cols_to_drop)
    df = df.melt(id_vars=[], var_name="Year", value_name="Remittances")
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Remittances"] = pd.to_numeric(df["Remittances"], errors="coerce")
    df = df.dropna(subset=["Year", "Remittances"])
    df = df[(df["Year"] >= 1990) & (df["Year"] <= 2023)]
    return df

if __name__ == "__main__":
    file_path = "/home/ubuntu/upload/API_BX.TRF.PWKR.CD.DT_DS2_en_csv_v2_38454.csv"
    cleaned_df = clean_remittance_data(file_path)
    cleaned_df.to_csv("/home/ubuntu/yemen_remittances_cleaned.csv", index=False)
    print("Data cleaned and saved to yemen_remittances_cleaned.csv")


