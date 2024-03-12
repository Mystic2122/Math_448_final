import pandas as pd

# Assuming you already have the data loaded into a DataFrame named 'data'
df = pd.read_json("NBA_player_data.json")
# Assuming your DataFrame is named df
df = df[df['G'] >= 20]

# Save the DataFrame to a nicely formatted JSON file with each row as a separate JSON object
df.to_json("NBA_player_data.json", orient="records", indent=4)

print(df.shape)