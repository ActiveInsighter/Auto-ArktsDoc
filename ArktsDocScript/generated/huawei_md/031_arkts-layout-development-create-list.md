# 创建列表 (List)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list

## 概述

列表是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。它适合用于呈现同类数据类型或数据类型集，例如图片和文本。在列表中显示数据集合是许多应用程序中的常见要求（如通讯录、音乐列表、购物清单等）。

使用列表可以轻松高效地显示结构化、可滚动的信息。通过在[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件中按垂直或者水平方向线性排列子组件[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)或[ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)，为列表中的行或列提供单个视图，或使用[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)迭代一组行或列，或混合任意数量的单个视图和ForEach结构，构建一个列表。List组件支持使用[条件渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、循环渲染、[懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)等[渲染控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-overview)方式生成子组件。

在圆形屏幕设备上，推荐使用[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件，使用方式可参考[创建弧形列表 (ArcList)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist)。

## 布局与约束

列表作为一种容器，会自动按其滚动方向排列子组件，向列表中添加组件或从列表中移除组件会重新排列子组件。

如下图所示，在垂直列表中，List按垂直方向自动排列ListItemGroup或ListItem。

ListItemGroup用于列表数据的分组展示，其子组件也是ListItem。ListItem表示单个列表项，可以包含单个子组件。

**图1** List、ListItemGroup和ListItem组件关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2LcVXgy-RSSx_-y2UvP7cw/zh-cn_image_0000002565210157.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=A07EEA26C65319C2E05D1FC088B7C251A4844F017A0960C78BD496EED6CEC419)

> **说明**
> List的子组件必须是ListItemGroup或ListItem，ListItem和ListItemGroup必须配合List来使用。

### 布局

List除了提供垂直和水平布局能力、超出屏幕时可以滚动的自适应延伸能力之外，还提供了自适应交叉轴方向上排列个数的布局能力。

利用垂直布局能力可以构建单列或者多列垂直滚动列表，如下图所示。

**图2** 垂直滚动列表（左：单列；右：多列）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/TavBPf2rSTabxyc2-2GVlw/zh-cn_image_0000002565210155.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=836CE71AF78D7B637C9432024EF5D434E01EF2E487611CFB5B071E53F50EEC65)

利用水平布局能力可以构建单行或多行水平滚动列表，如下图所示。

**图3** 水平滚动列表（左：单行；右：多行）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/1ZAsdE6qSCG2Vo20E57ezg/zh-cn_image_0000002534250334.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=B6218694C47859EE5E873B227EACE561C564869E61A06E823689F2AC6F0D79AD)

Grid和WaterFlow也可以实现单列、多列布局，如果布局每列等宽，且不需要跨行跨列布局，相比Grid和WaterFlow，则更推荐使用List。

### 约束

列表的主轴方向是指子组件列的排列方向，也是列表的滚动方向。垂直于主轴的轴称为交叉轴，其方向与主轴方向相互垂直。

如下图所示，垂直列表的主轴是垂直方向，交叉轴是水平方向；水平列表的主轴是水平方向，交叉轴是垂直方向。

**图4** 列表的主轴与交叉轴

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/26XAJjH-RPeafJgI6uyj8g/zh-cn_image_0000002534410280.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=FFC53B85FD1E7815757F6D4C20AF1AB80567403BE13BE641C3CD9DC9FF94FB36)

如果List组件主轴或交叉轴方向设置了尺寸，则其对应方向上的尺寸为设置值。

如果List组件主轴方向没有设置尺寸，当List子组件主轴方向总尺寸小于List的父组件尺寸时，List主轴方向尺寸自动适应子组件的总尺寸。

如下图所示，一个垂直列表B没有设置高度时，其父组件A高度为200vp，若其所有子组件C的高度总和为150vp，则此时列表B的高度为150vp。

**图5** 列表主轴高度约束示例1（**A**: List的父组件; **B**: List组件; **C**: List的所有子组件）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/GzwgxlReTmO3tdqgCfOX6g/zh-cn_image_0000002565290179.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=376696F512B50BA05A2B1F93F754F1EDDDEFC8CB3AE82000BCCA034D31C8A286)

如果子组件主轴方向总尺寸超过List父组件尺寸时，List主轴方向尺寸适应List的父组件尺寸。

如下图所示，同样是没有设置高度的垂直列表B，其父组件A高度为200vp，若其所有子组件C的高度总和为300vp，则此时列表B的高度为200vp。

**图6** 列表主轴高度约束示例2（**A**: List的父组件; **B**: List组件; **C**: List的所有子组件）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Nn1nUE94S2-pCgEN0-Vb8g/zh-cn_image_0000002565210159.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=1148E3240F2641B2ABCE5A2494B13977382964059F658575B6FC5CC826B384B5)

List组件交叉轴方向在没有设置尺寸时，其尺寸默认自适应父组件尺寸。

## 开发布局

### 设置主轴方向

List组件主轴默认是垂直方向，即默认情况下不需要手动设置List方向，就可以构建一个垂直滚动列表。

若是水平滚动列表场景，将List的[listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)属性设置为Axis.Horizontal即可实现。listDirection默认为Axis.Vertical，即主轴默认是垂直方向。

```typescript
List(

) {

}
.listDirection(Axis.Horizontal)
```

### 设置交叉轴布局

List组件的交叉轴布局可以通过[lanes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#lanes9)和[alignListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#alignlistitem9)属性进行设置，lanes属性用于确定交叉轴排列的列表项数量，alignListItem用于设置子组件在交叉轴方向的对齐方式。

List组件的lanes属性通常用于在不同尺寸的设备自适应构建不同行数或列数的列表，即一次开发、多端部署的场景。lanes属性的取值类型是"number | [LengthConstrain](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#lengthconstrain)"，即整数或者LengthConstrain类型。以垂直列表为例，如果将lanes属性设为2，表示构建的是一个两列的垂直列表，如图2中右图所示。lanes的默认值为1，即默认情况下，垂直列表的列数是1。

```typescript
List(

) {

}
.lanes(2)
```

当其取值为LengthConstrain类型时，表示会根据LengthConstrain与List组件的尺寸自适应决定行或列数。

```typescript
@Entry
@Component
export struct ListLayout {
  @State egLanes: LengthConstrain = { minLength: 200, maxLength: 300 };
  build() {

          List(

          ) {

          }
          .lanes(this.egLanes)

  }
}
```

例如，假设在垂直列表中设置了lanes的值为{ minLength: 200, maxLength: 300 }。此时：

- 当List组件宽度为300vp时，由于minLength为200vp，此时列表为一列。
- 当List组件宽度变化至400vp时，符合两倍的minLength，则此时列表自适应为两列。

同样以垂直列表为例，当alignListItem属性设置为ListItemAlign.Center表示列表项在水平方向上居中对齐。alignListItem的默认值是ListItemAlign.Start，即列表项在列表交叉轴方向上默认按首部对齐。

```typescript
List(

) {

}

.alignListItem(ListItemAlign.Center)
```

## ListItem生命周期

### 使用ForEach创建ListItem

List组件创建时，所有ListItem将会被创建。显示区域内的ListItem在首帧进行布局，预加载范围内的ListItem在空闲时完成布局。预加载范围之外的ListItem仅创建ListItem自身，ListItem其内部的子组件不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem将会创建其内部的子组件并完成布局，而滑出预加载及显示区域的ListItem将不会被销毁。

**图7** ForEach创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/1E-PH8jCSveDTZowLFpCDQ/zh-cn_image_0000002534250336.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=E1DFCEC3026C76CB34B096A2543B771AD195B0C2A23551F732B427809568CDB9)

### 使用LazyForEach创建ListItem

List组件创建时，显示区域中的ListItem会被创建与布局。预加载范围内的ListItem在空闲时创建与布局，但是不会被挂载到组件树上。预加载范围外的ListItem则不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem将被创建与布局，创建ListItem过程中，若ListItem内部包含@Reusable标记的自定义组件，则会优先从缓存池中复用。滑出预加载及显示区域的ListItem将被销毁，其内部若含@Reusable标记的自定义组件，则会被回收并加入缓存池。

**图8** LazyForEach创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/AWvgFdt-T5-qJEn0ceWOPg/zh-cn_image_0000002534410282.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=F16044657E1E2B6934DDC0754CBD1BCD69831B81AF56BF7EE963C1D5F37C2D1A)

### 使用Repeat创建ListItem

**使用virtualScroll**

List组件创建时，使用设置了[virtualScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat#virtualscroll)的Repeat生成ListItem，此时显示区域内的ListItem将被创建和布局。预加载范围内的ListItem在渲染线程空闲时创建和布局，并且挂载至组件树上。预加载范围外的ListItem则不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem，将从缓存池中获取ListItem并复用及布局，若缓存池中无ListItem，则会新创建并布局。滑出预加载及显示区域的ListItem将被回收至缓存池。

**图9** Repeat使用virtualScroll创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/3Fma7puNQWKL22eDgmH_Ng/zh-cn_image_0000002565290181.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=F5572CAA52ECFE8C8BAAAE9D09985EAD2E5837BD4BD4FD530040F8D0CC6FB4D9)

**不使用virtualScroll**

List组件创建时，所有ListItem均被创建。显示区域内的ListItem在首帧完成布局，预加载范围内的ListItem在空闲时完成布局。预加载范围外的ListItem不会进行布局。

当List组件滑动时，进入预加载及显示区域的ListItem将进行布局。滑出预加载及显示区域的ListItem不会销毁。

**图10** Repeat不使用virtualScroll创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/feaS9KMJRJe2T2pknZBpqQ/zh-cn_image_0000002565210161.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=1419D7A079D4D9AAA1418EE613DA2EB8EDFBC325AE17C16EF41CF2B659E15757)

## 在列表中显示数据

列表视图垂直或水平显示项目集合，在行或列超出屏幕时提供滚动功能，使其适合显示大型数据集合。在最简单的列表形式中，List静态地创建其列表项ListItem的内容。

**图11** 城市列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/e8-xK1gWRfmVy7nEpGYOsg/zh-cn_image_0000002534250338.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=E94732675228F3B61CD5EC812D41D47D340614E3AE5662C625E1C725B4428435)

```typescript
@Entry
@Component
export struct DataInList {
  build() {

          List() {
            ListItem() {

              Text($r('app.string.city_beijing'))
                .fontSize(24)
            }

            ListItem() {

              Text($r('app.string.city_hangzhou'))
                .fontSize(24)
            }

            ListItem() {

              Text($r('app.string.city_shanghai'))
                .fontSize(24)
            }
          }
          .backgroundColor('#FFF1F3F5')
          .alignListItem(ListItemAlign.Center)

  }
}
```

由于在ListItem中只能有一个根节点组件，不支持以平铺形式使用多个组件。因此，若列表项是由多个组件元素组成的，则需要将这多个元素组合到一个容器组件内或组成一个自定义组件。

**图12** 联系人列表项示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/p3MM2rG6RLOODKjoAbdF8g/zh-cn_image_0000002534410284.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=F290DCBAD6B8CF50E3C8ABE19D9B9403FF70C16788325850C698950AAD40508F)

如上图所示，联系人列表的列表项中，每个联系人都有头像和名称。此时，需要将Image和Text封装到一个Row容器内。

```typescript
List() {
  ListItem() {
    Row() {

      Image($r('app.media.iconE'))
        .width(40)
        .height(40)
        .margin(10)

      Text($r('app.string.peopleOne'))
        .fontSize(20)
    }
  }

  ListItem() {
    Row() {

      Image($r('app.media.iconF'))
        .width(40)
        .height(40)
        .margin(10)

      Text($r('app.string.peopleTwo'))
        .fontSize(20)
    }
  }
}
```

## 迭代列表内容

通常，应用通过数据集合动态地创建列表。使用[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)可从数据源中迭代获取数据，并在每次迭代过程中创建相应的组件，降低代码复杂度。

ArkTS通过[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)提供了组件的循环渲染能力。以简单形式的联系人列表为例，将联系人名称和头像数据以Contact类结构存储到contacts数组，使用ForEach中嵌套ListItem的形式来代替多个平铺的、内容相似的ListItem，从而减少重复代码。

```typescript
import { util } from '@kit.ArkTS';

class Contact {
  public key: string = util.generateRandomUUID(true);
  public name: ResourceStr;
  public icon: Resource;

  constructor(name: ResourceStr, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
export struct ListIteration {
  private contacts: Array<Contact> = [

    new Contact($r('app.string.peopleOne'), $r('app.media.iconA')),

    new Contact($r('app.string.peopleTwo'), $r('app.media.iconB'))
  ];

  build() {

          List() {
            ForEach(this.contacts, (item: Contact) => {
              ListItem() {
                Row() {
                  Image(item.icon)
                    .width(40)
                    .height(40)
                    .margin(10)
                  Text(item.name).fontSize(20)
                }
                .width('100%')
                .justifyContent(FlexAlign.Start)
              }
            }, (item: Contact) => JSON.stringify(item))
          }
          .width('100%')

  }
}
```

在List组件中，ForEach除了可以用来循环渲染ListItem，也可以用来循环渲染ListItemGroup。ListItemGroup的循环渲染详细使用请参见[支持分组列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#支持分组列表)。

## 自定义列表样式

### 设置内容间距

在初始化列表时，如需在列表项之间添加间距，可以使用[ListOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listoptions18对象说明)的space参数。例如，在每个列表项之间沿主轴方向添加10vp的间距。

```typescript
List({ space: 10 }) {

}
```

### 添加分隔线

分隔线用来将界面元素隔开，使单个元素更加容易识别。以系统设置场景为例（如下图所示），列表项左侧为图标（如蓝牙图标），右侧为文字描述且分割线在文字下方。

**图13** 设置列表分隔线样式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ISUricI5RuuSMLlTbNp1lQ/zh-cn_image_0000002565290183.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=385AE7910CC9FCC814EDE5F8D081EA161317BE91CD1D9C4532B85503614C3879)

List提供了[divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#divider)属性用于给列表项之间添加分隔线。在设置divider属性时，可以通过strokeWidth和color属性设置分隔线的粗细和颜色。

startMargin和endMargin属性分别用于设置分隔线距离列表侧边起始端的距离和距离列表侧边结束端的距离。

```typescript
class DividerTmp {
  public strokeWidth: Length = 1;
  public startMargin: Length = 60;
  public endMargin: Length = 10;
  public color: ResourceColor = '#ffe9f0f0';

  constructor(strokeWidth: Length, startMargin: Length, endMargin: Length, color: ResourceColor) {
    this.strokeWidth = strokeWidth;
    this.startMargin = startMargin;
    this.endMargin = endMargin;
    this.color = color;
  }
}

@Entry
@Component
export struct CustomListStyle {
  @State egDivider: DividerTmp = new DividerTmp(1, 60, 10, '#ffe9f0f0');

  build() {

          List(

          ) {

          }
          .divider(this.egDivider)

  }
}
```

此示例表示从距离列表侧边起始端60vp开始到距离结束端10vp的位置，画一条粗细为1vp的分割线，可以实现图9设置列表分隔线的样式。

> **说明**
> 1. 分隔线的宽度会使ListItem之间存在一定间隔，当List设置的内容间距小于分隔线宽度时，ListItem之间的间隔会使用分隔线的宽度。
> 2. 当List存在多列时，分割线的startMargin和endMargin作用于每一列上。
> 3. List组件的分隔线画在两个ListItem之间，第一个ListItem上方和最后一个ListItem下方不会绘制分隔线。

### 添加滚动条

当列表项高度（宽度）超出屏幕高度（宽度）时，列表可以沿垂直（水平）方向滚动。在页面内容很多时，若用户需快速定位，可拖拽滚动条，如下图所示。

**图14** 列表的滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/KsjpSeKoT8OkTY0Z8ixfUQ/zh-cn_image_0000002565210163.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=5EFCFAB46E620B6603D26F119026DD0F41983DAE2E35AEB9F5094B791C06FD05)

在使用List组件时，可通过scrollBar属性控制列表滚动条的显示。scrollBar的取值类型为[BarState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#barstate)，当取值为BarState.Auto表示按需显示滚动条。此时，当触摸到滚动条区域时显示控件，可上下拖拽滚动条快速浏览内容，拖拽时会变粗。若不进行任何操作，2秒后滚动条自动消失。

scrollBar属性API version 9及以下版本默认值为BarState.Off，从API version 10版本开始默认值为BarState.Auto。

```typescript
List(

) {

}

.scrollBar(BarState.Auto)
```

## 添加外置滚动条

列表[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)可与[ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar)组件配合使用，为列表添加外置滚动条。两者通过绑定同一个[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)滚动控制器对象实现联动。

1. 首先，需要创建一个[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)类型的对象listScroller。 ```typescript private listScroller: Scroller = new Scroller(); ```
2. 然后，列表通过[scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listoptions18对象说明)参数绑定滚动控制器。 ```typescript List({ scroller: this.listScroller }) { } ```
3. 最后，滚动条通过[scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar#scrollbaroptions对象说明)参数绑定滚动控制器。 ```typescript ScrollBar({ scroller: this.listScroller}) ```

**图15** 列表的外置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/x7go8RQbRYG7mRNOFhM79g/zh-cn_image_0000002534250340.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=7B77A0DD8A39101827379AF26F008EA92C74401FE681A0367C9122F2AED85E8B)

> **说明**
> - 滚动条组件[ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar)，还可配合其他可滚动组件使用，如[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)。
> - 在圆形屏幕设备上，[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)可以与弧形滚动条组件[ArcScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar)配合使用为列表添加弧形外置滚动条，使用方式可参考[创建弧形列表 (ArcList)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist)的[添加外置滚动条ArcScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist#添加外置滚动条arcscrollbar)章节。

## 支持分组列表

在列表中支持数据的分组展示，可以使列表显示结构清晰，查找方便，从而提高使用效率。分组列表在实际应用中十分常见，如下图所示联系人列表。

**图16** 联系人分组列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/uCB94I_DQ9mBTICymMsr9w/zh-cn_image_0000002534410286.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=45BE961F6FB93AE52E483B6C1298F00D1386F48236F9FFEBABE7D6A06C8371C2)

在List组件中使用ListItemGroup对项目进行分组，可以构建二维列表。

在List组件中可以直接使用一个或者多个ListItemGroup组件，ListItemGroup的宽度默认充满List组件。在初始化ListItemGroup时，可通过header参数设置列表分组的头部组件。

```typescript
@Entry
@Component
export struct GroupedList {
  @Builder
  itemHead(text: string) {

    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {

          List(

          ) {
            ListItemGroup({ header: this.itemHead('A') }) {

            }

            ListItemGroup({ header: this.itemHead('B') }) {

            }
          }

  }
}
```

如果多个ListItemGroup结构类似，可以将多个分组的数据组成数组，然后使用ForEach对多个分组进行循环渲染。例如在联系人列表中，将每个分组的联系人数据contacts（可参考[迭代列表内容](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#迭代列表内容)章节）和对应分组的标题title数据进行组合，定义为数组contactsGroups。然后在ForEach中对contactsGroups进行循环渲染，即可实现多个分组的联系人列表。可参考[添加粘性标题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加粘性标题)章节示例代码。

## 添加粘性标题

粘性标题是一种常见的标题模式，常用于定位字母列表的头部元素。如下图所示，在联系人列表中滚动A部分时，B部分开始的头部元素始终处于A的下方。而在开始滚动B部分时，B的头部会固定在屏幕顶部，直到所有B的项均完成滚动后，才被后面的头部替代。

粘性标题不仅有助于阐明列表中数据的表示形式和用途，还可以帮助用户在大量信息中进行数据定位，从而避免用户在标题所在的表的顶部与感兴趣区域之间反复滚动。

**图17** 粘性标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/xNX2faTuQPmFqLSSY1Xgfw/zh-cn_image_0000002565290185.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=6281473470DFFD0897039354C8D1F26A976A0144ADA3633E82768AD86A88A159)

List组件的[sticky](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#sticky9)属性配合ListItemGroup组件使用，用于设置ListItemGroup中的头部组件是否呈现吸顶效果或者尾部组件是否呈现吸底效果。

通过给List组件设置sticky属性为StickyStyle.Header，即可实现列表的粘性标题效果。如果需要支持吸底效果，可以通过footer参数初始化ListItemGroup的底部组件，并将sticky属性设置为StickyStyle.Footer。

```typescript
import { util } from '@kit.ArkTS';

class Contact {
  public key: string = util.generateRandomUUID(true);
  public name: string | Resource;
  public icon: Resource;

  constructor(name: string | Resource, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

class ContactsGroup {
  public title: string = '';
  public contacts: Array<object> | null = null;
  public key: string = '';
}

export class ContactsGroupDataSource implements IDataSource {
  private list: object[] = [];

  constructor(list: object[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): object {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

export let contactsGroups: object[] = [
  {
    title: 'A',
    contacts: [

      new Contact($r('app.string.contacts_A_one'), $r('app.media.iconA')),

      new Contact($r('app.string.contacts_A_two'), $r('app.media.iconB')),

      new Contact('Angela', $r('app.media.iconC')),
    ],
    key: util.generateRandomUUID(true)
  } as ContactsGroup,
  {
    title: 'B',
    contacts: [

      new Contact($r('app.string.contacts_B_one'), $r('app.media.iconD')),

      new Contact($r('app.string.contacts_B_three'), $r('app.media.iconE'))
    ],
    key: util.generateRandomUUID(true)
  } as ContactsGroup
];
export let contactsGroupsDataSource: ContactsGroupDataSource = new ContactsGroupDataSource(contactsGroups);

@Entry
@Component
export struct StickyHeaderList {

  @Builder
  itemHead(text: string) {

    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {

          List() {

            LazyForEach(contactsGroupsDataSource, (itemGroup: ContactsGroup) => {
              ListItemGroup({ header: this.itemHead(itemGroup.title) }) {

                if (itemGroup.contacts) {
                  LazyForEach(new ContactsGroupDataSource(itemGroup.contacts), (item: Contact) => {
                    ListItem() {
                      Row() {
                        Image(item.icon).width(40).height(40).margin(10)
                        Text(item.name).fontSize(20)
                      }.width('100%').justifyContent(FlexAlign.Start)
                    }
                  }, (item: Contact) => JSON.stringify(item))
                }
              }
            }, (itemGroup: ContactsGroup) => JSON.stringify(itemGroup))
          }
          .sticky(StickyStyle.Header)

  }
}
```

## 控制滚动位置

控制滚动位置在实际应用中十分常见，例如当新闻页列表项数量庞大，用户滚动列表到一定位置时，希望快速滚动到列表底部或返回列表顶部。此时，可以通过控制滚动位置来实现列表的快速定位，如下图所示。

**图18** 返回列表顶部

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/xEWL7jBKRFaRtEYQkrhqTA/zh-cn_image_0000002565210165.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=562D1EBE49548B91FD25C53F0B8302A9238B1F382AC12CC4FE13A78CE4B5D56A)

List组件初始化时，可以通过scroller参数绑定一个[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)对象，进行列表的滚动控制。例如，用户在新闻应用中，点击新闻页面底部的返回顶部按钮时，就可以通过Scroller对象的scrollToIndex方法使列表滚动到指定的列表项索引位置。

首先，需要创建一个Scroller的对象listScroller。

```typescript
private listScroller: Scroller = new Scroller();
```

然后，通过将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。在需要跳转的位置指定scrollToIndex的参数为0，表示返回列表顶部。

```typescript
Stack({ alignContent: Alignment.Bottom }) {

  List({ space: 20, scroller: this.listScroller }) {

  }

  Button() {

  }

  .onClick(() => {

    this.listScroller.scrollToIndex(0);
  })
}
```

## 响应滚动位置

许多应用需要监听列表的滚动位置变化并作出响应。例如，在联系人列表滚动时，如果跨越了不同字母开头的分组，则侧边字母索引栏也需要更新到对应的字母位置。

除了字母索引之外，滚动列表结合多级分类索引在应用开发过程中也很常见，例如购物应用的商品分类页面，多级分类也需要监听列表的滚动位置。

**图19** 字母索引响应联系人列表滚动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/yIuJ9hhEQ1O7EhsVq3-tYA/zh-cn_image_0000002534250342.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=B4DE4E551DAB1EB5E23004084F25B6E39EF6E5D21BE74543A85C4275898857D7)

如上图所示，当联系人列表从A滚动到B时，右侧索引栏也需要同步从选中A状态变成选中B状态。此场景可以通过监听List组件的[onScrollIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#onscrollindex)事件来实现，右侧索引栏需要使用字母表索引组件[AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer)。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引栏对应字母的位置selectedIndex。由于AlphabetIndexer组件通过selected属性设置了选中项索引值，当selectedIndex变化时会触发AlphabetIndexer组件重新渲染，从而显示为选中对应字母的状态。

```typescript
const alphabets = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

@Entry
@Component
export struct ResponsiveScrollPositionList {
  @State selectedIndex: number = 0;
  private listScroller: Scroller = new Scroller();

  build() {

          Stack({ alignContent: Alignment.End }) {

            List({ scroller: this.listScroller }) {

            }
            .onScrollIndex((firstIndex: number) => {

            })

            AlphabetIndexer({ arrayValue: alphabets, selected: 0 })
              .selected(this.selectedIndex)
              .onSelect((index: number) => {
                this.listScroller.scrollToIndex(index);
              })
          }

  }
}
```

> **说明**
> 计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

## 响应列表项侧滑

侧滑菜单在许多应用中都很常见。例如，通讯类应用通常会给消息列表提供侧滑删除功能，即用户可以通过向左侧滑列表的某一项，再点击删除按钮删除消息，如下图所示。其中，列表项头像右上角标记设置参考[给列表项添加标记](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#给列表项添加标记)。

**图20** 侧滑删除列表项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/PS8EAHgGQoSOYWUM-XWIvw/zh-cn_image_0000002534410288.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=BADBA998E03C3AC3D82FE698751B4225ED9BD36CBB9408440F15FEA2F513889E)

ListItem的[swipeAction属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeaction9)可用于实现列表项的左右滑动功能。swipeAction属性方法初始化时有必填参数SwipeActionOptions，其中，start参数表示设置列表项右滑时起始端滑出的组件，end参数表示设置列表项左滑时尾端滑出的组件。

在消息列表中，end参数表示设置ListItem左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据索引值来删除列表项对应的数据，从而实现侧滑删除功能。

1. 实现尾端滑出组件的构建。 ```typescript @Builder itemEnd(index: number) {  Button({ type: ButtonType.Circle }) {  Image($r('sys.media.ohos_ic_bottomsheet_close'))  .width(40)  .height(40)  }  .onClick(() => {  this.arr.splice(index, 1);  }) } ```
2. 绑定swipeAction属性到可左滑的ListItem上。 ```typescript ListItem() { }.swipeAction({  end: {  builder: () => {  this.itemEnd(this.index);  },  } }) ```

## 给列表项添加标记

添加标记是一种无干扰性且直观的方法，用于显示通知或将注意力集中到应用内的某个区域。例如，当消息列表接收到新消息时，通常对应消息列表的右上方会出现标记，提示有若干条未读消息，如下图所示。

**图21** 给列表项添加标记

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/-bnbdLxvRZ2kh81u_rGh2w/zh-cn_image_0000002565290187.png?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=93594200168F9E88015778197997BC176B569CBB6D93A9914B0ACD09A6B19B13)

在ListItem中使用[Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)组件可实现给列表项添加标记功能。Badge是可以附加在单个组件上用于信息标记的容器组件。

在消息列表中，若希望在消息的右上角添加标记，可在实现消息列表项ListItem中，将对应的组件作为Badge的子组件。

在Badge组件中，count和position参数用于设置需要展示的消息数量和提示点显示位置，还可以通过style参数灵活设置标记的样式。

```typescript
ListItem() {

  Badge({
    count: 1,
    position: BadgePosition.RightTop,
    style: { badgeSize: 16, badgeColor: '#FA2A2D' }
  }) {

  }
}
```

## 下拉刷新与上拉加载

页面的下拉刷新与上拉加载功能在移动应用中十分常见，例如，新闻页面的内容刷新和加载。这两种操作的原理都是通过响应用户的[触摸事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch)，在顶部或者底部显示一个刷新或加载视图，完成后再将此视图隐藏。

以下拉刷新为例，其实现主要分成三步：

1. 监听手指按下事件，记录其初始位置的值。
2. 监听手指按压移动事件，记录并计算当前移动的位置与初始值的差值，大于0表示向下移动，同时设置一个允许移动的最大值。
3. 监听手指抬起事件，若此时移动达到最大值，则触发数据加载并显示刷新视图，加载完成后将此视图隐藏。

> **说明**
> 页面的下拉刷新操作推荐使用[Refresh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh)组件实现。

下拉刷新与上拉加载的具体实现可参考[新闻数据加载](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-NewsDataArkTS)。

## 编辑列表

列表的编辑模式用途十分广泛，常见于待办事项管理、文件管理、备忘录的记录管理等应用场景。在列表的编辑模式下，新增和删除列表项是最基础的功能，其核心是对列表项对应的数据集合进行数据添加和删除。

下面以待办事项管理为例，介绍如何快速实现新增和删除列表项功能。

### 新增列表项

如下图所示，当用户点击添加按钮时，提供用户新增列表项内容选择或填写的交互界面，用户点击确定后，列表中新增对应的项目。

**图22** 新增待办

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/dtTyNO6VRh2gUMBSn9OQUQ/zh-cn_image_0000002565210167.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=F381D2D354D20396C5F7C27E2BAD88B8EAB5FEA8F497B842689B86967B365F03)

添加列表项功能实现主要流程如下：

1. 定义列表项数据结构，以待办事项管理为例，首先定义待办数据结构。 ```typescript import { util } from '@kit.ArkTS'; export class ToDo {  public key: string = util.generateRandomUUID(true);  public name: string;  constructor(name: string) {  this.name = name;  } } ```
2. 构建列表整体布局和列表项。 ```typescript import { ToDo } from './ToDo'; @Component export struct ToDoListItem {  @Link isEditMode: boolean;  @Link selectedItems: ToDo[];  private toDoItem: ToDo = new ToDo('');  build() {  Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {  }  .width('100%')  .height(80)  .borderRadius(24)  .gesture(  GestureGroup(GestureMode.Exclusive,  LongPressGesture()  .onAction(() => {  })  )  )  } } ```
3. 初始化待办列表数据和可选事项，最后，构建列表布局和列表项。 ```typescript import { ToDo } from './ToDo'; import { ToDoListItem } from './ToDoListItem'; @Entry @Component export struct AddListItem {  @State toDoData: ToDo[] = [];  @Watch('onEditModeChange') @State isEditMode: boolean = false;  @State selectedItems: ToDo[] = [];  private availableThings: string [] = [];  aboutToAppear(): void {  const context = this.getUIContext().getHostContext() as common.UIAbilityContext;  const reading = context.resourceManager.getStringByNameSync('Reading')  this.availableThings.push(reading)  const exercise = context.resourceManager.getStringByNameSync('Exercise')  this.availableThings.push(exercise)  const travel = context.resourceManager.getStringByNameSync('Travel')  this.availableThings.push(travel)  const listening = context.resourceManager.getStringByNameSync('Listening_Music')  this.availableThings.push(listening)  const watching = context.resourceManager.getStringByNameSync('Watching_Films')  this.availableThings.push(watching)  const singing = context.resourceManager.getStringByNameSync('Singing')  this.availableThings.push(singing)  }  onEditModeChange() {  if (!this.isEditMode) {  this.selectedItems = [];  }  }  build() {  Column(  ) {  Row() {  if (this.isEditMode) {  Text('X')  .fontSize(20)  .onClick(() => {  this.isEditMode = false;  })  .margin({ left: 20, right: 20 })  } else {  Text($r('app.string.TodoItem'))  .fontSize(36)  .margin({ left: 40 })  Blank()  Text('+')  .onClick(() => {  this.getUIContext().showTextPickerDialog({  range: this.availableThings,  onAccept: (value: TextPickerResult) => {  let arr = Array.isArray(value.index) ? value.index : [value.index];  for (let i = 0; i < arr.length; i++) {  this.toDoData.push(new ToDo(this.availableThings[arr[i]]));  }  },  })  })  }  List({ space: 10 }) {  ForEach(this.toDoData, (toDoItem: ToDo) => {  ListItem() {  ToDoListItem({  isEditMode: this.isEditMode,  toDoItem: toDoItem,  selectedItems: this.selectedItems  })  }  }, (toDoItem: ToDo) => toDoItem.name.toString())  }  }  }  } } ```

### 删除列表项

如下图所示，当用户长按列表项进入删除模式时，提供用户删除列表项选择的交互界面，用户勾选完成后点击删除按钮，列表中删除对应的项目。

**图23** 长按删除待办事项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/P--VrHFKSY2vi7WPJJq8Sg/zh-cn_image_0000002534250344.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=EAD7E3BC9F9AFDEDA707743BE6F46D084E3DD3FBB604DA219ED4F2B2C9EB2F43)

删除列表项功能实现主要流程如下：

1. 列表的删除功能一般进入编辑模式后才可使用，所以需要提供编辑模式的入口。 以待办列表为例，通过监听列表项的长按事件，当用户长按列表项时，进入编辑模式。 ```typescript import { util } from '@kit.ArkTS'; export class ToDo {  public key: string = util.generateRandomUUID(true);  public name: string;  public toDoData: ToDo[] = [];  constructor(name: string) {  this.name = name;  } } ``` 实现参考： ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) { } .gesture(  GestureGroup(GestureMode.Exclusive,  LongPressGesture()  .onAction(() => {  if (!this.isEditMode) {  this.isEditMode = true;  }  })  ) ) ```
2. 需要响应用户的选择交互，记录要删除的列表项数据。 在待办列表中，通过勾选框的勾选或取消勾选，响应用户勾选列表项变化，记录所有选择的列表项。 ```typescript import { util } from '@kit.ArkTS'; export class ToDo {  public key: string = util.generateRandomUUID(true);  public name: string;  public toDoData: ToDo[] = [];  constructor(name: string) {  this.name = name;  } } ``` 实现参考： ```typescript if (this.isEditMode) {  Checkbox()  .onChange((isSelected) => {  if (isSelected) {  this.selectedItems.push(new ToDo(this.toDoItem.name));  } else {  let index = this.selectedItems.indexOf(new ToDo(this.toDoItem.name));  if (index !== -1) {  this.selectedItems.splice(index, 1);  }  }  }) } ```
3. 需要响应用户点击删除按钮事件，删除列表中对应的选项。 ```typescript import { util } from '@kit.ArkTS'; export class ToDo {  public key: string = util.generateRandomUUID(true);  public name: string;  public toDoData: ToDo[] = [];  constructor(name: string) {  this.name = name;  } } ``` 实现参考： ```typescript Button($r('app.string.delete'))  .onClick(() => {  this.toDoData = this.toDoData.filter(toDoItem =>  !this.selectedItems.some(selectedItem => selectedItem.name === toDoItem.name));  this.isEditMode = false;  }) ```

## 长列表的处理

[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。

关于长列表按需加载优化的具体实现可参考[数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)章节中的示例。

当使用懒加载方式渲染列表时，为了更好的列表滚动体验，减少列表滑动时出现白块，List组件提供了[cachedCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#cachedcount)参数用于设置列表项缓存数，懒加载方式只会预加载List显示区域外cachedCount的内容，而非懒加载会全部加载。无论懒加载还是非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

```typescript
List(

) {

}.cachedCount(3)
```

以垂直列表为例：

- List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。
- List下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

> **说明**
> 1. cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
> 2. 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。

## 折叠与展开

列表项的折叠与展开用途广泛，常用于信息清单的展示、填写等应用场景。

**图24** 列表项的折叠与展开

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/IEeENnhuQtCsMys5Xxrf4A/zh-cn_image_0000002534410290.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=B8F74BF728D4AA233D94FD4885E41E0DF80BE000A82324B48CD9312FDBB6350E)

列表项折叠与展开效果实现主要流程如下：

1. 定义列表项数据结构。 ```typescript import { curves } from '@kit.ArkUI'; interface ItemInfo {  index: number,  name: ResourceStr,  label: ResourceStr,  type?: string, } interface ItemGroupInfo extends ItemInfo {  children: ItemInfo[] } ```
2. 构造列表结构。 ```typescript  @State routes: ItemGroupInfo[] = [  {  index: 0,  name: 'basicInfo',  label: $r('app.string.Personal_Basic_Information'),  children: [  {  index: 0,  name: $r('app.string.nick_name'),  label: 'xxxx',  type: 'Text'  },  {  index: 1,  name: $r('app.string.avatar'),  label: $r('sys.media.ohos_user_auth_icon_face'),  type: 'Image'  },  {  index: 2,  name: $r('app.string.age'),  label: 'xxxx',  type: 'Text'  },  {  index: 3,  name: $r('app.string.birthday'),  label: 'xxxxxxxxx',  type: 'Text'  },  {  index: 4,  name: $r('app.string.gender'),  label: 'xxxxxxxx',  type: 'Text'  },  ]  },  {  index: 1,  name: 'equipInfo',  label: $r('app.string.Device_Information'),  children: []  },  {  index: 2,  name: 'appInfo',  label: $r('app.string.Application_usage_information'),  children: []  },  {  index: 3,  name: 'uploadInfo',  label: $r('app.string.data_you_voluntarily_uploaded'),  children: []  },  {  index: 4,  name: 'tradeInfo',  label: $r('app.string.Trading_and_asset_information'),  children: []  },  {  index: 5,  name: 'otherInfo',  label: $r('app.string.Other_materials'),  children: []  },  ];  @State expandedItems: boolean[] = Array(this.routes.length).fill(false);  @State selection: string | null = null;  build() {  Column() {  List({ space: 10 }) {  ForEach(this.routes, (itemGroup: ItemGroupInfo) => {  ListItemGroup({  header: this.ListItemGroupHeader(itemGroup),  style: ListItemGroupStyle.CARD,  }) {  if (this.expandedItems[itemGroup.index] && itemGroup.children) {  ForEach(itemGroup.children, (item: ItemInfo) => {  ListItem({ style: ListItemStyle.CARD }) {  Row() {  Text(item.name)  Blank()  if (item.type === 'Image') {  Image(item.label)  .height(20)  .width(20)  } else {  Text(item.label)  }  Image($r('sys.media.ohos_ic_public_arrow_right'))  .fillColor($r('sys.color.ohos_id_color_fourth'))  .height(30)  .width(30)  }  .width("100%")  }  .width("100%")  .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })  })  }  }.clip(true)  })  }  .width("100%")  }  .width('100%')  .height('100%')  .justifyContent(FlexAlign.Start)  .backgroundColor($r('sys.color.ohos_id_color_sub_background'))  } } ```
3. 通过改变ListItem的状态，来控制每个列表项是否展开，并通过[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty#animation)和[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)来实现展开与折叠过程中的动效效果。 ```typescript @Builder ListItemGroupHeader(itemGroup: ItemGroupInfo) {  Row() {  Text(itemGroup.label)  Blank()  Image($r('sys.media.ohos_ic_public_arrow_down'))  .fillColor($r('sys.color.ohos_id_color_fourth'))  .height(30)  .width(30)  .rotate({ angle: !!itemGroup.children.length ? (this.expandedItems[itemGroup.index] ? 180 : 0) : 180 })  .animation({ curve: curves.interpolatingSpring(0, 1, 228, 22) })  }  .width("100%")  .padding(10)  .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })  .onClick(() => {  if (itemGroup.children.length) {  this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 528, 39) }, () => {  this.expandedItems[itemGroup.index] = !this.expandedItems[itemGroup.index];  })  }  }) } ```

## 切换布局方向

部分业务场景需要列表底部插入数据时，自动向上滚动，把新插入的节点展示出来。例如，直播评论、即时聊天等应用场景。而List组件正常布局时, 在内容下方增加节点，内容是保持不变的。此时，可以通过切换布局方向来实现所需效果。

**图25** 实时消息滚动显示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/CepTTT7PSYK0sNTJ-1240g/zh-cn_image_0000002565290189.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=81098B7FD2E7630FE3EBC9EE85557FAE47A617F32999FC263102D2279337D683)

1. 定义列表项数据结构。 ```typescript interface Message {  id: number  content: ResourceStr  sender: ResourceStr } ```
2. 构造列表结构，同时把[stackFromEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#stackfromend19)接口参数值设置为true，即可实现List列表在底部插入数据时，内容向上滚动。 ```typescript @Builder MessageItem(message: Message) {  Column() {  Text(`${message.sender}: ${message.content}`)  .fontSize(16)  .textAlign(TextAlign.Start)  .padding(10)  .backgroundColor(message.sender === 'system' ? '#F0F0F0' : '#E6F3FF')  .borderRadius(8)  }  .width('100%')  .alignItems(HorizontalAlign.Start)  .margin({ bottom: 8 }) } @State messages: Message[] = []; aboutToAppear(): void {  const context = this.getUIContext().getHostContext() as common.UIAbilityContext;  const welcomeLiveRoom = context.resourceManager.getStringByNameSync('welcome_live_room');  const system = context.resourceManager.getStringByNameSync('system');  const helloEveryone = context.resourceManager.getStringByNameSync('hello_everyone');  const anchors = context.resourceManager.getStringByNameSync('anchors');  this.messages = [  { id: 1, content: welcomeLiveRoom, sender: system },  { id: 2, content: helloEveryone, sender: anchors }  ]; } build() {  Column() {  List({ space: 10 }) {  ForEach(this.messages, (item: Message) => {  ListItem() {  this.MessageItem(item)  }  }, (item: Message) => item.id.toString())  }  .stackFromEnd(true)  .layoutWeight(1)  .alignListItem(ListItemAlign.Center)  }  .width('100%')  .height('100%') } ```

## 支持滑动离手事件

从API version 20开始，滚动类组件（[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)）支持滑动离手事件回调功能，当用户手指离开屏幕时，会触发该事件并上报离手瞬间的滑动速度。开发者可利用此接口实现类似新闻浏览页面的自定义限位滚动效果，短新闻限位滚动，长新闻自由滚动。

**图26** 自定义限位滚动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/82zrrFfYT6W6HaSPfvpW-g/zh-cn_image_0000002565210169.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=FA0E2B951D8E73A901EEF4ECD404CBEA1F2861F4D3CEA9F09A6361AEAF6C1B0E)

1. 定义新闻条目数据结构。 ```typescript class News {  public id: string;  public title: ResourceStr;  public content: ResourceStr;  public type: string;  constructor(id: string, title: ResourceStr, content: ResourceStr, type: string) {  this.id = id;  this.title = title;  this.content = content;  this.type = type;  } } ```
2. 构造新闻条目结构，通过type属性来区分长新闻，短新闻。 ```typescript @State newsData: Array<News> = [  new News('1', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),  new News('2', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),  new News('3', $r('app.string.new_title'), $r('app.string.new_long'), 'long'),  new News('4', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),  new News('5', $r('app.string.new_title'), $r('app.string.new_long'), 'long'), ]; ```
3. 滑动离手事件onWillStopDragging及新闻处理逻辑： - 上报离手瞬间滑动速度，支持正负方向速度检测，向上滑动为正，向下滑动为负。 ```typescript .onWillStopDragging((velocity: number) => { if (velocity < 0) { } else { } }) ``` - 通过[getItemRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#getitemrect11)接口方法获取当前项位置信息。 ```typescript let rect = this.scrollerForList.getItemRect(this.currentIndex); ``` - 处理短新闻：直接跳转相邻项。 ```typescript if (velocity > 10) { this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START) } else if (velocity < -10) { this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START) } ``` - 处理长新闻：计算剩余显示范围决定滚动终点。 ```typescript let rect = this.scrollerForList.getItemRect(this.currentIndex); if (velocity < -30) { if (rect) { let leftRect = rect.y + rect.height; let mainPosition = -velocity * DEFAULT_FRICTION / FRICTION_SCALE; if (leftRect + mainPosition > 0.75 * this.listHeight) { this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START); return; } else if (leftRect + mainPosition < 0.25 * this.listHeight) { this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.END, { extraOffset: LengthMetrics.vp(this.listHeight * 0.3) }) return; } } } else if (velocity > 30) { let leftRect = rect?.y + rect?.height; let mainPosition = velocity * DEFAULT_FRICTION / FRICTION_SCALE; if (leftRect + mainPosition > 0.75 * this.listHeight) { this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START); return; } } ```

## 设置边缘滑动效果

边缘滑动效果是指当用户滑动滚动组件至边缘后，继续滑动时触发的交互效果。当前List支持通过[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#edgeeffect)属性设置三种边缘滑动效果，分别为弹簧效果（即回弹效果）、阴影效果、无效果。具体效果说明请参见[EdgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#edgeeffect)的枚举说明。

当List组件的内容区大于等于一屏时，List的边缘滑动效果默认为回弹效果，如下图所示。

**图27** 边缘回弹效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ml1ds27oR5mR6s3_RKP2WQ/zh-cn_image_0000002534250346.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=6B4C200303066271A40FD544E0DB44A2A1039B8EE627B9373370605D7FC1925C)

设置.edgeEffect(EdgeEffect.None)时，List无边缘滑动效果，如下图所示。

**图28** 无边缘滑动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/pSYsEA5pRMaYsjvG84NoBg/zh-cn_image_0000002534410292.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=E94A5A487EFA7B2FDDB22E96A5F6FE526583D4AB53C395F46189593EE989C919)

从API version 18开始，List还支持只设置单边的边缘滑动效果，如设置.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })来实现起始边有边缘回弹效果，末尾边无效果，如下图所示。

**图29** 单边边缘滑动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/EUkFx-04SKCMflBmx7h3KQ/zh-cn_image_0000002565290191.gif?HW-CC-KV=V1&HW-CC-Date=20260331T023744Z&HW-CC-Expire=86400&HW-CC-Sign=5CE129D97A816A8872292E847C182342EB15C5577DDFD21DF8E37B1A0C835A8B)

需要注意的是，当List组件的内容区小于一屏时，List默认无边缘滑动效果。若要启用边缘回弹效果，可以通过设置.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })来实现。

## 示例代码

- [二维列表](https://gitcode.com/HarmonyOS_Samples/two-dimension-list)
- [List组件嵌套滑动](https://gitcode.com/HarmonyOS_Samples/nested-list)
- [列表编辑效果](https://gitcode.com/HarmonyOS_Samples/list-item-edit)
