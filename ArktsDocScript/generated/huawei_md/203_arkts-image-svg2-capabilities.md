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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/XOCON2-uQb2UOY3rdt0SkA/zh-cn_image_0000002572641041.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F0FE8DA03B511DD05C8F42A549DA63669C753225FDA75A97BAFE1F99B90A041C) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/u4zF4uv7S2eFU_AvM0F-jQ/zh-cn_image_0000002542120734.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=53BEEF33B3D48F06AF0D5C7A7076259D985EA6FF2AFA67C84518A7FABC721CFA) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/pQfI_8UJTxqjsj3-pJTfpg/zh-cn_image_0000002572681005.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=4A4246CF312E275813FCB7126122268707198D3A1CCA23D6234B672D2ABB0318) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/xBEVM-LbSCWptZnmi4LgUg/zh-cn_image_0000002541961098.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=3FDBB26A8894865E1DB72865383BAFDCBF960B2DD81984E4B6D12E027A31190B) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/iXGuK1ofT-GFH2N02jcZSQ/zh-cn_image_0000002572641043.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=C3182711DB59E8E5FE61C7C9BB0805BD1214956FFD341BFE96F5656D92B373FB) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/NcbGzhW6SE2LHY5rbxfAsA/zh-cn_image_0000002542120736.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=BB94C906C17E604E8F0088C97AA3D4A5C14DEDA9473B3F82A1D4DE6E08C34E1D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/nMxWjGLRSCKlc0odxq88XQ/zh-cn_image_0000002572681007.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=C9857E95DDE5D6E33E6BB7FE1EED587F5571B61FA8A45EFF41F1ED0E262C0CA5) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/WO4ZuDLrSR6cNcC_j-xJhQ/zh-cn_image_0000002541961100.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=84DCC59B444370DD309A2396EECD5FA721315E25C3FC729C4CB9EADDE6117A2D) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/afodBGdzTtqxgOB5hcu7xQ/zh-cn_image_0000002572641045.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D36C4735A24DE01F6E6FDA3FC1726188DC6B1506E0B8D01402D1F246C54AF10C) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/SNGBIgq2SVyZN-otH12XYw/zh-cn_image_0000002542120738.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=E833DF95F787FA4D925828E021907DA7FD3E96D088E41F2A0DD184F487D33440) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/hyLsZo4nQfmIZmul_DxLiw/zh-cn_image_0000002572681009.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=08BBAD75AFB0FCC28ECFA8BB1DCA7C3C603FF450C2503DC221CA5E49D733646B) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/WZdoXbo9QNKbFiAY60HZHg/zh-cn_image_0000002541961102.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CFDBB1EFED7D3928D265FE0F30CBED7D009DF941EF46ADED12BBD232FD6AA7F5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/740wvZYGTNaZhcpXyisj4A/zh-cn_image_0000002572641047.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=E986F39A4044C1E32A97A5594FF06A0D92B4EE3C66FE85359753372B05AA9CFE) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/T19Asi8gRWqPhAZCuVczXg/zh-cn_image_0000002542120740.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=0EB39A432B8395FD5952D148D3F568FA28871CCEDD56237B2839D9F1B403F27B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/i2YCFYQCRGiDwlzdklYgiA/zh-cn_image_0000002572681011.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=54F770F758C6CE348FC40B35D1785952D45B6784412B5862C55BC1FC4E8AECD9) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9pZqrLhGQPia9tK9J_-a_Q/zh-cn_image_0000002541961104.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=8A9DF8257562AE5BE92AC926CEC2F01F6339C190846101F69B3C4C04B23F5735) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KQwgByDXTzSxPucUN_DlDA/zh-cn_image_0000002572641049.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=7E13C256052F5B80F018E0F32C8491E07408DAB5EEE668FAD1869993EC5BB178) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/CTKRNsnuQrq3aAoKKnpx7Q/zh-cn_image_0000002542120742.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=1AE67843A3D661E75923E014F9FD2CCA9254E62BB014B7C2020BCA32871B029E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sNbfO_GSReyU4qYd1ogSUw/zh-cn_image_0000002572681013.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=ACA50F1B02374D9C3C1127C9CCFA7DC35B669FFDD5361053E5EE41BE7E0BBE53) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/9gC-zVReSuWV5m6XRGUr7w/zh-cn_image_0000002541961106.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=68D38BE05FB8B05978BCB82F9D692129D7D500FECB6F0DB626523CCCE47CAA5E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1GFV95UJSF6df5R2S5J9og/zh-cn_image_0000002572641051.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=A20E38F7F12B38DBA75D0788D0AA7E2948B621E42DC32EF1470FB35CC96086CC) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HYj_jhpoRhWSmapKFXltzg/zh-cn_image_0000002542120744.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=207CBFD2222E3895C95DE3FB694B86C208E56EE0DC3C20B1FA62492E087720D6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3j4mlAe7SUyGRaBhn9aOvg/zh-cn_image_0000002572681015.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=024292CC545A2262920C967B57EB178865415DDBF851382B8A22CAFED969D324) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/gq49Yd05QqerVBJ4EeAeMw/zh-cn_image_0000002541961108.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F3BC2DED861534FAAD906E6417B4D66311686DBBE1C0223AA873F057C72D3B03) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3EEFKcKTQ-SXF0tPz_noQw/zh-cn_image_0000002572641053.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=95F618EA93A47B5619E7743B14668FF26BBF43F0A157CEFD3FA97CD5A3F6BFD0) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ZNH8UKmUQEGfmY9HC2jejg/zh-cn_image_0000002542120746.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=85E5DC39563BE1E251A7A94FF555FC3D8675FED539573836A7ED2D15272DF26D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7BKcU1zkQHu6aXKWsLIWSw/zh-cn_image_0000002572681017.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=793A49C23B734592763008E70CECF11B7026AD6FDED8879314B202FF6134D351) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/MBOemEtMSfC9Uz25ooEmkQ/zh-cn_image_0000002541961110.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=912E6F8E7BF9F387AF718F2D3776370203B0533A570CD98BD5418C3C53D40DF6) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/vAVuyRBSSwm7uTmzV_f2cw/zh-cn_image_0000002572641055.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D67C2F7021CC80D59AB4B04DD0C7097649E49C33F21B19039DDFC9A1F9C8DFAE) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/tQpCsIU_RbiySJWb9szdvw/zh-cn_image_0000002542120748.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CEC7EC9BC79EA9EFE0F8BB86B1F6667DCD31D65888D4B6256E19C9A57C90595A) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/7T8VfcFrTQqoG0gl87vC7A/zh-cn_image_0000002572681019.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5235D68DAECBDDFCE96AF29A4EF9B62254EB3225A7BBF2B043A2A34A7E0F6CEF) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/1Owr0fGUQbedmGvIlAlCNg/zh-cn_image_0000002541961112.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D942CA8D5387D0CA9F7420F782B173A65D6F9E734EF9C8816AD3E06F38767283) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/d6F7kjjfRa2YIkVVvBF9rw/zh-cn_image_0000002572641057.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=BC71020A84E9A4200D742597990378CD43B67ACBC5E5D25E739647B0026907D0) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sYXMkjZdSxyYM6K6bAJmIw/zh-cn_image_0000002542120750.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=41F402A46EDE1499C94C870EDF4CE43213AD3736ADAB458C4D5AF53EB6CED727) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/-ujNBVM4R_ahO_NHBnK-Yg/zh-cn_image_0000002572681021.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=E7C4D8FE4B1F36FA1ED52EA807CF1A3DFD7881A44075A38E6F1E345776606D12) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/HXyoO8pcR5q04qCrRG70tg/zh-cn_image_0000002541961114.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=9346DB01C5E73DDD770FB01B5601F37B63913B6211E6553513DE519F0442B6FE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ivTqrWECSZuRkZMJCrnzlg/zh-cn_image_0000002572641059.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=ACC5F7172E4091836AD6FB64A87A9E9EE2CA8E565EA71C3A52F7171494D4BBAD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rWrF7831Q0u4Un0T-RvTGQ/zh-cn_image_0000002542120752.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=6D68531B2BD7A21F52CA6CAC5982C129512A823CBE29356F4270C0261AD9E1E1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dDu0I6H8QJSoin6P3VUVvA/zh-cn_image_0000002572681023.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=BE69C6F80627F6B9C722395CB52B1D811BF9F79D1563CEC9482364342923445C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/znhupIyDRAygp6M9EIDIDg/zh-cn_image_0000002541961116.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=7AD1FD00CD34B5723EE3A4E14EC0B6DD0AA5E18BAACD1077541DF694B12396CE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/RA0yrCxLSXCmaT0QTUazGA/zh-cn_image_0000002572641061.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=ABF70CBF509B380279F3DD4C9DDBB945224F7F690B9EE169C54D9D4CDE98B693) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Gxv1i8YrS5KMjgVruMesuQ/zh-cn_image_0000002542120754.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5D6B821D8917D517C1C14F64336841DDD03766C8DED97E5B9EE64DAFFE44B975) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/w3TSrLDYQEKdXUfK6ve_RA/zh-cn_image_0000002572681025.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=B7AFF00500CE8187FAE2DE9AA3090C38DC26208927491928B654414F613C2B0C) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4PvPGeHYQXGscIApv45pRA/zh-cn_image_0000002541961118.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=2E775CC02983439E644DCE12B5E9A1EABA70E4669D18FF00D3AE67122EBDCD7D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/UrZuhER_Rm6sCDSEh5ZSOw/zh-cn_image_0000002572641063.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=E537456DA3A8C18B856BFE32FE05E544CEAA2172BE75F857B5A30BD0A337B295) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iOeo0dMkQYuAafASNNMkWg/zh-cn_image_0000002542120756.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D2DD0FA7BAF6EC6C5DD496F800C0F67646389F72DC531F7C413EC41CF2A5296E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/HDXl7Hr9TTidKkjHGHg9vA/zh-cn_image_0000002572681027.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=275909FCD8E2AE67F258426AF2B31C6D5887E08C2ED8CF49BA55658BBE34CF78) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/9FSmAJoTS_y9HJ-_yxxlMw/zh-cn_image_0000002541961120.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=A06363EA43201E4A0DF9B859D6DF9B23793B15DCBE4E29A1ACE4B064D210F8C5) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GmkVSkwkRUGZBXxT9MUHKQ/zh-cn_image_0000002572641065.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=38FF892C3162B6C14F107DF9C88074515850DE5F9D8BB2A4F9BC5E8ACDFC5551) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/J6hW8wMLT2-0rj6eQIIALg/zh-cn_image_0000002542120758.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=B97477139EEB4B300AD4245DACDFBEE5291C7F1B15749182650135AA93C84929) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/9BDoHJ92SgiKrZ-z9n3yOA/zh-cn_image_0000002572681029.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=AAA9070422832E06A7D2CCF9F230A7BF78C0F606F07C7B37740058EBA099D4D1) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/OW2e38RmQCGThA3k_4zozQ/zh-cn_image_0000002541961122.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CDB6B1EFCCC607E153283FE5AAC623A6E5506AF88790CDE37B42898DF224A376) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Jz-RV9KwQOeNOoAN8n7cJQ/zh-cn_image_0000002572641067.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D6DD79E873274C42F243D6C7B5FDCD69769D6B92A0038C12C6DC5E166C60B841) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7qp97mtQQyqNw_BEgXDBuA/zh-cn_image_0000002542120760.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=28F9E8CD0B24B7E3D162EB863E316DA87768B432E6259EDF0F86D05E5EDE0EC6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/31s0cwBPQr-Vw3LWNi2T9w/zh-cn_image_0000002572681031.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F32996AF1C7C4443BEF4BB30FD9831AFB9F5A86C61D75FDDC9B6A5917B08BB03) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/A2QFdWQWQimMQeHVwIKUrg/zh-cn_image_0000002541961124.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=31CAC27AF6D129484977C209BD90DF5DEC265F517C9279DC66472B488349C549) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/B0YBeVoBSviqKKmo5F65OA/zh-cn_image_0000002572641069.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F5DC9FA46A0F7CE56AFBA944DECC52A1D5C714BA89F53E08063937ED870F1172) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/rcp8f3AWRj-x5LxXy75mwg/zh-cn_image_0000002542120762.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=03C0243C7927305BD9CA8FC396D6F73CAEF0F7DAF40778980A568B5237FF7538) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/BPaIwtR6T5SQg71JdjWCBQ/zh-cn_image_0000002572681033.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5B25E91B9545A5224F663A6946003CE60F2D87B19300A7DC43EF9828EBB2B10D) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/AKoKbUvUQ52qJWf6oEnFcw/zh-cn_image_0000002541961126.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=50FF19AE92FF1F9DB0E094F58093E144596EEBE330782E5204BFBC2B1E249460) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aMMnx0BaS3mn1h1meRJylg/zh-cn_image_0000002572641071.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=267D07F115504E13AB66A378061F738E5F70C3960EAB63E24FFEC302533A4718) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/OQNdOJszSjq1SDnvYvdMeg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=DA212FECE11E56C3BA012AABFA7AF8AF165695AF33BE082A7977CCEB260657AB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ycjmp067TX6LD0Mlhi_TAw/zh-cn_image_0000002572681035.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5679A58500F531807D0906252D11FACC42402B02A4E3848F59EE244ED729D852) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/d5j0vRGvSjG9JJvKZHL1cQ/zh-cn_image_0000002541961128.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=1ADFBCA2D2B2E6EA5F71BA50C52363A741D2FC9B050BF6D8776768404211D167) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/vbpBUr5CQ-K7sdL4cpSkQQ/zh-cn_image_0000002572641073.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=4BD20ED01E288D0C934FB2C0F8127D4C4B8B36E8161E6E6997F5633AA26A688C) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Rl-JGF89RW6h7nBxIj3kxg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F4AA6A4C07EEBBF1DC6C34BC7F6AFF7253D02817FF9BCF37191262054397CD3D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/l47uZ96LTRinBSrPGaFH0A/zh-cn_image_0000002542120766.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=2C26D884ED4126661351C900D50BAE47C0EAA10A680A3A2DAF07775537AE2805) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/kpg--wMSSsq-hFdfOJlBpw/zh-cn_image_0000002572681037.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=446B9E666AA9AB4458B095ADE1ED1426B125B3BA7E511B4C03D7F0157AEF1E01) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Tew9KmZDT9K-FBdB83enaA/zh-cn_image_0000002541961130.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=12FDB2CD71FAC9DCF84AC94104394CAD9701CFA5E2DBC2EFBDB4B97B3DEAF362) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qA6-Wr0wR6iRQ2AiSUDDvA/zh-cn_image_0000002572641075.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=4263242926F6A2958CC7AB396E7812E73BB24D637C9383A71757BC2CD7AABA5B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/pobwkoNiRDu7Jle9WP8HkA/zh-cn_image_0000002542120768.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5F54CEA1EFCF5482F94B4E0D288BBFA4D49D563E0A37EF1EC8F9A99347A57C04) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/dQ80W6hKQRy5WUvQgRRU8Q/zh-cn_image_0000002572681039.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=114124589976CB1262C935ECF8C2E54D4506CF6E4E2EBA7C98CD4168B12A4922) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/scY4F_yIQziMRuqfpqVBaw/zh-cn_image_0000002541961132.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=5F3855F4BFE4D38BC7CB99C143C45CF66D4194F18EB0AEF3AFE740FA596CE247) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/OYK9sjRET2uDBT_FwWY0JQ/zh-cn_image_0000002572641077.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CF9EF585D7AC51D4CC26E2AC7BEBB05CC1B2DF3C53FCC6E11E71F587DBE6A7F1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/3nm68xvQQxmhi1ISnTNvnQ/zh-cn_image_0000002542120770.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=8363E54B019CF940A1671ED62FD1A414538FC6A76797445A9AD68ED5CD731020) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qDdvESYKTsiowrBqAuZlww/zh-cn_image_0000002572681041.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=0148012DC95F7E7F839055F0FD076CB29C8D16F30AB787CF2F54CC68895E6BF5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/dq2Zmz47QhuWNppxQgXXMw/zh-cn_image_0000002541961134.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=AC1E7E280F0CCF9D8FB4FEC3B8A8EE82EDA79033EF06834179F065901DA154C3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VtKGxPsgQZ2Uwy-SkwVIgg/zh-cn_image_0000002572641079.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=E4B6A25D28B756BCF0F0B1A45EB842258BF9DB198F40FE0F3BE3B5964BAE342B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WHDlCee1SMiJJQ_lFLOunw/zh-cn_image_0000002542120772.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=DACF6B4C53DDC24B95C947C09BFF70CB655012597347C61E50F90B0E4F0154D1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/P9UA_AQvRu6bsiORqYoJmg/zh-cn_image_0000002572681043.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=B2944686CB198B47061BBAFE633677CCB0A552B68D36A104C57D258CB3BE73F0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/bGQJl1HgQRmArKQhi93opQ/zh-cn_image_0000002541961136.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=3980D113A78E7A7DDAD0E1A63E4D7A183E2127C10C9D605A9F01547CD174EA3F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/1uJueF5ZRqaYXSItwFendw/zh-cn_image_0000002572641081.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=8E17B57EC95C753D621339A75EF7E664901E58A5B4C5EFB0E89718A1A17CE942) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/P7NmOu2fRJelkTWkpXJ-Gw/zh-cn_image_0000002542120774.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=C2F25D9DEE5AC9C885AF78B8BF0DD90C162639DD27B0A96F7E6D51FFB9A70672) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/nb-9S4uzQ2uDqLEtz2TTSQ/zh-cn_image_0000002572681045.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=2146C42CED130CA1A77205C9D015AA7EF0389270A634335820CCA1F82C381CE0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/TSvgASDoRAGZx395Y9UVhw/zh-cn_image_0000002541961138.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=7E9B3026268EDEEA7EB48206AD4E846850AF0BDC0658E8C8C9D56099D256E69A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/fvxy5GNJRS-0KJB4BNja8Q/zh-cn_image_0000002572641083.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CDB358E4D154516D100657DDC0352226DB268CCE2F574A0562EEE2DEB8FC25B7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/xxHFB32XTjOerX_T5rs_mw/zh-cn_image_0000002542120776.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=D73804C0B2EE1882A25944C129CCF0CAD444F0DECC093D63844C7DF1F5DCE1DA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QKr1TBugSuaRhGz0o2iXmw/zh-cn_image_0000002572681047.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=8ABBF4147E604D7FB45269ADECED951BD9DB3097D3F10B3F357F209E32061279) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Bxmv2nloTx-X6NQh7ZzAgQ/zh-cn_image_0000002541961140.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=6F3BA8E9C9BA215915276A4A003B68DCC6572A3C3A3F15AC866F8039D8226ED5) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ue45WvtoSaewyE1SiPwKmA/zh-cn_image_0000002572641085.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=AED57466E69CD33D5C1CD5FC89468136A868408AA85C04F95E8453FEA4692386) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/bLMVRo5fS0Gbb2RCqF82kA/zh-cn_image_0000002542120778.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=09A47ACA219F6F2AD909F4ACFB2F7E4F0232D36393AC514BF2D210DAFC2B8D80) |

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
    <image id="image0_0_37" width="120" height="120" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAYAAAA5ZDbSAAAACXBIWXMAACE4AAAhOAFFljFgAAABZWlDQ1BEaXNwbGF5IFAzAAB4nHWQvUvDUBTFT6tS0DqIDh0cMolD1NIKdnFoKxRFMFQFq1OafgltfCQpUnETVyn4H1jBWXCwiFRwcXAQRAcR3Zw6KbhoeN6XVNoi3sfl/Ticc7lcwBtQGSv2AijplpFMxKS11Lrke4OHnlOqZrKooiwK/v276/PR9d5PiFlNu3YQ2U9cl84ul3aeAlN//V3Vn8maGv3f1EGNGRbgkYmVbYsJ3iUeMWgp4qrgvMvHgtMunzuelWSc+JZY0gpqhrhJLKc79HwHl4plrbWD2N6f1VeXxRzqUcxhEyYYilBRgQQF4X/8044/ji1yV2BQLo8CLMpESRETssTz0KFhEjJxCEHqkLhz634PrfvJbW3vFZhtcM4v2tpCAzidoZPV29p4BBgaAG7qTDVUR+qh9uZywPsJMJgChu8os2HmwiF3e38M6Hvh/GMM8B0CdpXzryPO7RqFn4Er/QfBIQM2AAAHoklEQVR4Ae2dT2wUVRjAv5kFW5RkV1uFxNhuYmIbTbrQgx7AlR7kYihcPGhsXALcbMQEgocm0AQPhoMkcqvETXowkQu2t3oobOGgB2B7oiZqiyER0pLdBKRN2B3fN8uQZXb+bLfzZt/7+v0S2jLbbZv9zfvee99731sDAkjN5lKPE5CzADIGQBos8a9GGph2sGh/NOzPt4STIlTgyupQftHvCYbXxc7ZXNpKwI9C6D5glMcyIG9WYNxLtOm+0DGX+7Jqwk2Wqw+GJaKscNZRyB13P/ac4M653GmownnRrFPA6EZKNMrvXkCHdTwL0dhyUS4w+mPAV2vZ/Pnal1DrczEsc8slQ8mowm7sk+0QXU3AaZZLipQ9SBYY9ojZhL+BIce2KrxsQoJHy1TBHIZpWbALGJKIbjdjio8ZYEgiMpBpsy79yFDDQsEMaVBwGhiqcAumDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmzhYgRG9nN2S2vwE9Hd2Q2vKifW1pbRmWVpehUFqAzYj2glHkF69/CCM79tqCg5j89xpM3r+2qWQbHVexeFBPxnoPCrn7n7XWZimUbsOxPy7aLZs6WgrGlnrp7VEY2N4DG+Hs0mXx7xegjHYhGuXODJwKDcfNMNZ7yP7sJxl/D0aH4sM7MP3gBkwt3wTdSGw5vOsMaEKUch2yqX77c6Hc2C8vra7AiZ6PxMCtBz5+9T27ny8/+Q/mH/0DuqDVNGnirSORynXAlpxN9jdcL5Rv2/21A/7uib6j8LPoHmT8HTLQRjC2Hqe1yWCi74jnda/wPdw9GHkkkYU2gnHELBOUNbJjT8N1bMUlEZa9vh8HeqqjheBm5rhR/R4vpldueF7HUbzsG2+jaCF4uGs3xAF2ARmPqReOov1oZR4eJ1oIfl9i3+smm+xruDZX9s98OZk0VVFeML6AcbaQgZcaW7BXH1yPX2hXAeUFD4jFgzhJbm28mcJSmjg+UDVM83Khi1SiNVGqTplYcEQkuQUz7YAFE4cFE4cFE4cFE0d5weUnj4FpHeUFh2WRomb+UWPeuZk5bjnmv7NZlBeMWaQ4JXtlrXo7uwKfg39f0IJEO9GiD56r21Uhm6LHdhyv/HQ9uGasKloIvhrTC1jbIN/4uz5IBq9mTS/fAFXRQvD0Sjy7GQs+kSJse26hrO5Gei0E+7WsqJm8f73hGm4ACBpkYbWEyhvotZkHT967DjLxu4m89mnVc/aO2hvntRGM+6JkjqaxysGLA12Dvs9RvfUi2ghGud9IKjNBSV4RIpvq8w3P+BzVWy+iVary+7szMC9hvunXesd6Dnlex5tt//y3WhSvaZeLPrpwMdJQbZeUerRebLl+G+0xkuhSmaidYEwlnvzzJ4gClHTyL++fhWUyXuANgZFEF7RcTZq8d23DZZ8oF8OsVzQIKpOZeqBuUsMLbZcLsd/cyNwYW6533rlb+WqF9aD1evCFFkMlLgxM+aQXL4VUDg6/4j9tUhGtBRdbrNP1G4njokLY7siRnXthVOFKBjdaC251s7nX5nYEB3B9v5+EYwvB53ece/NTabXKUaO14JHX9kArYLF30M2Bg7gw0diSF949Z9cJY0JEVbQ6wqEeDKcT/UehFTrNrbBjazJ0lQpb9IW7v9pHOeCig9dNUasr3mvfNLUzuVZAJbQ7Zcep5ouibNOZKjWbtECROMIOCs12ClOM8GUvjjSLNoKjFOtmvQek6SRaecEyxbrBefXZO5ebFo3JkLGeg4Fnh7RbtLKC4xTrhpJo5QS3U6yb9UpBwbhBIKggPG7RyghWSayb9Upx0p1hoqPIqYfRdsH4YmBm6DPxYqh8mAmyXtHDXYMiKfJJ6J4uPBhVFm0T3MxdrirrEd3M8YsyD0WNXTCeuTEqwrCOYt00KzpMMi5Z9ovMmYw9Z7EJxnQeboHJxngkUlw0IxozbzOZU77d0LGFH6QMvKTnop27d2bga5JyEeeQUsxN+22zraU9ZwJ/hgykCsa79rfBcbJi3Tii/bb7YF477mpJaYLtwzrfGVV+ZCwDXGnC0bMblHsh5v1c0gSH5WqpgwPJjEdVol92rPhITvmpFMHOEtpmZ2Rnc8cTY2p0WtLbBUh5z4ZscnP0uWFg2csJjy2+OOJ2ui58e4ApieWnUgSHVcRvFvy6KBxsxQWfskMcFkwcKYLjnuupigqvgxTB8w/1eV8hmahwdocUwTgVoP6WcWGoUj8sdbEBR5EHunZvumzW0tqK3XpVCNFav/soEw6PoonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgomDgheBocoit2DimGBwCyaLcGsaFiwBQxMLiqZlwC1gSGJU4Za5VoE8MFS5YsJQviRi9RVgSGEYkF8dytdG0UYFDlsAJWBIYLuswDh+bQtG04lq7QKjP6LvHUen+PWzefDjofx5gyVrjyUcrgmXzv8N9zdsm80dr5hwWjyQAkYbMCwbLrmI4fXNnbO5dNWEM+LBz4FRHgMHyWIc5YTl5x4LeiKKFp/2WSbsEj8kY1mQfvpQGph2sIgfjFr2cdGqQHEbQL6EMyEf/ge9rhOytvtnwQAAAABJRU5ErkJggg=="/>
  </defs>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/vV-EGMgVSJuITupvpxb6mA/zh-cn_image_0000002572681049.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=FB3664B3A916411C7462B892BB16BE957B1DDD0174A6CE04DF4B001341328C1C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kcHMnSapTWqg8EGGXsfOYw/zh-cn_image_0000002541961142.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=42CF587F93E4EC88361465E88208BAD075777DDBDEE8A30B427D327DB70EDC81) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/DlM-MBNTR26MZG3y8-GCeQ/zh-cn_image_0000002572641087.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=F842AA3D8AF68B8C352BAFC1C566D288F9CAA72009735E0E6B1339623EC7335A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/wB6wF4R3TgG-eBvHWwLi9w/zh-cn_image_0000002542120780.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=4B2EC71D8BAB23166E3AED5E367ECC1336E47ABF2C05C211DC61B33F6FE74245) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/WknhNiMLQfGKmvSrdAUh_w/zh-cn_image_0000002572681051.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=ECCA4360A9DFABCBE63D458FC04842F4961A1E1D296D741AC9D6BC7FE9DFA1A5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Qb326HaLRzWywKsu_se-6A/zh-cn_image_0000002541961144.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=CE3C2BCB86BCCBCA9DF12FAAB7666F6FF7999599790A2FAE57AAB59F7798369A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/qKivb77USP6TdFbNQSX2rQ/zh-cn_image_0000002572641089.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=A8FAFE10BA77209975D809AB724706FBA5FE895AFFDA29F3EC948DFEA321F4D6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/iNWSrIoHTK2oQQXPGAc8Rg/zh-cn_image_0000002542120782.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=37B4A7306307E9AB321B07838A94599A35C5BA6CB0219685F717D60EE1FEDAE1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/T6IkU3fBSICZgN0pRwSVgQ/zh-cn_image_0000002572681053.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=110D31A1234C18EB6DCAEA5B0DB5D5FDCD86422FE4B47F96205E92A06CC0BAFF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/D_37UJiBRQqo9_DVfNizFw/zh-cn_image_0000002541961146.png?HW-CC-KV=V1&HW-CC-Date=20260419T030042Z&HW-CC-Expire=86400&HW-CC-Sign=1160F2A447A8876F4E207779996567B852513926BBB70236035FCE9F00A1C358) |
