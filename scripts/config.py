pal = sns.color_palette("deep")

sns.set_context(
    "talk",
    font_scale=1,
    rc={
        "lines.linewidth": 1,
        "text.usetex": True,
        "font.size": 10,
        "font.family": 'sans-serif'
    })
sns.set_style('ticks')
sns.set_style({'ytick.direction': 'in', 'ytick.major.size': 6.0,  'ytick.minor.size': 3.0,
               'xtick.direction': 'in', 'xtick.major.size': 6.0,  'xtick.minor.size': 3.0})

font = {'size': 10}
rc('font', **font)


fig = plt.figure(figsize=(4, 3), dpi=200)
ax = fig.add_subplot(1, 1, 1)
