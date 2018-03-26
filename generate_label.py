import os
import re
import argparse
import glob


def convert_label_file(img_path, src_label, dst_label):
    charset = '0123456789+-*()'
    encode_maps = {}
    decode_maps = {}
    for i, char in enumerate(charset, 1):
        encode_maps[char] = i
        decode_maps[i] = char
    
    SPACE_INDEX = 0
    SPACE_TOKEN = ''
    encode_maps[SPACE_TOKEN] = SPACE_INDEX
    decode_maps[SPACE_INDEX] = SPACE_TOKEN
    str_value = re.compile(r'^[0-9]+')

    all_data = glob.glob(os.path.join(img_path, '*.png'))
    with open(src_label, 'r') as s:
        labels_content = s.readlines()
        """The label sequence equal to data name digital number"""
        labels = list(map(lambda x: x.split()[0], labels_content))
    data_label_map = {}

    for filename in all_data:
        code_name = str_value.findall(os.path.splitext(os.path.basename(filename))[0])[0]
        if int(code_name) < len(labels):
            code = labels[int(code_name)]
            code = [SPACE_INDEX if code == SPACE_TOKEN else encode_maps[c] for c in list(code)]
            data_label_map[filename] = code
    with open(dst_label, 'wt') as o:
        for item in data_label_map.items():
            o.write("{}:{}\n".format(item[0], ",".join(list(map(lambda s: str(s), item[1])))))
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert verification code labels.txt to a map label format")
    parser.add_argument('--src_label', type=str, required=True)
    parser.add_argument('--dst_label', type=str, default='labels.txt')
    parser.add_argument('--img_path', type=str, required=True)
    
    args = parser.parse_args()
    convert_label_file(args.img_path, args.src_label, args.dst_label)
