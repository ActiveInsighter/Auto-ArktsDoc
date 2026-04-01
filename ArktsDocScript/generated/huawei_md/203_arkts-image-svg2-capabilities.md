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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ii-kyNGOSPOMwAq-foHpaA/zh-cn_image_0000002534411520.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=6A93C5E94BB57C135D97F8FD1DBCC1861CE0766C81AA10D3BF90D24B911BA844) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IZ_5ZBQvT7W89wQIMjwv8Q/zh-cn_image_0000002565291421.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=DC2B1D8002C42E0D831EA3F3816B327B93720813A17089ECA7E875294E3F0ECC) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LVE_4LLeRTSfpd8S0seZug/zh-cn_image_0000002565211399.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=CD8B49ED54216F51FB67DB3218CFEFAD2E2C58A75795297261A871A662A7AFA5) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A72sbB7TTHuWW869yWGdjQ/zh-cn_image_0000002534251576.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=4325348A85DF315B66C636E316F304377A062E1364527565CBB252BEEC7BC6A0) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LW4xwmBtTGKE2WoB7sXEkw/zh-cn_image_0000002534411522.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=B981DAA5C5EF58CBADF7A33BFB2930C5EF442A429E6D7A3E1362AB9B610CB8A3) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qstJRj2MSVKsZ3winwkx-w/zh-cn_image_0000002565291423.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=4AB5C3C120E8CBD6FE43F3029D1DD13F0345349719B08451B56960E398511BDE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eiDytSAYTZKZZCWPOB2mgQ/zh-cn_image_0000002565211401.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=FA147A15CB04CE37332C19787DA16180E4D1205F03323A59DBE1E7DA931717C7) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/sElyaqdiSq2VMjUYeI-srQ/zh-cn_image_0000002534251578.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=50E6AC90BBEE60503E97DDABA1E822D85F764EC9A41F8A525708C0582AAB1A8F) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/EK38ItASRAKWIwpbCKuVog/zh-cn_image_0000002534411524.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5D5A00931CB3C9F6DE2FB6AF4A32D50F451EC4D6C8C6F9801BFD003EA7EE673B) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4NMB4IbpRZ-FcVDUkbanhQ/zh-cn_image_0000002565291425.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=AE583E47C3C8D5CA4DA1B3E9350CF617F5AAD86F2E6913B2D50994A3C7D6C16D) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/F306G7dOSZmMC4OegqcQ9A/zh-cn_image_0000002565211403.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=7F8612708F2F2E2CD4883455DC2149222AA53A51CD9A8738FB5F5356A3927AF3) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Bke1AR0jSU6s6rnSNgpTCw/zh-cn_image_0000002534251580.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=7A31C8B9BBF480BF50BBEA52EF1D6B9064FEB3DF01BDD31796BBB1DB97BBFE14) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hcAO4iYDTWWoPHiOExwgYg/zh-cn_image_0000002534411526.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=A7DBCC38DF1EAE7D85BAEE39CEEA061441A698887E380086A6E2998496382C85) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/2KdZFk0qQ7uH_JSD4jhpAA/zh-cn_image_0000002565291427.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=733D54CCBD0E3D90F8ADAB0FACB3A8458BF7E991025D20BC678C9534763175F1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sh_HjmXhSyimKMaTQI8q2Q/zh-cn_image_0000002565211405.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=80AF5B0C00649B5EE9D5F39C1CB5BA4871DB9FE2DFE2B1B3AA6721FE29AA7195) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/JigmDfrpR667kD6GTUcOQg/zh-cn_image_0000002534251582.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=A83B3839A035C721FCF657655AEAFCD7B47C9F5A684C4512A36C681A3E597672) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DhhYJ8V_RwaLzOrG2pef6g/zh-cn_image_0000002534411528.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=9028D0C4C5A276C2C3EF0BF0008F1D449E88EA73B677A234C1D2320D84FAE646) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bs1Nyw1oSEalRz2mMKNKzw/zh-cn_image_0000002565291429.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=E028972102E0326F84D450E2F21DE15FE7F28BB92B5DE11F4AF1A34076C2334B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3920RCa6TnuauqZ4QqYICA/zh-cn_image_0000002565211407.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=F23D49CBD922A7467796858179A1E8E123A85CD6DA748F2B1CA63C0CD38B9436) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/n1KsuxQWRsOgqduN_DWAng/zh-cn_image_0000002534251584.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=1059F89700A94851D0E8C47AD4CB6AA9CC698D3F38F098E617CB9EFCFC3EFC18) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NrmtU54qTtOHiS3q8GoOpw/zh-cn_image_0000002534411530.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=339B1848EE8C5C24BB32269071FA8907E3A93EFE9B33A1EBA3F235CEB9B61824) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GoRJcqUFSUGeWbODwYYa_A/zh-cn_image_0000002565291431.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=76BED7670899588458EA309BF6784D8EEFBA2FD2D8CCED8727B3B2B498875F85) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8VSXJ2EPQ7Oxnl4eUjSbpg/zh-cn_image_0000002565211409.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=48E1172BC7DBE68DAD88370AE58D64341638AD3C721705B757067606E539FCA0) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yfoy_YdMSFW26uaZgaQ3cQ/zh-cn_image_0000002534251586.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=8A8C7D5F825D07AE73D588A097B07996B0905BFEF9A9EA9C2C98A67929EA6C68) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/8QHr7RRvQZafaqyK0PHgvw/zh-cn_image_0000002534411532.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=70C6813EDB2B46C5753B8CD151F5EF18EB6FE29620533B7A6984D9136B73FBE9) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/76Buxi4tRIK__Pir7TgdBw/zh-cn_image_0000002565291433.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=BF3523146ADF9F5FECA8925E95E334B3B4C4F7AAE21CFED0EA32DDF01E967BD5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Ez_4Qre-TgWCbOJrvJT4Bw/zh-cn_image_0000002565211411.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=8B62A29A99BEF845BC1FEE6B5B411FBBDF7BFB225124967E5EDFD2770F6BF0FA) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/crwaIsXDT96N-IeYAbW0aw/zh-cn_image_0000002534251588.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=BAA0D0E4551C9F753E7F800F1142BE89A1336DA22D48A249ADE96DED31FB5849) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DJQkoOb8SSi6fJJxBpVH8Q/zh-cn_image_0000002534411534.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=8C2CA2F26F109A2586EC02EFEED239943C3BEEFF9DB1BAF5FABD427E1BF70771) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vmNZSo24SfitNb1mdYo7Yg/zh-cn_image_0000002565291435.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=19A4BBDF1EF79EBB7084958FC30D6ED21C50FBB196B460CEF9DACA24917F87F0) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WSgFDG7BQRy_Whm0iPxGUg/zh-cn_image_0000002565211413.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=071A081F8A9513E142B7AA22BEB2CB82780F7A9C208BBA413B8FA2DF70505B97) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DEynjX8dQOagdzDlHqYe6A/zh-cn_image_0000002534251590.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=3E4F84FE1D85ACA2E7DDD39A387C72B1DF096903FA442CAD7EA61C3085DB627B) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nSC56eGaSyiz8GITFKiZtQ/zh-cn_image_0000002534411536.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=335FBA59BD6CB141652F3F8F6104D5181706AC849CE93C8D3D75650F089B367D) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vQWoAnqxQ2S_09Air_PyeA/zh-cn_image_0000002565291437.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=587E1A355B4D96F0147010C445C2EBAA4B9A402F1201A1E963F33D02274A612D) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aRzPA3D6Sru1r0qqT_lbiA/zh-cn_image_0000002565211415.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=78487BCEF8C9B222BD4D50B9609717DE28C47EB165B8C842ED0E95A4E391EC35) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AK6F763hSYSDjwLqQruZhg/zh-cn_image_0000002534251592.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=2B11A2C41AA8D371E8C5B90C5A5A0C22A0B5F1A14B875BCA71C11451F1DBA0B4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AumZMu5QSn6qmq2YAkgImA/zh-cn_image_0000002534411538.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=292BA87A5C66057F4A071BBEA19AF88A3A5E792B73093893D3AEE252FB8F75A5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eGt-LIpyTsabAc4MQXW64Q/zh-cn_image_0000002565291439.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=417C7EF3BC3E16BE69A0A9A71AEE7C9F4BA459C3DAD6B2A7112B4645BF8B9592) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_-yf95JTTQyZDoalZ667Cw/zh-cn_image_0000002565211417.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=084B2147A1DC59BF83FB1A29420BFB204F663DD5C7CF782BF056DD3789128446) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/oZC-V7nGRhaw-Zz-3oun2g/zh-cn_image_0000002534251594.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=1E6D28968F6132731B328CBE3CB548FA375AF606A7E7E39872F8F32BF3EDE82C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GgPzWsdrRgS0Swq-ZDDDqg/zh-cn_image_0000002534411540.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5BCB64E8AB7E61AC5FBAAF65D99F5466588E6B5DF1F10DDA585F750CCC20594F) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/veKhEp8PS9yCxuMXzz89-g/zh-cn_image_0000002565291441.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=CFA86E81AE475AEF3F40AF5C23DC7C49950C285B3F6F305E2C0C8CD77207F166) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Xlm6fTeBTdyzCFbzalofag/zh-cn_image_0000002565211419.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5DBE003593F3FBAB004715A3AD32479EB3C38E807312F39611BA5216065E7ED0) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NunMMI4TQQOBcu80y8JvVg/zh-cn_image_0000002534251596.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=14FE70BE4AD1BFF78D05060E27E549F30AE0065B35978BEA12E037C7F383116E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9dizZSWlTRG3adRzGSjOOA/zh-cn_image_0000002534411542.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=C14E76DFBF5B2E771EF40368A3129D12404E41CDD9A2C9A9F63F366E0FD3150E) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EQKx3iiqTzmD6YjGLOYXFA/zh-cn_image_0000002565291443.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=2EC7FD030556BFB7652054E37A646E0E2C3300E6CE91F32F5A01397239DC5C3A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1WsXuK5aQnWjJi6xetnWrA/zh-cn_image_0000002565211421.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=63F0F907FA368B180B560683B17A05B2894996D183AEA1E9A5A09B439E1952ED) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uYUS40C6ReaYGs7HPMLS4A/zh-cn_image_0000002534251598.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=8DDC55034D0E101C3172195F7DE66728A4CD4963C3F29B82D91639B5363A6719) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cHSMm1g8QV-Me6LBPUV40Q/zh-cn_image_0000002534411544.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=EDE74523BB4DD333548287E9F0566B1CA44D9814282BDC4C98B59D47765AAAEC) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_nRJJHFsQKS_FcoMgJ9-Nw/zh-cn_image_0000002565291445.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=16C23B24A7684289BE82E4A9549F82997A7905F1311E8F58042B13E46E781770) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qIKsUZLxQ5eCHEfo_muz0g/zh-cn_image_0000002565211423.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=CEFCB968201794D8F6EFF640087EFBA7A994F947F25B6417EF0BAEC12D190A88) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/5ZPdsFE7TEKAEpQiijvQLw/zh-cn_image_0000002534251600.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=57834D3D4EA2CDEF1A117C92BDACE186806627359702425C002288AECD711B9C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vYljLAQvQ9OZsXQpKsgM4A/zh-cn_image_0000002534411546.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=CF6E58CAD35BD1B0541918EF4D8546977201A30C2DAAC2131FEBBCADB164A2EC) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/52HZkPiCR1SL_e7NYaf-ug/zh-cn_image_0000002565291447.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=164C99D7E7314809EE841F4A497324235DB81FCA8B23FC16D5AB6D2C0132941B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FC8C-rupS9qRw9ymJcR-RQ/zh-cn_image_0000002565211425.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=AF635571A333F50471D875D0084A8DD74B4D111ABC7B8679F95642EC77951295) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G14KchPeRRuW3rHCaVAp0Q/zh-cn_image_0000002534251602.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=D6DD26D39CD56C52BEAD181B33B0E3AD85A2DA09E9B2904076022CB5ECEF0943) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gBxz3uJbSTmQF7OESWFZcg/zh-cn_image_0000002534411548.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=918727D806A6D2F426D9A6F649BBBEE87205DB57BC510E2C8AC9BEE94B8D4753) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QEr0qsK_TU6E6zWy0wiFfQ/zh-cn_image_0000002565291449.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=7771F62585B50E8A25F0AC0A038080E39C53126119000A85DB8BFDD061A4F7DA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_HCxlBGaRdadDF1OOOoptg/zh-cn_image_0000002565211427.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=72C6CB79A2C496096D62B797134E196C0335F8AED1004635AC7AA8A09C449524) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/oO6TyryNTuiU1ImCdgdRQw/zh-cn_image_0000002534251604.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=6CF3DCD660B85180C52E0BFFD77FCDECC9A2E70E7AABE9F9E0BA53DC1FFBAA82) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WyNCM8-2Q76PjHhF6DDFaw/zh-cn_image_0000002534411550.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=6B699196A2E83F2AA9D52CE9FB5D115AA0F3ADFF7E5D1A23CE62739C1225F5BF) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ItI9jH7hQyK-e2jr4f-U8g/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=0C94A094EFBE726343C17273B0C1D18FB21B2CE088741ACA7FBB657E124EE052) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1z6iQdJfSZiGfwxO0-X6Dg/zh-cn_image_0000002565211429.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=4FF988D1C07FDD0F3229D8362E2552D586591BFFF2F2273CEE7FAEAF6CDD85FC) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4yMyaYbpTyuR9cBmW5L91w/zh-cn_image_0000002534251606.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=172B914CB5FADBB172398032C93E3B9C551EAD83D7FF4D74CF3976FC9B321658) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/59ZiPuz4QXe1rzLmFktNGA/zh-cn_image_0000002534411552.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=CC4D25FB56B269832D70C1A3D6FF619E19A7B92981CAD9D57470F1E5CEEF5B9A) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MpfXLUq9SbS5Jvu6n06cWw/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=DCB0231FDE4765D49859DA7214F3DBB60071565578F8BE145A90BE603101AB8E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/tiGGbyfxRtOYYvpk9Hro1A/zh-cn_image_0000002565291453.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=4FA2AC3DA1B87574C877C92055156E379EE84494B08E44B9FDCC4FE5412015F7) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yBCtH7JLSsuV5cR4z-raMQ/zh-cn_image_0000002565211431.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5B21B32C9D5C912E4BFA823DAF1753DA34F1C66FB9627C926F30F14C8CCB20FE) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/k1yWcafmSEmEMXe9Lr4W9Q/zh-cn_image_0000002534251608.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=6F789DF6468D9DDE47A4834F941B9EF7A04F497D3A4FD036DD2FD2132EFCD14C) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7NwI1coDQXqISDHeiNpJOA/zh-cn_image_0000002534411554.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=E1DD156B92A5674506D2D857CD9B492BFD4176B430EB6C8B7CEB551F95E5985F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ST5XGG9eQZmb3g48GkY17w/zh-cn_image_0000002565291455.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5325188EE42EF1DA84FB542F64F94FD77ECA981094A800EB75B4AF895161001C) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5LYlOjNmTZ-FucsQU70VIQ/zh-cn_image_0000002565211433.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=9E8065D46EACA220F19A3AFF6B4041A5C4C980E90B945255AC59BE68E8B76FBF) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuhAU9IlSDWFuGr0FU53bw/zh-cn_image_0000002534251610.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=D54181976E8F0FD8C54A11535659D0E938D1A4D220B57876728D4E6FD482AB4C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gf4tXK1KSD2XtIVjOP-9Dw/zh-cn_image_0000002534411556.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=A36BDEC753D2F3A238790CA1F1A833D5CB9FD13D0C96DEA7CF1F8A51B53118B1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/V4FSyf_SSwKGTr9yCRUg9g/zh-cn_image_0000002565291457.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=5A5811480147D373A5A69EDEBBBBA926BDB62E505811D0DA2E8594AA35C65F16) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/kdMZMjmRTj6nGHYBVUXwYw/zh-cn_image_0000002565211435.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=87CF6CB6114B73D9E7CD114F5B49935A41B0CCCC6D96C968CFB4228CB1FC0EC3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xb-R39t4QAC0OsF5lWyHDg/zh-cn_image_0000002534251612.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=6881469E446B984903AC9EAEEC46F9B77BAAC3FEAC6AEF36C6A35D7D4EC986A3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HnoQfmW2Ri6e5K1ffwWzaw/zh-cn_image_0000002534411558.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=F6EA249A90FA32E1AC9EEA4771BC5D6741B028361DAFBA78E41B1AF7D9AFD1A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wlZk-6epTIekWZYIeCO-3A/zh-cn_image_0000002565291459.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=3B721338D7A1A85C01C5D329FE4A5656FEB041718AACD1703CAF87C5BA38DB77) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2uZs4Q6pTJ2qFE87i-cJzA/zh-cn_image_0000002565211437.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=29CAEDA06FE7729AAC50C4A9851B0E4011D13CC1F686645FE87404D06F16DF58) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O5OWYVKpTEiIo047460RsQ/zh-cn_image_0000002534251614.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=573EB94DAAD226BB1CA7C7EE3C23057B06451137893E309BC42ECCCD2D45EC6C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Md_YXiTOSE-xtLVUZ_CYhg/zh-cn_image_0000002534411560.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=1CBDDBAA25F04BFEE1A2248100126DF8347D6F50EBC0E1F4BE8F760A0584F6FD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kFb6hRscTIiHIVztiqZMjg/zh-cn_image_0000002565291461.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=89E4498D6EA1F77D3203F1B0739C713C8B499412E3F112C0190BE1491619A40B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/pTh56Ja-SJ6FQHgb6lzWSA/zh-cn_image_0000002565211439.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=C7C7ECAA445E1721672CC99B00C84A510D897BE071227B4AB3B664F37574E84B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vMGeYhcRSZCB-qVDJDKCpg/zh-cn_image_0000002534251616.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=D3EBF3C59CD88FAFEBFC3F7B2E5886E8411885913F2FD98BDE985E8FDF00FA62) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nqUcPMrKQSCVCtwTZg92Gg/zh-cn_image_0000002534411562.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=49940E9A19CD6A1C714F1A862436236A36449051400AFD0AF9B40C3FC82072B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O8vSOm-hQFGFkpq1e5u1ZQ/zh-cn_image_0000002565291463.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=0558FC728270338138EBD69852369DF449FB1E3F7D03670E0B571A239D22ED6D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6uplnqqAQTmApsGDeqBpxg/zh-cn_image_0000002565211441.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=37CAD86F4A17E9960EA49B50D61190E880F04E317632505EFE1F252315E3292A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/I_rnRsxzSpGxBEwjN1XU8g/zh-cn_image_0000002534251618.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=2CABE7FDE3498FEF01F2A59ED924AF264A63B1152A6B0B7C8384823A52C70D59) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lXHCjT4eSV6w8LQaMbopvw/zh-cn_image_0000002534411564.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=9D4118E58CD9E5F821ACF1C23952D926EC28FA660C4519F03B7532D29DEFD018) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SJhv0EWETuWxFXXqwPiRkg/zh-cn_image_0000002565291465.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=96BEEBFDD6D6203A38372AD5F0DD08DDA09F86B511A2E48B5D9CF4EA83001FF8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Up-SzE_rT5KMvJAw-WuYeg/zh-cn_image_0000002565211443.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=32923F520562E2DA99B7F12C426B4D708A044D60829E4EF219BF98C63DA9A7D6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qT0NlbsyQE27uHHYdWm95w/zh-cn_image_0000002534251620.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=09CA83CF9B9EB4CB370042B891B84479A66547D43EF66D785DEFEC02AD4B29C2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qqxSsYC5TcuLwNBiEKfLjw/zh-cn_image_0000002534411566.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=DBF5EB5F83B5C7D3D822E076F95A7F9548E542EF17F1F6BB0D9F17DAB5B4EDC1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WdYtIMmgQlaRxBupL9XHqA/zh-cn_image_0000002565291467.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=564FA939386224E80DBEAE7A3BF2873625D5E926422C29FE017F7577557D96BA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/irXQlR3cR06IaYiez7cBeQ/zh-cn_image_0000002565211445.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=202687D0F9A63537EB4CDDD665B1AC216CC1BE70DCA1F019B60F59E82DD25177) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sOb8_9WAT1-72HPN0cUjZg/zh-cn_image_0000002534251622.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=C75D6C965B63F853A8444A7448500A01E6BD2C0220C41EA5014C5E248DD09C9F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KoQk2RgdSxOqe-vSgKkqHQ/zh-cn_image_0000002534411568.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=0A912B8336525F4D05A516CE85AA23E7A2AC4162771A49F2340E1477EE126BF8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/eCMDDMQaQJy8yAdkcnwR7g/zh-cn_image_0000002565291469.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=179F32407FB028499CB6BE16E37D80A5B8AFF7DFCEFD610B2635AEBED2C10ECF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V2fKSuNPQUmceefgjrkahw/zh-cn_image_0000002565211447.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=21A1F12314750F81F920705B308096B42AD1E986385A11854D4A58FAD2901625) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/1qAyH0vDQ3Caif_VOm6mSg/zh-cn_image_0000002534251624.png?HW-CC-KV=V1&HW-CC-Date=20260401T133139Z&HW-CC-Expire=86400&HW-CC-Sign=53D35A74E5F8F30D8AB28EED0A9D9A0D4E8247B33F3BFDD1291E1141E71B0076) |
