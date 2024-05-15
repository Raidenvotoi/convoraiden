# from apyori import apriori
# import csv
# # Dữ liệu mẫu
# transactions = [['d1', 'd3', 'd4'], 
#  ['d1', 'd3', 'd4'], 
#  ['d3', 'd5'], 
#  ['d4', 'd5'], 
#  ['d2', 'd3', 'd5']]


# # Áp dụng thuật toán Apriori
# results = list(apriori(transactions, min_support=0.3, min_confidence=0.01))

# # In ra tất cả các luật
# for rule in results:
#     print(("Items: " + str(rule.items)).replace("'",""))
#     print("Support: " + str(rule.support))
#     print("Confidence: " + str(rule.ordered_statistics[0].confidence))
#     print("Lift: " + str(rule.ordered_statistics[0].lift))
#     print()
# with open('association_rules.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Items', 'Support', 'Confidence']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for rule in results:
#         items_sorted = sorted(rule.items)  # Sort items
#         items_formatted = "{" + ", ".join(items_sorted) + "}"
#         writer.writerow({'Items': items_formatted, 'Support': rule.support, 'Confidence': rule.ordered_statistics[0].confidence})
from apyori import apriori
import csv
# Dữ liệu mẫu
transactions = [
    {'d1', 'd3', 'd4'},
    {'d1', 'd3', 'd4'},
    {'d3', 'd5'},
    {'d4', 'd5'},
    {'d2', 'd3', 'd5'}
]

# Áp dụng thuật toán Apriori
results = list(apriori(transactions, min_support=0.3, min_confidence=0.1))
with open('association_rules.csv', 'w', newline='') as csvfile:
    fieldnames = ['Rule', 'Support', 'Confidence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
# In ra thông tin thống kê của mỗi luật
    for rule in results:
        print("-----------------")
        print("Items:"+",".join(rule.items))
        print("Support: " + str(rule.support))
        print("Ordered Statistics:")
        
        
        for statistic in rule.ordered_statistics:
            item_base = ', '.join(statistic.items_base) if statistic.items_base else None
            item_add = ', '.join(statistic.items_add)
            if item_base is not None:
                rule_text = f"{item_base} -> {item_add}"
                print(f"  {item_base} -> {item_add}")
                support = str(rule.support)
                print("  Confidence:", statistic.confidence)
                writer.writerow({'Rule': rule_text, 'Support': support, 'Confidence': statistic.confidence})
