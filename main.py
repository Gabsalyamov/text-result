class FileData:

    def __init__(self, f_name):
        self.f_name = f_name
        self.data_txt = list()
        self.number_lines = 0

class BaseFile(FileData):
    def __init__(self, f_name):
        super().__init__(f_name)
        with open(self.f_name, 'r', encoding="utf-8") as fl:
            for line in fl:
                self.data_txt.append(line.strip())
                self.number_lines += 1

def get_key(d: dict, value: int):
    for key, v in d.items():
        if v == value:
            return key

if __name__ == '__main__':

    firs_file = BaseFile("1.txt")
    second_file = BaseFile("2.txt")
    third_file = BaseFile("3.txt")

    result_file = FileData("mytext.txt")

    files_dict = {firs_file: firs_file.number_lines,
                  second_file: second_file.number_lines,
                  third_file: third_file.number_lines}
    files_list = sorted(files_dict.values())

    for idx in files_list:
        tmp_file_data = get_key(files_dict, idx)
        result_file.data_txt.append(f'{tmp_file_data.f_name}\n')
        result_file.data_txt.append(f'{tmp_file_data.number_lines}\n')
        for indx in tmp_file_data.data_txt:
            result_file.data_txt.append(f'{indx}\n')

    print(result_file.data_txt)

    with open(result_file.f_name, 'w', encoding="utf-8") as f:
        f.writelines(result_file.data_txt)
