import pandas as pd

def list_to_csv(lst, model_name, file_name):
    tmp_dict = dict()
    tmp_dict[model_name] = lst
    pd.DataFrame(tmp_dict, index=list(range(len(lst)))).to_csv(f"../{file_name}")

    print(f"{file_name} 저장 완료!")