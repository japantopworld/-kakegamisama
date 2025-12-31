import pandas as pd
import random

def predict_miniloto(csv_path):
    df = pd.read_csv(csv_path)

    # 本数字だけ抽出（例：N1〜N5）
    numbers = df[['N1', 'N2', 'N3', 'N4', 'N5']].values.flatten()

    # 出現回数
    freq = pd.Series(numbers).value_counts()

    # 全数字（1〜31）
    all_nums = pd.Series(range(1, 32))

    freq = freq.reindex(all_nums, fill_value=0)

    # 未出現回数（直近何回出てないか）
    last_seen = {n: 0 for n in range(1, 32)}

    for _, row in df.iterrows():
        for n in range(1, 32):
            if n in row.values:
                last_seen[n] = 0
            else:
                last_seen[n] += 1

    sleep = pd.Series(last_seen)

    # スコア計算
    score = freq * 0.6 + sleep * 0.4

    # 上位から候補抽出
    candidates = score.sort_values(ascending=False).head(12).index.tolist()

    # そこからランダムで5個（偏り防止）
    result = sorted(random.sample(candidates, 5))

    return result, score.sort_values(ascending=False)
