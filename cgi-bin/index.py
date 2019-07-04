html = """
<html>
	<head>
		<title>
			image
		</title>
	</head>
	<body>
		<img src="http://img.redocn.com/sheji/20141219/zhongguofengdaodeliyizhanbanzhijing_3744115.jpg">
	</body>
</html>
"""  # 要返回的数据 response 的body
print("content-type:text/html")  # 返回响应的头部，具体描述的要返回的内容类型，在cgi当中用print进行返回
print("\n")  # 返回头部结束
print(html)  # 返回响应的body