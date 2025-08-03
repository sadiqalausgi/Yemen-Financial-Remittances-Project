import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Add Amiri font to matplotlib
font_path = "/usr/share/fonts/opentype/fonts-hosny-amiri/Amiri-Regular.ttf"
fm.fontManager.addfont(font_path)
plt.rcParams["font.family"] = "Amiri"

def visualize_remittance_data(file_path):
    df = pd.read_csv(file_path)

    # Plot 1: Remittances over time
    plt.figure(figsize=(12, 6))
    plt.plot(df["Year"], df["Remittances"], marker="o", linestyle="-", color="skyblue")
    plt.title("تحويلات اليمن السنوية (1990-2023)", fontsize=16)
    plt.xlabel("السنة", fontsize=12)
    plt.ylabel("التحويلات (بالدولار الأمريكي)", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/yemen_remittances_time_series.png")
    plt.close()

    # Plot 2: Year-over-year change
    plt.figure(figsize=(12, 6))
    plt.bar(df["Year"], df["Remittances_Change"], color="lightcoral")
    plt.title("التغير السنوي في تحويلات اليمن (1990-2023)", fontsize=16)
    plt.xlabel("السنة", fontsize=12)
    plt.ylabel("التغير في التحويلات (بالدولار الأمريكي)", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/yemen_remittances_yoy_change.png")
    plt.close()

if __name__ == "__main__":
    file_path = "/home/ubuntu/yemen_remittances_analyzed.csv"
    visualize_remittance_data(file_path)
    print("Visualizations generated and saved.")

