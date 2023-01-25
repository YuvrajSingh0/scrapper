import json

def reformateJson():
    path_to_json = "data.json"
    with open(path_to_json, 'r+') as f:
        data = json.load(f)
    
    imgDict = {}
    for item in data:
        rollnumebr = item["img"].split("/")[-1].split(".")[0]
        name = item["name"]
        imgUrl = item["img"]
        company = item["company"]
        branch = item["branch"]
        
        if rollnumebr not in imgDict:
            imgDict[rollnumebr] = {
                "name": name,
                "img": imgUrl,
                "company": [company],
                "branch": branch
            }
        else:
            imgDict[rollnumebr]["company"].append(company)
    
    oneCompany = {}
    for key, value in imgDict.items():
        if len(value["company"]) == 1:
            oneCompany[key] = value
    
    twoCompany = {}
    for key, value in imgDict.items():
        if len(value["company"]) == 2:
            twoCompany[key] = value
    
    threeCompany = {}
    for key, value in imgDict.items():
        if len(value["company"]) == 3:
            threeCompany[key] = value
    
    
    dataCollection = {
        "Having One Company": oneCompany,
        "Having Two Companies": twoCompany,
        "Having Three Companies": threeCompany
    }

    with open("datas.json", "w") as f:
        json.dump(dataCollection, f, indent=4)

    with open("new.json", "w") as f:
        json.dump(imgDict, f, indent=4)

    companyDict = {}
    for item in data:
        if item["company"] not in companyDict:
            companyDict[item["company"]] = 1
        else:
            companyDict[item["company"]] += 1
    
    with open("company.json", "w") as f:
        json.dump(companyDict, f, indent=4)
    

    remaining = 954 - len(imgDict)

    print(f"\n\n\n.............Data Reformating.............\n")
    print(f"The total number of students placed is {len(imgDict)}/954 in Percentage {round(len(imgDict)/954*100)}%.")
    print(f"The total number of students not placed is {remaining}/954 in Percentage {round(remaining/954*100)}%.")
    print(f"\n.............Data Reformated.............\n\n\n")

    companyDataDict = {}
    for item in data:
        if item["company"] not in companyDataDict:
            companyDataDict[item["company"]] = {
                item["name"]: {
                    "img": item["img"],
                    "branch": item["branch"]
                }
            }
        else:
            companyDataDict[item["company"]][item["name"]] = {
                "img": item["img"],
                "branch": item["branch"]
            }
    with open("companyData.json", "w") as f:
        json.dump(companyDataDict, f, indent=4)




reformateJson()