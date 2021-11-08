import pickle
import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import product
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.multitest import multipletests
from scipy.stats import chi2, chi2_contingency, chisquare


columns = ['PushEvent', 'ForkEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent', 'CreateEvent', 'PullRequestReviewCommentEvent', 'DeleteEvent', 'GollumEvent', 'MemberEvent', 'ReleaseEvent', 'CommitCommentEvent', 'PublicEvent', 'star_count', 'forks_count', 'open_issues_count', 'jaccard', 'CommentLen', 'iat', 'num_leaders', 'tpc_1', 'tpc_2']

x = pd.read_pickle('repo_features.pickle')

c2p = []
for c in columns:
	zh = x[x['Label'] == 0][c]
	us = x[x['Label'] == 1][c]

	z, p = ztest(zh, us)
	c2p.append([c, p])

print("Bonferroni!")
c2p = sorted(c2p, key=lambda x: x[1])
ps = [i[1] for i in c2p]
reject, pvals_corrected, _, alphacBonf = multipletests(ps, alpha=0.005,  method='bonferroni', is_sorted=True)

print("alphacBonf:", alphacBonf)
print("Feature, Old P, Corrected P, Reject?")
for cp, r, pc in zip(c2p, reject, pvals_corrected):
	print("%s,%.2E,%.2E,%s" % (cp[0], cp[1], pc, r))

import sys; sys.exit(0)

activity_columns = ['PushEvent', 'ForkEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent', 'CreateEvent', 'PullRequestReviewCommentEvent', 'DeleteEvent', 'GollumEvent', 'MemberEvent', 'ReleaseEvent', 'CommitCommentEvent', 'PublicEvent']


zh = x[x['Label'] == 0]['repo_id']
us = x[x['Label'] == 1]['repo_id']

pvals = []
print("Computing %d combos" % (len(zh) * len(us)))
for z, u in tqdm(product(zh, us)):
	zhacc = x[x['repo_id'] == z][activity_columns]
	usacc = x[x['repo_id'] == u][activity_columns]

	d = np.array([
		usacc.to_numpy()[0] + 1, 
		zhacc.to_numpy()[0] + 1
	])
	d = d.T

	stat, p, dof, expected = chi2_contingency(d)
	pvals.append(1-p)

pickle.dump(pvals, open("pvals.pkl", "wb"))

# us = []
# zh = []

# us = 

# for c in activity_columns:
# 	zh_ = x[x['Label'] == 0][c]
# 	us_ = x[x['Label'] == 1][c]	

# 	zh.append(zh_.mean())
# 	us.append(us_.mean())

# d = np.array([us, zh])
# d = d.T

# print("ZH!!", zh)
# stat, p, dof, expected = chi2_contingency(d)

# # interpret test-statistic
# prob = 0.95
# critical = chi2.ppf(prob, dof)
# print(dof, critical, stat)
# if abs(stat) >= critical:
# 	print('Dependent (reject H0)')
# else:
# 	print('Independent (fail to reject H0)')

# # interpret p-value
# alpha = 1.0 - prob
# print("p-value", p)
# if p <= alpha:
# 	print('Dependent (reject H0)')
# else:
# 	print('Independent (fail to reject H0)')

