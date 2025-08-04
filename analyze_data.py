
import pandas as pd

def analyze_remittance_data(file_path):
    df = pd.read_csv(file_path)
    print("\nDescriptive Statistics:")
    print(df.describe())

    print("\nRemittances over time:")
    print(df.sort_values(by='Year'))

    # Calculate year-over-year change
    df = df.sort_values(by='Year')
    df["Remittances_Change"] = df["Remittances"].diff()
    print("\nYear-over-year Remittances Change:")
    print(df)

    return df

if __name__ == "__main__":
    file_path = "yemen_remittances_cleaned.csv"
    analyzed_df = analyze_remittance_data(file_path)
    analyzed_df.to_csv("yemen_remittances_analyzed.csv", index=False)
    print("Analysis results saved to yemen_remittances_analyzed.csv")


