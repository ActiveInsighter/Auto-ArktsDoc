# 列表与网格概述
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview

许多应用存在滚动展示同类项目集合的需求，例如显示图片、视频、音乐、新闻、商品等。此类场景可以根据项目排列方式分别选择[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-grid)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-waterflow)实现，在圆形屏幕推荐使用[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist)。

## 列表

List适合单列和多列宽度相同的场景，如通讯录、音乐列表、购物清单等。

直播评论、即时聊天等应用场景需要在列表底部插入数据时，内容应自动向上滚动，以展示新插入的节点，此功能可通过配置[List从尾部开始布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#stackfromend19)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/D57aOML5T5m6N92FNbJ3SQ/zh-cn_image_0000002565210155.png?HW-CC-KV=V1&HW-CC-Date=20260402T023641Z&HW-CC-Expire=86400&HW-CC-Sign=CCB6E5842B68FE810326D84D0B4CAAF35E3751ACD93F34723DF99730E62A8A99)

## 网格

网格布局由“行”和“列”分割的单元格组成，通过指定“项目”所在单元格实现多种布局，应用场景包括九宫格图片展示、日历、计算器等。

对于部分项目占用多行或多列的场景，可以通过在创建Grid时传入合适的[GridLayoutOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#gridlayoutoptions10对象说明)来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/WnfcjJZ0Rgmn_2Ct45PybA/zh-cn_image_0000002534250332.png?HW-CC-KV=V1&HW-CC-Date=20260402T023641Z&HW-CC-Expire=86400&HW-CC-Sign=AD840215D00C1D38ED527DDE441E2FDA2688C9B03938C88344F8BAFC826D648C)

## 瀑布流

瀑布流布局是一种多列等宽但高度不等的布局方式，适用于需要错落排列的场景，如图片和视频展示、商品推荐等。

同一个页面内有不同列数分段混合布局的场景，可以通过设置[WaterFlowSections](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#waterflowoptions对象说明)实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/q6TGu4vGT2qo2DK4TGndcA/zh-cn_image_0000002534410278.png?HW-CC-KV=V1&HW-CC-Date=20260402T023641Z&HW-CC-Expire=86400&HW-CC-Sign=DAD5A1BE94E59E6BBAFC9821F4DAF7DD31A8CA5E0C7350A65A90A0EC026BB37F)

## 弧形列表

弧形列表是一种专为圆形屏幕设备设计的特殊列表，支持列表项在接近屏幕上下两端自动缩放的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/lzPUQZePSo6EJL7beLqxpg/zh-cn_image_0000002565290177.png?HW-CC-KV=V1&HW-CC-Date=20260402T023641Z&HW-CC-Expire=86400&HW-CC-Sign=71B9FB1B2F2B57412227C629DEEFA9BFF83F618FAFCCCF66340027CE1DEA604E)

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
