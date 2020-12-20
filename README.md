### 商品管理系统(Tkinter实现)

##### 功能

>* 登录
>* 注册
>* 数据库操作
>  * 显示数据库信息
>  * 删除信息
>  * 增加信息
>  * 查询信息



*****

### 实现方式

1. 登录和注册使用python的pickle，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，以此来进行文件读写，进行用户登录注册功能

2. 数据库操作，在每个python文件中(除了main文件外)，都会存在

   ```python
   import pymysql as pymysql
   conn = pymysql.Connect("localhost", "root", "cuiwenxuan", "shopsystem", charset="utf8")
       cur = conn.cursor();
   ```

   * 这样的一段代码，首先引入mysql包。

   * 然后需要修改的是conn里面的内容，localhost应该是不需要改变的，root为自己本机的MySQL用户名，而后跟的"cuiwenxuan"换为自己电脑中的MySQL密码，最后的"shopsystem"为自己的MySQL中使用Navicat自己创建的一个数据库名称。

   * 最后，需要使用游标对数据库进行相应的操作。

3. 增删改查

   * 已将其进行了封装，大部分为数据库的语法封装，在main.py中进行导入，而后直接进行操作即可

4. 图形化界面

   * 使用Tkinter组件，其主要使用button（按钮）,Text（多行文本输入框[反映内容]）,Label（文字标签）,Entry（输入框）,Toplevel（作为界面）等
   * 在各个窗口内部有相应的方法，会需要自己根据图形化界面进行手动代码调节，使用.place()方法，.title()更换标题等。
   * 各个组件有对应的属性，such as: x与y调节位置，font调节字体，bg调节背景颜色等。



