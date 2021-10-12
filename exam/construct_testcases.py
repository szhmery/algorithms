import os


def generate_report(folder):
    if not folder:
        return

    file_list = os.listdir(folder)
    if not file_list:
        return
    new_file = "report.txt"
    data_dict = {}

    for file_name in file_list:
        tmp_file = os.path.basename(file_name)
        tmp_file = tmp_file[:-4]
        res = tmp_file.split('_')
        switch = res[0]
        topo = res[1]
        # obj = re.match(r'(.*)_(.*).txt', file_name, re.M | re.I)
        # switch = obj.group(0)
        # topo = obj.group(1)

        if switch in data_dict:
            data_dict[switch][topo] = []
        else:
            data_dict[switch] = {topo: []}

        with open(os.path.join(folder, file_name), 'r') as f2:
            while True:
                line = f2.readline()
                if not line:
                    break
                cases = line.split(' ')
                case_name = cases[0]
                case_result = cases[1]
                data_dict[switch][topo].append(case_name + ":" + case_result)

    with open(os.path.join("/Users/sunzhaohui/PycharmProjects/interview/", new_file), 'w') as f1:
        for sw in data_dict:
            f1.write(sw + ":\n")
            for topo in data_dict[sw]:
                f1.write('\t' + topo + ":\n")
                for case in data_dict[sw][topo]:
                    if "\n" in case:
                        f1.write('\t\t' + case)
                    else:
                        f1.write('\t\t' + case + '\n')

    return new_file


if __name__ == '__main__':
    folder = "/Users/sunzhaohui/PycharmProjects/interview/test_data"
    generate_report(folder)
