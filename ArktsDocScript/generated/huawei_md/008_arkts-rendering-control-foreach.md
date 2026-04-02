# ForEach：循环渲染
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach

ForEach接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为[List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)。

API参数说明见：[ForEach API参数说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach)。

> **说明**
> 从API version 9开始，该接口支持在ArkTS卡片中使用。

## 键值生成规则

在ForEach循环渲染过程中，系统会为每个数组元素生成一个唯一且持久的键值，用于标识对应的组件。当键值变化时，ArkUI框架会视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。

ForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '__' + JSON.stringify(item); }。

ArkUI框架对于ForEach的键值生成有一套特定的判断规则，这主要与itemGenerator函数和keyGenerator函数的第二个参数index有关。具体的键值生成规则判断逻辑如下图所示。

**图1** ForEach键值生成规则

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/5QFBpct2QMyvssFLwcr7XQ/zh-cn_image_0000002534250226.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=2BA78DF583220E72A58BAAD0D0AA855E802CC28CF3E62770A2BCDA81B1007DEE)

> **说明**
> 1. ArkUI框架会对重复的键值发出运行时警告。在UI更新时，如果出现重复的键值，框架可能无法正常工作，具体请参见[渲染结果非预期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染结果非预期)。
> 2. 不建议在键值中包含数据项索引index，这可能会导致[渲染结果非预期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染结果非预期)和[渲染性能降低](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染性能降低)。
> 3. 如果开发者在itemGenerator函数中声明了index参数，但未在keyGenerator函数中声明index参数，框架会在keyGenerator函数返回值的基础上拼接index，作为最终的键值，这将会引发上述第二点中的问题。为避免此现象，请在keyGenerator函数中声明index参数。

键值生成示例:

```typescript
interface ChildItemType {
  str: string;
  num: number;
}

@Entry
@Component
struct Index {
  @State simpleList: Array<ChildItemType> = [
    { str: 'one', num: 1 },
    { str: 'two', num: 2 },
    { str: 'three', num: 3 }
  ];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: ChildItemType, index: number) => {
          ChildItem({ str: item.str, num: index })
        }, (item: ChildItemType, index: number) => {
          return item.str;
        })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ChildItem {
  @Prop str: string = '';
  @Prop num: number = 0;

  build() {
    Text(this.str)
      .fontSize(50)
  }
}
```

在上述示例中，当组件生成函数声明index时，建议键值生成函数也声明index参数，以避免渲染性能降低和渲染结果非预期。同时建议在键值生成函数实现中使用与UI相关的数据属性，在本示例中，数据属性str与UI界面显示相关，因此建议将其作为键值生成函数的返回值。

## 组件创建规则

在确定键值生成规则后，ForEach的第二个参数itemGenerator函数会根据键值生成规则为数据源的每个数组项创建组件。组件的创建包括两种情况：[ForEach首次渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#首次渲染)和[ForEach非首次渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#非首次渲染)。

### 首次渲染

在ForEach首次渲染时，会根据前述键值生成规则为数据源的每个数组项生成唯一键值，并创建相应的组件。

```typescript
@Entry
@Component
struct ForEachFirstRender {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: string) => {
          ForEachChildItem({ item: item })
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ForEachChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

运行效果如下图所示。

**图2** ForEach数据项不存在相同键值案例首次渲染运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/gFvuMyx-Rr609UunknlWiw/zh-cn_image_0000002534410172.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=BAF08CB3768CD5365ADF1AE469C8F1B6380E9652DCE34BA706E0830B5A48EE68)

在上述代码中，keyGenerator函数的返回值是item。在ForEach渲染循环时，为数组项依次生成键值one、two和three，并创建对应的ForEachChildItem组件渲染到界面上。

当不同数组项生成的键值相同时，框架的行为是未定义的。例如，在以下代码中，ForEach渲染相同的数据项two时，只创建了一个SameKeyChildItem组件，而没有创建多个具有相同键值的组件。

```typescript
@Entry
@Component
struct ForEachSameKey {
  @State simpleList: Array<string> = ['one', 'two', 'two', 'three'];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: string) => {
          SameKeyChildItem({ item: item })
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct SameKeyChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

运行效果如下图所示。

**图3** ForEach数据源存在相同值案例首次渲染运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/aqxEWhZnTB6mIccYxkdxZw/zh-cn_image_0000002565290071.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=133294CBA09455AA723487ECD82B2CEE16D80359FF0436A89CDB4D4F9DDE1701)

在该示例中，最终键值生成规则为item。当ForEach遍历数据源simpleList，遍历到索引为1的two时，创建键值为two的组件并记录。当遍历到索引为2的two时，当前项的键值也为two，此时不再创建新的组件。

### 非首次渲染

在ForEach组件进行非首次渲染时，它会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。例如，在以下的代码示例中，通过点击事件修改了数组的第三项值为"new three"，这将触发ForEach组件进行非首次渲染。

```typescript
@Entry
@Component
struct ForEachNotFirstRender {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Row() {
      Column() {
        Text('Click to change the value of the third array item')
          .fontSize(24)
          .fontColor(Color.Red)
          .onClick(() => {
            this.simpleList[2] = 'new three';
          })

        ForEach(this.simpleList, (item: string) => {
          NotFirstRenderChildItem({ item: item })
            .margin({ top: 20 })
        }, (item: string) => item)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct NotFirstRenderChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(30)
  }
}
```

运行效果如下图所示。

**图4** ForEach非首次渲染案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/DK9UeL8LRKuwG8yDfqfzFA/zh-cn_image_0000002565210051.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=7E40B6D56E07847353771BEF1BBF473698B5C2FD014F57B39A5BBDBF76D6E875)

从本例可以看出[@State](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)能够监听到简单数据类型数组simpleList数组项的变化。

1. 当simpleList数组项发生变化时，会触发ForEach重新渲染。
2. ForEach遍历新的数据源['one', 'two', 'new three']，并生成对应的键值one、two和new three。
3. 其中，键值one和two在上次渲染中已经存在，所以 ForEach 复用了对应的组件并进行了渲染。对于第三个数组项 "new three"，由于其通过键值生成规则 item 生成的键值new three在上次渲染中不存在，因此 ForEach 为该数组项创建了一个新的组件。

## 使用场景

ForEach组件在开发过程中的主要应用场景包括：[数据源不变](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#数据源不变)、[数据源数组项发生变化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#数据源数组项发生变化)（如插入、删除操作）、[数据源数组项子属性变化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#数据源数组项子属性变化)。

### 数据源不变

在数据源保持不变的场景中，数据源可以直接采用基本数据类型。例如，页面加载状态时，可以使用骨架屏列表进行渲染展示。

```typescript
@Entry
@Component
struct ArticleList {
  @State simpleList: Array<number> = [1, 2, 3, 4, 5];

  build() {
    Column() {
      ForEach(this.simpleList, (item: number) => {
        ArticleSkeletonView()
          .margin({ top: 20 })
      }, (item: number) => item.toString())
    }
    .padding(20)
    .width('100%')
    .height('100%')
  }
}

@Builder
function textArea(width: number | Resource | string = '100%', height: number | Resource | string = '100%') {
  Row()
    .width(width)
    .height(height)
    .backgroundColor('#FFF2F3F4')
}

@Component
struct ArticleSkeletonView {
  build() {
    Row() {
      Column() {
        textArea(80, 80)
      }
      .margin({ right: 20 })

      Column() {
        textArea('60%', 20)
        textArea('50%', 20)
      }
      .alignItems(HorizontalAlign.Start)
      .justifyContent(FlexAlign.SpaceAround)
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

运行效果如下图所示。

**图5** 骨架屏运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/CwO-tW6sQJubY-D4Nqh0zQ/zh-cn_image_0000002534250228.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=D0BA8FB27D26720BBE2320E968BEB43284B9896D00F33607053F299B0BFCC569)

在本示例中，采用数据项item作为键值生成规则，由于数据源simpleList的数组项各不相同，因此能够保证键值的唯一性。

### 数据源数组项发生变化

在数据源数组项发生变化的场景下，如数组插入、删除操作或者数组项索引位置交换时，数据源应为对象数组类型，并使用对象的唯一ID作为键值。

```typescript
class ArticleChangeSource {
  public id: string;
  public title: string;
  public brief: string;

  constructor(id: string, title: string, brief: string) {
    this.id = id;
    this.title = title;
    this.brief = brief;
  }
}

@Entry
@Component
struct ArticleListViewChangeSource {
  isListReachEnd: boolean = false;
  @State articleList: Array<ArticleChangeSource> = [
    new ArticleChangeSource('001', 'Article 1', 'Abstract'),
    new ArticleChangeSource('002', 'Article 2', 'Abstract'),
    new ArticleChangeSource('003', 'Article 3', 'Abstract'),
    new ArticleChangeSource('004', 'Article 4', 'Abstract'),
    new ArticleChangeSource('005', 'Article 5', 'Abstract'),
    new ArticleChangeSource('006', 'Article 6', 'Abstract')
  ];

  loadMoreArticles() {
    this.articleList.push(new ArticleChangeSource('007', 'New Article', 'Abstract'));
  }

  build() {
    Column({ space: 5 }) {
      List() {
        ForEach(this.articleList, (item: ArticleChangeSource) => {
          ListItem() {
            ArticleCardChangeSource({ article: item })
              .margin({ top: 20 })
          }
        }, (item: ArticleChangeSource) => item.id)
      }
      .onReachEnd(() => {
        this.isListReachEnd = true;
      })
      .parallelGesture(
        PanGesture({ direction: PanDirection.Up, distance: 80 })
          .onActionStart(() => {
            if (this.isListReachEnd) {
              this.loadMoreArticles();
              this.isListReachEnd = false;
            }
          })
      )
      .padding(20)
      .scrollBar(BarState.Off)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ArticleCardChangeSource {
  @Prop article: ArticleChangeSource;

  build() {
    Row() {

      Image($r('app.media.startIcon'))
        .width(80)
        .height(80)
        .margin({ right: 20 })

      Column() {
        Text(this.article.title)
          .fontSize(20)
          .margin({ bottom: 8 })
        Text(this.article.brief)
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: 8 })
      }
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

初始运行效果（左图）和手势上滑加载后效果（右图）如下图所示。

**图6** 数据源数组项变化案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/VzDbIxpEToKpCBiW0q1xRA/zh-cn_image_0000002534410174.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=DCE6E1A917B894605A9E64488EA3EB074573F1E15FBB7A582E1222FFCB7C4954)

在本示例中，ArticleCardChangeSource组件作为ArticleListViewChangeSource组件的子组件，通过[@Prop](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop)装饰器接收一个ArticleChangeSource对象，用于渲染文章卡片。

1. 当列表滚动到底部且手势滑动距离超过80vp时，触发loadMoreArticles()函数。此函数在articleList数据源尾部添加新数据项，增加数据源长度。
2. 数据源被@State装饰器修饰，ArkUI框架能够感知数据源长度的变化并触发ForEach进行重新渲染。

### 数据源数组项子属性变化

当数据源的数组项为对象数据类型，并且只修改某个数组项的属性值时，由于数据源为复杂数据类型，ArkUI框架无法监听到@State装饰器修饰的数据源数组项的属性变化，从而无法触发ForEach的重新渲染。为实现ForEach子组件重新渲染，需要结合[@Observed和@ObjectLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)装饰器使用。例如，在文章列表卡片上点击“点赞”按钮，从而修改文章的点赞数量。

```typescript
@Observed
class ArticleChangeChild {
  public id: string;
  public title: string;
  public brief: string;
  public isLiked: boolean;
  public likesCount: number;

  constructor(id: string, title: string, brief: string, isLiked: boolean, likesCount: number) {
    this.id = id;
    this.title = title;
    this.brief = brief;
    this.isLiked = isLiked;
    this.likesCount = likesCount;
  }
}

@Entry
@Component
struct ArticleListChangeView {
  @State articleList: Array<ArticleChangeChild> = [
    new ArticleChangeChild('001', 'Article 0', 'Abstract', false, 100),
    new ArticleChangeChild('002', 'Article 1', 'Abstract', false, 100),
    new ArticleChangeChild('003', 'Article 2', 'Abstract', false, 100),
    new ArticleChangeChild('004', 'Article 4', 'Abstract', false, 100),
    new ArticleChangeChild('005', 'Article 5', 'Abstract', false, 100),
    new ArticleChangeChild('006', 'Article 6', 'Abstract', false, 100),
  ];

  build() {
    List() {
      ForEach(this.articleList, (item: ArticleChangeChild) => {
        ListItem() {
          ArticleCardChangeChild({
            article: item
          })
            .margin({ top: 20 })
        }
      }, (item: ArticleChangeChild) => item.id)
    }
    .padding(20)
    .scrollBar(BarState.Off)
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ArticleCardChangeChild {
  @ObjectLink article: ArticleChangeChild;

  handleLiked() {
    this.article.isLiked = !this.article.isLiked;
    this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
  }

  build() {
    Row() {

      Image($r('app.media.startIcon'))
        .width(80)
        .height(80)
        .margin({ right: 20 })

      Column() {
        Text(this.article.title)
          .fontSize(20)
          .margin({ bottom: 8 })
        Text(this.article.brief)
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: 8 })

        Row() {

          Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
            .width(24)
            .height(24)
            .margin({ right: 8 })
          Text(this.article.likesCount.toString())
            .fontSize(16)
        }
        .onClick(() => this.handleLiked())
        .justifyContent(FlexAlign.Center)
      }
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

上述代码的初始运行效果（左图）和点击第1个文章卡片上的点赞图标后的运行效果（右图）如下图所示。

**图7** 数据源数组项子属性变化案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/pfGPWl0uSViSmpGiat8pWw/zh-cn_image_0000002565290073.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=246A9FF6431EDACFBF404A7E3784B0D62394D577F02F39532403D476C855266D)

在本示例中，ArticleChangeChild类被@Observed装饰器修饰。父组件ArticleListChangeView传入ArticleChangeChild对象实例给子组件ArticleCardChangeChild，子组件使用@ObjectLink装饰器接收该实例。

1. 当点击第1个文章卡片上的点赞图标时，会触发ArticleCardChangeChild组件的handleLiked函数。该函数修改第1个卡片对应组件里ArticleChangeChild实例的isLiked和likesCount属性值。
2. ArticleChangeChild实例是@ObjectLink装饰的状态变量，其属性值变化，会触发ArticleCardChangeChild组件渲染，此时读取的isLiked和likesCount为修改后的新值。

### 拖拽排序

在List组件下使用ForEach，并设置[onMove](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting#onmove)事件，每次迭代生成一个ListItem时，可以使能拖拽排序。拖拽排序离手后，如果组件位置发生变化，将触发onMove事件，上报组件移动原始索引号和目标索引号。在onMove事件中，需要根据上报的起始索引号和目标索引号修改数据源。数据源修改前后，要保持每个数据的键值不变，只是顺序发生变化，才能保证落位动画正常执行。

```typescript
@Entry
@Component
struct ForEachSort {
  @State arr: Array<string> = [];

  build() {
    Column() {

      Button('Add one item')
        .onClick(() => {
          this.arr.push('10');
        })
        .width(300)
        .margin(10)

      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Text(item.toString())
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .size({ height: 100, width: '100%' })
          }.margin(10)
          .borderRadius(10)
          .backgroundColor('#FFFFFFFF')
        }, (item: string) => item)
          .onMove((from: number, to: number) => {

            let tmp = this.arr.splice(from, 1);
            this.arr.splice(to, 0, tmp[0]);
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FFDCDCDC')
    }
  }

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.arr.push(i.toString());
    }
  }
}
```

**图8** ForEach拖拽排序效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/U7cecdcyRdaq2fmVSAHJBg/zh-cn_image_0000002565210053.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=158C47C80FB14B8B7A5EDC5C464BAF54A4D776AD9B0EEF5C6F2B8151729A422D)

注释掉onMove事件调用中的两行代码，点击Add one item触发渲染后的效果如下图所示。

**图9** ForEach拖拽排序效果在重新渲染后没有保留

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qN51TsnKQoChqQGXqKtt-g/zh-cn_image_0000002534250230.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=EA852C44439D5CFD71D7A298AD3D1FA914A0706A24BFB6E43CF9CBF25FBB3119)

## 使用建议

- 为满足键值的唯一性，对于对象数据类型，建议使用对象数据中的唯一id作为键值。
- 不建议在键值中包含数据项索引index，可能会导致[渲染结果非预期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染结果非预期)和[渲染性能降低](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染性能降低)。如果确实需要使用index，例如列表通过index进行条件渲染，开发者需接受ForEach在数据源变更后重新创建组件导致的性能损耗。
- 基本类型数组的数据项没有唯一ID属性。如果使用数据项作为键值，必须确保数据项无重复。对于数据源会变化的场景，建议将基本类型数组转换为具有唯一ID属性的Object类型数组，再使用唯一ID属性作为键值。
- 对于以上限制规则，index参数存在的意义为：index是开发者保证键值唯一性的最终手段；对数据项进行修改时，由于itemGenerator中的item参数是不可修改的，所以须用index索引值对数据源进行修改，进而触发UI重新渲染。
- ForEach在滚动容器组件 [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)以及[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow) 内使用的时候，不建议与[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) 同时使用。
- 在大量子组件的场景下，ForEach可能会导致卡顿。请考虑使用[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)替代。最佳实践请参考[使用懒加载优化性能](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lazyforeach-optimization)。
- 当数组项为对象类型时，不建议用内容相同的数组项替换旧项。若数组项发生变更但键值未变，会导致[数据变化不渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#数据变化不渲染)。

## 常见问题

对ForEach键值的错误使用会导致功能和性能问题。详见案例[渲染结果非预期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染结果非预期)和[渲染性能降低](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染性能降低)。

### 渲染结果非预期

在本示例中，通过设置ForEach的第三个参数KeyGenerator函数，自定义键值生成规则为数据源的索引index的字符串类型值。当点击父组件ForEachAbnormal中“Insert Item After First Item”文本组件后，界面会出现非预期的结果。

```typescript
@Entry
@Component
struct ForEachAbnormal {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Column() {
      Button() {
        Text('Insert Item After First Item').fontSize(30)
      }
      .onClick(() => {
        this.simpleList.splice(1, 0, 'new item');
      })

      ForEach(this.simpleList, (item: string) => {
        ForEachAbnormalChildItem({ item: item })
      }, (item: string, index: number) => index.toString())
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ForEachAbnormalChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(30)
  }
}
```

上述代码的初始渲染效果和点击“在第1项后插入新项”文本组件后的渲染效果如下图所示。

**图10** 渲染结果非预期运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/kqG37bMhQ1Cn9LLusEXznw/zh-cn_image_0000002534410176.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=45026D9FA2E6A2F99C7611BE3D2EB7C6FB19CD443B64277F7C91D8B320C031A4)

ForEach在首次渲染时，创建的键值依次为"0"、"1"、"2"。

插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。

ForEach依次遍历新数据源，遍历数据项"one"时生成键值"0"，存在相同键值，因此不创建新组件。继续遍历数据项"new item"时生成键值"1"，存在相同键值，因此不创建新组件。继续遍历数据项"two"生成键值"2"，存在相同键值，因此不创建新组件。最后遍历数据项"three"时生成键值"3"，不存在相同键值，创建内容为"three"的新组件并渲染。

从以上可以看出，当键值包含数据项索引index时，期望的界面渲染结果为['one', 'new item', 'two', 'three']，而实际的渲染结果为['one', 'two', 'three', 'three']，不符合开发者预期。因此，开发者在使用ForEach时应避免键值包含索引index。

### 渲染性能降低

在本示例中，ForEach的第三个参数KeyGenerator函数缺省。根据上述[键值生成规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#键值生成规则)，此例使用框架默认的键值，即最终键值为字符串index + '__' + JSON.stringify(item)。点击文本组件“在第1项后插入新项”后，ForEach将为第2个数组项及后面的所有数据项重新创建组件。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const TAG = '[Sample_RenderingControl]';
const DOMAIN = 0xF811;

@Entry
@Component
struct ReducedRenderingPerformance {
  @State simpleList: Array<string> = ['one', 'two', 'three'];

  build() {
    Column() {
      Button() {
        Text('Insert Item After First Item').fontSize(30)
      }
      .onClick(() => {
        this.simpleList.splice(1, 0, 'new item');
        hilog.info(DOMAIN, 'testTag', '[onClick]: simpleList is [${this.simpleList.join(', ')}]');
      })

      ForEach(this.simpleList, (item: string) => {
        ReducedChildItem({ item: item })
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct ReducedChildItem {
  @Prop item: string;

  aboutToAppear() {
    hilog.info(DOMAIN, TAG, '[aboutToAppear]: item is ${this.item}');
  }

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

以上代码的初始渲染效果和点击"Insert Item After First Item"文本组件后的渲染效果如下图所示。

**图11** 渲染性能降低案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/pUO5hJhhRj67VUaUwkGzuA/zh-cn_image_0000002565290075.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=69D4E9877ACC2CFC20E13786E1C644B34C25171E7ECE6C5072E885D31BB48158)

点击“Insert Item After First Item”文本组件后，DevEco Studio的日志打印结果如下所示。

**图12** 渲染性能降低案例日志打印图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/-7p7-hzOQqKdmruxe7wSLA/zh-cn_image_0000002565210055.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=46A34CF67D5832D95C3920FCDF5E76900ED0FF41BC341C577270759980F4A784)

插入新项后，ForEach为new item、 two、 three三个数组项创建了对应的ReducedChildItem组件，并执行了组件的[aboutToAppear()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear)生命周期函数。这是因为：

1. ForEach首次渲染时，生成的键值依次为0__one、1__two和2__three。
2. 插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，ArkUI框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。
3. ForEach依次遍历新数据源，遍历数据项one时生成键值0__one，键值已存在，因此不创建新组件。继续遍历数据项new item时生成键值1__new item，不存在相同键值，创建内容为new item的新组件并渲染。继续遍历数据项two生成键值2__two，不存在相同键值，创建内容为two的新组件并渲染。最后遍历数据项three时生成键值3__three，不存在相同键值，创建内容为three的新组件并渲染。

尽管本例中界面渲染结果符合预期，但在每次向数组中间插入新数组项时，ForEach会为该数组项及其后面的所有数组项重新创建组件。当数据源数据量较大或组件结构复杂时，组件无法复用会导致性能下降。因此，不建议省略第三个参数KeyGenerator函数，也不建议在键值中使用数据项索引index。

正确渲染并保证效率的ForEach写法是：

```typescript
ForEach(this.simpleList, (item: string) => {
  ForEachChildItem({ item: item })
}, (item: string) => item)
```

提供了第三个参数KeyGenerator，在这个例子中，对数据源的不同数据项生成不同的key，并且对同一个数据项每次生成相同的key。

### 数据变化不渲染

点击按钮Like/UnLike first article，第一个组件会切换点赞手势和后面的点赞数量，但是点击按钮Replace first article之后再点击按钮Like/UnLike first article就不生效了。原因是替换articleList[0]之后，articleList状态变量发生变化，触发ForEach重新渲染，但是新的articleList[0]生成的key没有变，ForEach不会将数据更新同步给子组件，因此第一个组件仍然绑定旧的articleList[0]。新articleList[0]的属性发生变更，第一个组件感知不到，不会重新渲染。点击点赞手势，会触发渲染。因为变更的是跟组件绑定的数组项的属性，组件会感知并重新渲染。

```typescript
@Observed
class ArticleChangeData {
  public id: string;
  public title: string;
  public brief: string;
  public isLiked: boolean;
  public likesCount: number;

  constructor(id: string, title: string, brief: string, isLiked: boolean, likesCount: number) {
    this.id = id;
    this.title = title;
    this.brief = brief;
    this.isLiked = isLiked;
    this.likesCount = likesCount;
  }
}

@Entry
@Component
struct ArticleListChangeData {
  @State articleList: Array<ArticleChangeData> = [
    new ArticleChangeData('001', 'Article 0', 'Abstract', false, 100),
    new ArticleChangeData('002', 'Article 1', 'Abstract', false, 100),
    new ArticleChangeData('003', 'Article 2', 'Abstract', false, 100),
    new ArticleChangeData('004', 'Article 4', 'Abstract', false, 100),
    new ArticleChangeData('005', 'Article 5', 'Abstract', false, 100),
    new ArticleChangeData('006', 'Article 6', 'Abstract', false, 100),
  ];

  build() {
    Column() {
      Button('Replace first article')
        .onClick(() => {
          this.articleList[0] = new ArticleChangeData('001', 'Article 0', 'Abstract', false, 100);
        })
        .width(300)
        .margin(10)

      Button('Like/Unlike first article')
        .onClick(() => {
          this.articleList[0].isLiked = !this.articleList[0].isLiked;
          this.articleList[0].likesCount =
            this.articleList[0].isLiked ? this.articleList[0].likesCount + 1 : this.articleList[0].likesCount - 1;
        })
        .width(300)
        .margin(10)

      List() {
        ForEach(this.articleList, (item: ArticleChangeData) => {
          ListItem() {
            ArticleCardChangeData({
              article: item
            })
              .margin({ top: 20 })
          }
        }, (item: ArticleChangeData) => item.id)
      }
      .padding(20)
      .scrollBar(BarState.Off)
      .backgroundColor(0xF1F3F5)
    }
  }
}

@Component
struct ArticleCardChangeData {
  @ObjectLink article: ArticleChangeData;

  handleLiked() {
    this.article.isLiked = !this.article.isLiked;
    this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
  }

  build() {
    Row() {

      Image($r('app.media.startIcon'))
        .width(80)
        .height(80)
        .margin({ right: 20 })

      Column() {
        Text(this.article.title)
          .fontSize(20)
          .margin({ bottom: 8 })
        Text(this.article.brief)
          .fontSize(16)
          .fontColor(Color.Gray)
          .margin({ bottom: 8 })

        Row() {

          Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
            .width(24)
            .height(24)
            .margin({ right: 8 })
          Text(this.article.likesCount.toString())
            .fontSize(16)
        }
        .onClick(() => this.handleLiked())
        .justifyContent(FlexAlign.Center)
      }
      .alignItems(HorizontalAlign.Start)
      .width('80%')
      .height('100%')
    }
    .padding(20)
    .borderRadius(12)
    .backgroundColor('#FFECECEC')
    .height(120)
    .width('100%')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

**图13** 数据变化不渲染

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/fZNm6jvpQ6CP8-aOSGOwKg/zh-cn_image_0000002534250232.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=8953C2DA9B9FA83CB89AD1C0D467377849F96F2DCAADFBE536917646C3B58AF9)

### 非必要内存消耗

如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '__' + JSON.stringify(item); }。当item是复杂对象时，将其JSON序列化会得到长字符串，占用更多的内存。

```typescript
class MemoryData {
  public longStr: string;
  public key: string;

  constructor(longStr: string, key: string) {
    this.longStr = longStr;
    this.key = key;
  }
}

@Entry
@Component
struct NonNecessaryMemory {
  @State simpleList: Array<MemoryData> = [];

  aboutToAppear(): void {
    let longStr = '';
    for (let i = 0; i < 2000; i++) {
      longStr += i.toString();
    }
    for (let index = 0; index < 3000; index++) {
      let data: MemoryData = new MemoryData(longStr, 'a' + index.toString());
      this.simpleList.push(data);
    }
  }

  build() {
    List() {
      ForEach(this.simpleList, (item: MemoryData) => {
        ListItem() {
          Text(item.key)
        }
      }

        , (item: MemoryData) => {
          return item.key;
        }
      )
    }.height('100%')
    .width('100%')
  }
}
```

对比自定义keyGenerator函数和使用默认键值生成函数两种情况下的内存占用（通过DevEco->Profiler->Realtime Monitor工具，可以获取相关进程的内存数据）。自定义keyGenerator函数，这个示例代码的内存占用降低了约70MB。

**图14** 使用默认键值生成函数下的内存占用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/RVTS4XHvTK6YvPquS7gwfA/zh-cn_image_0000002534410178.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=D66CA8302E5F4F1B12FF55528693DB03BB91EFDCFB5AFD284C884BDC47E7F39E)

**图15** 自定义键值生成函数下的内存占用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oZszEavbQD6kUFAvMz15Og/zh-cn_image_0000002565290077.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=917C1456581D8AA5CE2C21300B0781ED9D0EC8ADCDD1BAB819AAC910F5CEF817)

### 键值生成失败

如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '__' + JSON.stringify(item); }。然而，JSON.stringify序列化在某些数据结构上会失败，导致应用发生jscrash并退出。例如，bigint无法被JSON.stringify序列化：

```typescript
class KeyData {
  public content: bigint;

  constructor(content: bigint) {
    this.content = content;
  }
}

@Entry
@Component
struct GenerationKeyExample {
  @State simpleList: Array<KeyData> = [new KeyData(1234567890123456789n), new KeyData(2345678910987654321n)];

  build() {
    Row() {
      Column() {
        ForEach(this.simpleList, (item: KeyData) => {
          GenerationKeyChildItem({ item: item.content.toString() })
        }

          , (item: KeyData) => item.content.toString()
        )
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .backgroundColor(0xF1F3F5)
  }
}

@Component
struct GenerationKeyChildItem {
  @Prop item: string;

  build() {
    Text(this.item)
      .fontSize(50)
  }
}
```

开发者定义keyGenerator函数，应用正常启动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Z8_ShCGlTZGAZngIpvjN6g/zh-cn_image_0000002565210057.png?HW-CC-KV=V1&HW-CC-Date=20260402T023618Z&HW-CC-Expire=86400&HW-CC-Sign=D75F7413A7FA041D3BA77D7F4943F1F9023E3433CA7484CBF5CF25D937B81A08)

使用默认的键值生成函数，应用发生jscrash：

```typescript
Error message:@Component 'Parent'[4]: ForEach id 7: use of default id generator function not possible on provided data structure. Need to specify id generator function (ForEach 3rd parameter). Application Error!
Stacktrace:
    ...
    at anonymous (entry/src/main/ets/pages/Index.ets:18:52)
```
