# Z序控制
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order

组件的Z序，设置同一容器中兄弟组件的堆叠顺序。

> **说明**
> 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## zIndex

zIndex(value: number): T

设置组件的堆叠顺序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。当不涉及新增或减少兄弟节点，动态改变zIndex时会在zIndex改变前层级顺序的基础上进行稳定排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

### 示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

```typescript
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Stack() {

        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)

        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)

        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

Stack容器内子组件不设置zIndex的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/xTZynn6vSm2gKDeCShWNKA/zh-cn_image_0000002569129303.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=309E55D44AD02D98D22EFE391243C74B54515EC0DF5F159BEC9432B9895DCF81)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Ee-ezC1YQNmYcpQyZL-TYQ/zh-cn_image_0000002538129582.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=5A5A51D7C5938AB903600B8A45466CC7E6DCA367AE724D8A72881629BE447AD2)

### 示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

```typescript
@Entry
@Component
struct ZIndexExample {
  @State zIndex_: number = 0

  build() {
    Column() {

      Button("change Text2 zIndex")
        .onClick(() => {
          this.zIndex_ = (this.zIndex_ + 1) % 3;
        })
      Stack() {

        Text('1, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)

        Text('2, default zIndex(0), now zIndex:' + this.zIndex_)
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(this.zIndex_)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

不点击Button修改zIndex值的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/SGUH3By9T_2dOro35tlXUA/zh-cn_image_0000002538289516.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=A3FFCE27A9EAB9DCD19E398483F3F243F05A5F9A00EB41497C5C864E60F7A0A6)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/YdGRfF7TTt2yh1byK5RQew/zh-cn_image_0000002569169279.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=AF8AEDDA6691743A4BEADB80893D5FF7E9F1BABF7581E77AA0712667C788204E)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/uq0C4u2wTUSc3cDud50U0w/zh-cn_image_0000002569129305.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=BDC26AC252FFAB6F720AACF05912F09BF38E29DA6E27FDD6B16BB877314792AB)

### 示例3（设置不同容器内组件的zIndex属性）

该示例在不同容器内设置zIndex属性。其中，Text1、Text2和Text3在不同的Stack容器内。虽然Text3的zIndex值最小，但Text1、Text2仍无法按照预期显示在Text3的上方。

```typescript
@Entry
@Component
struct ZIndexExample {
  build() {
    Stack() {
      Stack() {

        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)

        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
      }.width('100%').height(200)

      Stack() {

        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ok-_SC7dRliIA6Y1pY8jcA/zh-cn_image_0000002538129584.png?HW-CC-KV=V1&HW-CC-Date=20260411T023509Z&HW-CC-Expire=86400&HW-CC-Sign=403A93463119D61FA20904E3BBBFAD06B802BAA5AB59912033FF408804439D40)
