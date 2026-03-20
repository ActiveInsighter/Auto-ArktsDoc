# SVG标签解析能力增强-图片与视频-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/MsGubtXLQAqnT-XqCdH1RA/zh-cn_image_0000002531226016.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3B1A0A829000FFA3F8984BBE0A63F0ADDE8555348BB18653B235C61F01775163) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/hoY8r7ysQSSTZZULQD2SEQ/zh-cn_image_0000002562025999.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=033149078C9A689EB00F3A88A15DF3738D9760EB7A5674F0381973DB9B67190C) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mct86Xz-TCWGliRmSFUIIQ/zh-cn_image_0000002562145985.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=CF1075CC8B2280837576877AA50E67408671B2F1DBD5A67C83D41235C2007A5E) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zCulBZSMQYSG76AwACd6JA/zh-cn_image_0000002531106084.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=1A3FFC7A56B35CF22E0C4EB8543E741687723C38A310AFA4055FCDD322DABE01) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/S5Bym8PZT6ulIQqqraZkeA/zh-cn_image_0000002531226018.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=9085493AD9FF649086BC855B00CE6D9DEF90FB454685D32D1D3FD4ED4B2367BE) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/IbEU8DcJQqyJc_jk4419SQ/zh-cn_image_0000002562026001.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=074003A6C16AAC69D0BF87336E6680A07D1EA9384ADC8BF71F5BC3BDA16425D0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eK8rWI09Teu6wCQr5nJPMw/zh-cn_image_0000002562145987.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=F863603F4CED4175E598B8619C88DEBF9ED14846CE3C3FA0F897C81BF00C03EA) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hDb7ycCaQae2i8EYs60ulw/zh-cn_image_0000002531106086.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C0988EDE854263D189FE5C0D529635500F7D7CCCD4C9D65A9DB9B3466A149874) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/2y43ulkURVC0VEYhefESkA/zh-cn_image_0000002531226020.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C38536F01E4995679779A4E4AE7F2441BA118845295C4C5C3805208116C59722) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/193mMcO-S0KUZk0DgvIpDw/zh-cn_image_0000002562026003.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=38AF4CF8C154A6B0B9990C91304D131B635C1EBC9A4FE9ACE3B9C8CDA335C48A) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/JpwqOTFISlm2gQmpBRS3vw/zh-cn_image_0000002562145989.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=379140FD91FC4FF2F83060FD1136181F45692FB0FAA80D0B4D915D8DAD7BB24B) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Gc1O_NdLS2GUdifGCdLB7A/zh-cn_image_0000002531106088.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=1F70AEE9BFF473A250BE6A9FFF9B21F10160C191863FFB8197E6A8BC310DDC6A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_At9qU-eRE-KRKfoWzpuQg/zh-cn_image_0000002531226022.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=4A200E2FF68284CAAC81740CFFF25A18A902FDA573B2782B1CF8786DA7C35163) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XMSf5UlzSby6QPdQC5aipg/zh-cn_image_0000002562026005.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=99266CE7B9BA2A8DF60BCE3AE9206454D0BF04DE9E19273BB0C7BF27F7ACF983) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/-Y_PP3ulTaqz7w3GQ6cMQA/zh-cn_image_0000002562145991.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=534D190EED024DC44CCD2544112D52BB329DBDF3EF2ADD5A8486F4A6E9FFE3F6) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/g95t-8LaQoeEiFO4MZvcWA/zh-cn_image_0000002531106090.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=93ECFB626016CAEC364E582254E1A310A325CC984D03A21CAE16953BA89C479B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/a1PNeI0sQdGbHPkFV_unMQ/zh-cn_image_0000002531226024.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3F0C11932A5C4A42ACF030AA48170D40DA416D116A1B1CC7A9D570D228845D86) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/rjffx4ftQIC97m0ASoOxeA/zh-cn_image_0000002562026007.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=925997044E81101C09468A24712A8797C4C69E5B1FACF082CEBBB6421C7F5196) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/IPo1iBkvS6uLCEGV_LNB_Q/zh-cn_image_0000002562145993.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=F73A95143327FCC1C4E4322DBA58649B89F6454416CD3E06D826DF80D74260F1) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ooxHBqleQzWNGjKkF2FVDw/zh-cn_image_0000002531106092.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=0E26EDD0A9BB17C47976EA4E57F8FA381C55BC099C49217115019BEC33E9EBEF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KGhqJo_3QAS_Oh-wenTI5g/zh-cn_image_0000002531226026.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=2A6C1B4F52A94DEB9AF2864766A164FB7A49891D1550DFEDEE0F436C804B1744) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_XSzxZabSN-YmDmdi1hCrg/zh-cn_image_0000002562026009.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C9E68198471B1C49D1023C00804174CF7A89B5E77EDEFB1249EF0D2800941C00) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WB-9znnzSlm64Gu2eFjkrA/zh-cn_image_0000002562145995.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=D1601C1A1BDCB0E4A460D48FA21067FFC5DF7AAF987F8B8FE6FE16BFC1E5FAFB) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/WBMjY2ihQg-MEOrMMy6g6w/zh-cn_image_0000002531106094.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=E5A11760ECDCE2A2B21CA0F87FA5B3A1D85AF6FE71807E243B63D3EF81FDF9E8) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/nsZIAqlGT96dM19SAzkqNw/zh-cn_image_0000002531226028.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=2B972C76E9A5668256912B7C8F370C7B94F874500F898A2EF870C61550E7C3A4) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nOqsIxreR9KnpLVLgnhKGQ/zh-cn_image_0000002562026011.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=0588622FD9A943554F5A0D28474E5C8FDDBB092D79381446FE04286EB57C1A76) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5FYNVTbHQrq6frtXlBf2Bg/zh-cn_image_0000002562145997.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=DB9EEB9B29EF771D863E7B4F8138C079597D5165871258D66E74F3CDFEC4D2EC) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/J28u8BgESKKUJy5IEn2l6w/zh-cn_image_0000002531106096.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A549185920F3AEEE41F61E070D9C456A65AB301E9DA62783FD98A4CAE2CEAC78) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/EcVtPbH9R0C3g1ThaKC8lg/zh-cn_image_0000002531226030.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C9C41268EFA016781BBB4DABB4D8E0DFDFC13E8A128581934AB6850446D42488) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/nEo1ZcJqQFaDTjBbLKjmOw/zh-cn_image_0000002562026013.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A55997BF81ECCA275B4555E4B74EBF20F277A47104707F78901055332F4C76EC) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KpNxHNSPRgaXImGaK65GdA/zh-cn_image_0000002562145999.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A2DDB00249037C3B23BBA1CC292CF29DD1FCA3C115522FB86A3B5E1342D73D56) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/GoTzTwV9RGWIhvkunMoHlg/zh-cn_image_0000002531106098.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=6EE6C5CF1CADCD80B2C21F7F28E05DB516D247C527006D7742A891AFC501DD03) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/sHyhQyXzQAifR_TyrI4Vfw/zh-cn_image_0000002531226032.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=122155AC937ECDD1C07382C1D08AF408EDFE8DC79F91225E41D284D53ADF4CCD) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MNhTmHqRT9KXatitgn76Zg/zh-cn_image_0000002562026015.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=0A8B511F8A7AE2C3B23C7CBFE547FFD0C41B2A3CCD96AC04D9B4995E71723789) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/DkcCpR9oRmu5BiVFeXFS0w/zh-cn_image_0000002562146001.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C7BD16207EE315BCA332972C6D042C38A8C1A002F030F230121719221715510F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/krxJcgkkRYiAphnKEQ_CZw/zh-cn_image_0000002531106100.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=1655F18A3E3B17E7D0F4A13323A275441A286A3E3B6C70B78012956F5A123E4F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/FL8gcSEnSf-s_OviHqLR_g/zh-cn_image_0000002531226034.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=2FD56D78BBFF7EAF95FD6431BBB7F383B3AAEF8037F7F6375A89C8C457D72A38) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8XUI3hD0RpiYqEYyjF_Sxw/zh-cn_image_0000002562026017.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=E7FDFE1DD12B9616EF1519CD0F01DA4427DB6A50E9E6A738588B42044E0E644F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/XgdWgq_mTbKbE_xSsSC4dg/zh-cn_image_0000002562146003.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=CB357A2ED506C3BB34F66C22D0A426CC19FD467640415FE7F3E3D25B65BF4D05) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/6sEhEPrbTKiGFAzHel5lcg/zh-cn_image_0000002531106102.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A289932B76412D9BFB0771208D07DF9BA9BF2C9EB3A1276D9045F65BAA2FCB61) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/frkhgIhMQaqv15-RjDFFZw/zh-cn_image_0000002531226036.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=ED28AF9C9726DCC20155A406C64F817BEE7D9C062200FEB475A3AE34CB49C65F) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HikxhtJsQsGFat-LngwjKA/zh-cn_image_0000002562026019.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3569FA06C9E324D7BBF195FB9FA3C197623C1E0AED66C3BBC0833B8C7B357CAD) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zUvT6SjQRpiyjZ3IQqEiuA/zh-cn_image_0000002562146005.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=74B7B54F362F17E91835C1B3620C7E08C753C90F86FEB61487A644F0BD9B098D) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CeUm7lnuQpSO-smMXisXBQ/zh-cn_image_0000002531106104.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=BD14D6D3ACB44CD55A15611C303C8FC8BC86B635BF8BB3F5FEC74D11329C969B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QeaoqrtwTI6igmpj9uyT0A/zh-cn_image_0000002531226038.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=5D7BBF7F7E8C49D46F8ED7541389D00480322E6DC27149986CF71BD7F670E5AD) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kPpcvB9sRwabtVzlYpm5Mg/zh-cn_image_0000002562026021.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=FFB14BFCF8BFB2AA045DD102D4E4E6A4BC9A35DC02857379BA9C1A8498124C41) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ivZ7iPxYQPWAxIWifJ1KFg/zh-cn_image_0000002562146007.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3B2462DC65958B64DD20F6C97DAFE1B101C81D232D9FB65139BEB55C751FC26A) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wZQkntFcTiuiHjiFYCTTZw/zh-cn_image_0000002531106106.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=DA3DCA4F79BCFA55FBD1940B8F12BD09D0481D7D150D4DF7C44304454D2915F6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/h6t6EC9pR5mQ5qTPslcfqg/zh-cn_image_0000002531226040.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=EECC8916019A6B6C26B0F8EBFF907869CD4F5FDEE7EDE0571E943F046E584D79) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MahNlqwbQHShWSkIueJLyg/zh-cn_image_0000002562026023.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=DDBA7A421A1B89A6087A29ED87021D3F40F7B89D56B5869AFC8706C640C746C5) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VAJaGi20TV2padLk7E_GKw/zh-cn_image_0000002562146009.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=2E06860A0351FF93D5741AFA07E3DF0D1DFF2D425AFA31E8EE0EECDE35E4D2D3) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/P15cbpUUQMaVkJNUumgzcA/zh-cn_image_0000002531106108.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=93FE980871147A66273FF4AAA71B06D069759A94B824D199494D7CEEA1D8A4F7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/stYmfh7MTCSotVPU3b0SKw/zh-cn_image_0000002531226042.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=BF3549450433323548307EBF8112F8D7CB15093D464C04A05314BBA73ADCA84C) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dgMA5i3JQauH20lYjohUJQ/zh-cn_image_0000002562026025.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=5B26723B60CE541A1A302729C186D2AA37DF032398A31BED05E17D5309E3181B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_pjHAW9-TgS-ZydTOuXv8A/zh-cn_image_0000002562146011.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=408C4B2253B563381884BAC3E8BC6B23F6B44F070EE80EB6A742CEB62AB9EEB5) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bfhAKlkWQM6laLnWgGTeuA/zh-cn_image_0000002531106110.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=5BC709F47BC9E79871394E8272F021CC1BC86CBB2BF24D3260407EE11507AD9B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yag93OgrSHa9z7whde7fMw/zh-cn_image_0000002531226044.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=353DEA50A05B95283EDD52D904198B65FE17B7A740DF4CA88FD406B228425831) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/KohZoDqrS7OdvWpHQ07tpA/zh-cn_image_0000002562026027.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=85473712AD7BD9307E97FE70B668DC930B67FD7122719822A478A8B3AF7D186C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MDiYMd-7TFSeIUskarK0Mw/zh-cn_image_0000002562146013.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=2FF9AF15DC6DA627854591B10FA4DCB720ADF2DDD75CC85098958177226E3AEE) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/abZ7fuRHSDqfc4LbSqHkzg/zh-cn_image_0000002531106112.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C75FABFC5C228DCA76FA885E5B473830E48F98B7EE6A3CF8D7CFD22063310E2F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ptAOhSadQ7yoDs1gVRgfuA/zh-cn_image_0000002531226046.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=384AB9F522D500F20461AF6188293F08D56F7C84734407A2957ADC5DBC6C638E) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JSfagPGsS6S_8zhTgVwsKQ/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=DBE90868DEAF860B7A8254E8718A7250FE0A34D2A1BA87B083F20B3D3B86E54D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Y6CUxnEzQSK7kCZ-zklEmA/zh-cn_image_0000002562146015.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=E16D5CD69553BDC48E2D9A6D9BB9715776C2060B623EB10BC0CB02D9613153A7) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Oq77nB48Rn-rwgaLlA4hnw/zh-cn_image_0000002531106114.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=4A26C8EEE6F5161087A198148A7F3D5C79612010151CC42F6A2796F9B21A9317) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/DclcQtdqQmaVCIt9HpJZsw/zh-cn_image_0000002531226048.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=8C7995BAE5512568CAE3922BDE1D7DA33D65355EBA2B8DAB60CE4D3719159D10) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GpzaKbncT16jtF_OeJx7_A/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=6FA52A98EB828A047786BD7C5F9D45266DE28211AFB4851B49E82E1C70D5F637) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QxzfjgwFRa62Z1pq5qpdmQ/zh-cn_image_0000002562026031.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=901C48D51A04CD87FDE76923D486A814E3C881DFFEAF50192AEBE3A2511B35C2) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/a1xtMoSrSM-L3ujpOBgSQQ/zh-cn_image_0000002562146017.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=BE4C9691107C068AFDD590A6E8B8755849D4D244B881501BD3F6125AE055003D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/br2qJVMYQWatQXb6bqYzhQ/zh-cn_image_0000002531106116.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=5EF9C273871197D27E7EF4EC8722A411F3DE7B7AB03402D8BE4640A167148C2C) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/pu0gQteMTwSov_uHsxjz4A/zh-cn_image_0000002531226050.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=441753E6433E4A0697068AF39A1F8068B3FC69A32554B5A0A48920EB9901F826) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jqO9UvEbS22tFGsO6tVZ-Q/zh-cn_image_0000002562026033.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=9D415545C66BE405FA3D5258E849890C33969843CA905C1E9A547B365D572036) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/T6SRypwRScmkghsqNkJkDg/zh-cn_image_0000002562146019.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3A1A56BC0715F5E041EF42D8AFE5FDA0CED45EE5EE2B3267E8E5F2DAD97AF5A3) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/F3Xd70RpQlG1Jce7stvITg/zh-cn_image_0000002531106118.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C10415FF6A7DFA11C6D8B36264C045EBE572E763C2FD0B83CBA59B24A0D194CF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Gy0FtAOFSFWcxls05FN0iw/zh-cn_image_0000002531226052.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=AD81169BD4ADDC2218EDB895E4577A93D0BFE9D0B0A3796FCED647E572827F30) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/jvvU7NrYRxaLc9yNBexMsw/zh-cn_image_0000002562026035.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=49AE92F0CCFDE2A63F073DC2986E889D5BC0A9D47985E9A331FA33FA2D4D6B2B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/r32_5jtpTua4n65TVKS7Cg/zh-cn_image_0000002562146021.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A320D0ECE6F3E96F5E338ADD5CCA29AB441B4E4306002D381C7250E31B592258) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/blbsWIQsT_iu9OGIXDZALA/zh-cn_image_0000002531106120.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=E5022189588BE8B108011EE5B8F86343DB09F9DD28E897C305BBD28B12F84AE7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fRlmlHaKRLSh1nuZnALoDg/zh-cn_image_0000002531226054.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=266E0C586748A4E16B55FB384FDA341559817188DEBA33EA807FDB617843B545) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V1mjjTDzQRSsnEbOPpnYCg/zh-cn_image_0000002562026037.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=FF7A23FBE625A5F8C12580E533B3E15B9BEE787C3D42539F0F2D7880C40FB9F3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jxcPM5R7SCmNSusonCc0aQ/zh-cn_image_0000002562146023.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=04A698AFBEF9DFF0496AF0B4A26AEA42B866248437D25FCA1518D865CB7C4F6E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ASfGTvrLSM2FUgj_QVWLyw/zh-cn_image_0000002531106122.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=6F006389C0FA2AF69AA51D36846B97401DCD40D766DD2E524FFB97964D54857D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wZrjWUDcS-6CHwiYaqccTQ/zh-cn_image_0000002531226056.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=BC535DC13E6A679F4A7C21C8A4A5800379B103E5FEF4033361B65D021985CD52) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/oASIdz_dQW-hs8rTRL7Tww/zh-cn_image_0000002562026039.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=4F3E06972E0C416CD3F07AA1B89673137E21A2E02ECB0038F25A093B155B7957) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/a4oALb_BThaymLQFVTVHaA/zh-cn_image_0000002562146025.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=A53C8BFB04572CA0D6BE50B7139F1480D090ED33F313C79B0EB22446A5E16CFB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Jqx8ArIWRX-y9eSLmeVi0w/zh-cn_image_0000002531106124.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=1F1F3714CA87748AE92074A88D34EC33B044E090592ABC8F1AE44586FA9B3202) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/dBLJHSVeR4avgT_OYAHYEQ/zh-cn_image_0000002531226058.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=0FD76EECC7D2144E927658FB6E87422BCD16E34C1124BDEBBFB64A46F3364A60) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/8pqRn1cYRVyqwr2newqOFg/zh-cn_image_0000002562026041.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=9EE7E897E0089849A264284A9651B152AFCF16E1403A2A48768EB96116503310) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4GvJyUxOR2ecmv_IPFCAaQ/zh-cn_image_0000002562146027.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=BD88E5C67D7E8D32ADDB94AF73BE91A57D7769C2D98C858DE5F6B2B73FFD16E0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/0f2hKesHSJ-Ob3qcaY1CUQ/zh-cn_image_0000002531106126.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=815F0D53194D2BC8F62E2B37536DD08EED34AD3A65F49356224D2C9137B0BAA1) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eV69HhchSOaz4n_yF74GVQ/zh-cn_image_0000002531226060.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=150ECE82CE2FD959635B1B14310599E4B834522340B7E6360C9E417C7101AB99) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/O19y5y2CSI2UGWaXxFS9zQ/zh-cn_image_0000002562026043.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=D69876347907E59AF7188BC34F1A7DD92822F8EE4CC5812DEA7445D83C7F63F3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xfQdLA5ZT76oVrC8yvrkpg/zh-cn_image_0000002562146029.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=F388DA6650442AC97EEF1579D2D2C8DD6EEA61999A08E7A877308FB83A56C43C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/JfxWl8mOTOyiD1mQfm-OVA/zh-cn_image_0000002531106128.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C9E22E089ABF6CA5C4FCA73B56A3264F6785E0C179D53C46432E8D08EA900D63) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IhJHv8ByQuyVSmMGbGKp-g/zh-cn_image_0000002531226062.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=DBE99E289BF18BFC9EE19331647128CAA9F7801A05C2C82875A0BDF082AF8576) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yasC9FFJSmCIM0IWuB4eBw/zh-cn_image_0000002562026045.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=FDE3286418E258EFDA5AE32573080B16A58BC79B87C8BAB463B0124FC9B05A1F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-voVzRYRSEiL5g3NmgL9Qw/zh-cn_image_0000002562146031.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=F17B743CB67B2E428D7F1EDEC9A00E3127334E4672B3F54EF91EB4A2FF817AA7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CLBScMeeR5ucLe8kiPIUNg/zh-cn_image_0000002531106130.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=ACC9C357DF853C4F680BFBFBA9CB844DCA74CFB1648D986F297CD5741D8A6115) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/gQmcqygQQ3ClntqIWGsWWA/zh-cn_image_0000002531226064.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=3453A5D820276A3F09C584EF44B3F805CE402F3378812523B987B7FABDD71052) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dxkx0DPKTwaohUnKFJSoXw/zh-cn_image_0000002562026047.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=4F132224B7EBBEA6675ED6C26C092877352F5ABF9BAD78D850AD5DF09A5B1723) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/IGQREW9FQ4e00wZH6kACWA/zh-cn_image_0000002562146033.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=80994757FE07795C1391EF208331DA84A0308F74A22488BA89CEB44034DB4C3C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nbFet5N3RripaMfi9K9IoA/zh-cn_image_0000002531106132.png?HW-CC-KV=V1&HW-CC-Date=20260320T144220Z&HW-CC-Expire=86400&HW-CC-Sign=C460EA944752F325A039BFC7D62A0C64A044CD003D8477E93137089A1AC4133D) |
