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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VGyU99-aReaayU5YM8brKg/zh-cn_image_0000002571292613.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=E898160B701BC7C7233F5D3544654F932E4E572109D71782A6C9CA8E00FEB170) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ewnyj0dtQYGTWVKRIw4vwQ/zh-cn_image_0000002540612666.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=4A90942614A7AD74CCF3B3EF274FE2C0D5CAD29DE4B6A0D50D01ED7B39311B65) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/2YOu03J7TDm_fJ6ttO0_Tw/zh-cn_image_0000002571172661.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=A812DD5A4748C0A6808D04B4D327B3EB8D7AC5486E453718ADC76CBCEA27C615) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-mc8ICV7TnaqzTdZQlQPDA/zh-cn_image_0000002540772320.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=FDAA95B3EB03774D689369E9CE1DD840F56D437EE4B67EDC4F2682D410F548BD) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ctK8rj8WSN67Ueene__nfg/zh-cn_image_0000002571292615.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=D62DEF2552FC59020CBC9BCE993789FB756E2465C965D1B77BA2834FA3332E1B) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Edl0TWBVSRmBAvT-fGX2Og/zh-cn_image_0000002540612668.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=EA5199AB169890F3B95209A1E384A66BD29721AAD1F68DB3319339005A18F15F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Hcsfa448TnS8M35xi2Kx-Q/zh-cn_image_0000002571172663.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=B78A1DEA70D6DCFDAD3BA89F256BC6228F12511E58A11B3527A550071E86C2CD) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/MRWCUrtpSOij--9CPfIPFQ/zh-cn_image_0000002540772322.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=78D3CFF085A7C4C647C99BFEB33C24A3925D47449B6918B7169A7A850B61A8E1) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/rz3Jisj9TqarN3MJSA0sEw/zh-cn_image_0000002571292617.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=78DBC6FF24F5D3A4D80394F53E4BDF8CE37A13EFC15320D5638B483643F06D29) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/cuYOd7mlSDOsLzRPs2ceSw/zh-cn_image_0000002540612670.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=85C0C86523C3902C8D390D91BB8A7F50D96165E15B8426BFC0D9D45E8E5FC200) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/b6Qt-3qcREihcvIK7O7CAw/zh-cn_image_0000002571172665.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=EDC641957A671A43D17CD4B7F58372DBF6087E976F2D6D5E8718C70F5D015A0F) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/6Pj4OrQqTxSAsztPUgS6dg/zh-cn_image_0000002540772324.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=7D8913D7F1314AE75C3AF59FD900038987D20D5C1AF76438A0842D8530064330) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/PCWy_RlvQ8-b9Qgl7X383A/zh-cn_image_0000002571292619.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=78D5AAE9DC37684D54FB10216D9F930F83CB77A64E32A337E5445533104346DF) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/DyTB_y46TAGTaCWpdWhsiw/zh-cn_image_0000002540612672.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=4031D5FEC75EF27AF5B47BABC7AE63A74AB90FCF27400E069CE4AEB6F9B4DEB8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZsM_nVMXRuiVXa6iHI9buw/zh-cn_image_0000002571172667.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=3A93C81B0EC0D23B53961E0331F446A961EF960379262CDDE2DB71731CB5B663) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9oo8WUI5QOCpCSyohW7RhQ/zh-cn_image_0000002540772326.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=C286FDB0313A6438F5F4D92797EA1886E1CE4DE5BF7394E86E16B79F5EB6EB34) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DX-JtqZCSkyp5ht1sjlcLw/zh-cn_image_0000002571292621.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=9444C3CE67CB5367D23DE0236503B49D605ADB81A4E8B0E80BA8647B939AE0F9) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/GKvq92jAS5GCmZNHoEmX3g/zh-cn_image_0000002540612674.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=E06F9A3A4F819B884B61CD9ED654A3A7005144829CE1A2E1BCDA483197058847) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Z2QFxtZtQl-TprIeuvOuBQ/zh-cn_image_0000002571172669.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=335C83DE316CD34C92B2E52C3CFAD528500DFB321A549087EC73966B0CF6989A) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Q8aMOB9xTNaOvJ3Z-A1J4g/zh-cn_image_0000002540772328.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=FD9D7FDC30F84241BE6054157569226081BA7E98656E11C5AB9CD5184710AB1E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9OF9HW1vTlWoiJDzWFrcEg/zh-cn_image_0000002571292623.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=35114AD63611D5FAB9424FF6DB83B832F023CFA952AC747F5F9F083F52925984) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jd0HZv1gSbu-xaVfEf8prw/zh-cn_image_0000002540612676.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=45021373E1D66CB5DE95EC66408827D55FDF8EE2DD1E9352B25BBF023D26FBDA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/VT90f6ASSpu63FREZROChQ/zh-cn_image_0000002571172671.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=F6C06C4437427C451E81CBD43729F1FCA7A9554F02A70C2742CB6F7A01ABDDC9) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0pNYWIEFSUG1YnUgX1Tdig/zh-cn_image_0000002540772330.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=78C87B26FE839626530F79F56D4B369F762FE9C18B926F1F3190B1F60E3B29AB) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zr7870VKRjKMbCdIqarOkQ/zh-cn_image_0000002571292625.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=2D80690F92892AB7430274D33138A189D9246EE6665A4CBBDECF89A0EEEB1A4A) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qKzO2jDyQveLJoOTe4Zorw/zh-cn_image_0000002540612678.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=B5AE72DE11E1E47E05D80B3F01EFF06F066E146ACB4008ADAAE656B1C6912612) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e6OfWO1CSE20KoZac_8JGg/zh-cn_image_0000002571172673.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=40AAA90960FBC9811806E3BDF157589B9B3B2878077BB8E6BE80DF48287C705D) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SFw0UjfMSzSkqtySCgj54Q/zh-cn_image_0000002540772332.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=DC3432F53581C44FBC42904CDCD7108F5E75FC15617F6DD53D3DC7BC9BE615AF) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/a7nlLz3LRieAcsBW_V7hgw/zh-cn_image_0000002571292627.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=0D376475EFAC7B615F71765AEE5923A27F904AEA30ABB7E8653DD89CACBB29B5) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/qEVKxjD-RomYTG5APeamBw/zh-cn_image_0000002540612680.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=5634A4FD90B76F522B85E8BCACDBA1C312A437ABA8B2EBAD62C0E9617BB51D19) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/VUNY7qLCRcqPaGAETAyOZA/zh-cn_image_0000002571172675.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=461017F7CC520FD7E5CD18227C505988723A2705D7AC4849A9F49C90235EEC8F) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DShelAQiT5a5UnXBgI2Hhg/zh-cn_image_0000002540772334.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=4A8CA371CAEA596ED306324D46B7B44AA5B3CBA724F47D18D136E9BDE233B290) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WlpILEALQr2i4NBUKjBI0w/zh-cn_image_0000002571292629.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=0EA29063731ECDE4F822A03016EE1616A39FC51E4E171C86322C0F874E0080BA) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ezIxJGBPRxWkFF3LOOfTRw/zh-cn_image_0000002540612682.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=48AD2ACB2F8406E0F4F94F886CCF50888ACC061A80D73AAE10DC4590A266DC3C) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/13eQS_P9QjKVAzLbmv3N9w/zh-cn_image_0000002571172677.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=168D28504D7A70B928D49F8C571E140AD37487BEBBDAB6D8889D5494FF7E745E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Y11OXsh1Q7-ZEEXOyFfEzw/zh-cn_image_0000002540772336.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=ED4D85C2B83397A5FC6D9A509C92CD71304D378858063AD137F73FC7A9C7C03D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZZqjDZ0GQrKEIED5LWfJZA/zh-cn_image_0000002571292631.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=35E61EBB39307D118791E9706FE9D7234728ED34EA882E8A4932E6D56E58DA66) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mgIILhUhTEO7DYUuKnKVhA/zh-cn_image_0000002540612684.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=95563ADACC6E04388B37E02A8CBE3D0E6CAD357C1F1F554D7DE8199F243B0662) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/EccIjkjVTte2I_tQph_JuQ/zh-cn_image_0000002571172679.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=23D3513EDA07939CE21CAE1A1F77E33619B236700BF27D863D0FEDCAAF97D86E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GfwmSol9Stajk4KvIjE7rA/zh-cn_image_0000002540772338.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=795CF8EF6A634D12FFEABFE62D80C6DA83849519C5D99439379DFBD78A92D066) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/E3NCxB_6TfaqlGCe3nFEHg/zh-cn_image_0000002571292633.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=BEBF8FBFB48AF1E95A8E490253C544E11CBC1D9E63D053F1DA1828C7C756CC02) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Ka2M1b9FQp-cr8QlevYLRw/zh-cn_image_0000002540612686.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=672DD2B79C1610E5889FAB065508E9944CE0BCD9CC60A05B4C6C8FBCE733DD9D) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/F7jXgGu_Reuz4mu5ZCXR5Q/zh-cn_image_0000002571172681.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=F1E2F8A28C97BA7141830630DEAC7A3ED1889B8F802C6551DA507287930263D0) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_LN902QQQOWu4i6FUp7kSA/zh-cn_image_0000002540772340.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=9B2FE73BAD6842AA8591BC85F5313A16C89D7155032CC1BFC0E0D9C3E41B9583) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/9yvs2lrDT4ynqjH-Rci6Ag/zh-cn_image_0000002571292635.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=BD2594FC6887A0207EDD71032A019D5F243674FFF8FAAC92A42DBF267ADD3E53) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jpgAO2exTOiJBY0MFpqC0A/zh-cn_image_0000002540612688.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=38884CCC8BB3BFA946927E1CF8B95BAEE252218E2DD62B660B7AF2D5EC17D2C5) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tAS0iJgmQM-Wci5_nkn8-w/zh-cn_image_0000002571172683.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=3F6A772BAF6339BE009CCA137971BCE572E0A81BC118987E3DEF8F094346C402) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Cr_zBaQzSCq2oxvDBdGG6A/zh-cn_image_0000002540772342.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=D5B5B986A340C4E30B911D066E1711C9AD6CF6443706567C3F8951D20FE8C575) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/c-Gmv0PST9yqhYoUomwZwQ/zh-cn_image_0000002571292637.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=509EE9E4E991DF034C211419CEDE644DD745BC1B5BB586DADC394D8D3AFD71DC) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/d8qIfw9vRDyYNHK5XCB4Lw/zh-cn_image_0000002540612690.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=8D0E5C049C9382C71B804A1920C116AB57CFE05ABB2CB176C6BD67C5594F440D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/GUvUxRwpSiKwqOYRTbx2Sg/zh-cn_image_0000002571172685.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=BB57A4751D83367D0BC6BC38C9D89951D32BC6BAE145C236108D32ECBE5DED58) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/aOH_rZZ4StaA7CQ-HPPzrQ/zh-cn_image_0000002540772344.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=369FDFAF93B9CCA3CD6B4E2554DC32D998E21108D99B508602B5E1E656357EA9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/zsVwXPysQ9GTZKvgseLF7Q/zh-cn_image_0000002571292639.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=08AC53D839140ED9F5DCC1E58BEB2FC18040E9DCCAE11C3C92E2F9867BEDA600) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Y_ycWxFpQIiLEoQa-_aPmQ/zh-cn_image_0000002540612692.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=AC86E7B2CFB7FE87CAF0114A4CB72DD74F6EEB016E3258451739F63A4D8517EF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AWYlgGLEShuaWPgTGcX8NQ/zh-cn_image_0000002571172687.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=9004959F59CB2F0B0BFC0E4DF4AB37F47A2DE1D9C23EACB216DDBDE94B1821C9) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Oginu0vbQ6OJx_4JTPBMGw/zh-cn_image_0000002540772346.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=1F2941CFC87ABF7CD87D11216D2E26EB742C45EA0572878C6625096891B6C851) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kyuU1ZF3RzSZwHd8rb_gXg/zh-cn_image_0000002571292641.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=A8511B894C74BFBDFFF4873B9BC207E05E025AF6400B671149EACF514B57B146) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uv3kmEHoTwy6HVIz35WEoA/zh-cn_image_0000002540612694.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=CA39CCB657F8F7E0FC94F103FE4B7765E72C4430C57A00C547E0201B0C303CDD) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/tQAvezM3SAy-zyMql8P5BA/zh-cn_image_0000002571172689.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=A3277A759981841898F771DA90E1EB1E9BD42A3E60781E6B6A0FD56AD4C851CD) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qPVEfhvuSnaaTWDg4yRLIQ/zh-cn_image_0000002540772348.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=111E534D8F55CDBA61435D0991A9170618682843D6F211A88184FDE6BC41828E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Jq3n6M6tRjaBskcTHfIFRA/zh-cn_image_0000002571292643.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=EA9AA5D2B11549061F70500959EC9C5A55AA0F8858B05AB24754DF94852F7FA3) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DuwR9acOTueEcVhxxF_ziQ/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=AD942D53A1493F09E41818096FACF689DC1D0E46344C0A767C138866726ABF32) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/guGGODViSn25ENiWZmUA-g/zh-cn_image_0000002571172691.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=58060675860614C5D9C40E885EA3033C9D192852DB118E48763124667B3D93C1) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/qrpiLlflS_2L2o-PaHS1HQ/zh-cn_image_0000002540772350.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=04C0E66773B2250BC340AAB7B7215CF4B71308530FBCC465CBFC87D21CFDE775) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/81KfNtzDRjqF3kLEAVOnQg/zh-cn_image_0000002571292645.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=5B42F539E235A3EF8DBC712F0719C7D3D67B516922D9B47B2A85F589FC58FA52) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/06h-K4k_RnyQN3X6-j8t7w/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=67025406AA4829707E7771FE27A3CE6834F483811AC4393027790EB92DD5A4DB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4vk3NxIZT-WnN9YKkBYw0A/zh-cn_image_0000002540612698.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=DFCEBF4A58E7F1A454E16A2E2781EC6026A8BC53055A1366635AC67E1D753E2C) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/fqRfwr1GSkew7iFt8WClqQ/zh-cn_image_0000002571172693.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=5843055F0E274D106139E543D22DD596A23E8EEC86CEA56895FAD9536CE9957F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kkc44PFGSa-f7T_H53onag/zh-cn_image_0000002540772352.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=5A839D60D34D54F384D01CDAAF83B4B3456E9418F9AA73F306319EC00C4C6DD5) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Oe_QKCMdQ7yrOGjKlse3Eg/zh-cn_image_0000002571292647.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=701049205A3DEA474D2E17AC4D2D1BE9499A34620CF810E2EA3D8F101499EE82) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Z1PvARE5QiSEKM8gsYci_A/zh-cn_image_0000002540612700.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=21D349186A7A0388D7756D349A82A2AFF0CFCC6635CF21CB86E5C2C2BA441BED) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KgyjkPvfRlu0mSHgmHPOFA/zh-cn_image_0000002571172695.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=66FDA2AC2C761C2DFE2A60D553EC645A47CBB7E5CC627CB5FCF96E9C44802171) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/BkyEsLNPRPatmOGME-qvHg/zh-cn_image_0000002540772354.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=FEDD09C6233CAE4A1A402500C99CD93D419B13B6A514FC33449C6002A52EA62C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qR8I1qnmTdWA425VDSf0yQ/zh-cn_image_0000002571292649.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=6DD515BD1EC7D86D59F65EB0B1CA64146F49FF8D7E2D27850DBAD79B7129423C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/abqTtW7KQJW_zQfSOTBACg/zh-cn_image_0000002540612702.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=39879C277FD856435AF0643DA417AA8C915CEB3EEED3BD8EBDDE5B499AF230BA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ngJ0GS45Q8mmueG1FCrwEg/zh-cn_image_0000002571172697.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=FFDB1F43E9797E0F2A3416AB8D67C73DFDDB95D4BC9325BEDBC3D91E63F88DEC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/m0C1aivHQ2uQGEMfQ1T1YA/zh-cn_image_0000002540772356.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=0AE68679A32174284C81A6A605474BA6FB9EE2FEAB97F6514771D94DAF439077) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CKnmngrjQrWuBjS9kDDt5A/zh-cn_image_0000002571292651.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=4C00A88855D05C39C5AE13A97FEEFAEB51ADCFCD3DCBFED290A1C3570B2B6361) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mOiuCNfxSXuM8jx1IqztFw/zh-cn_image_0000002540612704.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=03C067848FE24E88C8B9CC8617B42AD6F685D222A9E9F718C8B3E82F7E6F8260) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SZDRz3coTnyh1J5ERBaDFg/zh-cn_image_0000002571172699.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=6CF473ACFD9F576BFFD15C25FDFD8542EC56864F5B39A717C34773D004B15EDD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/j9KH97hnRwOxhsjJhJ41lw/zh-cn_image_0000002540772358.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=86B48F48C897901CBEBA6AA9613410674343D7747C39F920B6FF88AB8E67CB7A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/yyWOa-GURm-tg8YP5SkVmA/zh-cn_image_0000002571292653.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=7AAE0EB9CB28BDFFCE4311D76B9C06474A55B950407D7A738F9E2796CF26DF8F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HASZHNqxQiiJgs_Ukpjzxw/zh-cn_image_0000002540612706.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=42436689D65B3C52F53029178E2479B73B646A52E9E4863811CD8891EE87C3A2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6SStVNJlSVGMzL9RF-wqCA/zh-cn_image_0000002571172701.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=24235DE834E3BA25F8C1D44C4D7D4EA6F937122A68ABA15A77895FA3337FFB85) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vw3AU5MpR6qVg3ch6PYNLg/zh-cn_image_0000002540772360.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=52DBE523F5D4A4B9AB66D8F3732310D785AFA7AB6FD66111122670B026C84237) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lu574Ju7S22VkL6Iy-Nzpw/zh-cn_image_0000002571292655.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=AB34A893EDE529E72FE2CFF887298E9730AB46058A4995DC10C87585B941CACC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/2Z7kzhUGRYWI4v1vhoc06g/zh-cn_image_0000002540612708.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=67358FF583A1116AE7042DCA9A8D8D5FF3A866FD64BDCD3C02CF9C9120E6A6E0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dNSHuWxRTyqQ8zz-YCr_ig/zh-cn_image_0000002571172703.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=5D29B888CAC995EB080F9AE32DF4528EE14AFBCCE2754896726BC9261CFB8006) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YeRcPYHYSPqk100uvsnKAw/zh-cn_image_0000002540772362.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=3201B592BBAC3B5FC1123CC2360C42E844B94104DC36C13C9EA4D339FE2DBE74) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ovhyb3anRRy8yrUyABS_fA/zh-cn_image_0000002571292657.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=F3CFC183C1E4C21AAD462B12F801E4BB625A3E0E1C4DA2CC5B175DA2F15CB333) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/P1e4sORmRe6u7rbOULI0-g/zh-cn_image_0000002540612710.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=78CF854146DD5B34A76579820A4C5FA8F4B1EA814A58426D71885E16CA861CA7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qL5qpPM6Twef5I_bXkejPw/zh-cn_image_0000002571172705.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=695529DC516ED034D412A5592CB562173073BE1D3A487D751576481AD4B00C87) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IBo0e_0ZQKC3OnONVbwhQw/zh-cn_image_0000002540772364.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=013B885DB383FAD5DE55DC60DA97B02BE372814D47A261835730349996ED4D90) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4i5uRg2lQYi5CcZN-CnBmg/zh-cn_image_0000002571292659.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=12D7FC25B6247A1E98000BAD1143ADF5AE143C4652F4801E0B9E742DC31A590E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/S1h65Hb6QL-pZSAW1wAACg/zh-cn_image_0000002540612712.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=FDF61A03C7D24BA163437C6D04EE7DFC9236E767D0085EA3C3678A89BEC27809) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iRbHrC1TTzeKmnrow1g7zQ/zh-cn_image_0000002571172707.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=12DC994AAA0C138C9EC3685F1F3211D51DF929063D95A624E5D11D8B99F3F962) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/I6h4fSlCTn6GelkIqDvNQQ/zh-cn_image_0000002540772366.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=32B5D1A0D424169BFDBC9EF2D2BFB68D3F04A6BB48867EFE067D2491E41A6F5A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JAEJb5unToiK6oMjKfRlzQ/zh-cn_image_0000002571292661.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=DA0BE0E49ECB5A1C93F0DF1C884B84E55A820AEEAD302279B6A4B2FD424FCAB0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zkmjSzDATXymIWPvxdmlbw/zh-cn_image_0000002540612714.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=3D7CB146B15769849A9ED537D1D7B239D077283FF77EC9871C9BA88FA4E73291) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XMwfj9i0QIeFUDmMCQUGLg/zh-cn_image_0000002571172709.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=52A4FBC46977B7611B9B86E675E293278A3C59E450CA5C035B1A9EB50815A458) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/XgA5OTnGRH-pGtrCdShmDA/zh-cn_image_0000002540772368.png?HW-CC-KV=V1&HW-CC-Date=20260415T025101Z&HW-CC-Expire=86400&HW-CC-Sign=92746898830574CD24BF3F4D534E8B65C477F5A0CD6FC0A34B484723F99C0C1D) |
