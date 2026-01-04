import pandas as pd
import os

# Create outputs directory if it doesn't exist
os.makedirs('outputs', exist_ok=True)

# Load dataset
df = pd.read_csv("Top Indian Places to Visit .csv")

# Select required columns
df = df[[
    'City',
    'Name',
    'time needed to visit in hrs',
    'Google review rating',
    'Entrance Fee in INR',
    'Airport with 50km Radius',
    'Weekly Off',
    'Significance',
    'DSLR Allowed',
    'Number of google review in lakhs',
    'Best Time to visit'
]]

def generate_output_for_city(source_city, output_file):
    """Generate output for a specific source city"""
    
    # Filter out same city destinations
    destinations = df[df['City'] != source_city].copy()
    
    # Feature Engineering
    # Time score (lower time = higher score)
    destinations['Time Score'] = 1 / destinations['time needed to visit in hrs']
    
    # Cost score (lower fee = higher score)
    destinations['Cost Score'] = 1 / (destinations['Entrance Fee in INR'] + 1)
    
    # Airport accessibility
    destinations['Airport Score'] = destinations['Airport with 50km Radius'].apply(
        lambda x: 1 if x == 'Yes' else 0
    )
    
    # DSLR allowed bonus
    destinations['DSLR Score'] = destinations['DSLR Allowed'].apply(
        lambda x: 1 if x == 'Yes' else 0
    )
    
    # Final Score Calculation
    destinations['Final Score'] = (
        0.35 * destinations['Google review rating'] +
        0.35 * destinations['Number of google review in lakhs'] +
        0.15 * destinations['Time Score'] +
        0.10 * destinations['Cost Score'] +
        0.05 * destinations['Airport Score']
    )
    
    # Sort results
    top_destinations = destinations.sort_values(
        by='Final Score', ascending=False
    ).head(5)
    
    # Prepare output
    output_text = f"Source City: {source_city}\n"
    output_text += "=" * 80 + "\n"
    output_text += "\nTop 5 Weekend Destinations:\n\n"
    
    # Format the output
    for idx, (_, row) in enumerate(top_destinations.iterrows(), 1):
        output_text += f"{idx}. {row['Name']}\n"
        output_text += f"   City: {row['City']}\n"
        output_text += f"   Time needed: {row['time needed to visit in hrs']} hours\n"
        output_text += f"   Google Rating: {row['Google review rating']}/5.0\n"
        output_text += f"   Entrance Fee: ₹{row['Entrance Fee in INR']}\n"
        output_text += f"   Reviews: {row['Number of google review in lakhs']} lakhs\n"
        output_text += f"   Airport within 50km: {row['Airport with 50km Radius']}\n"
        output_text += f"   DSLR Allowed: {row['DSLR Allowed']}\n"
        output_text += f"   Best Time to Visit: {row['Best Time to visit']}\n"
        output_text += f"   Final Score: {row['Final Score']:.4f}\n"
        output_text += "\n" + "-" * 80 + "\n\n"
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    print(f"Output generated for {source_city} -> {output_file}")
    return output_text

# Generate outputs for three different cities
cities = ['Mumbai', 'Delhi', 'Bangalore']

for city in cities:
    output_file = f"outputs/output_{city.lower()}.txt"
    generate_output_for_city(city, output_file)

print("\nAll outputs generated successfully!")

