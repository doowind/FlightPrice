# -*- coding: utf-8 -*-
import requests
import json
import numpy as np
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import math
import os

image = None
image2 = None
btnStart = None





class MY_GUI():
    city = {'阿尔山': 'YIE', '阿克苏': 'AKU', '阿拉善右旗': 'RHT', '阿拉善左旗': 'AXF', '阿勒泰': 'AAT', '阿里': 'NGQ', '澳门': 'MFM',
            '安庆': 'AQG', '安顺': 'AVA', '鞍山': 'AOG', '巴彦淖尔': 'RLK', '百色': 'AEB', '包头': 'BAV', '保山': 'BSD', '北海': 'BHY',
            '北京': 'BJS', '白城': 'DBC', '白山': 'NBS', '毕节': 'BFJ', '博乐': 'BPL', '重庆': 'CKG', '昌都': 'BPX', '常德': 'CGD',
            '常州': 'CZX', '朝阳': 'CHG', '成都': 'CTU', '池州': 'JUH', '赤峰': 'CIF', '揭阳': 'SWA', '长春': 'CGQ', '长沙': 'CSX',
            '长治': 'CIH', '承德': 'CDE', '沧源': 'CWJ', '达县': 'DAX', '大理': 'DLU', '大连': 'DLC', '大庆': 'DQA', '大同': 'DAT',
            '丹东': 'DDG', '稻城': 'DCY', '东营': 'DOY', '敦煌': 'DNH', '芒市': 'LUM', '额济纳旗': 'EJN', '鄂尔多斯': 'DSN', '恩施': 'ENH',
            '二连浩特': 'ERL', '佛山': 'FUO', '福州': 'FOC', '抚远': 'FYJ', '阜阳': 'FUG', '赣州': 'KOW', '格尔木': 'GOQ', '固原': 'GYU',
            '广元': 'GYS', '广州': 'CAN', '贵阳': 'KWE', '桂林': 'KWL', '哈尔滨': 'HRB', '哈密': 'HMI', '海口': 'HAK', '海拉尔': 'HLD',
            '邯郸': 'HDG', '汉中': 'HZG', '杭州': 'HGH', '合肥': 'HFE', '和田': 'HTN', '黑河': 'HEK', '呼和浩特': 'HET', '淮安': 'HIA',
            '怀化': 'HJJ', '黄山': 'TXN', '惠州': 'HUZ', '鸡西': 'JXA', '济南': 'TNA', '济宁': 'JNG', '加格达奇': 'JGD', '佳木斯': 'JMU',
            '嘉峪关': 'JGN', '金昌': 'JIC', '金门': 'KNH', '锦州': 'JNZ', '嘉义': 'CYI', '西双版纳': 'JHG', '建三江': 'JSJ', '晋江': 'JJN',
            '井冈山': 'JGS', '景德镇': 'JDZ', '九江': 'JIU', '九寨沟': 'JZH', '喀什': 'KHG', '凯里': 'KJH', '康定': 'KGT', '克拉玛依': 'KRY',
            '库车': 'KCA', '库尔勒': 'KRL', '昆明': 'KMG', '拉萨': 'LXA', '兰州': 'LHW', '黎平': 'HZH', '丽江': 'LJG', '荔波': 'LLB',
            '连云港': 'LYG', '六盘水': 'LPF', '临汾': 'LFQ', '林芝': 'LZY', '临沧': 'LNJ', '临沂': 'LYI', '柳州': 'LZH', '泸州': 'LZO',
            '洛阳': 'LYA', '吕梁': 'LLV', '澜沧': 'JMJ', '龙岩': 'LCX', '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '漠河': 'OHE',
            '牡丹江': 'MDG', '马祖': 'MFK', '南昌': 'KHN', '南充': 'NAO', '南京': 'NKG', '南宁': 'NNG', '南通': 'NTG', '南阳': 'NNY',
            '宁波': 'NGB', '宁蒗': 'NLH', '攀枝花': 'PZI', '普洱': 'SYM', '齐齐哈尔': 'NDG', '黔江': 'JIQ', '且末': 'IQM', '秦皇岛': 'BPE',
            '青岛': 'TAO', '庆阳': 'IQN', '衢州': 'JUZ', '日喀则': 'RKZ', '日照': 'RIZ', '三亚': 'SYX', '厦门': 'XMN', '上海': 'SHA',
            '深圳': 'SZX', '神农架': 'HPG', '沈阳': 'SHE', '石家庄': 'SJW', '塔城': 'TCG', '台州': 'HYN', '太原': 'TYN', '扬州': 'YTY',
            '唐山': 'TVS', '腾冲': 'TCZ', '天津': 'TSN', '天水': 'THQ', '通辽': 'TGO', '铜仁': 'TEN', '吐鲁番': 'TLQ', '万州': 'WXN',
            '威海': 'WEH', '潍坊': 'WEF', '温州': 'WNZ', '文山': 'WNH', '乌海': 'WUA', '乌兰浩特': 'HLH', '乌鲁木齐': 'URC', '无锡': 'WUX',
            '梧州': 'WUZ', '武汉': 'WUH', '武夷山': 'WUS', '西安': 'SIA', '西昌': 'XIC', '西宁': 'XNN', '锡林浩特': 'XIL',
            '香格里拉': 'DIG', '襄阳': 'XFN', '兴义': 'ACX', '徐州': 'XUZ', '香港': 'HKG', '烟台': 'YNT', '延安': 'ENY',
            '延吉': 'YNJ', '盐城': 'YNZ', '伊春': 'LDS', '伊宁': 'YIN', '宜宾': 'YBP', '宜昌': 'YIH', '宜春': 'YIC', '义乌': 'YIW',
            '银川': 'INC', '永州': 'LLF',
            '榆林': 'UYN', '玉树': 'YUS', '运城': 'YCU', '湛江': 'ZHA', '张家界': 'DYG', '张家口': 'ZQZ', '张掖': 'YZY', '昭通': 'ZAT',
            '郑州': 'CGO',
            '中卫': 'ZHY', '舟山': 'HSN', '珠海': 'ZUH', '遵义(茅台)': 'WMT', '遵义(新舟)': 'ZYI'}
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.drawed = False
        self.lastShowPoint = -1
        self.lastDotPosX = 0
        self.lastDotPosY = 0
    def move_update(self,event):
        if self.drawed == False:
            return
        pointX = math.floor((event.x  - 50) / self.xGap)
        if(self.lastShowPoint != pointX):
            if(pointX >= 0 and pointX < len(self.DotsInfo)):
                posY = self.DotsInfo[pointX]
                date = self.DateInfo[pointX]
                price = self.PriceInfo[pointX]
                self.lastShowPoint = pointX
                move_x = pointX * self.xGap - self.lastDotPosX + 50 - 3
                move_y = posY - self.lastDotPosY - 3
                self.canvas.move(self.BigDot, move_x, move_y)
                self.canvas.delete('o')
                curAnchor = W
                if pointX > self.maxNum - 10:
                    curAnchor = E
                self.TextInfo = self.canvas.create_text(50 + pointX * self.xGap +10,posY - 15,text = self.getDataStr(str(date)) + " : " + str(price) + "元",tags='o',anchor = curAnchor,fill = "#778899")
                self.lastDotPosX = pointX * self.xGap + 50 - 3
                self.lastDotPosY = posY - 3
                print(str(date) + ":" + str(price))
    def set_init_window(self):              
        screen_width = self.init_window_name.winfo_screenwidth()
        screen_height = self.init_window_name.winfo_screenheight()
        window_width = 1280
        window_height = 640
        posX = int((screen_width - window_width) * .5)
        posY = int((screen_height - window_height) * .5)

        self.init_window_name.title("机票查询工具v0.2")  # 窗口名
        self.init_window_name.geometry(str(window_width) + 'x' + str(window_height) + '+' + str(posX) + '+' + str(posY))

        #上面 frame
        self.frame_top = Frame(self.init_window_name,width=1280, height=120)
        self.frame_top.pack(fill = X,padx = 50,pady = 50)
        # 标签
        self.label_city_from = Label(self.frame_top, text="出发城市:",anchor=E)
        self.label_city_from.pack(side='left')
        self.input_city_from = Entry(self.frame_top)
        self.input_city_from.pack(side='left')
        # 按钮
        curPath = os.path.dirname(__file__)
        finalPath = os.path.join(curPath, "img/btn_trans.png")
        self.init_window_name.iconbitmap = (os.path.join(curPath, "icon_new.ico"))
        
        global image
        image = PhotoImage(file=finalPath)
        btnTrans = Button(self.frame_top, text="转换", image=image, bd=0, relief=FLAT,command = self.onSwitch)
        btnTrans.pack(side = 'left', expand='yes',padx = 50)

        finalPath = os.path.join(curPath, "img/btn_search.png")
        global image2
        image2 = PhotoImage(file=finalPath)
        btnSearch = Button(self.frame_top, text="查询", image=image2,bd=0, relief=FLAT,command = self.onSearch)
        btnSearch.pack(side = 'right',padx = 10)
        labelDay = Label(self.frame_top, text="天",anchor=W)
        labelDay.pack(side = 'right',padx = 10)
        #下拉框
        self.numberChosen = ttk.Combobox(self.frame_top, width=12, textvariable=IntVar())
        self.numberChosen['values'] = (30,60,90,180) # 设置下拉列表的值
        self.numberChosen.pack(side = "right",padx = 10)
        self.numberChosen.current(2)
        
        labelCheck = Label(self.frame_top, text="查询时长:",anchor=E,width = 20)
        labelCheck.pack(side = 'right',padx = 10)

        # 文本框
        self.input_city_to = Entry(self.frame_top)  # 处理结果展示
        self.input_city_to.pack(side = 'right')
        self.label_city_to = Label(self.frame_top, text="到达城市:")
        self.label_city_to.pack(side = 'right')

        
        #读取本地缓存信息
        self.readSaveInfo()
        # frame
        self.chart_frame = Frame(self.init_window_name,height=400,borderwidth=2,relief=RIDGE)
        self.chart_frame.pack(fill = X)
        # canvas
        self.canvas = Canvas(self.chart_frame,height= 400,bg="#DCDCDC")
        self.canvas.pack(fill = X)
        self.canvas.bind("<Motion>",self.move_update)


    def readSaveInfo(self):
        #判断缓存是否存在
        curPath =  os.path.dirname(__file__)
        dirExsit = os.path.exists(curPath+"/save")
        if not dirExsit:
            os.mkdir(curPath+"/save")
            print("make dir ok")
        else:
            print("dir exist --> ")
        fileExsit = os.path.exists(curPath+"/save/cache.npy")
        if fileExsit:
            dic = np.load(curPath+"/save/cache.npy",allow_pickle = True).item()
            if dic["from"] != None:
                self.input_city_from.insert(0,str(dic["from"]))
            if dic["to"] != None:
                self.input_city_to.insert(0,dic["to"])
        else:
            print("file not exsit")
    def savePos(self,fromPos,toPos):
        curPath =  os.path.dirname(__file__)
        dic = {"from":fromPos,"to":toPos} 
        np.save(curPath + "/save/cache",dic)
        print("save ok --->")
    def getDataStr(self,oringStr):
     #   year = oringStr[:4]
        month = oringStr[4:6]
        day = oringStr[-2:]
        return str(month) + "-" + str(day)

    def requestInfo(self,fromCode,toCode):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN',
            'Cache-Control': 'max-age=0',
            # 'content-type': 'application/json',
            'Host': 'flights.ctrip.com',
            'Content-Length': '63',
            'Origin': 'https://flights.ctrip.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
        }
        data = {"flightWay": "Oneway", "dcity": fromCode, "acity": toCode, "army": False}
        response = requests.post('https://flights.ctrip.com/itinerary/api/12808/lowestPrice', data=data,
                                 headers=headers)
        price = json.loads(response.text)
        priceDic = price['data']['oneWayPrice'][0]
        priceCount = len(priceDic)
        print("cur total count --->" + str(priceCount))
        startX = 50
        startY = self.canvas.winfo_height() - 100
        totoalHeight = self.canvas.winfo_height() - 150
        self.maxNum = int(self.numberChosen.get())
        if(priceCount < self.maxNum):
            self.maxNum = priceCount
        self.xGap = (self.canvas.winfo_width() - 100) / self.maxNum
        print("cur max num --->" + str(self.maxNum) + "," + str(self.canvas.winfo_width()) +"," + str(self.xGap))
        #找出最大值和最小值
        minValue = 99999
        maxValue = 0
        index = 0
        for key in priceDic:
            curValue = priceDic[key]
            if curValue > maxValue:
                maxValue = curValue
            if(curValue < minValue):
                minValue = curValue
            index = index + 1
            if(index >= self.maxNum):
                break
        bottomValue = minValue - 30
        topValue = maxValue + 10
        if bottomValue < 0:
            bottomValue = 0
        print(minValue,maxValue,bottomValue,topValue)
        #标出最小价格和最大价格
        minY = startY - totoalHeight * ((minValue - bottomValue) / (topValue - bottomValue))
        maxY = startY - totoalHeight * ((maxValue - bottomValue) / (topValue - bottomValue))
        self.canvas.create_text(startX - 10,minY,text = str(minValue) + "元",anchor = E,fill = "#778899")
        self.canvas.create_text(startX - 10,maxY,text = str(maxValue) + "元",anchor = E,fill = "#778899")
        allPoint = []
        self.DotsInfo = []
        self.DateInfo = []
        self.PriceInfo = []
        index = 0
        for key in priceDic:
            curValue = priceDic[key]
            dox = startX + self.xGap * index
            doy = startY - totoalHeight * ((curValue - bottomValue) / (topValue - bottomValue))
            allPoint.append((dox,doy))
            self.DotsInfo.append(doy)
            self.DateInfo.append(key)
            self.PriceInfo.append(curValue)
            if index == 0 or index == self.maxNum - 1:
                self.canvas.create_text(dox,startY,text = self.getDataStr(key) ,anchor = N,fill = "#778899")
            index = index + 1
            if(index >= self.maxNum):
                break
        self.canvas.create_line(allPoint, fill = "#778899")
        self.drawed = True
    def reqPrice(self,fromCode,toCode):
        startX = 50
        startY = 100
        # 画线
        self.canvas.delete(ALL)
        #圆点
        self.BigDot = self.canvas.create_oval(0,0,6,6,fill = "#778899",width = 0)
        self.lastDotPosX = 0
        self.lastDotPosY = 0
        #每天的信息文本
        # x轴
        self.canvas.create_line(startX, self.canvas.winfo_height() - startY, self.canvas.winfo_width() - startX,self.canvas.winfo_height() - startY , fill = "#778899",width = 1.5)
        # y轴
        self.canvas.create_line(startX, self.canvas.winfo_height() - startY,startX,50 , fill = "#778899",width = 1.5)
        self.requestInfo(fromCode,toCode)

    def onSwitch(self):
        tempStr = self.input_city_from.get()
        self.input_city_from.delete(0,"end")
        self.input_city_from.insert(0,self.input_city_to.get())
        self.input_city_to.delete(0,"end")
        self.input_city_to.insert(0,tempStr)
    def onSearch(self):
        from_pos = self.input_city_from.get()
        to_pos = self.input_city_to.get()
        if(from_pos == "" or to_pos == ""):
            tkinter.messagebox.showinfo('提示', '出发地和目的地不能为空')
            return
        from_code = self.city.get(from_pos)
        to_code = self.city.get(to_pos)
        if(from_code == None and to_code == None):
            tkinter.messagebox.showinfo('提示', '未找到所填写地点的机场，请检查是否填写正确')
        elif(from_code == None):
            tkinter.messagebox.showinfo('提示','未找到出发地机场')
        elif(to_code == None):
            tkinter.messagebox.showinfo('提示','未找到目的地机场')
        elif(from_code == to_code):
            tkinter.messagebox.showinfo('提示','出发地不能与目的地相同')
        else:
            self.reqPrice(from_code,to_code)
            self.savePos(from_pos,to_pos)


def gui_start():
    mainWindow = Tk()
    ZMJ_PORTAL = MY_GUI(mainWindow)
    ZMJ_PORTAL.set_init_window()
    mainWindow.mainloop()
gui_start()
