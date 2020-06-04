def sockMerchant(n, ar):
    ar_items = {}
    pair_count = 0
    for i in range(n):
        if ar[i] not in ar_items:
            ar_items[ar[i]] = 1
        else:
            ar_items[ar[i]] += 1
    for key in ar_items:
        if ar_items[key] >= 2:
            pair_count += ar_items[key] // 2
    return pair_count
