def imageuri(content):
    end =0
    image =[]
    extension = [".jpg",".png",".gif",".jpeg","imgur.com"]
    while len(content)!= 0 and end != -1:
        begin = content.find("http://",end)
        if begin == -1:
                return image
        else:
            end = content.find(" ",begin+1)
            if end != -1 :
                cont = content[begin:end].strip("\n")
                for ext in extension:
                    if ext in cont: 
                        image.append(cont)
                        break                       
            else: 
                end = content.find("\n",begin+1)
                if end != -1:
                    cont = content[begin:end]
                    for ext in extension:
                        if ext in cont: 
                            image.append(cont)
                            break        
                else:
                    cont = content[begin:len(content)]
                    for ext in extension:
                        if ext in cont: 
                            image.append(cont)
                            return image            
 
    return image
                
                
                                      
                
def test():
    assert imageuri("早上起來莫名其妙的覺得指甲太長於是就拿了指甲剪來用\n http://i.imgur.com/C3HJb3X.jpeg\n 原來是剪指甲剪啊 我還以為我在剪指甲\n 令人肚爛的是指甲還沒斷") == ["http://i.imgur.com/C3HJb3X.jpeg"]
    assert imageuri("我老爸在知道有南天門之後\n 非常不甘心的做了下面這個\n http://i.imgur.com/e0SfoIi.jpg\n http://i.imgur.com/N5ya.gif\n http://i.imgur.com/m6stoQY.jpg\n 這個作品的名字叫做五折…\n 因為老爸喜歡把全聯的五折貼紙貼在上面\n 這個作品最大的特色就是可以同時擺放兩支手機\n 以上分享我爸媽無聊的作品…\n 傷眼抱歉") ==["http://i.imgur.com/e0SfoIi.jpg","http://i.imgur.com/N5ya.gif","http://i.imgur.com/m6stoQY.jpg"]
    assert imageuri("於是就有了以下對話\n http://i.imgur.com/C3HJb3X.jpg\n http://imgur.com/l3q7JBt\n 因為我爸跟我媽還有小阿姨一些日本通去 , 且小阿姨是在日商工作\n 我想說她一定知道這個東西 , 也就沒特別說明\n http://c3H3b3X.jpeg") == ["http://i.imgur.com/C3HJb3X.jpg","http://imgur.com/l3q7JBt","http://c3H3b3X.jpeg"]
    
    print (imageuri("早上起來莫名其妙的覺得指甲太長於是就拿了指甲剪來用\n http://i.imgur.com/C3HJb3X.jpeg\n 原來是剪指甲剪啊 我還以為我在剪指甲\n 令人肚爛的是指甲還沒斷"))
    print (imageuri("我老爸在知道有南天門之後\n 非常不甘心的做了下面這個\n http://i.imgur.com/e0SfoIi.jpg\n http://i.imgur.com/N5ya.gif\n http://i.imgur.com/m6stoQY.jpg\n 這個作品的名字叫做五折…\n 因為老爸喜歡把全聯的五折貼紙貼在上面\n 這個作品最大的特色就是可以同時擺放兩支手機\n 以上分享我爸媽無聊的作品…\n 傷眼抱歉")) 
    print (imageuri("於是就有了以下對話\n http://i.imgur.com/C3HJb3X.jpg\n http://imgur.com/l3q7JBt\n 因為我爸跟我媽還有小阿姨一些日本通去 ,且小阿姨是在日商工作\n 我想說她一定知道這個東西 , 也就沒特別說明\n http://c3H3b3X.jpeg"))
    print ("Test finish!")

#test()
