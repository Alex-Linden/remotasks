import pandas as pd

df = pd.read_csv("test.csv")

# Reduce dataframe to only AMD processor laptops
amd_laptops = df[df["processor_brand"] == "AMD"]



# def gb_to_numeric(x):
#     return int(x.split(" ")[0])

def gb_to_numeric(x):
    val = x.split(" ")[1]
    if val.isdigit():
        return int(val)
    else:
        return None

#converts all ram_gb data to a number
amd_laptops.loc[:, 'ram_gb'] = amd_laptops['ram_gb'].apply(lambda x: gb_to_numeric(x))

amd_laptops_more_than_4gb_ram = amd_laptops[amd_laptops['ram_gb'] > 4]


#converts all ssd data to a number
#amd_laptops_more_than_4gb_ram.loc[:, 'ssd'] = amd_laptops_more_than_4gb_ram['ssd'].apply(lambda x: gb_to_numeric(x))

amd_over_4gb_ram_512gb_hdd = amd_laptops_more_than_4gb_ram[amd_laptops_more_than_4gb_ram['ssd'] > 512]

amd_over_4gb_ram_512gb_hdd = amd_over_4gb_ram_512gb_hdd.sort_values(by='star_rating', ascending=False).head(5)
print(amd_over_4gb_ram_512gb_hdd.to_string())

