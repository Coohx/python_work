*创建新主题逻辑*
===
<br>

- 主题页面topics.html 点击某个主题时,会捕获主题ID,传递到后面所有的视图函数中

- new_topic.html 是添加新主题显示的页面,因为首次http请求方法是GET

- 当用户点击提交新主题是,http请求方法是POST,用户被重定向到topics.html页面

*创建新条目逻辑*
===
<br>

- 在单个主题页面下点击`add new entry`会跳转到new_entry.html页面,过程中会捕获当前主题ID

- 后面的一系列视图函数会接收这个ID

