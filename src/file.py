import const


def export_csv(df):
    df.to_csv(f'{const.dataPath}{const.symbol}.csv', index=False)


def export_json(df):
    df.to_json(f'{const.dataPath}{const.symbol}.json', index=False)


def export_png(plt):
    plt.savefig(f'{const.chartPath}{const.symbol}.png')