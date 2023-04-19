# вар_1
best_revenue = float("-inf")
best_month = None

revenue = [None, 1000, 2000, None, 3000, None, None, 5000, 4000, 4500, None, None]
for month, month_rev in enumerate(revenue):
    if month_rev is not None and month_rev > best_revenue:
        best_revenue = month_rev
        best_month = month + 1

print(best_revenue, best_month)


# вар_2
best_revenue = None
best_month = None

revenue = [None, 1000, 2000, None, 3000, None, None, 5000, 4000, 4500, None, None]
for month, month_rev in enumerate(revenue):
    # потрібна зайва перевірка best_revenue is None or
    if month_rev is not None and (best_revenue is None or month_rev > best_revenue):
        best_revenue = month_rev
        best_month = month + 1

print(best_revenue, best_month)
