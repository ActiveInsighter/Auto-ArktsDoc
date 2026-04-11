# SVG标签解析能力增强
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities

从API version 21开始，当Image组件的[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)属性设置为true时，将启用SVG标签解析能力增强功能，该增强功能主要包含SVG1.1规范中的以下功能。

- 易用性提升：SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用的URL类型进行严格校验；Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性对整个SVG图源生效；Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性不对SVG图源中fill = 'none'的元素填充颜色。
- 仿射变换能力扩展：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。
- 解析能力扩展：[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。
- 显示效果扩展：分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。

## SVG标签解析能力增强对SVG图源标签和属性的影响

启用增强的解析处理能力后，影响的SVG元素和属性说明如下：

| 元素 | 属性 | 说明 |
| --- | --- | --- |
| clipPath | clipPathUnits | clipPathUnits裁剪路径单元，指定裁剪路径的坐标系统基准。 clipPathUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| filter | filterUnits primitiveUnits x y width height | filterUnits滤镜单元，定义滤镜效果（如模糊、阴影）的坐标和尺寸基准。 primitiveUnits滤镜原语单元，定义滤镜内元素效果的坐标和尺寸基准。 filterUnits和primitiveUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 x：滤镜区域x轴偏移分量，默认值：-10% y：滤镜区域y轴偏移分量，默认值：-10% width：滤镜区域宽，默认值：120% height：滤镜区域高，默认值：120% |
| mask | maskUnits maskContentUnits x y width height | maskUnits遮罩单元，控制遮罩的坐标系统和内容渲染方式。 maskContentUnits遮罩内容单元，控制遮罩内元素的坐标系统和内容渲染方式。 maskUnits和maskContentUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 x：遮罩区域x轴偏移分量，默认值：-10% y：遮罩区域y轴偏移分量，默认值：-10% width：遮罩区域宽，默认值：120% height：遮罩区域高，默认值：120% |
| radialGradient | gradientUnits | gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。 gradientUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| linearGradient | gradientUnits | gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。 gradientUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| pattern | patternUnits patternContentUnits | patternUnits图案单元，控制图案整体（<pattern>）的坐标系和内容缩放。 patternContentUnits图案内容单元，控制图案内部元素的坐标系和内容缩放。 patternUnits和patternContentUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| g | opacity clip-path | opacity透明度：对整个分组下的多层子元素生效。 clip-path裁剪路径：对整个分组下的多层子元素生效。 |
| 通用 | transform | 用于对SVG元素进行2D变换（如平移、旋转、缩放、倾斜等）。 translate(x, y)‌：沿X/Y轴平移元素。 ‌ rotate(angle, [cx], [cy])‌：旋转元素（可选参数指定旋转中心）。 ‌scale(sx, [sy])‌：缩放元素（单参数时X/Y轴等比缩放）。 ‌skewX(angle)/skewY(angle)‌：沿X/Y轴倾斜元素。 ‌ matrix(a, b, c, d, e, f)‌：通过矩阵定义复杂变换。 |
| 通用 | transform-origin | 用于定义变换的基准点。需和[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性配合使用。 当配置transform-origin时，按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。 |

## SVG易用性提升

SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用国际化资源标识（IRI）类型严格校验；调整Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性生效范围；调整Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性生效范围。

### 颜色解析格式变更

当Image组件的SVG图源使用十六进制格式的颜色时，颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA，涉及的SVG属性包括fill、stroke、stopColor、stop-color。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview#objectfit)参数。

SVG图源属性设置8位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#ff000030" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WA7BldDTRwuWwnQ9o5fsyQ/zh-cn_image_0000002569169621.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=09259D39BBA4254976B7953197E735648139F9A2CCD4CB531DE2B49259D44FA8) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/wFu60U6ERS2FRYi_y7QsXA/zh-cn_image_0000002569129647.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=75852BD6DEABD08C6758A75FA1714F5CFB2EEC0756347ACFEB14C8E91A548461) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/P4GVjIWnRXO14JStSX2TGg/zh-cn_image_0000002538129926.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=58AE6A6DB04DADE8E801096434A04B085D50AE17E6CB2551CBF0D2E946C8668D) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/gC3OsaDDTuaHk3Y_xXuovA/zh-cn_image_0000002538289860.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=024E84397688D33ED2C2C8B63ABEB12A885EE24369790DF1CEB8897A96EB0606) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qU6EAAysR0yO2ruP3swxcw/zh-cn_image_0000002569169623.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=CF7773915E71A768A65F9326C7F11B8748C6C6896F64E5D9543BD79D6BA87663) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/knsxJXv0RvGyGD_nwLgvIw/zh-cn_image_0000002569129649.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=EC69F5F8A61A1EA583E5C04D5294A324FF55F0247749D86256D7CB15C44860F5) |

### 引用国际化资源标识（IRI）类型严格校验

严格校验filter滤镜/clip-path裁剪路径/mask遮罩引用的URL类型，避免引用类型不匹配。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| --- | --- |
| 滤镜/裁剪路径/遮罩引用的URL类型不匹配，导致错误的显示效果。 | 滤镜/裁剪路径/遮罩引用的URL类型不匹配时，不显示对应效果。 例如，mask、clippath、filter、pattern、渐变等标签都有各自的id，filter、clip-path和mask属性绑定其它类型的标签id时，对应效果不生效。只有mask属性绑定mask标签id、clip-path属性绑定clipPath标签id和filter属性绑定filter标签id时，对应效果才生效。 |

当URL类型不匹配时，遮罩效果不生效，示例图源如下：

```typescript
<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="myClipPath">
      <circle cx="50" cy="50" r="40"/>
    </clipPath>
    <mask id="myMask">
      <rect x="0" y="0" width="100" height="100" fill="red"/>
    </mask>
  </defs>

  <rect x="10" y="10" width="180" height="80" fill="blue" mask="url(#myClipPath)"/>
</svg>
```

### 调整colorFilter生效范围

Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性从只对stroke边框生效调整为对整个SVG图源生效。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 原始图源 | 提升前 | 提升后 |
| --- | --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/V912thuQTum9vNXWNnSoMA/zh-cn_image_0000002538129928.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=3FA3491A5B41B5438430FB1FF29D0BD8A616E48AEA33DA6608288EAA1F2F9EF8) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wPtQWSAZTVWEbuxsslmESA/zh-cn_image_0000002538289862.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=9BD0F49FCFD547B9202BE6A468A9BF528184FD87AF28289CC9E6A932CCE5632E) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/7KZrugncQfO9vq8XE3EsCg/zh-cn_image_0000002569169625.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=FE7D5B908C07C0130B3603D304CD0A0CB909554C3441836A9FF25FE0F4362544) |

示例图源和示例代码如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

    <rect x="10" y="10" width="180" height="80" stroke="gray" stroke-width='16' fill="orange"/>
</svg>
```

```typescript
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image111.svg'))
          .width(220)
          .height(220)
          .colorFilter(
            [ 0.6, 0,   0,   0, 0,
              0.2, 0.8, 0,   0, 0,
              0.2, 0.2, 1.2, 0, 0,
              0,   0,   0,   1, 0 ]
          )
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### 调整fillColor生效范围

当SVG图源中元素的fill属性为none时，Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性从填充颜色变更为不填充颜色。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| --- | --- |
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/DEkQvnCPSmmmDg-VgJ0bEA/zh-cn_image_0000002569129651.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=BA6FB83432ACEA32F3B5A34EC7D5E7A56659201AAD1F156AB69C0C1488F34078) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/P5Vw43eIRmSor8l5UxsgOQ/zh-cn_image_0000002538129930.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=E76D9DEB8D05756B005E59551A39DD58C393770218AA45E7DF6AD6D644AED47F) |

示例图源和示例代码如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="180" height="80" fill="none"/>
</svg>
```

```typescript
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image11.svg'))
          .width(220)
          .height(220)
          .fillColor('blue')
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 仿射变换能力扩展

对于[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。

### 支持变换全局中心点配置

SVG支持解析[transform-origin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation)属性来配置全局中心点的能力，前后效果对比如下表格说明：

> **说明**
> SVG图片最终显示效果受Image组件的'[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形配置变换功能和transform-origin属性。 | 固定按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点进行仿射变换。 | 按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。 |
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Se0xlVHrTt2rJ3-M1Pi8Sw/zh-cn_image_0000002538289864.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=CD735957BC72EBFF4805EEE721BEAF422CA355DF7008CD8D413B8814EE04A86B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/rXtEWpWeSYi8JG0zqmwTtA/zh-cn_image_0000002569169627.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=757EAF3D7919F01BCBCD4CF9CC88FC25D63348B3ABF6BD42007827130F9EBE0E) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/odjX-RCiQRuASYHrtYuqOg/zh-cn_image_0000002569129653.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B5A6147A11E7A77F84112190ABA4E5CF5A9C33FCA626E7B65F27824C0D76D084) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Xab1F-pCSZCwcJqy1bcXxg/zh-cn_image_0000002538129932.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=DB693C49BBB5CD38A36E90CF356AA7C85C92C94F2AD01F88573337E210EAC427) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/1FNPcjpHQqmeXjsR6WJQ2w/zh-cn_image_0000002538289866.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=BB9DFC189F4EE17CCE705F65FCE79F731CC7EAB71075A22133551582313A00B1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/a5z8lWXNRZiUMLhh-XkFyw/zh-cn_image_0000002569169629.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A8C0267859803F0555D304ACDD8AEE019B290D4D0AC74639D7623CCAE1D46C02) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k2hVM9xlS4ieoHHRArSnsQ/zh-cn_image_0000002569129655.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=F73714948B7C59E92728A9D3BBFB55D8EB74400B162DDDF4B9F51443623953AC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/pAGp6Z0TRxCGRI0Q29dqjw/zh-cn_image_0000002538129934.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=8D2880E47C0CD1474299B38392276589A60654EAF0FB4950AC56172F2484307A) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ITUKINqtQF6ErPcmI5tnEA/zh-cn_image_0000002538289868.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=1BC969515AA99EBE5BAD0B0305672157EF254AFA4E3441971D257E178CAB859E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/H-8zfDGJTjefOEwUb3uZXQ/zh-cn_image_0000002569169631.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=30CE9D0F3709DBF7B2C57FCD2756586628BD6530D5DED513D8785382FF51238D) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UopHQIonTeyIzZTWkfM0hg/zh-cn_image_0000002569129657.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B8B5E16B49AEE5410785A2FEE1B1BC3B478E22551FF3ADFF049DC7E556A0843F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/drWaBlTORdelcn7A719SAg/zh-cn_image_0000002538129936.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=6A1C4AFA5D4090000C802839CAB4E5A2AA590A709B14F18A449A40B090F96241) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/iggABZlxSvyPgXH5mYe3Pw/zh-cn_image_0000002538289870.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=748E2AD54A16B8ED853B3D0156530FF48D8656EA506168556700492D317A9323) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cJh7ILdmQgy3oHSUFSsIRw/zh-cn_image_0000002569169633.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=1303EC401D7F1A8CD515474160B88B7868CD443C6C05D03765BD04DFA2B88FBD) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wxneaY78SmmvUVJ2vWxOEg/zh-cn_image_0000002569129659.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=91F1FD33F253FB105A6EE4B640C3C90976E5D113F0E3C98957584FAD3E2FA7A7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/kCZHi5JYR4WQmKg7V1zIjA/zh-cn_image_0000002538129938.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=5EDB55C1DB838F545F2B7CD242D62AE479402B0A90E7CCBD4F0947222DDAB538) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9N3l79yIQgalCLg-XdTHww/zh-cn_image_0000002538289872.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=C5BF158B48D999055FB3275B5626C72E533B2F8CFCCC745835544B3634CD5D6D) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/PlUCN6qCSy6wEi4AQhpDwg/zh-cn_image_0000002569169635.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B4388769F1FD831FCFDCA4D5273E5BFE6013E5CFEFE32181874D41B171891925) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/5I7MHlVgTNOTYZRQl7M2-g/zh-cn_image_0000002569129661.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=2111A3E578F048BD9026B0B1DF4E01C7B75C83BF2FBE1084C3DF55B9108DFB65) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iSCpOMtHSpuAEyWVH104mQ/zh-cn_image_0000002538129940.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=EF553B3F2003DE7FB571CF37A3499F551AF119276AB65A4D40A92A0D7CBBBDAC) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Ctz23_WpSPqJzHrncUpsQg/zh-cn_image_0000002538289874.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=5A7081F6847C1AB35068D7C1ED8C832BE50B85909B4F8751F5C68DECA57A74EA) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NozJl6fnSfGca5qMmTUByQ/zh-cn_image_0000002569169637.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=AC33E8F14B92F8A5838092FB40248712447EC06719D8DA87D9FFD8E798D1F2EF) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/RxHI0F3vRYGRSjIYjGCS2A/zh-cn_image_0000002569129663.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=6939F17E517EEA0FBC172AADBF76312E0194AFF5FA9D82CA4AF3F8AE63E68F90) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/otcgLRW3RgqHN-ARwHruLw/zh-cn_image_0000002538129942.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=8D439A13CBDF6146B1A7B80264DD9DAE0E87F000025A3E00FC0E6A3352B0816B) |

### 裁剪路径内支持仿射变换操作

支持clip-path裁剪路径内的transform仿射变换操作。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="circleClip" clipPathUnits="objectBoundingBox">

      <circle cx="50" cy="50" r="40" transform="translate(50 50)" />
    </clipPath>
  </defs>

  <rect x="10" y="10" width="250" height="250" fill="blue"
        clip-path="url(#circleClip)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/3lWak_ZQTb62WrcBY3jVpA/zh-cn_image_0000002538289876.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A5793FCE361AAEEFAE787594903E7C31FE49FDEEA4470D1727BD02C514B6A3FD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/K4Kp3cPsQ-m3aDtPTGV8fQ/zh-cn_image_0000002569169639.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=3D52DB6B8A2D37FF568DAF402E3E53263B65B16377238D2141ACA1531BEF8710) |

### 组合场景支持仿射变换操作

支持多种元素组合场景的仿射变换操作。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

transform操作在use中，use对象也在相同的mask元素内。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
      <use xlink:href="#rect1" transform="translate(0.6, 0.000000) scale(0.5 0.5)" />
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5" fill="red"  />
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/MhqRW4hPQRqxYBDiQIU58Q/zh-cn_image_0000002569129665.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B4975F5C99421B9AA29D791E9399A93425A13BD1A0B316FB5E557AAC9D681FF8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/fIRb1xZ3QEixJ-Pvmerc9Q/zh-cn_image_0000002538129944.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=2EEB3B01C07329ABFCDE4915280175337C8CED5981E509D868F2BC8C3988A510) |

transform操作在g标签中，且不包含scale操作。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
        <g transform="translate(0.6, 0.000000)">
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5"  fill="red"  />
      </g>
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JAZ-SguVQiitfbF7sL8hEA/zh-cn_image_0000002538289878.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=6483C3B7ECA98C15BBCEFCEECE704E96B33615EEB16041C68118741C99AC0707) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/rPpylfC_SUyW7Z-cPQPDNQ/zh-cn_image_0000002569169641.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=1A2CD6BDD26FA7A7E5CC5808514D4D649FD1B11FBA94EC39004AD910B594FC4F) |

## SVG解析能力扩展

[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。

### viewBox属性支持对齐和缩放规则可配置

viewBox主要用来控制在SVG动态拉伸效果，可以通过参数preserveAspectRatio来控制内容区显示的对齐和缩放规则。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

SVG包含“preserveAspectRatio”属性且值为“none”，示例图源和行为变更如下：

```typescript
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" />
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" />
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| --- | --- | --- |
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/C1SlGxBVTKqErf7ytRHrkw/zh-cn_image_0000002569129667.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=6B5B7C59902C75ADCCDB2E876EFC0717F723CFED0D4D3B5B4DE74E28FC15968F) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/l28bICioQNCGGdZxnD6_6g/zh-cn_image_0000002538129946.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A6029F3AD80DE60B574D1F40D4E914E49EABB31AA0F2B37DF65D5EAF2ECE8AC0) |

SVG包含“preserveAspectRatio”属性且值为“<align> [<meetOrSlice>]”，示例图源和对齐方式、缩放比例变更如下：

```typescript
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="xMinYMin meet" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" />
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" />
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| --- | --- | --- |
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/5HZVY3vkQlWdihTUYZSkFw/zh-cn_image_0000002538289880.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A24A71686528C85CB1869648020DF50AAC82B1312AB81D47368AB2FA0B417B12) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pS6YKmB4Qe-8ebwVPI_Mjw/zh-cn_image_0000002569169643.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=258350B3AB643FA178CF563C745C13AE567F6800A437795D2F9AC7308F53CBD6) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/I8DEpRaTSrGurQYY_iLGlQ/zh-cn_image_0000002569129669.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=304F85620C1B3EFDA1E1572788BEE10251BD97A5C0FE0E1781CE582B1BB165B5) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/_ScuHyYkSmeRTVayw4WGfg/zh-cn_image_0000002538129948.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=EEA7A4283FB3A6EBEBE69DF8D83ED21A1EFF4DA08DEADAC20D93F3A4256DAB22) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/CjRH8FUGQTWhCNQXg8_xHw/zh-cn_image_0000002538289882.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=8B6702BFEE9B6230D660C723B7DFA8E8DFA9289BA31459B0DE70F9944CAA7EDE) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/wvQj85SDRaadsv9GtszzSw/zh-cn_image_0000002569169645.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=F15117765273EC13C94BEC568DE6F97603E59E5504851DABDA0212D1FC4566AE) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/lo8bjWlwSre2MEbMTk0utA/zh-cn_image_0000002569129671.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=0966C6E30A4201B17A23206BB9F8387AFEA1ADD5A0B58F3065485A6862E659CB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bkLV89w3RHKjnTMZMd_98A/zh-cn_image_0000002538129950.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=5BD5CACFB6F8E77D9959B6C99A8A261F8BC7C6521D830924A31903E299AD305D) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/dICKzYPtTbOrBQou7ZpxIQ/zh-cn_image_0000002538289884.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=0EBC775BEBD04FE4D00C729DEF9516D74A68A2F487FB286D78C52FFAABFD379E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q8jkDJi7TWepJc-5PayLtw/zh-cn_image_0000002569169647.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=D8BA1A8C33D8FEDB6D3CD09D21F2BE32DAC2989C0CFC8BF1BDFD19EB091D7C29) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zSPPmRjUSJ6U1Qrgh27fBg/zh-cn_image_0000002569129673.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=8A84C498636FE8C285D4A74D803F8EA478A31C77861EBC286BE66B59DCBB24DF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/BU49f7P-SPCrhHCN1gMOnA/zh-cn_image_0000002538129952.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=C77FCC8DFCA8C802093E312654D7D5D167E02C40FC558B9C1D64CE5080F6E4F5) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/hT9i0WLFToq2-_VzSyck-A/zh-cn_image_0000002538289886.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=58C0C39C8313369E9281838B5AF1AA3BD88A5847BC03C4BFC08BBA441D900C46) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/kLFyu2rgSdiz14rPDzJd1g/zh-cn_image_0000002569169649.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=47478EFD4F5ECCE4F0FDA095E566E10699BAFDF7433363B42C403D1488BDF156) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/xtTXzOfsQPS2fizxukD1lg/zh-cn_image_0000002569129675.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=413BF5F2ECCD3C5ABC66F05277C2E02D8063260AD9BF5A5B51300AAE943DC68F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/j8V8pSV2R36EYelSK5HqXg/zh-cn_image_0000002538129954.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=31078BF65E68DF4DFD08AC18FAE0FD1889403A43861BBAF1DCAAC5F5BE579CB3) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/gRdVeSUpRNamya71LIVGgA/zh-cn_image_0000002538289888.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=37AF069C4C530F93140EEF6DA9B071D8D0C39D16FA7B9A75566F4D3E2499FCA5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/SOq7Y8CWQPOH8tmIyqK57Q/zh-cn_image_0000002569169651.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=F05A8DF708F13F4D56DF26F8CF6231E2F25369FD9A2410FB51B23FCBE0C108DB) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/qkASV5rCQ9iWZJF8Ejvcqg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=7B876120FB0DFDF83B9356A1C3A66EFE51C133C618376598BA36AD2F0725FBE2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7R_p7m7uSzKbn8qO0sIKQg/zh-cn_image_0000002538129956.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=32000A57AFD34C1575DFCB8CAC88C631030C989B6C843A268874C10BA69EF9A2) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/MKXf5mg0SDm4dqbk00fXGw/zh-cn_image_0000002538289890.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=F3470C9BBB07D73469D06BF37477AF555F37FFC951954FEAFFDEE83F791DCF36) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XRH3qKHTQqCntguZKTvtlw/zh-cn_image_0000002569169653.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=959D4297BEC9D1D156234863B2EFAFAA31330EC7599887AF7C618A2E1339B52A) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WcIHDSESSuyW8JjU0mXxHg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=7F5A6BACB579E262813AAF0F7F62A0D72012E40021D6BA433BD9EC82CEDA75C3) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/6yjZBXjKT8aih5jG-eF2DQ/zh-cn_image_0000002569129679.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=8E8DD8279298A82658B015079FC03CF7F8284DCDF544F5F151ACC07968720D17) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ow88rYlEQZGWvoVu0E5afA/zh-cn_image_0000002538129958.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=274F927628174A10BBBFF6499BF8A7946267331C479CAA01E504B3449F653EEA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zxYjrsTHQfq50H3CvOvlLQ/zh-cn_image_0000002538289892.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=0304A306BEF512B26F96A7A956B254D9C3991F78AF347740411E443B7E8B172F) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/q0F5Bco5Q0OKTzmRM8YnWQ/zh-cn_image_0000002569169655.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A64A53E202FA0C918F71B663DA610F7E3F629E9C3A1643D0F3A0232AE3BA5543) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Iqj_E5yaTPOPucDVvTe2_g/zh-cn_image_0000002569129681.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=E8126D5063F732DA543AF1E0BC21E64A819DF6F842134D58DC6CA3A9766081D9) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GWplHjzfT3iqyZNtxKb9rQ/zh-cn_image_0000002538129960.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A78183AF5A85C7D73F89EE974FCEA4D171E710BB8C476A8634BEB7FE1F87E52B) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6Nlvc7jPQtOrDVxIpjgyeQ/zh-cn_image_0000002538289894.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=52E568199724BFF0E8115A72EB883A486D7691C335D2175D4C7383C04D5A3FEC) |

### 支持裁剪路径单元的解析

支持裁剪路径单元值[clipPathUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加clipPathUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

下面图源示例当裁剪路径单元为"objectBoundingBox"时，长方形裁剪路径位于应用裁剪路径长方形图形左上角x,y乘以图形包围盒宽度和高度。尺寸为width乘以图形包围盒的宽度，height乘以图形包围盒的高度。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="clip1" clipPathUnits="objectBoundingBox">
      <rect x="0.2" y="0.2" width="0.7" height="0.6" />
    </clipPath>
  </defs>
  <rect x="10" y="10" width="100" height="100" fill="blue" clip-path="url(#clip1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/rqwFtlz9TM2WGVI809ZP7g/zh-cn_image_0000002569169657.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=230994CE35657FA5A5511D853989792619CB503E87DB51543E5EADD5ECCB524E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Mn6lah5gTG-kqrAZqLYZhg/zh-cn_image_0000002569129683.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=3C5D4C112DECD9140299A5C4DA67D77D17E5733C68D829BF442CB4BF4E7462AA) |

### 支持渐变单元的解析

支持渐变单元值[gradientUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加gradientUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个线性渐变从绝对坐标(10，10) 到 (180，180)的长方形范围内。

```typescript
 <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="10" y1="10" x2="180" y2="180"  gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="180" height="180" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zF9vbxIhSi618dQnStAQqA/zh-cn_image_0000002538129962.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=97545623484FD10BA12DF7D6D6C0704C9C0D72C0FC0AFC332AAF23CC01AF7247) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/E4haMeE8RtWuGVYbetJL1A/zh-cn_image_0000002538289896.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=EC80E58D8833DF789FD6E687778C06F5E51A1B4DF6B0E0B5FD4E3EC212C5E23C) |

图源示例显示一个径向渐变从绝对坐标圆心 (100，90) 开始，半径为90的渐变效果。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
     <radialGradient id="grad2" cx="100" cy="100" r="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="90" fill="url(#grad2)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/L_7LW9cCSsSlDDlcDlVTpw/zh-cn_image_0000002569169659.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=224394698CD77F547B9C8295DFFFC1583A76BFFDF765979D033ED56026A25603) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8gJ3xnW2QJWV9baL7NGfhg/zh-cn_image_0000002569129685.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=4A90FF5116736B15E0AD48953C6B2A092BFAAB4EC738ED07D0D734CBB584A404) |

### 支持遮罩单元和遮罩内容单元的解析

支持遮罩单元[maskUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和遮罩内容单元[maskContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加maskContentUnits和maskUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个五角星遮罩范围从绝对坐标 (10，10)到(200，200)，遮罩内容相对于应用矩形左上角，水平尺寸乘以图形包围盒宽度，垂直尺寸乘以图形包围盒高度。

```typescript
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" maskUnits="userSpaceOnUse" x="10" y="10" width="200" height="200" clip-rule="evenodd" maskContentUnits="objectBoundingBox">
        <path d="M 0.5,0.05 L 0.2,0.99 L 0.95,0.39 L 0.05,0.39 L 0.8,0.99 Z" fill="blue" fill-rule="nonzero"/>
    </mask>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="red" mask="url(#mask1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/yWMapRNBSYyTz21_rngQ5A/zh-cn_image_0000002538129964.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=C4F77A8475F3800EB96FC20BEA829B6A028A4A62F44629BA9E057785BFFFFC77) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/zeqdY0ILTMKktBF5v8rrxg/zh-cn_image_0000002538289898.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=93489978E0B944C1F6B2371618F4E14A165823C39D907C84A701A287A6D92016) |

### 支持图案单元和图案内容单元的解析

支持图案单元[patternUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和图案内容单元[patternContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加patternUnits和patternContentUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源图案单元位置尺寸为绝对坐标，图案内容位置、尺寸相对于应用图案的图形，横轴乘以图形包围盒宽度，纵轴乘以图形高度。

```typescript
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1" patternUnits="userSpaceOnUse" x="10" y="10" width="100" height="100" patternContentUnits="objectBoundingBox" >
      <rect x="0" y="0" width="0.25" height="0.25" fill="red" opacity="0.5" />
      <rect x="0.25" y="0.25" width="0.25" height="0.25" fill="blue" opacity="0.5" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200"  stroke="red" stroke-width="2" fill="url(#pattern1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Hd1piXuOTRWMqWbkP9sQZg/zh-cn_image_0000002569169661.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B0448C8E74B0772135454BFF7E164ED9778D195B675DAEDBA1DDA981A8A0AE1B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/MPvt2bEgTUSgXTegFYVoIw/zh-cn_image_0000002569129687.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=FBA887FB71C86EDA611D01CB83587AA13CCB7175AF7A310833D35F04864BBC98) |

### 支持滤镜单元和原语单元解析

支持滤镜单元[filterUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和原语单元[primitiveUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加filterUnits和primitiveUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。目前支持到的原语有feFlood,feOffset,feGaussianBlur,feBlood,feColorMatrix,feComposite。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例：原语值为"objectBoundingBox"时，feGaussianBlur的模糊标准差X，Y轴的stdDeviation数值分别需要乘以应用滤镜图形包围盒的宽度和高度。滤镜原语子区间x，y坐标相对图形左上角分别乘以图形包围盒的宽度和高度，滤镜原语子区间尺寸的width，height参数分别乘以图形包围盒的宽度和高度。

```typescript
 <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
 <defs>
   <filter id="blend" primitiveUnits="objectBoundingBox">
     <feGaussianBlur in="SourceGraphic" stdDeviation="0.1, 0.1" x="25%" y="25%" width="50%" height="50%" />
   </filter>
 </defs>

 <g fill="none" stroke="blue" stroke-width="4">
    <rect width="200" height="200" fill="none"/>
    <line x2="200" y2="200"  stroke="blue" stroke-width="4" />
    <line x1="200" y2="200"  stroke="blue" stroke-width="4"/>
 </g>
 <circle fill="green" filter="url(#blend)" cx="100" cy="100" r="90"/>
 </svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/4Nlp2ZYyTxmLrgR0SR9UtA/zh-cn_image_0000002538129966.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=25083FE8994EA28E2395C6105D86C59DAC306A19D9D9086703C975E36D6C85F8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/nZKJx7zPSKa7erBj-LwHkg/zh-cn_image_0000002538289900.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=867D153D3B23B17F90F9DEDC1004D5A0AEE95CE32C8017BA2558EF009D8570EF) |

## 显示效果扩展

分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。

### 分组标签中透明度

分组标签g元素中透明度opacity从对整个分组下的一层子元素生效到对整个分组下的多层子元素生效。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源有两层分组标签嵌套，被裁剪路径截取的半圆形的透明度为0.4。

```typescript
<svg  width="200" height="200" viewBox = "0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="myClip" clipPathUnits="userSpaceOnUse">
      <rect x="25" y="0" width="60" height="60" />
    </clipPath>
  </defs>
  <g opacity="0.4" clip-path="url(#myClip)"  fill="red"  >
    <g >
    <circle cx="25" cy="25" r="25"  />
    </g>
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1fUwORl5TkCNixdG44ShkA/zh-cn_image_0000002569169663.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=9A561D3498DFE218C20D7B978CC9BC4212CA64CDFF22E33C262411055E5A34CF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/2gxdcq9MTBSc_Ajo4Na0dA/zh-cn_image_0000002569129689.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=B597F35A9AEF1BCD3EBB3924284E851BD3E917B4E03A4C9D378924477CE64C84) |

### 分组标签内引用裁剪路径规则

增强g标签内clip-path裁剪路径规则的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源裁剪路径引用于g标签里，默认裁剪路径规则为"nonzero"，路径标签里的填充规则为"evenodd"，左图实际的填充规则为"evenodd"，右图的填充规则为裁剪路径的默认规则，也就是"nonzero"。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="heartClipPath" >
   <path d="M 100,10 L 40,198 L 190,78 L 10,78 L 160,198 Z" fill-rule="evenodd" />
    </clipPath>
  </defs>

  <g opacity="0.4" clip-path="url(#heartClipPath)" >
  <rect x="0" y="0" width="200" height="200" fill="red"  />
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/OXc7fTELR4urBx32L54VSQ/zh-cn_image_0000002538129968.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=15D8641F979D568C5F92A4FD458B50C2FA72B721D3A193BF03F9F86BEEC9B39A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UWCM5_F4RzaDfLr42sUA0w/zh-cn_image_0000002538289902.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=5FC894503F3E71F1FBF72D0D4CE3E6D6BDA6457223439EAF5A5E262035B6AAFA) |

### pattern支持平铺效果

[pattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)图案支持重复平铺效果。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源如下：

```typescript
  <svg width="210" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1"  x="0" y="0" width="0.5" height="0.5"  >
      <rect x="0" y="0" width="50" height="50" fill="red" />
      <rect x="50" y="50" width="50" height="50" fill="blue" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="url(#pattern1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AlGvj17HQJiMyeO6O6m74Q/zh-cn_image_0000002569169665.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=1E95A9CACC2592B5E7691CA76A8ECEB32BCAB1367A7500B3E775FFCA918D9D80) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/FBxBSBghTGGJiJDIGqYR6Q/zh-cn_image_0000002569129691.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=48E54427568E0F6D2D04BFEAEF097868DAFD5656A97FF3737897D4F8BC75B803) |

### pattern偏移值处理

支持pattern图案在x，y参数非0时，从只显示平移后的部分图形变更为显示完整图形。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="40" height="40" fill="url(#pattern0_0_37)"/>
  <defs>
    <pattern id="pattern0_0_37" patternContentUnits="objectBoundingBox" x="0.5" width="1" height="1">
      <use xlink:href="#image0_0_37" transform="scale(0.00833333)"/>
    </pattern>
    <image id="image0_0_37" width="120" height="120" xlink:href="data:image/png;base64,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"/>
  </defs>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/twaYB_bFQCiGaaVcDHQ-og/zh-cn_image_0000002538129970.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=4AF8E20118BDAA3D3FA45B2DF3F65BA1277F66109410C7C86A132BEE2106ED43) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lzZaKrs3Rk-qQrAZr9AB7g/zh-cn_image_0000002538289904.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=CAF141623439363A3CDFD7F239C28FFCD231026C5CE10D5FB371373B697438BF) |

### 线性渐变

[linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)线性渐变支持做平移和缩放。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <linearGradient id="grad1" x1="50%" y1="0%" x2="0%" y2="50%">
            <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="115" y="15" width="170" height="110" fill="url(#grad1)" />
    <line x1="200" y1="15" x2="115" y2="70" stroke="black" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KelqlMJSRVm8lVEAk3IKpg/zh-cn_image_0000002569169667.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=BC5AEB490F2FE6D0CF9493885F100B17058958CE30ED5F72A32134C4FD83D935) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/FiMfgQkJT1qNwoWxTlsL3A/zh-cn_image_0000002569129693.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=23BA33D91FD546D542598BF50066A6E07126F82655B356DD7E9453D9DCD04290) |

### 径向渐变

[radialGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)径向渐变支持做平移和缩放。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <radialGradient id="grad1" cx = "50%" cy="50%" r= "50%" fx="40%" fy="40%"  >
            <stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />
            <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
        </radialGradient>
    </defs>
    <rect x="10" y="10" width="100" height="80" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Wu-PjMW-Rw-jGAC9YQoQlA/zh-cn_image_0000002538129972.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=9D1C3C56AC26C2DB66A91A6F462F1248B9B6935381169E988C44B8B596F1B725) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/YUxBEHhQRzWPkg1AaTOowQ/zh-cn_image_0000002538289906.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=7632D8ED5132948BC27BB96FE04EB5CC6155D9505E1B24B7ED3BD9CB81619848) |

### mask参数异常时默认效果变更

[mask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)遮罩的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" x="0%” y=“0%" width="100" height="100" maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse">
      <circle cx="50" cy="50" r="50" fill="red" />
    </mask>
  </defs>
  <rect x="0" y="0" width="200" height="200" fill="blue" mask="url(#mask1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/xms_HpfSSzylyJYQcjA4vQ/zh-cn_image_0000002569169669.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=5D649753AD57C6A1C154FB4A36AA47A5908DAE2F71F14523163DF12DF321036F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ChDDm1t_Te6mY0YFfcuung/zh-cn_image_0000002569129695.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=7CD3087BCEAFD2D3583FD1F90507BCEFEF309507D5030B181B71C773332266B1) |

### filter参数异常时默认效果变更

[filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)滤镜的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" width="300" height="300">
  <defs>
    <filter id="blurMe" x="0%” y=“0%" width="100%" height="100%">
      <feColorMatrix in="SourceGraphic" type = "hueRotate" values="180"/>
    </filter>
  </defs>
  <circle cx="60" cy="60" r="50" fill="blue" filter="url(#blurMe)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/R7vmi6zjRuOt-cdxQFv2yw/zh-cn_image_0000002538129974.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A954C4C6E42A69AEA1434E6343CA2182ACAA180110B6847389590FC18C322215) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Ub_fSxThQFK-ZxbLJxSMFw/zh-cn_image_0000002538289908.png?HW-CC-KV=V1&HW-CC-Date=20260411T023656Z&HW-CC-Expire=86400&HW-CC-Sign=A6DD470272D3F2F70AB5AEAF893A87E3EA876DC6D563B304E000424E2F82437B) |
