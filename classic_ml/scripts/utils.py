import pandas as pd

def _split_features(df, target):
    """Разбивает колонки на числовые, категориальные и ID-like."""
    numeric = []
    categorical = []
    id_like = []

    for col in df.columns:
        if col == target:
            continue
        nunique = df[col].nunique()
        if pd.api.types.is_numeric_dtype(df[col]) and nunique > 20:
            numeric.append(col)
        elif nunique <= 30:
            categorical.append(col)
        else:
            id_like.append(col)

    return numeric, categorical, id_like