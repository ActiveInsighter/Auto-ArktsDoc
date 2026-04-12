# 列表与网格概述
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview

许多应用存在滚动展示同类项目集合的需求，例如显示图片、视频、音乐、新闻、商品等。此类场景可以根据项目排列方式分别选择[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-grid)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-waterflow)实现，在圆形屏幕推荐使用[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist)。

## 列表

List适合单列和多列宽度相同的场景，如通讯录、音乐列表、购物清单等。

直播评论、即时聊天等应用场景需要在列表底部插入数据时，内容应自动向上滚动，以展示新插入的节点，此功能可通过配置[List从尾部开始布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#stackfromend19)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/4C0hS-nJRH2ybiCs-od-Cg/zh-cn_image_0000002569168377.png?HW-CC-KV=V1&HW-CC-Date=20260412T025258Z&HW-CC-Expire=86400&HW-CC-Sign=D654E2B4B55FAA01C2C35739EF0AB93859620775AC6FCAF6A692D69F7147AF71)

## 网格

网格布局由“行”和“列”分割的单元格组成，通过指定“项目”所在单元格实现多种布局，应用场景包括九宫格图片展示、日历、计算器等。

对于部分项目占用多行或多列的场景，可以通过在创建Grid时传入合适的[GridLayoutOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#gridlayoutoptions10对象说明)来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/eHaouC0zS5WPOuFc47foYw/zh-cn_image_0000002569128403.png?HW-CC-KV=V1&HW-CC-Date=20260412T025258Z&HW-CC-Expire=86400&HW-CC-Sign=FF3F1BFF42F11F12B3E2571D906D05F49E740A11FF4DE7577D8E4A3EE710712A)

## 瀑布流

瀑布流布局是一种多列等宽但高度不等的布局方式，适用于需要错落排列的场景，如图片和视频展示、商品推荐等。

同一个页面内有不同列数分段混合布局的场景，可以通过设置[WaterFlowSections](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#waterflowoptions对象说明)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/tXzzzNfOQyGAX-4aiM6PRA/zh-cn_image_0000002538128682.png?HW-CC-KV=V1&HW-CC-Date=20260412T025258Z&HW-CC-Expire=86400&HW-CC-Sign=B8290A30102ABB5C703F2DE90D20FA409AE60CEB75D0411BEEFEC853764F5196)

## 弧形列表

弧形列表是一种专为圆形屏幕设备设计的特殊列表，支持列表项在接近屏幕上下两端自动缩放的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/L243_kBYSki_InyVCTrkNw/zh-cn_image_0000002538288616.png?HW-CC-KV=V1&HW-CC-Date=20260412T025258Z&HW-CC-Expire=86400&HW-CC-Sign=ECA1E5548EA704FF3D59BF814EDB2D836287892EC2FBD5059479549F3F08E55D)

## 能力对比

| 业务场景 | List | Grid | WaterFlow | ArcList |
| --- | --- | --- | --- | --- |
| 滚动通用能力 | 支持 | 支持 | 支持 | 支持 |
| 项目分组 | [ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup) | [GridLayoutOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#gridlayoutoptions10对象说明) | [WaterFlowSections](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#waterflowoptions对象说明) | 不支持 |
| 指定项目吸顶 | 支持通过[sticky](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#sticky9)属性实现吸顶 | 不支持 | 不支持 | 不支持 |
| 项目拖拽排序 | 支持[拖拽排序](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting)，包括内置动画和拖动到边缘自动滚动 | 仅所有项目都占1行1列时[支持内置动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#supportanimation8)，且不支持拖动到边缘自动滚动 | 不支持 | 不支持 |
| 项目横滑 | 支持通过[swipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeaction9)属性实现横滑 | 不支持 | 不支持 | 不支持 |
| 项目间距 | 支持 | 支持 | 支持 | 支持 |
| 项目分割线 | 支持 | 不支持 | 不支持 | 不支持 |
