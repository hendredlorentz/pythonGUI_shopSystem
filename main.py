import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle

# 实例化object，建立窗口window
import GetInfo
import Search_ThatItem
import addInfo
import change_Item
import delete_item
window = tk.Tk()

# 给窗口的可视化起名字
window.title('clf_homework')

# 设定窗口的大小(长 * 宽)
window.geometry('400x300')

# 搞个画布
canvas = tk.Canvas(window, width=400, height=135, bg='black')


# 进行图片渲染
image_file = tk.PhotoImage(file='pka.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='欢迎', font='楷体').pack()

# 用户信息(会与后面的函数进行数据连接）
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)
# 用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
# 定点
entry_usr_name.place(x=120, y=175)

# 用户密码
var_usr_pwd = tk.StringVar()
# 密码的show为*，要不然就看见了
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
# 定点
entry_usr_pwd.place(x=120, y=215)


# 定义用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        # 读取
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        # 的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            # 直接先写一个默认的用户
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()  # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input

    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
        #     这里就是登录成功会进行的弹窗信息
            print("hello")
            shop_main()

        # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tkinter.messagebox.showerror(message='密码输错了！')
    else:  # 如果发现用户名不存在
        # 一个弹窗
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        # 点击了注册
        if is_sign_up:
            usr_sign_up()

#搜索ID找商品
def searchNumber():
    def getInputOfSearch():
        search_Number = searchIn.get()
        # 测试拿到数据了没
        print("输入框中的商品编号:",search_Number)
        var = Search_ThatItem.getSearchInfo(search_Number)
        search_show.insert('insert','查询结果为(编号，名称，价格，品牌):')
        search_show.insert('insert','\n')
        search_show.insert('end', var)
        search_show.insert('end', '\n')
    window_search = tk.Toplevel(window)
    window_search.geometry('300x300')
    window_search.title('搜索')
    tk.Label(window_search, text='输入查询商品序号', font=('楷体', 13)).place(x=10, y=5)
    searchIn = tk.StringVar()
    search_entry = tk.Entry(window_search,show = None,textvariable=searchIn)
    search_entry.place(x=100, y=50)
    btn_search = tk.Button(window_search,text='搜索',font=('楷体',9),width=5,height=1, command=getInputOfSearch)
    btn_search.place(x=130,y=100)
    search_show = tk.Text(window_search,height=5)
    search_show.place(x=0,y=150)


#添加商品
def addItem():
    def add_in():
        new_name = item_name.get()
        new_price = item_price.get()
        new_itemInfo = item_itemInfo.get()
        flag = addInfo.addInfo(new_name,new_price,new_itemInfo)
        if(flag):
            tk.Label(window_add, text='添加成功！', font=('Arial', 12)).place(x=20, y=180)
            shop_main()
        else:
            tk.Label(window_add, text='添加失败！', font=('Arial', 12)).place(x=20, y=180)

    window_add = tk.Toplevel(window)
    window_add.geometry('300x200')
    window_add.title('添加')

    item_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_add, text='商品名称: ').place(x=10, y=10)  # 定位放置
    entry_new_name = tk.Entry(window_add, textvariable=item_name)  # 创建一个注册名的entry，变量为new_name
    entry_new_name.place(x=130, y=10)

    item_price = tk.StringVar()
    tk.Label(window_add, text='商品价格: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_add, textvariable=item_price, show=None)
    entry_usr_pwd.place(x=130, y=50)

    item_itemInfo = tk.StringVar()
    tk.Label(window_add, text='商品信息: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_add, textvariable=item_itemInfo)
    entry_usr_pwd_confirm.place(x=130, y=90)


    btn_comfirm_add = tk.Button(window_add, text='添加', command=add_in)
    btn_comfirm_add.place(x=180, y=120)

# 修改内容（以Id为标准进行修改）
def changeItem():
    def change_It():
        theId = item_number.get()
        theName = item_name.get()
        thePrice = item_price.get()
        theIntro = item_itemInfo.get()
        flag_update = change_Item.changeInfo(theId,theName,thePrice,theIntro)
        if(flag_update):
            tk.Label(window_change, text='更新成功！', font=('Arial', 12)).place(x=20, y=200)
            shop_main()
        else:
            tk.Label(window_change, text='更新失败！', font=('Arial', 12)).place(x=20, y=200)

    window_change = tk.Toplevel(window)
    window_change.geometry('300x300')
    window_change.title('修改')

    item_number = tk.StringVar()
    tk.Label(window_change,text='商品编号:').place(x=10,y=10)
    entry_new_number = tk.Entry(window_change, textvariable=item_number)
    entry_new_number.place(x=130, y=10)
    item_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_change, text='商品名称: ').place(x=10, y=50)
    entry_new_name = tk.Entry(window_change, textvariable=item_name)
    entry_new_name.place(x=130, y=50)

    item_price = tk.StringVar()
    tk.Label(window_change, text='商品价格: ').place(x=10, y=90)
    entry_usr_pwd = tk.Entry(window_change, textvariable=item_price, show=None)
    entry_usr_pwd.place(x=130, y=90)

    item_itemInfo = tk.StringVar()
    tk.Label(window_change, text='商品信息: ').place(x=10, y=130)
    entry_usr_pwd_confirm = tk.Entry(window_change, textvariable=item_itemInfo)
    entry_usr_pwd_confirm.place(x=130, y=130)

    btn_comfirm_update= tk.Button(window_change,font=('楷体', 12), text='修改', command=change_It)
    btn_comfirm_update.place(x=180, y=170)

# 删除函数（根据Id进行删除）
def delete_Item():
    def getInputOfDelete():
        delete_Number = deleteIn.get()
        # 测试拿到数据了没
        print("输入框中的商品编号:",delete_Number)
        flag_delete = delete_item.deleteInfo(delete_Number)
        if(flag_delete):
            tk.Label(window_delete, text='删除成功！', font=('楷体', 10)).place(x=20, y=160)
            shop_main()
        else:
            tk.Label(window_delete, text='删除失败！', font=('楷体', 10)).place(x=20, y=160)
    window_delete = tk.Toplevel(window)
    window_delete.geometry('300x200')
    window_delete.title('删除')
    tk.Label(window_delete, text='输入删除商品序号', font=('楷体', 13)).place(x=10, y=5)
    deleteIn = tk.StringVar()
    delete_entry = tk.Entry(window_delete,show = None,textvariable=deleteIn)
    delete_entry.place(x=100, y=50)
    btn_delete = tk.Button(window_delete,text='删除',font=('楷体',9),width=5,height=1, command=getInputOfDelete)
    btn_delete.place(x=130,y=100)


# 定义商城界面
def shop_main():
    window_libray = tk.Toplevel(window)
    window_libray.geometry('600x300')
    window_libray.title('商品后台管理界面')
    scroll = tk.Scrollbar()

    tk.Label(window_libray,text='商品列表',font=('楷体',15)).place(x=10,y=5)
    # 搜索按钮
    btn_searchInfo = tk.Button(window_libray, text='搜索',font=('楷体',14),width=5,height=1, command=searchNumber)
    # 添加按钮
    btn_addInfo = tk.Button(window_libray,text='添加',font=('楷体',14),width=5,height=1, command=addItem)
    # 修改按钮
    btn_changeInfo = tk.Button(window_libray,text='修改',font=('楷体',14),width=5,height=1, command=changeItem)
    # 删除按钮
    btn_deleteInfo = tk.Button(window_libray,text='删除',font=('楷体',14),width=5,height=1, command=delete_Item)
    btn_searchInfo.place(x=130,y=0)
    btn_addInfo.place(x=200,y=0)
    btn_changeInfo.place(x=270,y=0)
    btn_deleteInfo.place(x=340,y=0)

    tk.Label(window_libray,text='请注意：新窗口打开后请及时关闭旧窗口',font=('楷体',12)).place(x=50,y=50)

    tk.StringVar()
    t = tk.Text(window_libray,height=8)

    # 动态渲染内容
    # print("wefwefw",GetInfo.getInfo())
    var = GetInfo.getInfo()
    t.insert('insert',"数据分别为(编号，名称，价格，品牌):")
    t.insert('insert', '\n')
    for i in range(len(var)):
        t.insert('end', var[i])
        t.insert('end', "\n")
    # GetInfo.getInfo()
    t.place(x=5,y=100)


# 定义用户注册功能
def usr_sign_up():
    def sign_to():
        # 以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        # 这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')

        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')

        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)

            #     这里可以写登录成功进入的窗口

            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()

    # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 定位放置
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的entry，变量为new_name
    entry_new_name.place(x=130, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to)
    btn_comfirm_sign_up.place(x=180, y=120)

# 主函数界面
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=230, y=240)


window.mainloop()