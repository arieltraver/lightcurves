import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
tree = ET.parse('sync.xml')
root = tree.getroot()
data = {'num_planets': [], 'stellar_mass': []}

# Loop through the XML elements and extract the data
for element in root:
    data['num_planets'].append(element[0].text)
    data['stellar_mass'].append(element[1].text)
    print('appended')
    

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('result.csv', index=False)