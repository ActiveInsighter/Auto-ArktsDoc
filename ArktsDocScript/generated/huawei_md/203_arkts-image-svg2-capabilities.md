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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/45xyL-rsQI6AOzbrMee5Nw/zh-cn_image_0000002568253825.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=05E5309443B28E08769C848F119A6D2B1559BD2B356BFE9CA8032364A568C939) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/7FvzF9BkTNuKIdKUmSHkKw/zh-cn_image_0000002537174116.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=372072FC5720FC6BADD169333BAB5B95EDA71ADD370A733D39A1DB954C495B5F) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/42tSgV35RPKcd5m0lmAkRQ/zh-cn_image_0000002537334036.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=97C5ACE8C0059BCADB197AE23B88C2F3AE9AB98ED66571D602E26D369C99B731) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/77UEboWMQAChwyeHzvUwiQ/zh-cn_image_0000002568173831.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=F887644FEF1E8AC638C1E1DF92E96AD4499E3D5B2CF5428CC8E16CAD1DFB53ED) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/aSsW3slBQCSCmh8exE2xbg/zh-cn_image_0000002568253827.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=C0F650DAD075B9002906C656135F179ADCF153AB3EC2A12C152EA1A8F92DFA83) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Nd-o7YLxTp2WwVyCq6C8yQ/zh-cn_image_0000002537174118.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=68301A936189F4EFB0F4F69A72C4006355D8B815D3EFCD98F13E167602DA59E1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/CAn_uCAwQ76f5bLBjY3a0w/zh-cn_image_0000002537334038.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1FB4955C21928CAE9373E5CA292771C9748FA6C38F314AAAE67CEC42DC64984D) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/otQWout1Qb2Daf068iDnEw/zh-cn_image_0000002568173833.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1660B834B4FE8867EDD0614ACA9EA9F7E6627A4F39283EDAE32589E98BCBF110) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/aAb_OuRqQBy7YFniWynN3w/zh-cn_image_0000002568253829.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=C2081BA32A0C41CC3AFEE4AAFE47D26826ED7B7A7AC828A2B5028BE57D3BADA8) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VYQ96kwFTuC8zSLdK9BkhQ/zh-cn_image_0000002537174120.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=B9E5FB9B52D024606B3624D0FF6177C06B4A1ABA1BB0EF12307D9C3AD30EAFA0) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/12kbammoSC-7NXCgtCKf0g/zh-cn_image_0000002537334040.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=96F96E22FC126DA88A784B56941C8023D5DD400E32A99EF738C35893526B7E52) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/2WE-_0uST9OtmFUx1IygeQ/zh-cn_image_0000002568173835.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=8277FA96BB8DE5EA6450A3DB481D18248B4F55E6317BDA4E742CC22D52394ED5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/YSe307DLSXC4JzJKV6eLWw/zh-cn_image_0000002568253831.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1CF211391AF01BA052F7D1FF319723A7EB75210F2A924ABFEEA811BF79B19CB9) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/pAeefupETkufOKbhOMme3g/zh-cn_image_0000002537174122.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=8C7DDEC4258F09BA3927C600686FF71B6B37B776724572C0999C68BC2B30560D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uvocXxb0SL-17lpaM0y5Rg/zh-cn_image_0000002537334042.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=4B3E1E5D9FF33C97587CFD8C91BCC30D57BF31E01647A9720F3F2A81383CEF17) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/08YrSa2dQl2sBHkBDHUNfQ/zh-cn_image_0000002568173837.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0CC902A9BBCC3C87CB3F1F263B29CD484701B52A93A1A59DD9AA650EA0B5F035) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ICzzwrMmRL6d7l2YHgB8PQ/zh-cn_image_0000002568253833.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=73DE6AD035A9DA6BDDDFA6D52F4C120DB6A1EC2E4752C690F90BE67E45C0CCF0) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/g_q8khm-QdaJ351XeOHo9g/zh-cn_image_0000002537174124.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D1C464F1281024A756753279E85349F4C3B1C7F48CA772C3678E5FB4C728C9F2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/--8uK_3RQry0HjvWxpXqIg/zh-cn_image_0000002537334044.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=4DA34FED23E22E02A08944069FB13A6F30E328A9FB2C143340627E9B53A139F0) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ocL9M-suQmChE1r_pZM6Iw/zh-cn_image_0000002568173839.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=7F194579964C3443176FA2DEBCD896079CFC036EDA8E0544FAF6BDBA6C375119) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8U1jVOSWTdKEShTiRpUhzA/zh-cn_image_0000002568253835.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=AABECD82320891DBC5B7E7F018C1CFD3D0843E8EE034187A0464B28557429282) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/vn6im5O9SQWxqKo_eE4uqw/zh-cn_image_0000002537174126.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D61318FF6B3A1608AAF54F94DA01E40E3F1B6B8E6D3065BF8520BFFA0EFF0EC2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/M_F5hzY1SHeRSUUZC2ITDw/zh-cn_image_0000002537334046.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1FD5081D25A782D343A04BAC7B78ED130B60FD524B80E565A06E6D448FB53B97) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/krYvY2UuSKiWEswtdsMS1g/zh-cn_image_0000002568173841.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=33F93AC10AA3C7DEDC020B70317B497688DC5BE2DFC00A1DF219013A3A55BE5A) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/xHMHF4dsT0qdRcHZfW9FuA/zh-cn_image_0000002568253837.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0540CAE848A47CF0E7F3DE9E51F62DFDB20D646C3DE3ED8B3237CC75597BC7CE) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/lvKWyZbVRjaedYnIiNfSTw/zh-cn_image_0000002537174128.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=EEF16A0CB2B03166D513B599FFFF37160DE196AD3DC981B602B1BE9490891E37) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/umyDKDlxR7-wEPpdOCJdAw/zh-cn_image_0000002537334048.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=878603683477736BC76E82B5CBD983BD012544789C87E42A76E326A2908EFB19) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/c6nM60LISVCFrLSao64HfQ/zh-cn_image_0000002568173843.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=8BA11A5A9EE06BE7680398CCBB5699BD2695EDB1A49991D963B52ED6A72E4EC1) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/iUPeLv0KTXak8uxl4cCgGQ/zh-cn_image_0000002568253839.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=8060913BBBA2DCD3D0438500C47CFAB15A60C52456557192CFE314BAA7E01AB2) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/oX5aZxAgS3SM3pBrj-436w/zh-cn_image_0000002537174130.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=A880EE6D5CD386A2C8FD5419F660844B480BC666E712BC6ECDABD92DC0126110) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/sOKbkqk_SDG6AvhMb0M0Ww/zh-cn_image_0000002537334050.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=5F7CD0B1C61D69E20EC50A36E32FE9C0F1B31CB4CEC6607521A039DD2919741C) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CjGhX0Z2TPGJK-MFTnwDxQ/zh-cn_image_0000002568173845.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=5497947D9E02762C28CA743847F2D3D7EAE3CC09539577BA1248B02AD33950BA) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/cTdz-z--QiaDIpSqYgIECA/zh-cn_image_0000002568253841.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0A2FAF66CAD9876B795D3F4ABD3345C0845267B5FF27C44D24608E40DE72D9C1) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/6ZgZhJ6rRHOUtOoWVWqRxA/zh-cn_image_0000002537174132.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=E29CA083842E61CDD019E8751BE5B7DA798C37FE30CAE3B746DB1655F803BD19) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/87ebU61DQhO8QD3S355Wuw/zh-cn_image_0000002537334052.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=BEFCE65FD7F1677C4047FE10FC673F4B5E216494E9440000B5FE1124AC565D5E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/szPZXMufThGZpVoNNZAafA/zh-cn_image_0000002568173847.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=567BF4EFD1047FF9B405BA30F9361B55BB91BBB5CC2F70B63D55D50BCCEA628A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/G6OHzGXNSdKSnurJ2r6duQ/zh-cn_image_0000002568253843.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=94DF9C50D5743A90F6D94E283FABDBB689ED3567F832C15E0158973615B5A41F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/s3jgoLiiT-2kqqJUDMPEZQ/zh-cn_image_0000002537174134.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=2B55CCFE6B595D5B2F06F1FE364D7467FA1D2DD213E5BD52C61BD7DD12B2BABF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ErgZ1ZW_S9CbgfVo13-Q0w/zh-cn_image_0000002537334054.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=7F4C208688EA01E868376116B64D88E646EFA4A03E579ABD540DB4BF5130D2DA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/p9c53UCHQjWTsVrfHISHzw/zh-cn_image_0000002568173849.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=6BB1A1600BA71CA97AE505768639A727504CFFB67E405C9B5808D79DEE34E27A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/378UtI3yQdGQxN8x7XbJtA/zh-cn_image_0000002568253845.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=546FD08FA070E3499560AA1D61EBC7427D7E4A737F6A4EC141A63B4F4D77EB4F) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GHzxFYYDSsaBGPrE80zLjQ/zh-cn_image_0000002537174136.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=A907CB274B917A3D4A16747BDFE1BAEE8BB1BEDAC88326024865F099615F16DA) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/lSoI1uQCTCqIO9u3PQlO9Q/zh-cn_image_0000002537334056.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=F16A6A2C790A51210FFCC931294282BFC2CDB5DBF0017242CA57B5925234184F) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Sf5Z7TrMTaa30lSMJ_sHmg/zh-cn_image_0000002568173851.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=BAC38C6E7175D8CD4C7BD2D825677B3D4527EE01B550D65E91011CEAF2F26EFF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lC6b7kSKSGWlD35LMHN-nA/zh-cn_image_0000002568253847.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D173B7E6185F281BD381F5B4A89ED62BBDF97A59AD5F3BE50A741E61C834DFF3) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ohk0RNybTieg4KPBt4CSJA/zh-cn_image_0000002537174138.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=038A024BD0C300520D037DF372C1A663EEDBE3BA89F222671B93888A3D3DE9EE) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/kg3oOD9lRxWfju_bXiJeeA/zh-cn_image_0000002537334058.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=EEC6D968F595C2E8DA4938AE26D0BEF97E1554C45794265C92CD514FE7CDFC13) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/f519LwHqTwWyAggnOhz0mg/zh-cn_image_0000002568173853.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=BA41817BD657C8167BCED0E970F7EC3F7E0A8A0EB310D569FDEB444BA77DE2EB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/weALKAymRl2xFhPZRR1Smg/zh-cn_image_0000002568253849.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=C09B76810D70C7AD515B069EFF342D54E34F6F18D063A4E9800D1509EC7B144A) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/0pWfnZ-bSnOtu567Lvjj1Q/zh-cn_image_0000002537174140.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0A76475BF7A9363B39CE171FEADBA415437210D4285FE0F89E8DD1D05926ADA3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Mdyxq3-_SFiCnYKFnXj39A/zh-cn_image_0000002537334060.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=098975572B9298806E25EB236452FB0E80F4CAFFB711673BD41867072D01B631) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XoYBXwamSl-1OtcBbYDX0w/zh-cn_image_0000002568173855.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=752A73CE177D1E6C8E29F90EB19788FBA36C9E62F2AA2EF79B7AA9473B803E2C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YuS2smwPSeu6ULtnc20rVQ/zh-cn_image_0000002568253851.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=B95D06F39F4BD5326B2AFC31BE8C6A76C2C3CE51FA9D76D031B2581C76B31208) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/GCeqeMACTniVWS3M_yaL1A/zh-cn_image_0000002537174142.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=982825A18258C86D4F2B48F64B8D97446A8C48A63B5AFF59C3AF61B69BE03BB3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/K7u44wRhThy5BddpAZrJsA/zh-cn_image_0000002537334062.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=96FC6442B9E68A5A8AA884F4847BAC1D00C0D1EA1D4D74B3E58E1E7C97C64CFC) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/3u_L2yF4TVuaafiGkGVBeQ/zh-cn_image_0000002568173857.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=A3DF097D6DDE084B830A4F150C42A487EE4E5DCB2BA4C11376FD76DD4411BCDF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/UjBvuym_QSOD6K3yuYz5xg/zh-cn_image_0000002568253853.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=4774B6605DA908A651A1268A1C02BF4DBF4852CC12A0F8053AA146FCE7411ED7) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/IHX8yecHQh-M80olfD4muA/zh-cn_image_0000002537174144.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=E1A38384B1325833479DB269DCC247F2FF8F8CDE8DCFA4E549DC111AE9B4D321) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4Nto1GUKRKa0QKaNf9pYvA/zh-cn_image_0000002537334064.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=ADEE5D9ECB93727248DA5017B25A47ED00EE8A80E41738BD7C641D05F0791612) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wulssJLTRWCQz5XCt7Igbg/zh-cn_image_0000002568173859.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=A52F97CC2786065CEBAA07951C94243D2DDBF9BE6A2452B7C5023B8737FA85EF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MiDj_xHJR9aZXNf39nfZ0w/zh-cn_image_0000002568253855.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=2475FF8B306CAE14B125CF1EA706C5A0D67B64A0D87892C3018816C0C1272FE2) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/YSiQSiKJQgSxIBXQgWEPmA/zh-cn_image_0000002537174146.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=B3431AD33C3F7EA52EF104A2C577DFBBA838AB03DDCC51FDEFA23B0E09AEB261) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/SaLR4yQZSB2i5X3wMOi-FQ/zh-cn_image_0000002537334066.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=8A6BFE1A5E3F7C8FF7780B7C4C7AD1C98082A63A1C28A394D55AACC5EF19C8D7) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/rfLletk4TaSmxPNeHxGg8A/zh-cn_image_0000002568173861.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=9AD6CD7A14F511F60FF406B43487D1555EDC0EAD217FAD30D6E223E6695E9009) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/zKpDvbuiRTy-opcZqs7J4w/zh-cn_image_0000002568253857.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=AB87661E3540445CB75533FEB34759E985D5F2E08FAE524C96D94FE2B343324B) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fpvXg8pZQImSRsandRq-1Q/zh-cn_image_0000002537174146.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=E9854F6F74426F2F1FB8A5AD7D83DC2F053854BD11E81EA2CB7CF0781D8A7616) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/0PX9-IT5Tye4shnzBfrpdA/zh-cn_image_0000002537174148.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0D36E355F28EC5B6763BD22672996FE8B307074B71B507F45E546BDD40D12F2F) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/DMTISzflSMSFyI481Nl9Aw/zh-cn_image_0000002537334068.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=9B695D775E4DF7C4F2788FF347D753E31BD75D5A50D1CF764F95A1498F897BC2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-C7TPOiORK2qTpPEv2J8rg/zh-cn_image_0000002568173863.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=FA73720C4BF627D51EBB503EB173277CC964589889EA88F82700FF0F26BF0BE9) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iJ5UE-DnTwCVf6fynURluA/zh-cn_image_0000002568253859.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1EBF9B41471468785C913C77A3AECD66381CE22F4CEB596ECB35090BAC45865E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/N9j5sQy4Q52kQHLfjseAlg/zh-cn_image_0000002537174150.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=FAF2F7B41AE0A07CB36C3872055D7767ED0251682796B8F77099ED6AB505A300) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/MoI0YsrlSx2qvxjdqMii3w/zh-cn_image_0000002537334070.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=F97D08A369ACA59DA16684FEE1672F7085EC10831B1CBFE1E44ABD51AFD02723) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/NQ2LupoeSYe7u7qyY4tCPg/zh-cn_image_0000002568173865.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=B319A2B02464D2DA3DCD8A34D22BC59D2297CE6A012BF76AC496DA3F223E1D97) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/FwRxXvRBQuqs9qGGKpkAhQ/zh-cn_image_0000002568253861.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=C679A162B7167DEC4833E6D3257713C3B915C6A256D6CAD2E97E459BF06C9EB9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Ytkg95U7RoyubkDVr7xcDA/zh-cn_image_0000002537174152.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=609B3CD894623E58E507306C665A10253615D66E48787FCB86975B482A837821) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fR7VItmATc-qd71_hY3Ohw/zh-cn_image_0000002537334072.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=5511A0C257FE43B80FC3614E15CA551161D18F3F39F8E21DFF8B9A04F439273E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/G0emO6IIS3mfaxQ6rekBUw/zh-cn_image_0000002568173867.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=EFC323C06685D1A4D65018425E085FC322AB99E0CFB2B498B0EFC92C0249F7C0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/g73u4fShTJavr5-F5NBIUw/zh-cn_image_0000002568253863.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=A3DF3204F255716ACE88C8531AA33919693ABA1A8B0AB175625B66EC00651C74) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/56_ZqSPbTfqi0uEF3KmrrA/zh-cn_image_0000002537174154.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=4438D0E8C81EB2E54A708AA31C3768DAEB860921A009EC2CC1DC333FC2F61842) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/737zJF9cStG8kkTUbJfe_A/zh-cn_image_0000002537334074.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=466BC182AC393D855F3B961879D6B9D6ECC20018BC459480FD916676699313B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/O5itD47KQwuX7L8C7nN4DA/zh-cn_image_0000002568173869.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=3B1FE11CF97A157D764B279D3311956D004B96336B937728B449B22C02FA519F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fZP982pIRW-VEVRWC7kaxw/zh-cn_image_0000002568253865.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=DC2AE8AD71655D320BABA999148AB4F5DDD59F6221792D2273110E7ED058EC4D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/voJ6Yc-xQ6WddXfpcXOVSA/zh-cn_image_0000002537174156.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=EA9B718B938BBAC8FD28F5AE7AD1A36F099D8114ABD886FB8CF222069A4887C1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2sx--GfXTIW2ufYOsqhaNw/zh-cn_image_0000002537334076.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=ADDA09C6BF9EA051DADF879CFE6313BE6BFE47C201FBC4B6343C6D252328E1FA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/XXVkFdnDT5aPk-G4TGHu4w/zh-cn_image_0000002568173871.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=73ECA5EDBFB29F668E9A9D978F4BEA1B60DC485996BBE465F3B67B755261D37A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/bEzT4kdnQHKyr5apz9vNOA/zh-cn_image_0000002568253867.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D216B44B799D6F3B710CED036FEF60C655B897127DF0EE5034A9A8D99170743A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1vE-8e1yRWCH0uh27DATSw/zh-cn_image_0000002537174158.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=43F6E0B43FBF9584E111D81C455127EB86A05BB6B5FFCF8BE06A6B0715372965) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/dKum298pQ1aDnowty4eftw/zh-cn_image_0000002537334078.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=0692A71EDEDEC4A3464BDD286FA191184EB808606FCC83F01C19BB5F93DC0AD4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/pNoJQo4-QKmLSe5dQhNarw/zh-cn_image_0000002568173873.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=788B67B19C8199B9F64EE8E9F113827A597E42F1D9E3B85AA6524707AF2306CA) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/BpsE6ro4RpGAlWA5a7VvJA/zh-cn_image_0000002568253869.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=72A903D0A149F739DCF0A5F8D4256A5FEA10188114F1A1CAC6386EC4FCE85E91) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/vxPajUIER6iM6VhD0z3mIw/zh-cn_image_0000002537174160.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=F467578AAB9F8CA25E294D484D020F51025BED49CCB8888D8727D52BE05E844B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/PDu_Eg9XT4KeiD0q8g0Lcg/zh-cn_image_0000002537334080.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D7B497C7A5ABFEB6639B9C84B6E8ECA6A981A8CF5D273BC3B6A534646FA3C4ED) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Nqg22YE0QP-DR0VZ9Euz2Q/zh-cn_image_0000002568173875.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=D935567C98177BCF8BD2D719C6E87BB2EE2532DCECC8A3FD4D623394D4A7A633) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/g6jssnTeTZ27v_viCVI2GA/zh-cn_image_0000002568253871.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=F6804E415FE28AB9DD62A5E4182646057B453BDA3751082DAFE2A57E1107A8FB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/vOQgazStSSu1iwGr7C55fw/zh-cn_image_0000002537174162.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=B012D1C309416F1CEF3FAE23D219455F6C2720BDC599AE987B80D7E6E4AC768B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/v3LFpuSTQjCfTYBSJ_lXbA/zh-cn_image_0000002537334082.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=155932CB8E7EA2381542C286A6A607D63B8432ED997F56FCA4F852DE25B106D8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Xb-YjBxBTvmbw8I932BeAQ/zh-cn_image_0000002568173877.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=ED53BCFD32F345ACC5D8BCD5C3449BB275D630CFD9C349A69A03D4344D2102E0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/AL8ClguYTbaUvnc03WRI7Q/zh-cn_image_0000002568253873.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=74AADA0A054CA8CBE785E8E9F708A016952A3D32A4CD50F002C2F94488F907B4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/FjPF_3tFRo2TavwqNGMKmQ/zh-cn_image_0000002537174164.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=FDAC65753398B751B8B90BB06BEB40E40EB5F5EB3C735A1C5996FBE48ED97E60) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/hBncQdqfSEaawgGj97l4tw/zh-cn_image_0000002537334084.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=1F30EAEDAB75BC6777F8AE2EB66B01DD2B752EF4100A4761E9E5582F8EBAD8A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/fZoVOIs3T0CUlXset27PgQ/zh-cn_image_0000002568173879.png?HW-CC-KV=V1&HW-CC-Date=20260410T025539Z&HW-CC-Expire=86400&HW-CC-Sign=672E8DFC132D29B8AA3EEC01C55765E88A106BB0A40F7B9331DB8B7F92B4BF21) |
