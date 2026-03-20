# ContextMenu-菜单-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-menu

在页面范围内关闭通过[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12)属性绑定的菜单。

> **说明**
> 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## ContextMenu.close(deprecated)

static close()

可以通过该方法在页面范围内关闭通过[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12)为组件绑定的菜单。

> **说明**
> 从API version 18开始废弃，建议使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getContextMenuController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getcontextmenucontroller12)获取[ContextMenuController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller)实例，再通过此实例调用替代方法[close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller#close12)。
>
> 从API version 12开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getContextMenuController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getcontextmenucontroller12)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 示例

该示例为ContextMenu.close关闭通过bindContextMenu属性绑定的菜单。

> **说明**
> 推荐通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getContextMenuController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getcontextmenucontroller12)来明确UI的执行上下文。

```typescript
@Entry
@Component
struct Index {
  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('ContextMenu1')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Column() {
        Text('Long press to show ContextMenu')
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
      .onDragStart(()=>{

        ContextMenu.close()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/OUw_hIAcQyqlZ24KgEX4eg/zh-cn_image_0000002531106254.gif?HW-CC-KV=V1&HW-CC-Date=20260320T120356Z&HW-CC-Expire=86400&HW-CC-Sign=85F3DE332D243B441085D9CD7FE26C04585A66B1CE6BE20EBE6C562EA27BCAFB)
