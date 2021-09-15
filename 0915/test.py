features_unique_list = [[1, 2], [1, 2, ], [1, 2, 3], [1, 2]]
features_length = 4
y_unique_value = [1, 2]

before_check_ind = 0

for i in range(features_length):
    feature_length = len(features_unique_list[i])

    if i != features_length-1:
        for k in range(len(y_unique_value)):
            check_col_ind = before_check_ind + k
            tmp = []
            for j in range(feature_length):
                now = check_col_ind + len(y_unique_value)*j
                tmp.append(now)
            print(tmp)
        before_check_ind = now + 1
