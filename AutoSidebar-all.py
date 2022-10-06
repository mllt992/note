import os

content = '- [首页](/首页.md)\n'
# 我不会在项目根目录下放太多的文件，所以就不读取项目根目录下的md文件了
# 读取根目录下文件夹
path_base = "./"
fileList = os.listdir(path_base)
index= '- [首页](/首页.md)\n'

def getMD(path, tabs,text):
    """
    path:路径
    """
    global content
    # 获取目录下文件和文件夹
    files = os.listdir(path_base + path)
    # print(files)
    # 遍历结果，依次处理
    for i in files:
        # 判断是不是文件夹
        # print("获取到"+path_base+path+"/"+i)
        if os.path.isdir(path_base + path + "/" + i):
            # print(i+"是文件夹")
            # 判断是不是隐藏文件夹，如果是隐藏文件夹则不添加路径
            if i[0:1:1] != "." and i != "public":
                # print(i+"符合要求")
                text += tabs + "- [" + i +"]("+path_base[1:] + path + "/"+i+"/_index"+")"+ "\n"
                content += tabs + "- [" + i + "](" + path_base[1:] + path + "/"+i+ "/_index" + ")" + "\n"
                # content += tabs + "- " + i + "\n"
                getMD(path + "/" + i, tabs + "\t",index+ "- " + i + "\n")
        else:
            # print(i+"是文件")
            # 如果不是文件夹，判断是不是隐藏文件
            if i[:1] != "." and i[:1] != "_" and i[-3::1] == ".md" and i[-6::1] != "assets":
                # print(i+"符合要求")
                # i[:-3]是截取扩展名前面的部分，也就是不包括扩展名的文件名
                text += tabs + "- [" + i[:-3] + "](" + path_base[1:] + path + "/" + i + ")" + "\n"
                content += tabs + "- [" + i[:-3] + "](" + path_base[1:] + path + "/" + i + ")" + "\n"
    with open( path_base + path + "/"+ "_sidebar.md", "w+", encoding="utf-8") as f:
        f.write(text)
    print("____________________________")
    print(text)
    print("____________________________")

for i in fileList:
    # 判断是不是文件夹
    if os.path.isdir(path_base + i):
        if i[0:1:1] != "." and i != "public":
            # content += "- " + i + "\n"
            content +=  "- [" + i + "](" + path_base[1:] + i + "/_index" + ")" + "\n"
            # 读取目录下文件
            getMD(i, "\t",index)

print(content)

with open("_sidebar.md", "w+", encoding="utf-8") as f:
    f.write(content)
