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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ii-kyNGOSPOMwAq-foHpaA/zh-cn_image_0000002534411520.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C9F602482D0C15F771C32E36A07E25BF9DA82D0A9A320AAD34042A29DD2455A1) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IZ_5ZBQvT7W89wQIMjwv8Q/zh-cn_image_0000002565291421.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4B2F7AD32234F1864C450E45CACAC61BCC2F3FAA2406A2133E830A8C0375E41B) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LVE_4LLeRTSfpd8S0seZug/zh-cn_image_0000002565211399.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=82162916C275527062B70684EB75818FAABD398CC32047CB1549A4FBCDE8BDB3) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A72sbB7TTHuWW869yWGdjQ/zh-cn_image_0000002534251576.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C538E24A5674166F14B85C6891148E9A640325C4B3667A1087D371631B1EFB4C) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LW4xwmBtTGKE2WoB7sXEkw/zh-cn_image_0000002534411522.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C86F76D386ACFAFDE02DFE2E528803E9EAF457261F25D09C98C94A951500BF22) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qstJRj2MSVKsZ3winwkx-w/zh-cn_image_0000002565291423.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C78FFD13231384A24E33117ED5A6F776EDC911C371E8E6532C232CD17B931101) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eiDytSAYTZKZZCWPOB2mgQ/zh-cn_image_0000002565211401.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4358419D0ECF861F852F3C6E10182A85780CD77C4DC55E8372F9794034C6DBF9) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/sElyaqdiSq2VMjUYeI-srQ/zh-cn_image_0000002534251578.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=6DFEDF28FE4F8ED2E551890E3888268042DA3311EB89B6182626A0BA21B3B53E) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/EK38ItASRAKWIwpbCKuVog/zh-cn_image_0000002534411524.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=610AB9083E62305F967494C73708B9C72EE11B83F1DD517867510AF877582224) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4NMB4IbpRZ-FcVDUkbanhQ/zh-cn_image_0000002565291425.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=43CAD6A12492BF0DA614F68A9B528B4BFB6912CA3C31CFC4F4FC025BEB36C8E4) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/F306G7dOSZmMC4OegqcQ9A/zh-cn_image_0000002565211403.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=2445BC3070C5349828E2FE05C9AA8014330822220DE45D0B2D1864A2CE7C2147) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Bke1AR0jSU6s6rnSNgpTCw/zh-cn_image_0000002534251580.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=060D439CEDB3F3C85683145701D44E7B5F130A957EDD5CB05BB1F04DEEBFAC2D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hcAO4iYDTWWoPHiOExwgYg/zh-cn_image_0000002534411526.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=F55319DFA54331CFAADB121218AC57D3897947AA3A30CCB907F404710CF8F3D2) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/2KdZFk0qQ7uH_JSD4jhpAA/zh-cn_image_0000002565291427.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=A473C6EC3D825F065DDBA4E585E3C4690F75AE05907CBADD479F1755E2BB685B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sh_HjmXhSyimKMaTQI8q2Q/zh-cn_image_0000002565211405.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=7FAD5F7B57CDA717A1E2275E0E3B2AFA2FA939E8844A4FFC1876A9E1752DA0D1) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/JigmDfrpR667kD6GTUcOQg/zh-cn_image_0000002534251582.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=8BE95E709D782D614CCE1DC9FF4A5F3FF651F1483578C0E6859FACCBD42819EA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DhhYJ8V_RwaLzOrG2pef6g/zh-cn_image_0000002534411528.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=88678883608F7EC09D67437577389949D2703A51354B4FD9792EC3B206CD55DA) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bs1Nyw1oSEalRz2mMKNKzw/zh-cn_image_0000002565291429.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C3B2678C4F47D93CB7FBD06B3BAE38A0DF287D86DCF8D656804C512BF083E3B3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3920RCa6TnuauqZ4QqYICA/zh-cn_image_0000002565211407.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=94D55B3E86AAC1F526A99DC7DF3586AC13DBE1E5102F927F82AC7D8297A20088) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/n1KsuxQWRsOgqduN_DWAng/zh-cn_image_0000002534251584.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=552AF683C360630A402BFBD04F48A37A09DEEF03CA92D4C209DB4AB8026AFD33) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NrmtU54qTtOHiS3q8GoOpw/zh-cn_image_0000002534411530.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=E23D6206C148AFE56A61793A82E07F31C6DAC6681AE6922E113B19E5A2292F01) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GoRJcqUFSUGeWbODwYYa_A/zh-cn_image_0000002565291431.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4AADC3D39653DEE1D052B8ADD751090359E8622C2955B3A13CDF819857F95CD6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8VSXJ2EPQ7Oxnl4eUjSbpg/zh-cn_image_0000002565211409.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C036EC8E32C2B9CDE926875236C4F9DB6EE40B41E7B9956581A913880FA42EF4) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yfoy_YdMSFW26uaZgaQ3cQ/zh-cn_image_0000002534251586.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=CCA10F1B7AC24154742746422248ED1CE52F15A8EE69124C917E60EC1DCC8ED0) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/8QHr7RRvQZafaqyK0PHgvw/zh-cn_image_0000002534411532.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=6FAD79C09AEC5D3ABE24F735FB54C19B6FFC2D96CBA3BB182F9547E7F89ECFB4) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/76Buxi4tRIK__Pir7TgdBw/zh-cn_image_0000002565291433.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=3D437BCB878D325EF3CF0AB5CFFFDEC1398EF69A8285ADB44EB260DFBE6D91FF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Ez_4Qre-TgWCbOJrvJT4Bw/zh-cn_image_0000002565211411.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=07C3BB610B42AFEE4ACC58487D5E111505AEED1115E2145139BE6AE3150A6DAF) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/crwaIsXDT96N-IeYAbW0aw/zh-cn_image_0000002534251588.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=07CBC383B286D53454A5F17050AD2B13C25AA27D9BD4E9C0733C281FDF459573) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DJQkoOb8SSi6fJJxBpVH8Q/zh-cn_image_0000002534411534.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=BDFE7AC6BFA0894AE1CA20BB8207D953EFEFB15DF59BDF1515F30967B734BC70) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vmNZSo24SfitNb1mdYo7Yg/zh-cn_image_0000002565291435.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=5BDB031CA4E575D7229AFDD0221C73F9D460F7773BB1F225A2366B4C97C963B1) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WSgFDG7BQRy_Whm0iPxGUg/zh-cn_image_0000002565211413.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=CCB1BBF6F058D887AB7D15D47BF4C2A7FC2B03ADA1E490E9CAC1C9C60E6AB098) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DEynjX8dQOagdzDlHqYe6A/zh-cn_image_0000002534251590.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=766190911821D1366174E16C3636CFE35F788AB43FCEC7390D20A858B9EEE5B3) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nSC56eGaSyiz8GITFKiZtQ/zh-cn_image_0000002534411536.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=660B107938CA0C98F6225691A2A358F8FCDCBFA705053068F1B459E44CD307E2) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vQWoAnqxQ2S_09Air_PyeA/zh-cn_image_0000002565291437.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=19D46A82B5E629D506A8B2C20BD4E7CE043931F6B011F39F06D5E551A5F6E87B) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aRzPA3D6Sru1r0qqT_lbiA/zh-cn_image_0000002565211415.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=2A0F56A439AE6E96A76D0E15552DDFDFCABD6F1885D9ABF989A4B7169595A3BF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AK6F763hSYSDjwLqQruZhg/zh-cn_image_0000002534251592.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=3CC3030C6F7A6CC37C44DDEFC55D6C11DD6BDF1E1E1B8BEB2CCDCC46AF53B46C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AumZMu5QSn6qmq2YAkgImA/zh-cn_image_0000002534411538.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=BCC5BEE7DDE39B992AB15E63948536E96D251046173F42D88A9E69CD4621930A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eGt-LIpyTsabAc4MQXW64Q/zh-cn_image_0000002565291439.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=3C8C28138DF70E5AA95032A0D0CBA8CAE73D9C035FEFA5F45634F3FC83D06C82) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_-yf95JTTQyZDoalZ667Cw/zh-cn_image_0000002565211417.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=03ABA812D6AEE7BCA0B15A240571002F5992E40001251940B05AA11840D8A5B9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/oZC-V7nGRhaw-Zz-3oun2g/zh-cn_image_0000002534251594.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=482F04DD55F7010B84421618C2A109A0AF96E614F2E12F139B114A476FBB66F0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GgPzWsdrRgS0Swq-ZDDDqg/zh-cn_image_0000002534411540.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=0D811844C50454B76A298AF1CBF309F13089E5A29FD3F7B4DA4157165673FA6E) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/veKhEp8PS9yCxuMXzz89-g/zh-cn_image_0000002565291441.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=88E5FF6049F04F9FC5F5696B04180F155949D8C3088D5F661EFF3C887D653D27) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Xlm6fTeBTdyzCFbzalofag/zh-cn_image_0000002565211419.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=D2BEE3378A824C6203C4E80C935B91BB8F8486C3E2DB3D0ED754030C82EE3396) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NunMMI4TQQOBcu80y8JvVg/zh-cn_image_0000002534251596.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=B23CE1ECD9F3A19D25B01FDB6269BB420D5956620E41AC3F13C79CBCAD8736CC) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9dizZSWlTRG3adRzGSjOOA/zh-cn_image_0000002534411542.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=B9CE8EA2AE06101013A358A190A47AA45F86609BC36D2E75EC144382BE8EBFE7) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EQKx3iiqTzmD6YjGLOYXFA/zh-cn_image_0000002565291443.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4A0863420A9C8C49FE4EC71C76C504273E82FF53BFF60E77F286A148CDAA0D42) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1WsXuK5aQnWjJi6xetnWrA/zh-cn_image_0000002565211421.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=7AFBCF58C2627A489305E7AA7D7DEC3EEB0D4DD4054DAE5B8D9E242075B2C72F) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uYUS40C6ReaYGs7HPMLS4A/zh-cn_image_0000002534251598.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=26D50B93C916DEC171A10E1C9AC4597AAE14D051D09360BA02244539137E0457) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cHSMm1g8QV-Me6LBPUV40Q/zh-cn_image_0000002534411544.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4ED15E14DDE7368F07DBDBDB86B240A635EAD56C041A8B5CD99572E07AF0AAB5) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_nRJJHFsQKS_FcoMgJ9-Nw/zh-cn_image_0000002565291445.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C767E69008218308B6AD79C617C4A797FB489C9F99EBB5B4BDA5C2BAC0E00D77) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qIKsUZLxQ5eCHEfo_muz0g/zh-cn_image_0000002565211423.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=EEAA2DDAB3C24FB3CDF28E45CDC594205A2A8D558DFC749FF51D4BE246842A90) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/5ZPdsFE7TEKAEpQiijvQLw/zh-cn_image_0000002534251600.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=178745119AB4E5BB60E8B1ACA89DB9322FAF73E3274553DC75451998BE865A8C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vYljLAQvQ9OZsXQpKsgM4A/zh-cn_image_0000002534411546.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=2C62A576227BB2216898AE2720B3D91912AED2B135D6D32544BD27F68C21E43B) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/52HZkPiCR1SL_e7NYaf-ug/zh-cn_image_0000002565291447.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=EACA73561BEFD651C7CA363666FE16637E7C9AAAAD07DC27F656C1C0AD3DA52B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FC8C-rupS9qRw9ymJcR-RQ/zh-cn_image_0000002565211425.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=3B6E26BD5161D3B1E824BF7D6A2E31CF598D9FB55AF86E0AA00AE919BE869E30) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G14KchPeRRuW3rHCaVAp0Q/zh-cn_image_0000002534251602.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=DFA96472B4CA568BC009A1CC833EAF9CA003D1A72D70EAE224014F41A26AE739) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gBxz3uJbSTmQF7OESWFZcg/zh-cn_image_0000002534411548.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4E3ED741F052A1A2A68AA8B29A2DD0E2E1AD39BFAA340E1C3A433958EC79E476) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QEr0qsK_TU6E6zWy0wiFfQ/zh-cn_image_0000002565291449.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4DE9423C3B5C968F5C3600343FE7D2A58435E2853BC35479BC329CCB8D3B7BDF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_HCxlBGaRdadDF1OOOoptg/zh-cn_image_0000002565211427.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=83071CA9467A6E3381D91E8905D1AC7318FF317F3F5AD1124A7DB9CD60B025D5) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/oO6TyryNTuiU1ImCdgdRQw/zh-cn_image_0000002534251604.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=E3EDB84736A0571F79D37A01D371C693DE71AAFCA13E88C1717C1B46DE6FBA74) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WyNCM8-2Q76PjHhF6DDFaw/zh-cn_image_0000002534411550.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=472F76F96B4874A262DA5EDF806CCDD36EECEBADA9456D012372369A050C403E) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ItI9jH7hQyK-e2jr4f-U8g/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=A5F88A4F206B3374A552E3497E36C51D936E9B0746EDD710A7AC847E3AC82ABF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1z6iQdJfSZiGfwxO0-X6Dg/zh-cn_image_0000002565211429.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=C820B7A45726B3C82738154B7BDA7E4C8C8AB3D0A1BD79ABC9836989848ACABD) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4yMyaYbpTyuR9cBmW5L91w/zh-cn_image_0000002534251606.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=37D8C467E229A8821AF5E9D00B50984D4B65D01C4CEB6E1C1C12B15E88D33CC1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/59ZiPuz4QXe1rzLmFktNGA/zh-cn_image_0000002534411552.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=DDBDEFD71C787EBB747A858B576E36EF4B66EA18DBE9A2BF879EBBBC29CCBACA) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MpfXLUq9SbS5Jvu6n06cWw/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=2ED0D9723C538D5E774D81F2C23668272B16B80A8444968A18B8A2FE2D0C9733) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/tiGGbyfxRtOYYvpk9Hro1A/zh-cn_image_0000002565291453.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=8662E2E2B584E3A1E37728BB3CBF1B87524DF24A52238B72C22C38A0DD56FF3C) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yBCtH7JLSsuV5cR4z-raMQ/zh-cn_image_0000002565211431.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=5495E80E41E9ACD9C7A7B9DAAC3A6CD2798710FAFBB345CCB794452B58FE8500) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/k1yWcafmSEmEMXe9Lr4W9Q/zh-cn_image_0000002534251608.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=80CD3274F22324C13D9841917A5C3294FDFD91048A9B281E0F683D84EBC032AE) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7NwI1coDQXqISDHeiNpJOA/zh-cn_image_0000002534411554.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=7271C2B1E5EB77AD4BEAD219CFC1DB4638B866FDCD4E902CD50C843A6F57BB91) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ST5XGG9eQZmb3g48GkY17w/zh-cn_image_0000002565291455.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=272D1C2A2E3783C6928C03C846DFAC2082FB8975AFF913027532C886A90C66C6) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5LYlOjNmTZ-FucsQU70VIQ/zh-cn_image_0000002565211433.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=237DA56D605CE20C1D7C872E3EA28663506042F37F8AE303D8013B6217600D74) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuhAU9IlSDWFuGr0FU53bw/zh-cn_image_0000002534251610.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=61F3F2B77CCFED6F6D8AA81EC1A0BFF55F11742996A287D10189C76CD0435D47) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gf4tXK1KSD2XtIVjOP-9Dw/zh-cn_image_0000002534411556.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=16B8A3FD6F2B29A3EBF7F2B7D0EA49AE93A5B8F17592C8B7159DE0DEDF3739AF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/V4FSyf_SSwKGTr9yCRUg9g/zh-cn_image_0000002565291457.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=79629E58C24BDDB7C7EF068BBADE2EE6EBBDAD5270C0B99D5288267370CE01D3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/kdMZMjmRTj6nGHYBVUXwYw/zh-cn_image_0000002565211435.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=460A22F51F09DA7D7573D6CF79681818983750BC60F3D227F407A613B18BC8A8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xb-R39t4QAC0OsF5lWyHDg/zh-cn_image_0000002534251612.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=40578B820779A0C0EA1362799FD82F440B2A2D20C81FCD03E883EE3075DE84B9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HnoQfmW2Ri6e5K1ffwWzaw/zh-cn_image_0000002534411558.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=6DC3BFF7C366BBD2846434D5116889F3F0112D1266B63B42C0A0EE3A41CB1900) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wlZk-6epTIekWZYIeCO-3A/zh-cn_image_0000002565291459.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=A9297B75433BDEDD26195EF8C947C206F9115FF25F564C4ABB33B41C73008139) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2uZs4Q6pTJ2qFE87i-cJzA/zh-cn_image_0000002565211437.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=FA0C6E08C4E80E23BACF389D8322DC377518D98CCB45703689C338B62DF193AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O5OWYVKpTEiIo047460RsQ/zh-cn_image_0000002534251614.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=AD592D8C194520F2FD3D337086A638C67999623DB2CF4051AFC959E1224C6D0E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Md_YXiTOSE-xtLVUZ_CYhg/zh-cn_image_0000002534411560.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=CDA581FDA59E57B0D8626F218D397DDD18DBCFD5424C383838166AAB62CC0418) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kFb6hRscTIiHIVztiqZMjg/zh-cn_image_0000002565291461.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=F8EB13F5478B04189323AC9799055FE81A89F2E03E25CBCCB796AF5B8A46D6D1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/pTh56Ja-SJ6FQHgb6lzWSA/zh-cn_image_0000002565211439.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=94BE043FF32C91D1D33FD56F2BC7DF223DC50C01A7834C5F468E7B49F6579361) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vMGeYhcRSZCB-qVDJDKCpg/zh-cn_image_0000002534251616.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=103C12F139E6D3B9F878112E408C11D3016456703AC02637A026DF5798A2566D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nqUcPMrKQSCVCtwTZg92Gg/zh-cn_image_0000002534411562.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=CAA71637F730BF8B6AD6BB9C8D0990E50130A357E1234C2F6F77FE58530E5773) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O8vSOm-hQFGFkpq1e5u1ZQ/zh-cn_image_0000002565291463.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=251F1C97F073704DED0E5B659150D6CA67C240D582D671F6CAEBAE5CFA49502A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6uplnqqAQTmApsGDeqBpxg/zh-cn_image_0000002565211441.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=510C69B4C910B90E55841A4473B265D23E92FDE071194035BC985C5C67ACA4B1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/I_rnRsxzSpGxBEwjN1XU8g/zh-cn_image_0000002534251618.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=4507650021E0BD3365B39F21352016275C1080530BCF14BEF51FA71BC13D4196) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lXHCjT4eSV6w8LQaMbopvw/zh-cn_image_0000002534411564.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=5F853D58B710BDE729B99DCBE5662E25C4AEED006B500EF2A74BEC17B45B7C1D) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SJhv0EWETuWxFXXqwPiRkg/zh-cn_image_0000002565291465.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=B5F0F669C66C7B15EE5D1F07F85D7AC67AC878CF3BA8350334FF61CD7B8A80D6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Up-SzE_rT5KMvJAw-WuYeg/zh-cn_image_0000002565211443.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=A01DA3FAF1AF48FA916255D43DC19372B25021BE15D6AE1F94899FBD37BE8FBC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qT0NlbsyQE27uHHYdWm95w/zh-cn_image_0000002534251620.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=B2BD7AB7A151BE99F00886835BE918BD997DAA12C8862064C7123961FBC69F82) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qqxSsYC5TcuLwNBiEKfLjw/zh-cn_image_0000002534411566.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=D7EBE54F79FA2047BB2ED84A9D7F037E609BB09CD5852236CBADFA0340ADE7AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WdYtIMmgQlaRxBupL9XHqA/zh-cn_image_0000002565291467.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=A7A5780AC431656224281DCE12B8FFEE18DF0BCB4497EA93AA5B2D06A3D7D1C8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/irXQlR3cR06IaYiez7cBeQ/zh-cn_image_0000002565211445.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=264E49DD5F5FACAF86CD46521A3C81195FE4864222FCFC744C28C31C041F6C2E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sOb8_9WAT1-72HPN0cUjZg/zh-cn_image_0000002534251622.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=12404BCF0720462999B8983DC8B8E691C3DFD3ABCC86C3920AA85BBED7D11ACE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KoQk2RgdSxOqe-vSgKkqHQ/zh-cn_image_0000002534411568.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=14F88A9170DA9ED860114C0457ECB8EC3AFF8BE3F4C730AB4B35CD1E147446F8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/eCMDDMQaQJy8yAdkcnwR7g/zh-cn_image_0000002565291469.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=6BFA67BF029FAFE725D9A0D17A30C754B5D1BC9C321E6C09B7A499D9AAB4BA13) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V2fKSuNPQUmceefgjrkahw/zh-cn_image_0000002565211447.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=40C526F4161F4A8BA40836009FE770A3B7EBC66B8494986EC62A8E353C29E8AC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/1qAyH0vDQ3Caif_VOm6mSg/zh-cn_image_0000002534251624.png?HW-CC-KV=V1&HW-CC-Date=20260401T025556Z&HW-CC-Expire=86400&HW-CC-Sign=EC8143D5223EAB0809962BAF8090FA09AF5DC162B0F510FDD3B2CF6CDF1FDDA1) |
