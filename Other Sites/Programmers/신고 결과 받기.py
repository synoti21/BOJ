def solution(id_list, report, k):
    answer = []
    report_ndup = set(report)
    report_arr = []
    ban_dict = {}
    fin_ban_dict = {}
    id_dict = {}

    m = 0

    for i in id_list:
        id_dict[i] = m
        m += 1

    for i in range(0, len(id_list)):
        answer.append(0)

    for i in report_ndup:
        temp = i.split(" ")
        report_arr.append(temp);
        ban_dict[temp[1]] = 0

    for i in report_arr:
        ban_dict[i[1]] += 1

    for i in ban_dict.keys():
        if ban_dict[i] >= k:
            fin_ban_dict[i] = ban_dict[i]

    for i in report_arr:
        if (i[1] in fin_ban_dict.keys()):
            answer[id_dict[i[0]]] += 1

    return answer