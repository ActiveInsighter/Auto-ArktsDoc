# 子组件
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme

WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色。

> **说明**
> 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
> WithTheme支持的系统组件如下：
> TextInput
> 、
> Search
> 、
> Button
> 、
> Badge
> 、
> Swiper
> 、
> Text
> 、
> Select
> 、
> Menu
> 、
> TimePicker
> 、
> DatePicker
> 、
> TextPicker
> 、
> Checkbox
> 、
> CheckboxGroup
> 、
> Radio
> 、
> Slider
> 、
> Progress
> 、
> QRCode
> 、
> Toggle
> 、
> PatternLock
> 、
> Divider
> WithTheme相关使用指导请参考
> 设置应用内主题换肤
> 。

## 子组件

支持单个子组件。

## 接口

WithTheme(options: WithThemeOptions)

设置应用局部页面自定义主题风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WithThemeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme#withthemeoptions) | 是 | 设置作用域内组件配色。 |

## 属性

不支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

## 事件

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## WithThemeOptions

设置WithTheme作用域内组件缺省样式及深浅色模式。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| theme | [CustomTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme#customtheme) | 否 | 是 | 用于自定义WithTheme作用域内组件缺省配色。 默认值：undefined，缺省样式跟随系统[token默认样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning#系统缺省token色值)。 |
| colorMode | [ThemeColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-blur-style#themecolormode枚举说明) | 否 | 是 | 用于指定WithTheme作用域内组件配色深浅色模式。 默认值：ThemeColorMode.SYSTEM |

## CustomTheme

type CustomTheme = CustomTheme

自定义配色。

| 类型 | 说明 |
| --- | --- |
| [CustomTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme#customtheme) | 自定义WithTheme作用域内组件缺省配色。 |

## 示例

设置局部深浅色时，需要添加dark.json资源文件，深浅色模式才会生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Z6V25GU5T36eXJj94WO_AQ/zh-cn_image_0000002562026225.png?HW-CC-KV=V1&HW-CC-Date=20260320T122341Z&HW-CC-Expire=86400&HW-CC-Sign=2061402A09214E44152E27DD3FDAF0041F96A94440449AB27006E3531D1D4D5D)

dark.json数据示例：

```typescript
  {
    "color": [
      {
        "name": "start_window_background",
        "value": "#000000"
      }
    ]
  }
```

### 示例1（指定局部深浅色模式）

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {

      Column() {
        Text('无WithTheme')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('33%')
      .backgroundColor($r('app.color.start_window_background'))

      WithTheme({ colorMode: ThemeColorMode.DARK }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('DARK')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }

      WithTheme({ colorMode: ThemeColorMode.LIGHT }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('LIGHT')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }
    }
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START])
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/KdAsAE4BSGSRwHsr6XPM8A/zh-cn_image_0000002562146211.png?HW-CC-KV=V1&HW-CC-Date=20260320T122341Z&HW-CC-Expire=86400&HW-CC-Sign=2BF647A08173ED110697467FF5D7C9E38D94CE85A895F8E26CC003FC44293AB0)

### 示例2（自定义WithTheme作用域内组件缺省配色）

```typescript
import { CustomTheme, CustomColors } from '@kit.ArkUI';

class GreenColors implements CustomColors {
  fontPrimary = '#ff049404';
  fontEmphasize = '#FF00541F';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#1111FF11';
  backgroundEmphasize = '#FF00541F';
  compEmphasizeSecondary = '#3322FF22';
}

class RedColors implements CustomColors {
  fontPrimary = '#fff32b3c';
  fontEmphasize = '#FFD53032';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#44FF2222';
  backgroundEmphasize = '#FFD00000';
  compEmphasizeSecondary = '#33FF1111';
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors

  constructor(colors: CustomColors) {
    this.colors = colors
  }
}

@Entry
@Component
struct IndexPage {
  static readonly themeCount = 3;
  themeNames: string[] = ['System', 'Custom (green)', 'Custom (red)'];
  themeArray: (CustomTheme | undefined)[] = [
    undefined,
    new PageCustomTheme(new GreenColors()),
    new PageCustomTheme(new RedColors())
  ]
  @State themeIndex: number = 0;

  build() {
    Column() {
      Column({ space: '8vp' }) {
        Text(`未使用WithTheme`)

        Button(`切换theme配色：${this.themeNames[this.themeIndex]}`)
          .onClick(() => {
            this.themeIndex = (this.themeIndex + 1) % IndexPage.themeCount;
          })

        Button('Button.style(NORMAL) with System Theme')
          .buttonStyle(ButtonStyleMode.NORMAL)
        Button('Button.style(EMP..ED) with System Theme')
          .buttonStyle(ButtonStyleMode.EMPHASIZED)
        Button('Button.style(TEXTUAL) with System Theme')
          .buttonStyle(ButtonStyleMode.TEXTUAL)
      }
      .margin({
        top: '50vp'
      })

      WithTheme({ theme: this.themeArray[this.themeIndex] }) {

        Column({ space: '8vp' }) {
          Text(`使用WithTheme`)
          Button('Button.style(NORMAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.NORMAL)
          Button('Button.style(EMP..ED) with Custom Theme')
            .buttonStyle(ButtonStyleMode.EMPHASIZED)
          Button('Button.style(TEXTUAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.TEXTUAL)
        }
        .width('100%')
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/wPifUQObR9W3dC35SR_F2A/zh-cn_image_0000002531106310.gif?HW-CC-KV=V1&HW-CC-Date=20260320T122341Z&HW-CC-Expire=86400&HW-CC-Sign=37F01281B6A5C177B8C7A430679F630C988B06C55835343FF63E7039562600D7)
