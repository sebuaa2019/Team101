# Log 格式规范
## 生产环境
```
[YYYY-MM-DD-00:00:00] [$LEVEL] [$PATH] INFORMATION.
LEVEL = {WARNING, ERROR, INFO}
```
### 说明
生产环境日志用于开发人员进行相关软件开发时调试使用

|项|说明|
| --- | --- |
|YYYY-MM-DD-00:00:00|系统时间，格式为年-月-日-24小时制时间|
|$LEVEL 	| log信息级别，正常时反馈INFO，异常时反馈WARNING或ERROR|
|$PATH	| build文件相对于工程文件的路径|
|INFORMATION	|反馈信息，便于开发人员进行调试 |
## 测试环境
```
[YYYY-MM-DD-00:00:00] [$TESTCASE_NAME] [$LEVEL] [$PATH] INFORMATION.
LEVEL = {WARNING, ERROR, INFO}
```
### 说明
测试环境日志用于测试人员进行相关测试时使用，并将发现的问题反馈给开发人员

|项|说明|
| --- | --- |
|YYYY-MM-DD-00:00:00|系统时间，格式为年-月-日-24小时制时间|
|$TESTCASE_NAME	|测试样例名称|
|$LEVEL 	| log信息级别，正常时反馈INFO，异常时反馈WARNING或ERROR|
|$PATH	| test文件相对于工程文件的路径|
|INFORMATION	|反馈信息，便于测试人员发现问题并上报开发者 |
## 运行环境
```
[YYYY-MM-DD-00:00:00] [$LEVEL] [DEVICE_ID] [$STATE] [$EVENT] INFORMATION.
LEVEL = {WARNING, ERROR, INFO}
STATE = $LOCATION-$BETTARY_STATE-$MILEAGE
LOCATION=($PLAT_ROW, $PLANT_COLUMN)
BETTARY_INFORMATION=(INT)
MILEAGE=(FLOAT)
EVENT={MOVING, $WORKING, SLEEP, WAIT, HANG_UP}
WORKING={WEED, IRRIGATE}
```
### 说明
运行环境日志用于用户使用时记录AIC系统的运行状态，便于反馈使用时发现的问题

|项|说明|
| --- | --- |
|YYYY-MM-DD-00:00:00|系统时间，格式为年-月-日-24小时制时间|
|$LEVEL 	| log信息级别，正常时反馈INFO，异常时反馈WARNING或ERROR|
|DEVICE_ID|	小车ID|
|$STATE |小车状态，包含小车位置、电池状态和总里程，供AIC系统使用者查看系统中小车的状态|
|$EVENT|	小车当前事件，包括移动、工作（执行特定任务）、睡眠、待命（等待任务分配）、挂起（小车发生例外情况）|
|INFORMATION	|反馈信息，便于测试人员发现问题并上报开发者 |
# 日志系统测试说明
日志系统依赖于python中成熟、可靠的库logging，经过人工干预长时间输出多种不同格式的信息，可以确信日志系统的可靠性。
