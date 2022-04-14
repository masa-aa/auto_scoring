import subprocess
from subprocess import PIPE
import glob
import os
import re


def rename(folder: str) -> None:
    """034_1116209123_name.txt -> 1116209123_name.txt in folder"""

    files = glob.glob(os.getcwd() + "/" + folder + "/*")
    count = 0

    for file in files:
        if re.search('[0-9]{3}', file):
            count += 1
        rename_file = re.sub('[0-9]{3}_1116', '1116', file)
        rename_file = re.sub('_[^1]{1,}Q', '_Q', rename_file)
        os.rename(file, rename_file)

    print(f"-----renamed {count} files------")


def output(filename: str, arg="") -> tuple:
    """filename(Cのコード)をコンパイルして引数argで実行する"""

    _, file = filename.split("\\")
    ID, _ = file.split(".")
    try:
        # コンパイル
        out = subprocess.run(f"gcc {filename} -o {ID}.exe", shell=True, stdout=PIPE, stderr=PIPE, text=True, timeout=10)
        if out.returncode != 0:
            return ID, "CompileError"
        if out.stderr:
            return ID, "FileError"
    except:
        return ID, "FileError"

    try:
        # 実行
        out = subprocess.run(f"{ID}.exe {arg}", shell=True, stdout=PIPE, stderr=PIPE, text=True, timeout=1)
        # 削除
        subprocess.run(f"del {ID}.exe", shell=True)

        if out.returncode == 0:
            return ID, out.stdout.replace("\n", " ")
        else:
            return ID, "RunTimeError"
    except:
        return ID, "CompileError"


def output_text(filename: str, outputs: list) -> None:
    """filename(.txt)にoutputsを書き込む"""
    f = open(filename, 'a')
    for ID, out in outputs:
        f.write(f"{ID} : {out}\n")


def all_execution(folder: str, arg: str = "", save: str = "") -> list:
    """folder内の.cファイルにoutputを作用させる. outputsを保存する場合はsaveにファイル名(.txt)を指定する．"""
    rename(folder)
    files = glob.glob(os.getcwd() + "/" + folder + "/*")

    outputs = []
    for file in files:
        _, file = file.split("/")
        if re.search('.c', file):
            out = output(file, arg)
            print(*out, sep=" : ")
            outputs.append(out)

    if save:
        output_text(save, outputs)

    return outputs


def equal_text(text1, text2):
    """2つのtextが改行, スペース除いて一致するか判定する. """
    s = text1.replace("\n", "").replace(" ", "")
    t = text1.replace("\n", "").replace(" ", "")

    return s == t


def equal(folder: str, outputs: list, save: str = ""):
    """folder(.txt)とoutputsが一致するか判定する. 結果を保存する場合はsaveにファイル名(.txt)を指定する．"""
    rename(folder)
    files = glob.glob(os.getcwd() + "/" + folder + "/*")

    compare = []
    for ID, output in outputs:
        realID = ""
        for c in ID:
            if c.isdigit():
                realID += c
            else:
                break
        ID = realID
        if "Error" in output:
            print(ID, output, sep=" : ")
            compare.append((ID, output))
            continue

        for file in files:

            if realID in file:
                text = ""
                is_open = False
                for encode in ["UTF-8", "Shift_JIS", "EUC-JIS", "ISO-2022-JP", "CP932"]:
                    try:
                        text = open(file, encoding=encode).read()
                        is_open = True
                        break
                    except:
                        pass

                if is_open:
                    result = ID, equal_text(text, output)
                else:
                    result = ID, "Cannot Open File"

                print(*result, sep=" : ")
                compare.append(result)

    if save:
        output_text(save, compare)

    return compare


if __name__ == '__main__':
    outputs = all_execution(folder="sample_c", arg="2 2", save="sample.txt")

    equal(folder="sample_txt", outputs=outputs, save="sample_equal.txt")
