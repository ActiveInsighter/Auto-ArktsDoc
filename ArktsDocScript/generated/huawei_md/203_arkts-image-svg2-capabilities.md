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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ii-kyNGOSPOMwAq-foHpaA/zh-cn_image_0000002534411520.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9083E8E665953B234116C9AB5710CAB894803904CF9CFB552F26E28046BA7A84) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IZ_5ZBQvT7W89wQIMjwv8Q/zh-cn_image_0000002565291421.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=5F7B201D1088BD9C4F0809A58219B6D95EB0F5F67796E5D4E29F9C1321B7057E) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LVE_4LLeRTSfpd8S0seZug/zh-cn_image_0000002565211399.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=23E4964221F253C4DE947F60639C6473C495C96DAA00933445772246FCA48112) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A72sbB7TTHuWW869yWGdjQ/zh-cn_image_0000002534251576.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=0B1DC158944EE6B66A711D29064625FE55C36E9DE7597067732FB70ADA6C3CB1) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LW4xwmBtTGKE2WoB7sXEkw/zh-cn_image_0000002534411522.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=085FC042B72AE0CBE54DD6F452CA49A50C66AB5F7AB5A741BC37D4CC710908B9) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qstJRj2MSVKsZ3winwkx-w/zh-cn_image_0000002565291423.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=3A0E4D615F4B7C15901D3D90CDFFA8C5D7D8967916641258438A0DA0EAFDDC9E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eiDytSAYTZKZZCWPOB2mgQ/zh-cn_image_0000002565211401.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D46F61F247F479B4078A5C92D49BE46FCBF1054C83C57601626F1B0B8268D316) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/sElyaqdiSq2VMjUYeI-srQ/zh-cn_image_0000002534251578.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9565EF01E4DE9952B7AC4A6E1CC095F4294FCBB74DFB037DD958EE56C3273C31) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/EK38ItASRAKWIwpbCKuVog/zh-cn_image_0000002534411524.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=1A4AD4B2449996F28FF876402D0C43415E2AB8D70C64A676A80AD42DC622ABE0) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4NMB4IbpRZ-FcVDUkbanhQ/zh-cn_image_0000002565291425.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=891177D79375FD38AA08348BB872D21A04F7124A264A5B4937F13F951C4E3EDA) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/F306G7dOSZmMC4OegqcQ9A/zh-cn_image_0000002565211403.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9E91BF0919975F50434EAA43068005433C0FDA32F6A16F50F9DC5FB433C1ED6C) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Bke1AR0jSU6s6rnSNgpTCw/zh-cn_image_0000002534251580.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=2757ADECF8FA9AC320D42D9F0A0446B94E306A5236F554FDDCBE1EF698347642) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hcAO4iYDTWWoPHiOExwgYg/zh-cn_image_0000002534411526.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9A7C598AEBBF933F9A748C01A15B9901B3329346DD0C25B2C38E23A1BB67A8B8) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/2KdZFk0qQ7uH_JSD4jhpAA/zh-cn_image_0000002565291427.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=5797C114B825F3EFC7E2BD1F6B9E6F40B49A808EFD7AE518209453AD1CBA4489) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sh_HjmXhSyimKMaTQI8q2Q/zh-cn_image_0000002565211405.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=504A39596F8460E760EC8F2E3A1AA2F890062871165479DAE7C9354C59C32005) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/JigmDfrpR667kD6GTUcOQg/zh-cn_image_0000002534251582.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4221D8DE5191780F51FB198B0EC85BA39A972D1E9CE4C14B601CFA6BCD64EC57) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DhhYJ8V_RwaLzOrG2pef6g/zh-cn_image_0000002534411528.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F15BBFD1E4D7025327E0FDB7E9433EBBECA1607E7CBBE64F47B50862337CF2A1) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bs1Nyw1oSEalRz2mMKNKzw/zh-cn_image_0000002565291429.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=28A8DB2D2A797266DD7A491454A3400DF38B90EAC8816F6042242268A6054CFB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3920RCa6TnuauqZ4QqYICA/zh-cn_image_0000002565211407.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=2F7E1429E53C257482D83BD74BCA6FD66A6D5171503CE765FCD60525EFE480E1) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/n1KsuxQWRsOgqduN_DWAng/zh-cn_image_0000002534251584.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=14EB4E88B0346D2488524BA028E99504B39F485397520A312F2B5CF95039A869) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NrmtU54qTtOHiS3q8GoOpw/zh-cn_image_0000002534411530.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=66AE7BC1EC72544D56FA0289D5923B3AC9B52EF4D22AD392A08071D67A729071) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GoRJcqUFSUGeWbODwYYa_A/zh-cn_image_0000002565291431.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=72E34A95CA2260F3772191BE7546161981A9CE5E2A48EA30AC036291B69EA2DD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8VSXJ2EPQ7Oxnl4eUjSbpg/zh-cn_image_0000002565211409.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=04057E6A34D7C648F24F893641FA43C4384AB1A6E63172C2305C641B9155DEBF) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yfoy_YdMSFW26uaZgaQ3cQ/zh-cn_image_0000002534251586.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F16CE4C0430B5814F39FE0B0694A284E5AC3ECC3FC866E1C2A940BF2667CD107) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/8QHr7RRvQZafaqyK0PHgvw/zh-cn_image_0000002534411532.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=C61F0222C4982DD60901F7320342975D73E943070B3454F3B66ED6D42229273E) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/76Buxi4tRIK__Pir7TgdBw/zh-cn_image_0000002565291433.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=464093F87C72A9B9C0EDE53FB39F6CD1CE59AE1DF0236CC1000527CD55E4CB58) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Ez_4Qre-TgWCbOJrvJT4Bw/zh-cn_image_0000002565211411.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F97287368B2AFF57AC4ACA3171B276375481F7A080E4C93108A732DB4B8EDE07) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/crwaIsXDT96N-IeYAbW0aw/zh-cn_image_0000002534251588.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=6B9681E7BE5C2FA23D366210342BA0124C58361B56568818004F9744EC4BD486) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DJQkoOb8SSi6fJJxBpVH8Q/zh-cn_image_0000002534411534.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=CCD3442CF83B0D0508DAECEB53480932FC8336E21FC54C5B34AB5C5371C68833) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vmNZSo24SfitNb1mdYo7Yg/zh-cn_image_0000002565291435.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=AEF6522DB2C799B8DD7A310B25F6A8584357E161FFC9C28DDA482A8501A63746) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WSgFDG7BQRy_Whm0iPxGUg/zh-cn_image_0000002565211413.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=5C9663276394AA7E35AB6531642C0F30CEF98DDEE42760B3CEA8749AFB858E3E) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DEynjX8dQOagdzDlHqYe6A/zh-cn_image_0000002534251590.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=28E9116B6DC9C1A7D9FF2407B72612190BE0AC36B1963DF60A418BF4C46888A3) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nSC56eGaSyiz8GITFKiZtQ/zh-cn_image_0000002534411536.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=E7DF72FFAA91487FA887069D525CB1C3F81C9136EB78578D444E6E7BF7099B9D) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vQWoAnqxQ2S_09Air_PyeA/zh-cn_image_0000002565291437.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=1C12060ED91571BCAEB1E47D961B3025249341DFFB1DC41B245BF8C0633DC669) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aRzPA3D6Sru1r0qqT_lbiA/zh-cn_image_0000002565211415.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=C3B211DE743C72B88F85D85B1A4CCEDC45A7F169917581212DB5CA8B043E8E43) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AK6F763hSYSDjwLqQruZhg/zh-cn_image_0000002534251592.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=8B549A87EFD8B5955D633EF04AC8517282FCBE9DB2A49E5F8EE4D8BAA3701FE6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AumZMu5QSn6qmq2YAkgImA/zh-cn_image_0000002534411538.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4618886677C3DD5A8EE309B40E87CD1F9AD1BF541061421F25DA1B0925B028A0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eGt-LIpyTsabAc4MQXW64Q/zh-cn_image_0000002565291439.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=DC66F2471B7E950D6683964CA87CB7FFEC2E54DAA5CCF5A4C4B00764714C9EC8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_-yf95JTTQyZDoalZ667Cw/zh-cn_image_0000002565211417.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=6A95111BEE31C3EB7F3F94D342579D6B29107FE527911A66E91F2CF9424AD233) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/oZC-V7nGRhaw-Zz-3oun2g/zh-cn_image_0000002534251594.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=E8FE9AA4B3D7BC6C5E1A89DDAD00E64CA8E0176678ABEB744A59DDFA59F6D43F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GgPzWsdrRgS0Swq-ZDDDqg/zh-cn_image_0000002534411540.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F70EA8B8CA134C2DEBE0B5905509BCE7AAD5F3709B1394E6A7BE0D65B540FFA5) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/veKhEp8PS9yCxuMXzz89-g/zh-cn_image_0000002565291441.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=033FB394CEBE3729239DCFC982F7B2BD5A78CBCD7BF99DA31B98EAFA5D5D4D33) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Xlm6fTeBTdyzCFbzalofag/zh-cn_image_0000002565211419.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=254AEE20BDE26392D8027D654D2A48CC477F3AE6D3260ED963B1CDE04B7C6A2F) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NunMMI4TQQOBcu80y8JvVg/zh-cn_image_0000002534251596.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=1A18455731174782E928290203AA1D9528E74C9307DB8C3F1D0F120EB3EA511E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9dizZSWlTRG3adRzGSjOOA/zh-cn_image_0000002534411542.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=8934079B0686280D451588BE9F98FABDB34AE732CB34272AE4460D178949B19B) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EQKx3iiqTzmD6YjGLOYXFA/zh-cn_image_0000002565291443.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=A69FB3C56CECB0B6A3842CAFC35325FE17D10F24B9688C3B133850495F2E50B4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1WsXuK5aQnWjJi6xetnWrA/zh-cn_image_0000002565211421.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=B6D9E195E3501D4EF8E2BC326285C4E917CC3C0CB29B8227395A0A81FE6464CF) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uYUS40C6ReaYGs7HPMLS4A/zh-cn_image_0000002534251598.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=39B6B20AA272222293547A932418EC9C557A86D552FC7F6C59FCC5453B745C36) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cHSMm1g8QV-Me6LBPUV40Q/zh-cn_image_0000002534411544.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=7D331263F6305349C022263843409816FA9089C4E10E7EE7BA7DA4674E3FEA52) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_nRJJHFsQKS_FcoMgJ9-Nw/zh-cn_image_0000002565291445.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D167CA68D9ABF1C61A4AC38379BA89AF073C7180ED4D9A3311131BD7F50C2157) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qIKsUZLxQ5eCHEfo_muz0g/zh-cn_image_0000002565211423.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D599FDAE11A917664E35F3C3A3D897009BA5F2CDC4C6AF7273BC107FC4CBB639) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/5ZPdsFE7TEKAEpQiijvQLw/zh-cn_image_0000002534251600.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9AC30927AF0DE93E7FCEBC417038B965B263E74396356B417CA2E92BC2FF0128) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vYljLAQvQ9OZsXQpKsgM4A/zh-cn_image_0000002534411546.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D09479F938D70CCD7CE27F5064828FD8EA271830E01572CAE8A0B92020870B77) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/52HZkPiCR1SL_e7NYaf-ug/zh-cn_image_0000002565291447.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=EE554B8BB5C131C7AEF26C59AD697B22AB435120038253E8456CC462957D7290) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FC8C-rupS9qRw9ymJcR-RQ/zh-cn_image_0000002565211425.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=C35216F3CC7EEB879AB325275B00FEEC2EC50ADCE4A08CA398B15FBC08E79B8E) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G14KchPeRRuW3rHCaVAp0Q/zh-cn_image_0000002534251602.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=5DE03EBC397681BADB99AADF3F14369328A92E9E9C94490FB22E13B5109C088B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gBxz3uJbSTmQF7OESWFZcg/zh-cn_image_0000002534411548.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4C6A412ED995710BC488BABB22B431174A1D5AF7885054270C0313A48A972340) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QEr0qsK_TU6E6zWy0wiFfQ/zh-cn_image_0000002565291449.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F066B79CC72D687056495BE01B9ACA480C28BCF7813EF841A0EDDDB70BB13FD4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_HCxlBGaRdadDF1OOOoptg/zh-cn_image_0000002565211427.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=51C4620011E222C2F7F607C25D0163627209D468020432E4BCDAA21B20FF9F24) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/oO6TyryNTuiU1ImCdgdRQw/zh-cn_image_0000002534251604.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=37A3F32C8D3FF5C2A863D477AE5C3794AA153ABF15B83B5D552DB7C7F67DA7D6) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WyNCM8-2Q76PjHhF6DDFaw/zh-cn_image_0000002534411550.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D112E2585AA428A11084A1FA5BD67D10D9FD5658A253004BBB8CE435FB8A81E8) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ItI9jH7hQyK-e2jr4f-U8g/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=112E0942869F9F29C74199E690B39E1EED4116E0E8193D292D0B453A965CDECA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1z6iQdJfSZiGfwxO0-X6Dg/zh-cn_image_0000002565211429.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=49F1FD38FED3274A540B543229E33F03D9F4CCDAF5183A84D8542ADA3A8810AC) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4yMyaYbpTyuR9cBmW5L91w/zh-cn_image_0000002534251606.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4B5DC998B1E153D231B68CBF1E683164C582398593F9ABE5EEF0615576A07F0A) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/59ZiPuz4QXe1rzLmFktNGA/zh-cn_image_0000002534411552.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=93FB7B9C6AA6EFC37A897133139E74AE4E7B12E9CC01DCBCB8F1B3FC63DFB12D) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MpfXLUq9SbS5Jvu6n06cWw/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=E2750411CC975B2D503BD15CFCA851A8EBC5504017E754154A96DD9F37CF8638) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/tiGGbyfxRtOYYvpk9Hro1A/zh-cn_image_0000002565291453.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9842F69B8CDB1F6873B559AE6EE9A83B58812269B18B25A07A8D21A19ACE00E8) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yBCtH7JLSsuV5cR4z-raMQ/zh-cn_image_0000002565211431.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D59D61292D55A3295EC4AF33BBA170EE9FD25D723E526A5BF852BC5B5BD80190) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/k1yWcafmSEmEMXe9Lr4W9Q/zh-cn_image_0000002534251608.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=2E97BD4FD14F840DB096867B79D32115A9A143B35E7CA79B4290048AF564E25D) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7NwI1coDQXqISDHeiNpJOA/zh-cn_image_0000002534411554.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=619FB1DE5CCE96865F6EB55797C6E178CAC64AB025CDB62605F4A7FD94F916EB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ST5XGG9eQZmb3g48GkY17w/zh-cn_image_0000002565291455.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=7A38302C3711C8847277453B3324D2E74F2E63BA5EAD4019B6EEE2E67D998EBA) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5LYlOjNmTZ-FucsQU70VIQ/zh-cn_image_0000002565211433.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=6E92E56B126E5AA69FAB524626DC5291ACD55A44996A5BF17370CB26527F81BA) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuhAU9IlSDWFuGr0FU53bw/zh-cn_image_0000002534251610.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=F318D058B7F062AAA4589ABB3672F7F8369E16CA3E5F70E91B66775EA3218EBC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gf4tXK1KSD2XtIVjOP-9Dw/zh-cn_image_0000002534411556.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=697BA5762D732134FAD5B51EB2F9D9BF7D035141923EEB2635CE0178CE4D5470) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/V4FSyf_SSwKGTr9yCRUg9g/zh-cn_image_0000002565291457.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=65926C91B08F2C419AAF2CE6BB1358F75FDA86C918E28CC941AA8F5E84DB5451) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/kdMZMjmRTj6nGHYBVUXwYw/zh-cn_image_0000002565211435.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=A2ED0667DB86ABC8EC51F07CAAF0EACD54E6180AF3F40873EB7146DC12300F29) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xb-R39t4QAC0OsF5lWyHDg/zh-cn_image_0000002534251612.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9D0682D1312086B39C1EB4D02F40ACB7644F914EB4318F49C1E8FB49CAED808F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HnoQfmW2Ri6e5K1ffwWzaw/zh-cn_image_0000002534411558.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9374EDB10A84748E2FBDA7F33764B827F1B7CBB139905E03ABE44DDD61614003) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wlZk-6epTIekWZYIeCO-3A/zh-cn_image_0000002565291459.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=EB2A6937F35F050D08CBA830B5C09FBB554B994BD052BB22D2329A4D3506B9BF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2uZs4Q6pTJ2qFE87i-cJzA/zh-cn_image_0000002565211437.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=546CA3053E85A14E404A4802336DA3AF77789DE83F193762B2004DB7B06DD363) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O5OWYVKpTEiIo047460RsQ/zh-cn_image_0000002534251614.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=88BB3BE1353AFF997103F394D28540A41E1C11181D94A66DA98B0BC3CAD2771E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Md_YXiTOSE-xtLVUZ_CYhg/zh-cn_image_0000002534411560.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=E5DC5EA58F7E47BE48396293EF3C6CEE6885A026C7B7E2996E1D3166A734DB6B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kFb6hRscTIiHIVztiqZMjg/zh-cn_image_0000002565291461.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4A3EBCB41100A480E0E2B8FF19BF14DAA32624D192017D9F08B16648DDBDC7A7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/pTh56Ja-SJ6FQHgb6lzWSA/zh-cn_image_0000002565211439.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=17754520CF83FC2C0EB3A16C8F9BA5091F3857452AD667EB24997CA197866ED1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vMGeYhcRSZCB-qVDJDKCpg/zh-cn_image_0000002534251616.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=FE0C08ED8F1C9164573123BA2B8CB5BD094B7B972FD060ADAA7084A5E12F30E6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nqUcPMrKQSCVCtwTZg92Gg/zh-cn_image_0000002534411562.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=9C542A93A58E60B40BFF12390FC89D88F1FEE0D7260B841C5E4C4B1B373436E8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O8vSOm-hQFGFkpq1e5u1ZQ/zh-cn_image_0000002565291463.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=052ECA67FC9C6ED09A5382C2AA716FB94AB25646FAF9C3854A50B5B5149184A5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6uplnqqAQTmApsGDeqBpxg/zh-cn_image_0000002565211441.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=C6B954E5120BBCC63BAE4306DE26F765ABBA66AD5784FAEC4FC7ED914543F2AE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/I_rnRsxzSpGxBEwjN1XU8g/zh-cn_image_0000002534251618.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=79B4D6ED8B5898F8A756A09311F43C71BD1FA0BDEF9AEA54F71C29D4E999425E) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lXHCjT4eSV6w8LQaMbopvw/zh-cn_image_0000002534411564.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=4893BA46A120247B3B57E37B8194B3077A0E3D1534C35BE69766279C70182A3B) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SJhv0EWETuWxFXXqwPiRkg/zh-cn_image_0000002565291465.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D3A05D2341F9D97F64D064180C36A3BD40430E260B5A5AE055F78889E1E30F52) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Up-SzE_rT5KMvJAw-WuYeg/zh-cn_image_0000002565211443.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=1CB3DA8069B18C7FE818E6351CCD6778984ACE2934AA60F3AB1A068E9FEC7B7F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qT0NlbsyQE27uHHYdWm95w/zh-cn_image_0000002534251620.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=892F74D45616967BFFDFDF8D7CCCE274740C768B81E2B1BC95B3BD5F00D83F44) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qqxSsYC5TcuLwNBiEKfLjw/zh-cn_image_0000002534411566.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=E11EF539C81FE8AA02C5C24762ABA0F8DD379A1D0F022722E426F48A8F452C40) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WdYtIMmgQlaRxBupL9XHqA/zh-cn_image_0000002565291467.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=1368B7B62A3863839FCD6A3E8C00F0ED2C98F7B73D6508580902E304D38E2C8C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/irXQlR3cR06IaYiez7cBeQ/zh-cn_image_0000002565211445.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=C149ED058B5DAC78AB1B66A1D573E54D51C7989758863B08545F45EED6E0C71C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sOb8_9WAT1-72HPN0cUjZg/zh-cn_image_0000002534251622.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=25006A89AF529C1D95ABEA74A0C8FBAE913FC882F3600C724FF238DF78986A14) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KoQk2RgdSxOqe-vSgKkqHQ/zh-cn_image_0000002534411568.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=5DAB3A77864D2C52F3C3071993619384A73790704775264AFF2321DD09A7AABB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/eCMDDMQaQJy8yAdkcnwR7g/zh-cn_image_0000002565291469.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=35A3023E85A9EBC551790418FE1CCDEB0AFC3CE668E4AC6BA80B6C4968796F4E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V2fKSuNPQUmceefgjrkahw/zh-cn_image_0000002565211447.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=D6518BAD35E684BE4EA64B42A283DC65806F3E339B49606B23DB0DBD65764B2B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/1qAyH0vDQ3Caif_VOm6mSg/zh-cn_image_0000002534251624.png?HW-CC-KV=V1&HW-CC-Date=20260330T121842Z&HW-CC-Expire=86400&HW-CC-Sign=EF5BE70870AF8DA7C87E635385AC412E194095079A6714D5409CCFFB8D0C353E) |
