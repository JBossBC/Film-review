# movie rate system


## 技术栈

语言:python3(忘了是3.9还是3.11)

前端:vue、bootstrap、echarts、jquery、axios

+ vue:使用他的MVVC(双向绑定的响应式数据)
+ bootstrap:使用他的css样式，主要用了模态框、表格、按钮、表单的样式
+ echarts用来制作响应式图表
+ jquery:用来定位dom元素(这里没使用原生的document,涉及到bootstrap的模态框绑定了jquery)
+ axios:向后端请求数据

后端:django+spark

+ django:第一次使用python的web框架，对他的一些特性还有设计理念不太能够理解，所以代码写得很差，完全屎山
+ spark:不太建议使用python来构建spark的客户端,在开发过程中，使用spark streaming的时候我遇到了不能解决的问题，貌似是python版本与spark不能兼容所致，具体的解决方案我也没去看源码，毕竟不会太仔细研究spark。最好使用scala，官方原生的语言去开发spark，也可以用java，最后再选择python。



本实验开发注重效率，没有注重代码质量和工程问题。因为之前遇到的spark streaming的DSStream不能使用transformation的转换因子的问题(上述提到的python和spark版本的问题，一直报错说什么元组的索引超出范围)，所以这边实时数据处理用的随机数假装，请各位谨慎采用。
