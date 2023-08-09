"""
和文件相关的类定义
"""
import json
from typing import List
from data_define import Record


# 先定义一个抽象类来做顶层设计，确定有哪些功能实现
class FileReader:

    def read_data(self) -> List[Record]:
        # 读取文件数据，读到的每一行数据都转换为Record对象，将他们都封装到list内返回
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    # 复写（实现抽象方法）父类方法
    def read_data(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: List[Record] = []
        for line in f.readlines():
            line = line.strip()     # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    # 复写父类方法
    def read_data(self) -> List[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: List[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
