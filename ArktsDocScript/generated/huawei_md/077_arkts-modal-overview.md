# 绑定模态页面概述
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-overview

模态页面是一种大面板交互式的弹窗，和其他弹窗组件一样，通常用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作。相比于其他弹窗组件，模态页面的内容都需要开发者通过自定义组件来填充实现，可展示的视图往往也很大。默认需要用户进行交互才能够退出模态页面。ArkUI当前提供了**半模态**和**全模态**两类模态页面组件。

- **​半模态：​**开发者可以利用此模态页面实现多形态效果。支持不同宽度设备显示不同样式的半模态页面。允许用户通过侧滑，点击蒙层，点击关闭按钮，下拉关闭半模态页面。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ygKXDa2OTMWNN07TWuAeHg/zh-cn_image_0000002569128561.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025342Z&HW-CC-Expire=86400&HW-CC-Sign=33E64FB9BBED954A875686906E4831AA2ABCA09478E822A48CFEEAF6B8F615CF)
- **全模态：​**开发者可以利用此模态页面实现全屏的模态弹窗效果。默认需要侧滑才能关闭。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/FVoOOPtIRiK4kV2NCdXpvg/zh-cn_image_0000002538128840.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025342Z&HW-CC-Expire=86400&HW-CC-Sign=54B943939C274502AC61B1B74DB372B5B0BFDCD523B48345C6AF7093621C4193)

## 使用场景

| 接口 | 使用场景 |
| --- | --- |
| [bindContentCover](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-contentcover-page) | 用于自定义全屏的模态展示界面，结合转场动画和共享元素动画可实现复杂转场动画效果，如缩略图片点击后查看大图。 |
| [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sheet-page) | 用于半模态展示界面，如分享框。 |
| [openBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#openbindsheet12)/ [updateBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#updatebindsheet12)/ [closeBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#closebindsheet12) | 用于不依赖UI组件的场景，如全局拉起、更新、关闭。 |

## 规格约束

- 建议使用UIContext中的弹窗方法。其他规格约束可参考[openBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#openbindsheet12)、[updateBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#updatebindsheet12)、[closeBindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#closebindsheet12)说明。
