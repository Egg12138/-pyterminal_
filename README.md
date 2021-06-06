# -PyTerminalKits
一个工具合集
服务于终端

[toc]

## 定位
是一个非常简单的练手项目， 所以代码风格不一定pythonic， 但是一定多使用Py的语言特性(Python3 3.9之前)

## 长远规划

* 未来能够支持Julia接口、C接口、Rust接口等等（比如进入Ju计算模式等……还不确定）
* 能够有一个比较好的扫描器， （现在是用os.system和其他能调用终端的库， 之后可能计划牺牲性能用Py来做……具体来说是还没额外实现的命令调用系统的）
* 支持remote SSH
* 提供科研数据的处理tools， 
* (幻想)实现类似MyBase的mini SQL（需求强烈。现在就看多久能实现了）
* ADD YOUR IDEAS.......
## 近期任务

* 确定一下功能
* 把波数据的处理写掉
* 把命令行parser写掉。
* 添加RGB色盘工具（Java)

## Logs



## Tree

class DataKit

     call many other classes
     
class CommandParser
     
     自定义命令提示符样式（文本自定义已完成， 文件插件形式的add new style未完成）
     


