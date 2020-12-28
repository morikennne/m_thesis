""" $ python3 summarize_tex_src.py """

import sys

# ここでソースファイル名を指定（main.tex は書かない）
input_file_list =   ["abstract", 
                    "introduction",
                    "related_work",
                    "basic_IQ",
                    "segment_IQ",
                    "switch",
                    "eval",
                    "summary",
                    "appendix1",
                    "appendix2",
                    "appendix3",
                    "publication",
                    "acknowledgement"
                  ]

# 出力ファイル名
output_file_name = "tex_src"

# 区切り線
separation = "+++++++++++++++++++++++++\n"

def prosessing():
    # 出力ファイルのオープン
    output_file = open(output_file_name, "w")

    # main を最初に開く
    with open("main.tex", "r") as input_file:
        text = input_file.read() # 取得
        # 書き込み
        output_file.write(separation + "main.tex\n" + separation)
        output_file.write(text)
        output_file.write("\n\n")

    for name in input_file_list:
        path = "src/" + name + ".tex" # src/filename.tex
        with open(path, "r") as input_file:
            text = input_file.read() # 取得
            # 書き込み
            output_file.write(separation + path + "\n" + separation)
            output_file.write(text)
            output_file.write("\n\n")

    output_file.close() # ファイルクローズ

if __name__ == "__main__":
    prosessing()
