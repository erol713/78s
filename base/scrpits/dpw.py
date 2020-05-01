import pandas as pd
import json
import numpy as np
import textract


def dpword(request):

    text = textract.process(
        "reports/Vivacom - Data Protector/Report/Vivacom Data Protector Seveneighths Summary.docx")

    df = text.decode("utf-8")

    df = df.split("Summary")[-1].strip()
    df = df.split("\n")

    while("" in df):
        df.remove("")

    size = len(df)

    idx_list = [idx for idx, val in
                enumerate(df) if "CELL MANAGER #" in val]

    res = [df[i: j] for i, j in
           zip([0] + idx_list, idx_list +
               ([size] if idx_list[-1] != size else []))]

    info = []

    for i in res[1:]:
        cmNames = []

        for j in i:
            if len(j) < 3:
                continue

            if "CELL MANAGER #" in j:

                cmNames.append(j.split(":")[1])
                continue

            cmNames.append(j.split(".")[0])
        info.append(cmNames)

    summ = {}
    for i in info:

        cm = []
        license = []
        installed = []
        used = []
        nm = i[0]

        for j in i[1:]:
            x = j.split(",")
            installed.append(x[0].split()[0])
            license.append(' '.join(x[0].split()[1:]))
            if len(x) < 2:
                used.append("1")
                continue
            used.append(x[1].split()[0])

        cm.append(installed)
        cm.append(used)
        cm.append(license)

        summ[nm] = cm

    return(summ)
