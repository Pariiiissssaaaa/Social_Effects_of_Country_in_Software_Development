import pandas as pd

sheet = pd.read_excel("OrganizationRepos.xlsx", sheet_name="Repos")

for ridx, row in sheet.iterrows():
	if row['Crawled'] == 'Yes':
		continue

	url = row['Repo URL']
	filename = row['Repo Name'].replace(" ", "_").replace("(", "").replace(")", "")
	print(
		"git clone {} {}".format(url, filename)
		)

