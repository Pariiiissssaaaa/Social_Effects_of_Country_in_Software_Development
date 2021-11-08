import pandas as pd

sheet = pd.read_excel("OrganizationRepos.xlsx", sheet_name="Repos")

for ridx, row in sheet.iterrows():
	if row['Crawled'] == 'Yes':
		continue
	url = row['Repo URL']
	filename = row['Repo Name'].replace(" ", "_").replace("(", "").replace(")", "")

	repo_name = row['Repo URL'].replace("https://github.com/", "")
	url= 'https://api.github.com/repos/' + repo_name
	print(
		"curl -u 'fredzilla' %s > %s.api" % (url, filename)
		)

