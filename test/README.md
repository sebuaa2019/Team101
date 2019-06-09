# 测试说明

## 需求设计实现追踪图

![需求设计实现追踪概览图](https://github.com/sebuaa2019/Team101/raw/master/media/TrackTopView.png)

## 业务需求ID索引
| Business_Requirement_ID | 业务需求名称 |
| --- | --- |
| BR1 | 植株长势监控 |
| BR2 | 植株灌溉调控 |
| BR3 | 植株健康评定 |
| BR4 | 农田综合分析控制 |
| BR5 | 用户交互 |

##  业务功能ID索引
| Business_Function_ID | 业务功能名称 |
| --- | --- |
| BF1 | 环境监测 |
| BF2 | 植株信息获取 |
| BF3 | 裁剪植株 |
| BF4 | 灌溉植株 |
| BF5 | 小车巡逻 |
| BF6 | 农田信息分析 |
| BF7 | 外部管理界面 |

## 子系统ID索引
| Subsystem_ID | 子系统名称 |
| --- | --- |
| SS_ID1 | 综合视觉分析 |
| SS_ID2 | 综合控制系统 |
| SS_ID3 | 边缘控制平台 |
| SS_ID4 | 云服务平台 |

## 子系统功能ID索引
| Subsystem_Function_ID| 功能所属子系统 | 子系统功能名称 |
| --- | --- | --- |
| SF_SS_ID1_1 | 综合视觉分析 |  |
| SF_SS_ID2_1 | 综合控制系统 | 小车前进指定路程 |
| SF_SS_ID2_2 | 综合控制系统 | 小车后退指定路程 |
| SF_SS_ID2_3 | 综合控制系统 | 小车前进指定时间 |
| SF_SS_ID2_4 | 综合控制系统 | 小车后退指定时间 |
| SF_SS_ID2_5 | 综合控制系统 | 小车左转指定角度 |
| SF_SS_ID2_6 | 综合控制系统 | 小车右转指定角度 |
| SF_SS_ID2_7 | 综合控制系统 | 小车左转指定时间 |
| SF_SS_ID2_8 | 综合控制系统 | 小车右转指定时间 |
| SF_SS_ID2_9 | 综合控制系统 | 机械臂下臂移动到指定位置 |
| SF_SS_ID2_10 | 综合控制系统 | 机械臂上臂移动到指定位置 |
| SF_SS_ID2_11 | 综合控制系统 | 机械臂钳收缩 |
| SF_SS_ID2_12 | 综合控制系统 | 机械臂钳舒张 |
| SF_SS_ID3_1 | 边缘控制平台 | 向云服务中心发送消息 |
| SF_SS_ID3_2 | 边缘控制平台 | 从云服务中心接受指令 |
| SF_SS_ID3_3 | 边缘控制平台 | 向终端发送指令 |
| SF_SS_ID3_4 | 边缘控制平台 | 从终端接受消息 |
| SF_SS_ID3_5 | 边缘控制平台 | 完成云服务中心指令到发送给终端指令的转化 |
| SF_SS_ID3_6 | 边缘控制平台 | 完成终端消息到云服务中心消息的转化 |
| SF_SS_ID4_1 | 云服务平台 |  |

## 业务功能需求与业务需求回溯关系
| Business_Requirement_ID | Business_Function_IDs |
| --- | --- |
| BF1  | BR2, BR3 |
| BF2 | BR1, BR3 |
| BF3 | BR1, BR3, BR5 |
| BF4 | BR2, BR5 |
| BF5 | BR4, BR5 |
| BF6 | BR4, BR5 |
| BF7 | BR5 |

## 业务功能需求与业务需求回溯关系
| Business_Function_ID | Business_Requirement_IDs |
| --- | --- |
| BF1  | BR2, BR3 |
| BF2 | BR1, BR3 |
| BF3 | BR1, BR3, BR5 |
| BF4 | BR2, BR5 |
| BF5 | BR4, BR5 |
| BF6 | BR4, BR5 |
| BF7 | BR5 |

## 子系统设计与业务功能需求回溯关系
| Subsystem_ID | Business_Function_IDs |
| --- | --- |
| SS_ID1 | BF1, BF2, BF3, BF4, BF5 |
| SS_ID2 | BF1, BF3, BF4, BF5 |
| SS_ID3 | BF1,BF2,BF3,BF4,BF5,BF6 |
| SS_ID4 | BF1, BF6, BF7 |

## 子系统功能与业务功能需求回溯关系
| Subsystem_Function_ID | Business_Function_IDs |
| --- | --- |
| SF_SS_ID2_1 | BF1, BF2, BF5 |
| SF_SS_ID2_2 | BF1, BF2, BF5 |
| SF_SS_ID2_3 | BF1, BF5 |
| SF_SS_ID2_4 | BF1, BF5 |
| SF_SS_ID2_5 | BF1, BF2, BF5 |
| SF_SS_ID2_6 | BF1, BF2, BF5 |
| SF_SS_ID2_7 | BF1, BF5 |
| SF_SS_ID2_8 | BF1, BF5 |
| SF_SS_ID2_9 | BF3, BF4 |
| SF_SS_ID2_10 | BF3, BF4 |
| SF_SS_ID2_11 | BF3 |
| SF_SS_ID2_12 | BF3 |
| SF_SS_ID3_1 | BF6 |
| SF_SS_ID3_2 | BF1,BF2,BF3,BF4,BF5 |
| SF_SS_ID3_3 | BF1,BF2,BF3,BF4,BF5 |
| SF_SS_ID3_4 | BF6 |
| SF_SS_ID3_5 | BF1,BF2,BF3,BF4,BF5 |
| SF_SS_ID3_6 | BF1,BF2,BF3,BF4,BF5 |
| SF_SS_ID4_1 |  |

## 子系统单元测试追踪关系
| Subsystem_ID | 模块名称 | 路径 |
