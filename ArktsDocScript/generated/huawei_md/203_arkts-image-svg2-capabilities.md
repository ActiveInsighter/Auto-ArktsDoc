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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/XOCON2-uQb2UOY3rdt0SkA/zh-cn_image_0000002572641041.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2FB704BE6CFBB4284742F232A5931E230D79B933AC5FDEEF8B7730402B64CE32) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/u4zF4uv7S2eFU_AvM0F-jQ/zh-cn_image_0000002542120734.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=78AF09D3C30619D6888B8884EB8748EAEB9CFF4163C04DCAE03B8607F37FBDC3) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/pQfI_8UJTxqjsj3-pJTfpg/zh-cn_image_0000002572681005.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=1465B42A775CFE9ABA90ED4D4FC952050BEFAD0EA6D5E41EF10B438BDF80F62E) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/xBEVM-LbSCWptZnmi4LgUg/zh-cn_image_0000002541961098.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=81CF73DB0D5FA5D67C8FA4FD2F90083A9173A27A0C4E9C05D06BDC0C1B6500C9) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/iXGuK1ofT-GFH2N02jcZSQ/zh-cn_image_0000002572641043.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2FC10D96B66B47B962ED20D767FCDB7102807F645EE1FAD18554DBB17B8468DB) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/NcbGzhW6SE2LHY5rbxfAsA/zh-cn_image_0000002542120736.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FA37D7B6963C891A0045A042F248AE0A142FEE6AD36579126EBD4E7EA71BBBE1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/nMxWjGLRSCKlc0odxq88XQ/zh-cn_image_0000002572681007.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FEE81424D93448741B1A7E12BECF3667EC4596EAB8D7AA24A34EE3494B38688C) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/WO4ZuDLrSR6cNcC_j-xJhQ/zh-cn_image_0000002541961100.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=525CDFB319E36691E9E4B4917998A6413E846ADEC0483541698CDE882F465281) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/afodBGdzTtqxgOB5hcu7xQ/zh-cn_image_0000002572641045.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=9AA5FD40BAFFC48DA251B5D130142740CEC603A54BCD7BF2CA1C39359099244A) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/SNGBIgq2SVyZN-otH12XYw/zh-cn_image_0000002542120738.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=C4DD2CBF744B7DDB3FF0D9E9ED79A4718B465319B8953D30A2830655C1EAC887) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/hyLsZo4nQfmIZmul_DxLiw/zh-cn_image_0000002572681009.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=51646E07D559F7A97194A056054CBB1485976BACCD18478E45F7275CF377D289) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/WZdoXbo9QNKbFiAY60HZHg/zh-cn_image_0000002541961102.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B5F0F44CCA72F148E5295F7C3516F702ECE3CADC5946E29C25C84BA8DCB20266) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/740wvZYGTNaZhcpXyisj4A/zh-cn_image_0000002572641047.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FCC32E434DA8F173C51D3B5511048FB83DECED5F24EB92ADDF6E8277EE344F44) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/T19Asi8gRWqPhAZCuVczXg/zh-cn_image_0000002542120740.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=C00C55B95A0F65C194277871DE0F7760A8290BDD9F83F33D09481AD070634C42) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/i2YCFYQCRGiDwlzdklYgiA/zh-cn_image_0000002572681011.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=29D5DC084CEC7D1664675ACDD6FE749BEB9CFFF95CE1410AB0AEB524B171639E) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9pZqrLhGQPia9tK9J_-a_Q/zh-cn_image_0000002541961104.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D9DE0BD643E4C9D828312BBCD5BA0131067A185F545E679D8FAEEB9D160BD5A1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KQwgByDXTzSxPucUN_DlDA/zh-cn_image_0000002572641049.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=119E39BE6F0EB2C7B1512D2384B98F60378A228D3045D76EA2B6C5946B51D6CD) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/CTKRNsnuQrq3aAoKKnpx7Q/zh-cn_image_0000002542120742.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=3A9071C308412757EACF5E18E8062DCAA1CE72E49FF9999502FCACBFD28CFA1C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sNbfO_GSReyU4qYd1ogSUw/zh-cn_image_0000002572681013.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=A1C618BC076E2CB4B92C0ED51456A4539A566F31F2849BB02A7500A8498EA952) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/9gC-zVReSuWV5m6XRGUr7w/zh-cn_image_0000002541961106.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2D876FFBA8C2E342443BF4FE42BC6664C8D47ED8A48AF18DBD2DD7B56AE05FAD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1GFV95UJSF6df5R2S5J9og/zh-cn_image_0000002572641051.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=C90F7B1BDF4189AB5F07D258CEBC98C210D9E2C933816AA0AD173D7FF84D3043) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HYj_jhpoRhWSmapKFXltzg/zh-cn_image_0000002542120744.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B02C88DFEEA656866501C116F908E8BE617754C2B4DEB7853343F86067414917) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3j4mlAe7SUyGRaBhn9aOvg/zh-cn_image_0000002572681015.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=AECB247F3B5AFF09CB8982C2A87840D77BF20EA185D4FDF2130DC8D3883D3A32) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/gq49Yd05QqerVBJ4EeAeMw/zh-cn_image_0000002541961108.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=527CF4CB4A6A60410DB65392AF67BA925498A99D2612A56DEB1F1BD94E36F651) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3EEFKcKTQ-SXF0tPz_noQw/zh-cn_image_0000002572641053.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=A11B47A1C54A3421C57375F593AA5BF16078D8D4AB27A5F5019B3DBD2CD15BEC) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ZNH8UKmUQEGfmY9HC2jejg/zh-cn_image_0000002542120746.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=5A8E5E0D6ADBB8BB26D8164E23E8241B13B1B20DDDFE690FBCA3D5E9F04C1C08) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7BKcU1zkQHu6aXKWsLIWSw/zh-cn_image_0000002572681017.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=0250B50BC9860876DF9E73F3B95A9120B42939EEF36D5B7590B94C5C5C3D1A59) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/MBOemEtMSfC9Uz25ooEmkQ/zh-cn_image_0000002541961110.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=07FAD7D1B1E65C35B58011454545CFFB72D1896A06303FFACFD1408E77264500) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/vAVuyRBSSwm7uTmzV_f2cw/zh-cn_image_0000002572641055.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=DB4F03025F07A937016DA8DCF4B2C42D5EA9E4475BB2ABB9ABF7638CEA4ABF84) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/tQpCsIU_RbiySJWb9szdvw/zh-cn_image_0000002542120748.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D08E20C1C6DEB055751FFFC278687D5F97C3F68E0B5179A62841F236BE6F2A9A) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/7T8VfcFrTQqoG0gl87vC7A/zh-cn_image_0000002572681019.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2F58058DBA1109BFED69D4F90F0FC11DF8F444ED2EC6961AB4A52880B0275A48) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/1Owr0fGUQbedmGvIlAlCNg/zh-cn_image_0000002541961112.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=7480C247EB84CD2C9E668C2B94FFF938A503C2836DA50FEFEEC7E37C79440EE0) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/d6F7kjjfRa2YIkVVvBF9rw/zh-cn_image_0000002572641057.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=F0C044C8E898DDD9BDDB8A85E0D48B18C00C8497BBE38DA9D6368847CDF8A312) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sYXMkjZdSxyYM6K6bAJmIw/zh-cn_image_0000002542120750.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B2C7E041D21ADD4CE9190E3CAF0D11F497CA577ECD091FDF00AE007FC382190F) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/-ujNBVM4R_ahO_NHBnK-Yg/zh-cn_image_0000002572681021.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=197929E7CCA86696347A4B0ECA8243B1A17E5F57B08B433F678962D39E5589AC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/HXyoO8pcR5q04qCrRG70tg/zh-cn_image_0000002541961114.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B2984E77C926EAD2B2F13B768E8EEFCA631ABA0FD7BF6D69E04C3B2DE9F20314) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ivTqrWECSZuRkZMJCrnzlg/zh-cn_image_0000002572641059.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=DD14061F03F773F5DDE1C1CEC26A3BBE644B47ED25D0DEECEF4BF05230665783) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rWrF7831Q0u4Un0T-RvTGQ/zh-cn_image_0000002542120752.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=8A8DE0AB9469AC98EA9B4E16750CAAAB59C72EBBCC050B5BBE789DDB60A88A11) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dDu0I6H8QJSoin6P3VUVvA/zh-cn_image_0000002572681023.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=642EAD2CD8B3AE97BA8A074A248E102C44D4088F8987F972933EC678190CEBFD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/znhupIyDRAygp6M9EIDIDg/zh-cn_image_0000002541961116.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=EEB7BAE474262D9622CD449FDE2F8675C453E043A5FE8871589F763D16FF2336) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/RA0yrCxLSXCmaT0QTUazGA/zh-cn_image_0000002572641061.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=59310D0FB6A6034604A19C81F6084A16B8A7669746560470D958E054D5C4DF24) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Gxv1i8YrS5KMjgVruMesuQ/zh-cn_image_0000002542120754.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=BFD05E071BBE33774D58F2F0E4A60936ADCEA66250B26582572B8FEBF82F3A94) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/w3TSrLDYQEKdXUfK6ve_RA/zh-cn_image_0000002572681025.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D944E820BEBCDA4C6B04EFAFD3876BA2FFC345D6C420E747919D0B924EAF6873) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4PvPGeHYQXGscIApv45pRA/zh-cn_image_0000002541961118.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=DCA17FC630800B7AD8FAB779C2B31BC7A3E91ADA71B1E8FA24C07D7DDEEDEF84) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/UrZuhER_Rm6sCDSEh5ZSOw/zh-cn_image_0000002572641063.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B5B5A0E4B7012EEABAC38867DDC41529B21081172E44F3E4047AB72EDE8D6C78) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iOeo0dMkQYuAafASNNMkWg/zh-cn_image_0000002542120756.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2D41C6D71C61255D577C92DD449BAEC3E621E40F606BD952D51A15BF8B199EB9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/HDXl7Hr9TTidKkjHGHg9vA/zh-cn_image_0000002572681027.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=856D9DFD6C70E16EE3BC80BA8B702E0AE34705B27CDF230F857F284459A8BBEB) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/9FSmAJoTS_y9HJ-_yxxlMw/zh-cn_image_0000002541961120.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=95842310FE347A6E1A0FB348266D844CC656C61ED37CD38443683E382487AFDC) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GmkVSkwkRUGZBXxT9MUHKQ/zh-cn_image_0000002572641065.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=C8686018A5FD63F8D3DF1DEC65D83DB9BB4D751E10192C6CC4AD315F170703CE) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/J6hW8wMLT2-0rj6eQIIALg/zh-cn_image_0000002542120758.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=A2D614513ED3B0A5FA0E1804D97FFFDE0EDEE899D63B891B0706664469A1673F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/9BDoHJ92SgiKrZ-z9n3yOA/zh-cn_image_0000002572681029.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=455D5BEE9BB010FBA74794B63DEA3E6B10CA0446B1EA815C5531AA751BCB359C) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/OW2e38RmQCGThA3k_4zozQ/zh-cn_image_0000002541961122.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D9A17EAFE3DEA4DDC64296178A0D4DF17D493D9BAD871EDCCC4BDBEDF3469E87) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Jz-RV9KwQOeNOoAN8n7cJQ/zh-cn_image_0000002572641067.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=AB2CABC50B849DDFFD9C0040D42C2C772434DC9E16CFE23E487A048AD7958858) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7qp97mtQQyqNw_BEgXDBuA/zh-cn_image_0000002542120760.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=B592212A08575AB54125B5498E551819CFB402B510512816BB4751E70B70C580) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/31s0cwBPQr-Vw3LWNi2T9w/zh-cn_image_0000002572681031.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=82D9F958857E2C27CB62CED1611A85619F00F9C79146DF5BDB3779008DE43CBB) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/A2QFdWQWQimMQeHVwIKUrg/zh-cn_image_0000002541961124.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=551B30C99087890C71321817C09F6C0F0B4383B0986BCDC510E8F2E2D3758FF1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/B0YBeVoBSviqKKmo5F65OA/zh-cn_image_0000002572641069.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=2E5E8A089EB80A58B16FAE8146ABDEF5F9732D7BF4EF1BAA9B01F7587A6CACF1) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/rcp8f3AWRj-x5LxXy75mwg/zh-cn_image_0000002542120762.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D7A1BAF7CBB4D6D95EBE49BB1380262E80F43F230244B88ABD3C5A561A99791C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/BPaIwtR6T5SQg71JdjWCBQ/zh-cn_image_0000002572681033.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=F8B2457F566DB92DE795371A3E21C88755A63185C4B2A3E3BAFF16FC45312057) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/AKoKbUvUQ52qJWf6oEnFcw/zh-cn_image_0000002541961126.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FB56DF115826EB50D8A37A999269EE5D70CACDCC47D7B2C7EC06108AA0999C36) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aMMnx0BaS3mn1h1meRJylg/zh-cn_image_0000002572641071.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=42A7C61194E3550C316DDFAE379316163EDC6873F2B56D5328C07B23164E0870) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/OQNdOJszSjq1SDnvYvdMeg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=7AADB05EA23CB4491265FB8BC073DD8C33343A12BE39593310152F3DDB97E8BB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ycjmp067TX6LD0Mlhi_TAw/zh-cn_image_0000002572681035.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=5A9297A4CED537D5A18E41074AC3055F651BED504B39F60DD10AE849ABD24509) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/d5j0vRGvSjG9JJvKZHL1cQ/zh-cn_image_0000002541961128.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=44E6DB188F90150250B1226954CD4E1C835AFA61A97C506F11A6CF4C96B58A9F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/vbpBUr5CQ-K7sdL4cpSkQQ/zh-cn_image_0000002572641073.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=90EE43A919EC5D548F3EFC9A7BB937D786E51903371E039268A78C9EE7EBA7A6) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Rl-JGF89RW6h7nBxIj3kxg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=57DCA2D51EAB5FAB90E6712037F1B759A5CC427BE3CB98EB37196FB3882E084B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/l47uZ96LTRinBSrPGaFH0A/zh-cn_image_0000002542120766.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=F8728785FFA63ACF86E2FE1D32E5EAFCC2EA7E6BA66330784F5007D0D4CD3ABE) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/kpg--wMSSsq-hFdfOJlBpw/zh-cn_image_0000002572681037.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=7B44D693F5FF5544542AE1BB91AB2DA641DE433A525D3E9D49EC4712C70ACF80) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Tew9KmZDT9K-FBdB83enaA/zh-cn_image_0000002541961130.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=1BE08A4EBE22C58BFB80F3B77FF1A2B1FA4ED82FD69A572B3CAD15D26F8979E6) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qA6-Wr0wR6iRQ2AiSUDDvA/zh-cn_image_0000002572641075.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=1F6467BEF411B50CF85EE32B660FA8DFA8258D51DAFDBBB53889E1F86F8A4044) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/pobwkoNiRDu7Jle9WP8HkA/zh-cn_image_0000002542120768.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=8222081BF14647BEBF58D9DB97E9F7DF57E2B9AD0BACEAA37957671BE444DD44) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/dQ80W6hKQRy5WUvQgRRU8Q/zh-cn_image_0000002572681039.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=926DE18E7E44FFC36919F3F942991726FEF96C246AD55B56D6E8683EABE587DD) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/scY4F_yIQziMRuqfpqVBaw/zh-cn_image_0000002541961132.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D77EF0B3027EB4AA982748FD51D0AB3B849E8664806DFC8D259DB752422EBAA0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/OYK9sjRET2uDBT_FwWY0JQ/zh-cn_image_0000002572641077.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=83CBBEB727A3247FAE98293BAB1D9E1B7BC7776B25129005817E6E7EB1364695) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/3nm68xvQQxmhi1ISnTNvnQ/zh-cn_image_0000002542120770.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=553E4EFDDD98F91430124F40C182F946E68B451C7C42591D2229F4F95908B321) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qDdvESYKTsiowrBqAuZlww/zh-cn_image_0000002572681041.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=82ABD156392D855711B547AAA1BBC9BDE79871122386F6BE58B1B71083E8FEBC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/dq2Zmz47QhuWNppxQgXXMw/zh-cn_image_0000002541961134.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=6A43A7C823039969E912077235EB0510DD745C84F24EAECD72C9B3F907CA6500) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VtKGxPsgQZ2Uwy-SkwVIgg/zh-cn_image_0000002572641079.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D5E19081329094AF302416B59EF8921F026331872510833A5E3E4A31645912C5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WHDlCee1SMiJJQ_lFLOunw/zh-cn_image_0000002542120772.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=03F3F5EB0F1859A60EC1B79DC6C95B0D71442E78F210BB3D9B78DAB467466FC9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/P9UA_AQvRu6bsiORqYoJmg/zh-cn_image_0000002572681043.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=40A4ECA6AFF07A569A1E48D184256E0FAD832F71ADBBF700CB00BB6B29E14E8A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/bGQJl1HgQRmArKQhi93opQ/zh-cn_image_0000002541961136.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=826543E745DF81AD93ABCF67E74B7ED648CD7E38BD883B621EAF77ADA7847246) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/1uJueF5ZRqaYXSItwFendw/zh-cn_image_0000002572641081.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FA9EB4BC48F49E1F2EF886B06DA123B64AC09CCFCBCD6EDBD356E1DAAFE35FA8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/P7NmOu2fRJelkTWkpXJ-Gw/zh-cn_image_0000002542120774.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=5F8EA9F63CE4BAF34528615EA8B0294F479F9C0EEF475A351373086DF055F6AA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/nb-9S4uzQ2uDqLEtz2TTSQ/zh-cn_image_0000002572681045.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=DCD4E95DD4F8DC5108DC08A57E9A4304E7461E5A0845557C821634BDF4498F03) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/TSvgASDoRAGZx395Y9UVhw/zh-cn_image_0000002541961138.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=7FA0225385F0328527A623941E31D1A0D100E7D174A66B63DD7F31A06D956797) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/fvxy5GNJRS-0KJB4BNja8Q/zh-cn_image_0000002572641083.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=3EF44D28EC08F4663B4341B3086160D3C446E62A43B39EDDF15C1E16638BF5F9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/xxHFB32XTjOerX_T5rs_mw/zh-cn_image_0000002542120776.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=057CC40C3E93CCB2052300A6619A3357CDDB3B3C8743C56964504F2B93F2B9C8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QKr1TBugSuaRhGz0o2iXmw/zh-cn_image_0000002572681047.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=001003B7F037E6FD87848F2C9AB451EA3B4D0E21088E12F6F84E62238854B073) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Bxmv2nloTx-X6NQh7ZzAgQ/zh-cn_image_0000002541961140.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=E6091B8C2C37F7146A0CF375397799C89B480CDCC8260EBB7A7A9C5F5A71008D) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ue45WvtoSaewyE1SiPwKmA/zh-cn_image_0000002572641085.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=7F8C4F6A9338C2423E466482E828E1DFD0D671EC4D148B927E0F8D445F3D3DAA) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/bLMVRo5fS0Gbb2RCqF82kA/zh-cn_image_0000002542120778.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=172B69D2703513AF986187CF45FB4F2F6517CD151096BBFC349D6E4DAC7ED0C4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/vV-EGMgVSJuITupvpxb6mA/zh-cn_image_0000002572681049.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=91262393625168F86C261214E0B0525D5894D566144E2B0B8B7833EC69FA2DD2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kcHMnSapTWqg8EGGXsfOYw/zh-cn_image_0000002541961142.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=360A2C886E67C4E529438726DCF4F3138CE71EFA3EF6E82E75B57395FC00CD99) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/DlM-MBNTR26MZG3y8-GCeQ/zh-cn_image_0000002572641087.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=82E8DF4BCB7F74E2627F9EB9E0D2960052F12C87E0092B359C2CDA2E80A5111D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/wB6wF4R3TgG-eBvHWwLi9w/zh-cn_image_0000002542120780.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=38D21C9AEF76A555D13CD3079A53F4B61C08FF1D7C8D20EF34D4AA5F997706E1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/WknhNiMLQfGKmvSrdAUh_w/zh-cn_image_0000002572681051.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=FF4F829932EDC5F2CF613A846019B4C7CEC9F05AE6FEAC56D750F18739E19AD8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Qb326HaLRzWywKsu_se-6A/zh-cn_image_0000002541961144.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=D6B27B91E0F45A80A28E8329352E246BD74E2B19C833129FE213B2EB40957C11) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/qKivb77USP6TdFbNQSX2rQ/zh-cn_image_0000002572641089.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=E2CE58F78ED9D923FE96133BEF7196694CEE71385CC5088268B08F48D53BFFC4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/iNWSrIoHTK2oQQXPGAc8Rg/zh-cn_image_0000002542120782.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=BD40F52A54CC41F3E549D098235304B34F8BD2A3B8AE11BC8F6510D99C574903) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/T6IkU3fBSICZgN0pRwSVgQ/zh-cn_image_0000002572681053.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=66C13383F7EB3FB00FE86FE6EDCB0731E6848CDC6FA29557F023EB6C66A08880) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/D_37UJiBRQqo9_DVfNizFw/zh-cn_image_0000002541961146.png?HW-CC-KV=V1&HW-CC-Date=20260420T030131Z&HW-CC-Expire=86400&HW-CC-Sign=DCC3444B87E0FD34B9307EF82B4905203A49DEF60F9D777BB69C4BB25D4963E4) |
