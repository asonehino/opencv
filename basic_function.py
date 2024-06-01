# *arguments는 가변인자(variable argument) : 별이 한개면 리스트
# **keywords는 키워드인자(keyword artument) : 별이 두개면 리스트

def caffe (beverage, *arguments, **keywords):
    print("Do you have any", beverage, "?")
    for arg in arguments:
        print(arg)
    print("****")
    for kw in keywords:
        print(kw, ":", keywords[kw])

caffe("coffee", "it's yummy, sir.", "Would you try?",
      barista = "hyunho",
      client = "BSSM",
      cup = "Venti-size")