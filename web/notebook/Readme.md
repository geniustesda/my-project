# 简易留言板
1.在Web浏览器上显示一个包含“提交留言”表单的页面

2.可以在提交留言表单中输入名字和留言正文

3.通过提交留言表单发送的名字和留言内容会被保存

4.已保存的名字、留言、提交日期会显示在页面中

5.整个应用由一个页面构成，页面上部为提交留言表单，下部显示已提交的内容

6.提交的内容按新旧顺序由上到下排列

7.可经由网络（互联网）使用本系统

8.可同时在多台计算机上显示已提交的内容


#### NOTE：

跨站脚本攻击（Cross Site Scripting，XSSA）是一种常见的漏洞，用户能在某些以植入HTML的形式显示输入内容的应用中，故意植入一些攻击型的脚本（比如HTML标签或JavaScript 等）。

XSS 漏洞可被用在会话劫持、钓鱼等恶意行为上。

与 XSS 同样恶名昭彰的漏洞还有跨站请求伪造Cross Site Request Forgery，CSRF）。
用户通过与目标应用程序无关的外部输入表单（这些输入表单通常用于攻击）发送数据，一旦目标应用程序处理了这些数据，就会引发使用者意料之外的操作。

CSRF 漏洞可被用来触发使用者意料之外的操作（比如在线购买商品、泄露个人信息等）。