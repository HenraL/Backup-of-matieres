import tkinter as tk


class ColourPicker:
    """ A class in charge of displaying a window to allow the user to pick a colour """

    def __init__(self):

        self.hexcol = {
            "0": "00", "1": "01", "2": "02", "3": "03",
            "4": "04", "5": "05", "6": "06", "7": "07",
            "8": "08", "9": "09", "10": "0a", "11": "0b",
            "12": "0c", "13": "0d", "14": "0e", "15": "0f",
            "16": "10", "17": "11", "18": "12", "19": "13",
            "20": "14", "21": "15", "22": "16", "23": "17",
            "24": "18", "25": "19", "26": "1a", "27": "1b",
            "28": "1c", "29": "1d", "30": "1e", "31": "1f",
            "32": "20", "33": "21", "34": "22", "35": "23",
            "36": "24", "37": "25", "38": "26", "39": "27",
            "40": "28", "41": "29", "42": "2a", "43": "2b",
            "44": "2c", "45": "2d", "46": "2e", "47": "2f",
            "48": "30", "49": "31", "50": "32", "51": "33",
            "52": "34", "53": "35", "54": "36", "55": "37",
            "56": "38", "57": "39", "58": "3a", "59": "3b",
            "60": "3c", "61": "3d", "62": "3e", "63": "3f",
            "64": "40", "65": "41", "66": "42", "67": "43",
            "68": "44", "69": "45", "70": "46", "71": "47",
            "72": "48", "73": "0x49", "74": "4a", "75": "4b",
            "76": "4c", "77": "4d", "78": "4e", "79": "4f",
            "80": "50", "81": "51", "82": "52", "83": "53",
            "84": "54", "85": "55", "86": "56", "87": "57",
            "88": "58", "89": "59", "90": "5a", "91": "5b",
            "92": "5c", "93": "5d", "94": "5e", "95": "5f",
            "96": "60", "97": "61", "98": "62", "99": "63",
            "100": "64", "101": "65", "102": "66", "103": "67",
            "104": "68", "105": "69", "106": "6a", "107": "6b",
            "108": "6c", "109": "6d", "110": "6e", "111": "6f",
            "112": "70", "113": "71", "114": "72", "115": "73",
            "116": "74", "117": "75", "118": "76", "119": "77",
            "120": "78", "121": "79", "122": "7a", "123": "7b",
            "124": "7c", "125": "7d", "126": "7e", "127": "7f",
            "128": "80", "129": "81", "130": "82", "131": "83",
            "132": "84", "133": "85", "134": "86", "135": "87",
            "136": "88", "137": "89", "138": "8a", "139": "8b",
            "140": "8c", "141": "8d", "142": "8e", "143": "8f",
            "144": "90", "145": "91", "146": "92", "147": "93",
            "148": "94", "149": "95", "150": "96", "151": "97",
            "152": "98", "153": "99", "154": "9a", "155": "9b",
            "156": "9c", "157": "9d", "158": "9e", "159": "9f",
            "160": "a0", "161": "a1", "162": "a2", "163": "a3",
            "164": "a4", "165": "a5", "166": "a6", "167": "a7",
            "168": "a8", "169": "a9", "170": "aa", "171": "ab",
            "172": "ac", "173": "ad", "174": "ae", "175": "af",
            "176": "b0", "177": "b1", "178": "b2", "179": "b3",
            "180": "b4", "181": "b5", "182": "b6", "183": "b7",
            "184": "b8", "185": "b9", "186": "ba", "187": "bb",
            "188": "bc", "189": "bd", "190": "be", "191": "bf",
            "192": "c0", "193": "c1", "194": "c2", "195": "c3",
            "196": "c4", "197": "c5", "198": "c6", "199": "c7",
            "200": "c8", "201": "c9", "202": "ca", "203": "cb",
            "204": "cc", "205": "cd", "206": "ce", "207": "cf",
            "208": "d0", "209": "d1", "210": "d2", "211": "d3",
            "212": "d4", "213": "d5", "214": "d6", "215": "d7",
            "216": "d8", "217": "d9", "218": "da", "219": "db",
            "220": "dc", "221": "dd", "222": "de", "223": "df",
            "224": "e0", "225": "e1", "226": "e2", "227": "e3",
            "228": "e4", "229": "e5", "230": "e6", "231": "e7",
            "232": "e8", "233": "e9", "234": "ea", "235": "eb",
            "236": "ec", "237": "ed", "238": "ee", "239": "ef",
            "240": "f0", "241": "f1", "242": "f2", "243": "f3",
            "244": "f4", "245": "f5", "246": "f6", "247": "f7",
            "248": "f8", "249": "f9", "250": "fa", "251": "fb",
            "252": "fc", "253": "fd", "254": "fe", "255": "ff"
        }
        # hex cols
        self.r = 0
        self.g = 0
        self.b = 0
        self.hex_computed = {}
        # GUI cols
        self.c = tk.Label
        self.e = tk.Spinbox
        self.d = tk.Spinbox
        self.k = tk.Spinbox
        self.hex_code = tk.Entry
        # self.colour="#e2a2c2"
        # self.colour="#ffffff"
        self.colour = "#000000"

        self.hexlit = [
            {"hex(0)": "0x0"},
            {"hex(1)": "0x1"},
            {"hex(2)": "0x2"},
            {"hex(3)": "0x3"},
            {"hex(4)": "0x4"},
            {"hex(5)": "0x5"},
            {"hex(6)": "0x6"},
            {"hex(7)": "0x7"},
            {"hex(8)": "0x8"},
            {"hex(9)": "0x9"},
            {"hex(10)": "0xa"},
            {"hex(11)": "0xb"},
            {"hex(12)": "0xc"},
            {"hex(13)": "0xd"},
            {"hex(14)": "0xe"},
            {"hex(15)": "0xf"},
            {"hex(16)": "0x10"},
            {"hex(17)": "0x11"},
            {"hex(18)": "0x12"},
            {"hex(19)": "0x13"},
            {"hex(20)": "0x14"},
            {"hex(21)": "0x15"},
            {"hex(22)": "0x16"},
            {"hex(23)": "0x17"},
            {"hex(24)": "0x18"},
            {"hex(25)": "0x19"},
            {"hex(26)": "0x1a"},
            {"hex(27)": "0x1b"},
            {"hex(28)": "0x1c"},
            {"hex(29)": "0x1d"},
            {"hex(30)": "0x1e"},
            {"hex(31)": "0x1f"},
            {"hex(32)": "0x20"},
            {"hex(33)": "0x21"},
            {"hex(34)": "0x22"},
            {"hex(35)": "0x23"},
            {"hex(36)": "0x24"},
            {"hex(37)": "0x25"},
            {"hex(38)": "0x26"},
            {"hex(39)": "0x27"},
            {"hex(40)": "0x28"},
            {"hex(41)": "0x29"},
            {"hex(42)": "0x2a"},
            {"hex(43)": "0x2b"},
            {"hex(44)": "0x2c"},
            {"hex(45)": "0x2d"},
            {"hex(46)": "0x2e"},
            {"hex(47)": "0x2f"},
            {"hex(48)": "0x30"},
            {"hex(49)": "0x31"},
            {"hex(50)": "0x32"},
            {"hex(51)": "0x33"},
            {"hex(52)": "0x34"},
            {"hex(53)": "0x35"},
            {"hex(54)": "0x36"},
            {"hex(55)": "0x37"},
            {"hex(56)": "0x38"},
            {"hex(57)": "0x39"},
            {"hex(58)": "0x3a"},
            {"hex(59)": "0x3b"},
            {"hex(60)": "0x3c"},
            {"hex(61)": "0x3d"},
            {"hex(62)": "0x3e"},
            {"hex(63)": "0x3f"},
            {"hex(64)": "0x40"},
            {"hex(65)": "0x41"},
            {"hex(66)": "0x42"},
            {"hex(67)": "0x43"},
            {"hex(68)": "0x44"},
            {"hex(69)": "0x45"},
            {"hex(70)": "0x46"},
            {"hex(71)": "0x47"},
            {"hex(72)": "0x48"},
            {"hex(73)": "0x49"},
            {"hex(74)": "0x4a"},
            {"hex(75)": "0x4b"},
            {"hex(76)": "0x4c"},
            {"hex(77)": "0x4d"},
            {"hex(78)": "0x4e"},
            {"hex(79)": "0x4f"},
            {"hex(80)": "0x50"},
            {"hex(81)": "0x51"},
            {"hex(82)": "0x52"},
            {"hex(83)": "0x53"},
            {"hex(84)": "0x54"},
            {"hex(85)": "0x55"},
            {"hex(86)": "0x56"},
            {"hex(87)": "0x57"},
            {"hex(88)": "0x58"},
            {"hex(89)": "0x59"},
            {"hex(90)": "0x5a"},
            {"hex(91)": "0x5b"},
            {"hex(92)": "0x5c"},
            {"hex(93)": "0x5d"},
            {"hex(94)": "0x5e"},
            {"hex(95)": "0x5f"},
            {"hex(96)": "0x60"},
            {"hex(97)": "0x61"},
            {"hex(98)": "0x62"},
            {"hex(99)": "0x63"},
            {"hex(100)": "0x64"},
            {"hex(101)": "0x65"},
            {"hex(102)": "0x66"},
            {"hex(103)": "0x67"},
            {"hex(104)": "0x68"},
            {"hex(105)": "0x69"},
            {"hex(106)": "0x6a"},
            {"hex(107)": "0x6b"},
            {"hex(108)": "0x6c"},
            {"hex(109)": "0x6d"},
            {"hex(110)": "0x6e"},
            {"hex(111)": "0x6f"},
            {"hex(112)": "0x70"},
            {"hex(113)": "0x71"},
            {"hex(114)": "0x72"},
            {"hex(115)": "0x73"},
            {"hex(116)": "0x74"},
            {"hex(117)": "0x75"},
            {"hex(118)": "0x76"},
            {"hex(119)": "0x77"},
            {"hex(120)": "0x78"},
            {"hex(121)": "0x79"},
            {"hex(122)": "0x7a"},
            {"hex(123)": "0x7b"},
            {"hex(124)": "0x7c"},
            {"hex(125)": "0x7d"},
            {"hex(126)": "0x7e"},
            {"hex(127)": "0x7f"},
            {"hex(128)": "0x80"},
            {"hex(129)": "0x81"},
            {"hex(130)": "0x82"},
            {"hex(131)": "0x83"},
            {"hex(132)": "0x84"},
            {"hex(133)": "0x85"},
            {"hex(134)": "0x86"},
            {"hex(135)": "0x87"},
            {"hex(136)": "0x88"},
            {"hex(137)": "0x89"},
            {"hex(138)": "0x8a"},
            {"hex(139)": "0x8b"},
            {"hex(140)": "0x8c"},
            {"hex(141)": "0x8d"},
            {"hex(142)": "0x8e"},
            {"hex(143)": "0x8f"},
            {"hex(144)": "0x90"},
            {"hex(145)": "0x91"},
            {"hex(146)": "0x92"},
            {"hex(147)": "0x93"},
            {"hex(148)": "0x94"},
            {"hex(149)": "0x95"},
            {"hex(150)": "0x96"},
            {"hex(151)": "0x97"},
            {"hex(152)": "0x98"},
            {"hex(153)": "0x99"},
            {"hex(154)": "0x9a"},
            {"hex(155)": "0x9b"},
            {"hex(156)": "0x9c"},
            {"hex(157)": "0x9d"},
            {"hex(158)": "0x9e"},
            {"hex(159)": "0x9f"},
            {"hex(160)": "0xa0"},
            {"hex(161)": "0xa1"},
            {"hex(162)": "0xa2"},
            {"hex(163)": "0xa3"},
            {"hex(164)": "0xa4"},
            {"hex(165)": "0xa5"},
            {"hex(166)": "0xa6"},
            {"hex(167)": "0xa7"},
            {"hex(168)": "0xa8"},
            {"hex(169)": "0xa9"},
            {"hex(170)": "0xaa"},
            {"hex(171)": "0xab"},
            {"hex(172)": "0xac"},
            {"hex(173)": "0xad"},
            {"hex(174)": "0xae"},
            {"hex(175)": "0xaf"},
            {"hex(176)": "0xb0"},
            {"hex(177)": "0xb1"},
            {"hex(178)": "0xb2"},
            {"hex(179)": "0xb3"},
            {"hex(180)": "0xb4"},
            {"hex(181)": "0xb5"},
            {"hex(182)": "0xb6"},
            {"hex(183)": "0xb7"},
            {"hex(184)": "0xb8"},
            {"hex(185)": "0xb9"},
            {"hex(186)": "0xba"},
            {"hex(187)": "0xbb"},
            {"hex(188)": "0xbc"},
            {"hex(189)": "0xbd"},
            {"hex(190)": "0xbe"},
            {"hex(191)": "0xbf"},
            {"hex(192)": "0xc0"},
            {"hex(193)": "0xc1"},
            {"hex(194)": "0xc2"},
            {"hex(195)": "0xc3"},
            {"hex(196)": "0xc4"},
            {"hex(197)": "0xc5"},
            {"hex(198)": "0xc6"},
            {"hex(199)": "0xc7"},
            {"hex(200)": "0xc8"},
            {"hex(201)": "0xc9"},
            {"hex(202)": "0xca"},
            {"hex(203)": "0xcb"},
            {"hex(204)": "0xcc"},
            {"hex(205)": "0xcd"},
            {"hex(206)": "0xce"},
            {"hex(207)": "0xcf"},
            {"hex(208)": "0xd0"},
            {"hex(209)": "0xd1"},
            {"hex(210)": "0xd2"},
            {"hex(211)": "0xd3"},
            {"hex(212)": "0xd4"},
            {"hex(213)": "0xd5"},
            {"hex(214)": "0xd6"},
            {"hex(215)": "0xd7"},
            {"hex(216)": "0xd8"},
            {"hex(217)": "0xd9"},
            {"hex(218)": "0xda"},
            {"hex(219)": "0xdb"},
            {"hex(220)": "0xdc"},
            {"hex(221)": "0xdd"},
            {"hex(222)": "0xde"},
            {"hex(223)": "0xdf"},
            {"hex(224)": "0xe0"},
            {"hex(225)": "0xe1"},
            {"hex(226)": "0xe2"},
            {"hex(227)": "0xe3"},
            {"hex(228)": "0xe4"},
            {"hex(229)": "0xe5"},
            {"hex(230)": "0xe6"},
            {"hex(231)": "0xe7"},
            {"hex(232)": "0xe8"},
            {"hex(233)": "0xe9"},
            {"hex(234)": "0xea"},
            {"hex(235)": "0xeb"},
            {"hex(236)": "0xec"},
            {"hex(237)": "0xed"},
            {"hex(238)": "0xee"},
            {"hex(239)": "0xef"},
            {"hex(240)": "0xf0"},
            {"hex(241)": "0xf1"},
            {"hex(242)": "0xf2"},
            {"hex(243)": "0xf3"},
            {"hex(244)": "0xf4"},
            {"hex(245)": "0xf5"},
            {"hex(246)": "0xf6"},
            {"hex(247)": "0xf7"},
            {"hex(248)": "0xf8"},
            {"hex(249)": "0xf9"},
            {"hex(250)": "0xfa"},
            {"hex(251)": "0xfb"},
            {"hex(252)": "0xfc"},
            {"hex(253)": "0xfd"},
            {"hex(254)": "0xfe"},
            {"hex(255)": "0xff"}]
        self.mono_hex = [
            "0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9", "a", "b", "c", "d",
            "e", "f"
        ]

    def create_hex(self) -> None:
        """ Create the hexadecimal list of possibilities """
        rgb = []
        mn = self.mono_hex
        for i in range(256):
            rgb.append(str(i))
        self.hex_computed = {}
        c = 0
        for i in enumerate(mn):
            for b in enumerate(mn):
                self.hex_computed[f"{rgb[c]}"] = f"{i[1]}{b[1]}"
                c += 1
        # print(self.hex_computed)

    def process_hex(self):
        """ Process the hexadecimal """
        self.r = self.hex_computed[str(self.r)]
        self.g = self.hex_computed[str(self.g)]
        self.b = self.hex_computed[str(self.b)]
        # print(self.r,self.g,self.b)
        self.colour = "#"
        self.colour += f"{self.r}{self.g}{self.b}"

    def get_user_colour(self):
        """ Get the user's colour """
        self.r = self.e.get()
        self.g = self.d.get()
        self.b = self.k.get()
        self.process_hex()
        self.c.config(bg=self.colour)
        self.hex_code.delete(0, tk.END)
        self.hex_code.insert(0, f"{self.colour}")

    def window(self) -> None:
        """ The window in charge of allowing the user to pick selfs colour """
        TT = tk.Tk()
        self.c = self.c(TT, bg=self.colour)
        self.c.pack(fill=tk.X, side=tk.TOP)
        Framec = tk.Frame(TT, relief=tk.FLAT)
        Framec.pack(side=tk.TOP, fill=tk.X)
        Framel = tk.Frame(Framec, relief=tk.FLAT)
        Framel.pack(side=tk.LEFT)
        Framer = tk.Frame(Framec, relief=tk.FLAT)
        Framer.pack(side=tk.RIGHT)
        Framehex = tk.Frame(TT, relief=tk.FLAT)
        Framehex.pack(side=tk.TOP, fill=tk.X)

        r = tk.Label(Framel, text="R:")
        r.pack(fill=None, side=tk.TOP)
        v = tk.Label(Framel, text="V:")
        v.pack(fill=None, side=tk.TOP)
        b = tk.Label(Framel, text="B:")
        b.pack(fill=None, side=tk.TOP)

        self.e = self.e(
            Framer,
            from_=0,
            to=255,
            wrap=True,
            increment=1,
            command=self.get_user_colour
        )
        self.e.pack()
        self.d = self.d(
            Framer,
            from_=0,
            to=255,
            wrap=True,
            increment=1,
            command=self.get_user_colour
        )
        self.d.pack()
        self.k = self.k(
            Framer,
            from_=0,
            to=255,
            wrap=True,
            increment=1,
            command=self.get_user_colour
        )
        self.k.pack()

        entry_desc = tk.Label(Framehex, text="Hexadecimal code :")
        entry_desc.pack(side=tk.LEFT)
        self.hex_code = self.hex_code(Framehex, width=40)

        self.hex_code.pack(side=tk.RIGHT)
        # r.update
        TT.mainloop()


if __name__ == "__main__":
    CI = ColourPicker()
    CI.create_hex()
    CI.window()
