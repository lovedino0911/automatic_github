class TeacherLove() :
    def __init__(self, name = None, subj = None, where = None, likereason = None) :
        self.__name = name
        self.__subj = subj
        self.__where = where
        self.__likereason = likereason

    def setName(self, name) :
        self.__name = name
    def setSubj(self, subj) :
        self.__subj = subj
    def setWhere(self, where) :
        self.__where = where
    def setLikereason(self, likereason) :
        self.__likereason = likereason
    
    def getName(self, name) :
        return self.__name
    def getSubj(self, subj) :
        return self.__subj
    def getWhere(self, where) :
        return self.__where
    def getLikereason(self, likereason) :
        return self.__likereason
    
    def __str__(self) :
        return "(%g, %g, %g, %g)" % (self.__name, self.__subj, self.__where, self.__likereason)
    
science = TeacherLove("박세열", "과학", "1학년 교무실", "cuuuuuuuuuuute")
kisul = TeacherLove("김동일", "기술", "교육정보부", "cuuuuuuuuuuuuuuuuuuuuuttttttteeeeeee")
jungbo = TeacherLove("지수현", "정보", "교육정보부")
suhak = TeacherLove("이희림", "수학", "1학년 교무실")
kookuh = TeacherLove("정현주", "국어", "1학년 교무실")
hankuksa1 = TeacherLove("??", "한국사", "예체능부")
sahue1 = TeacherLove("김태수", "사회", "1학년 교무실")
sahue2 = TeacherLove("문종서", "사회", "1층교무실")
hankuksa2 = TeacherLove("??", "한국사", "??")
cheyook1 = TeacherLove("김양현", "체육", "??")
