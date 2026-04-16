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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VGyU99-aReaayU5YM8brKg/zh-cn_image_0000002571292613.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=CDC1F27378559DD90FB6412124D57B9C6CA3982F2F71B3AB7971C4C4096F69D2) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ewnyj0dtQYGTWVKRIw4vwQ/zh-cn_image_0000002540612666.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=8C86265EA458C962149D6916FA1E157B11645CAE51B8D7585045DB97BF4A41EC) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/2YOu03J7TDm_fJ6ttO0_Tw/zh-cn_image_0000002571172661.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=9F1E1AE0C8182C407A2D93E35C7F0942B0687318591A75E02D3D3F1277462F8F) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-mc8ICV7TnaqzTdZQlQPDA/zh-cn_image_0000002540772320.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=12A50226C2240EEE12875B6FFF4815E5AC49A2CD5EFBBE4FCAC87A9DEA35D086) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ctK8rj8WSN67Ueene__nfg/zh-cn_image_0000002571292615.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E7CBE2DD00478AE7D8A94F20C9F32E20B19100A266807F777FAB3786DBC13677) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Edl0TWBVSRmBAvT-fGX2Og/zh-cn_image_0000002540612668.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=85D50368CA1CF976FDA79404AD5C5EEE5E4C202AB280D2CB75656D74C1F46A3A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Hcsfa448TnS8M35xi2Kx-Q/zh-cn_image_0000002571172663.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=5B0FC4F58945B4B08EB80460F321BA24AEF67636BBB6A45A98AAF63142914753) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/MRWCUrtpSOij--9CPfIPFQ/zh-cn_image_0000002540772322.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=8EA0D4D0F1C3FDE352E61A81C6DCB679CE513BEB96A515242514004C6A85CDD6) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/rz3Jisj9TqarN3MJSA0sEw/zh-cn_image_0000002571292617.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=07D0F46C00B0192DB546AA498E67A21F9D5EC57DEA42AB775AECF1DDF2D3C49B) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/cuYOd7mlSDOsLzRPs2ceSw/zh-cn_image_0000002540612670.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=EEC25ACD1DBC4EE7A9457819EC9A25B028A3937C3744E813DE0DE709F2DA852A) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/b6Qt-3qcREihcvIK7O7CAw/zh-cn_image_0000002571172665.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=A1CFA106693F4E8B41E1C69F9CD288345F65EF80BB94658BC898A4BF8CB4D364) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/6Pj4OrQqTxSAsztPUgS6dg/zh-cn_image_0000002540772324.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=11C713B8CC562BCA32E541910D4D74533A2A54E8A0D319A6BCA69D9FE0F5D950) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/PCWy_RlvQ8-b9Qgl7X383A/zh-cn_image_0000002571292619.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=3E68AE0B608ECCEF1478159288E669AE70A6B57D061799A5388190E792BCCAE6) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/DyTB_y46TAGTaCWpdWhsiw/zh-cn_image_0000002540612672.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=C7D39D79970E019B4FCD03A126694F916BCAB0BA760B9F80786D111240DCACF7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZsM_nVMXRuiVXa6iHI9buw/zh-cn_image_0000002571172667.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=D2E80A0CA3A12B8D5010F64EABC617A0F30176FA4DD825EBF4494EBBD16AB1EE) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9oo8WUI5QOCpCSyohW7RhQ/zh-cn_image_0000002540772326.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=5767067854338614C3187CB006175AE642A79A996E56A849ADC1885C02AF472A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DX-JtqZCSkyp5ht1sjlcLw/zh-cn_image_0000002571292621.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=9DB9EC137FB0300D6407FAD77021599E11A79829BDC7778E8D3234B4E879814D) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/GKvq92jAS5GCmZNHoEmX3g/zh-cn_image_0000002540612674.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=C47000C04185EA90643F65F1A04BF941398743B52BF4A767EF6A727B570DBDDE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Z2QFxtZtQl-TprIeuvOuBQ/zh-cn_image_0000002571172669.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=460CA4AC72D407E2A87496902DA60B00983FCF45838BE531889D959557996C55) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Q8aMOB9xTNaOvJ3Z-A1J4g/zh-cn_image_0000002540772328.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=F60E92AB4F3D545C7D832DF159A069D062F494D9CE7F57475EBF76BCA883B371) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9OF9HW1vTlWoiJDzWFrcEg/zh-cn_image_0000002571292623.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=54F050884908E2B4E9A60959CF8589DF17062FFED2378F6DFF16F8592AF56CFB) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jd0HZv1gSbu-xaVfEf8prw/zh-cn_image_0000002540612676.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=FEDB1054B5AD9C4976EA16C9AC8873B615A65B562C68F31EAD29F0829CE02CCB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/VT90f6ASSpu63FREZROChQ/zh-cn_image_0000002571172671.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E5EE3FFF8503CA7D6E75E1D11E40E7B0B604C5831B7BF8E5A727E7CC2B474831) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0pNYWIEFSUG1YnUgX1Tdig/zh-cn_image_0000002540772330.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=725D1D4F16649E3FBD6B2EE6B78142F224FB1B03B66FC2A828763B19341AA1E0) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zr7870VKRjKMbCdIqarOkQ/zh-cn_image_0000002571292625.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E508102A1CB73282C387526CF8E4C3EC648E4AE67FFE180659980AF8C75A1D72) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qKzO2jDyQveLJoOTe4Zorw/zh-cn_image_0000002540612678.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=F3DC3E6262C681F7398782C34FC7E70BC4A5A163144BBEC0B533A67B1F2CD469) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e6OfWO1CSE20KoZac_8JGg/zh-cn_image_0000002571172673.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=7094861FFA39466F05F249D3811B431BC9A30D496986A53ABC95846B2399542F) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SFw0UjfMSzSkqtySCgj54Q/zh-cn_image_0000002540772332.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=FAD432C0A0B2C94C7A65F47CDAA0FEE853EAE070132335D4531C18D505004CF0) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/a7nlLz3LRieAcsBW_V7hgw/zh-cn_image_0000002571292627.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=3C3A091A0FC4963DB5FDE1DE9FF7DDAEE8F2D1008BA9354688311F69DCA72654) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/qEVKxjD-RomYTG5APeamBw/zh-cn_image_0000002540612680.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E898ED7FA686598CD577DDA8C5E80A883BA712D487B9D6FB3943BF5D1AD22F06) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/VUNY7qLCRcqPaGAETAyOZA/zh-cn_image_0000002571172675.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=5B296F80B3688C492CFB17D251C8357F07EA192667496B4C447982AA8022F71C) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DShelAQiT5a5UnXBgI2Hhg/zh-cn_image_0000002540772334.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=12C1952F939E6E1E42176142AFDD8C43FF602BCDEF963A54349893DE61F92C7C) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WlpILEALQr2i4NBUKjBI0w/zh-cn_image_0000002571292629.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=824090482B2DCA23E4E923CDADB611E1F8DE90EBF7C44F6562ABAE39FFAA01FC) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ezIxJGBPRxWkFF3LOOfTRw/zh-cn_image_0000002540612682.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=58337A7ED7F2639C9032269E7E21AD5BB49F135EBEC7119107F4EE1BDF04265E) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/13eQS_P9QjKVAzLbmv3N9w/zh-cn_image_0000002571172677.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=2228066FFF7FB712155B657C2C391D6D48ED17F872A38CB962733C093715F0A4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Y11OXsh1Q7-ZEEXOyFfEzw/zh-cn_image_0000002540772336.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=316C1BE4C405B36321622B9FD43EC6BD399C59293A1BCA796822A375AE9ACCDD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZZqjDZ0GQrKEIED5LWfJZA/zh-cn_image_0000002571292631.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=B82C9D778A0C5F618BFA92A590D077EEF387B2DAB146E39345D2CA75015E269E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mgIILhUhTEO7DYUuKnKVhA/zh-cn_image_0000002540612684.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=0788586A440F39BA49F40B7D2A182395CAC9B43284A1D2A8ADA8252606D52C53) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/EccIjkjVTte2I_tQph_JuQ/zh-cn_image_0000002571172679.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=57C5D3748F5079D78A190E03C12C9ADC46169D06884A7153D6A5625D8EC6C662) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GfwmSol9Stajk4KvIjE7rA/zh-cn_image_0000002540772338.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=B98F7A82CDC505F3064D7C0419359415E87A7418D0D7BBB3654845849D648EAB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/E3NCxB_6TfaqlGCe3nFEHg/zh-cn_image_0000002571292633.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=B7CA5FAB22A46FEFAB661012CC1460FB78F652C74E8A83611FD12B70E57C46F8) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Ka2M1b9FQp-cr8QlevYLRw/zh-cn_image_0000002540612686.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=2ED93D78F98E57E110B25E75ECEBB0661578C148FD1CFD77EED9B54793C0B88E) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/F7jXgGu_Reuz4mu5ZCXR5Q/zh-cn_image_0000002571172681.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=581F63F2627D8B057C93406D48C4C52D8BC85145BCA2C978F32D3BF8C20B3D2D) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_LN902QQQOWu4i6FUp7kSA/zh-cn_image_0000002540772340.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=89880FB305F260CED2FE7AC3EDBF5A029441CACD7BE0B2E8CF9E9E8168E7B9DF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/9yvs2lrDT4ynqjH-Rci6Ag/zh-cn_image_0000002571292635.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=67768BE52022D49DE323563477BB122F13A1F44FCF6149FE757EA4D9EEFDEAC5) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jpgAO2exTOiJBY0MFpqC0A/zh-cn_image_0000002540612688.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=C7E826BD2511CFF4D27E05E7BA6A53EBA4131380AE9D3F4D7F90511540379B53) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tAS0iJgmQM-Wci5_nkn8-w/zh-cn_image_0000002571172683.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=8368ADBC39806C897D77D6461E82996F1D4AA14D6E01E90C9CB99BC06881B66A) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Cr_zBaQzSCq2oxvDBdGG6A/zh-cn_image_0000002540772342.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=C9C45CFD75406606570A7C8AEFC4A6FABC8F420E0F8C9B7C7DB279A1511E3729) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/c-Gmv0PST9yqhYoUomwZwQ/zh-cn_image_0000002571292637.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=57790BC1269E58126C71F3F46778095BB399F66B58A1EDEBA635A6BCA1646F0A) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/d8qIfw9vRDyYNHK5XCB4Lw/zh-cn_image_0000002540612690.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=1D101822D4AB2F1DF13B4E2F76C2D57ED50830A5A8D305F977BC0605CF02F45A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/GUvUxRwpSiKwqOYRTbx2Sg/zh-cn_image_0000002571172685.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=4AF065B2A15593C632A0C004A66A6D1F591575F63757B349B5291F11CB5B6DB8) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/aOH_rZZ4StaA7CQ-HPPzrQ/zh-cn_image_0000002540772344.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=45F4404EA4E916DDE1E37DBD7B4649293787F53970A7F048923C26C4D1C3C314) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/zsVwXPysQ9GTZKvgseLF7Q/zh-cn_image_0000002571292639.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=15603D9AC9476A4B10B6B2BBA83F284DC2D1F6AE81162EEA7894B3A9BC394C3F) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Y_ycWxFpQIiLEoQa-_aPmQ/zh-cn_image_0000002540612692.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=1F9DCE8E44F0D2DC78D2F2A89AB1870D8121BDECEC0A9A4CA9EC4371253289E7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AWYlgGLEShuaWPgTGcX8NQ/zh-cn_image_0000002571172687.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=CEE9ECC8A1B6CAE911CD58177A4E7E562064C1BBE2446139F92237D45849AF5D) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Oginu0vbQ6OJx_4JTPBMGw/zh-cn_image_0000002540772346.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=0452C6389A0AA33CB7894ABDDA59A03FE9889DF4FDB75871A98D74BD59EEA0B1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kyuU1ZF3RzSZwHd8rb_gXg/zh-cn_image_0000002571292641.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=6F2C8784927CE4D98E1DB58A5E80E62753F63BEE5E90DE0FF1BFE35DC7C96B45) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uv3kmEHoTwy6HVIz35WEoA/zh-cn_image_0000002540612694.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=119D3EBF52D23CEB58583CDD6166B354C63450441F6B7A16C834EC975A0CAFD7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/tQAvezM3SAy-zyMql8P5BA/zh-cn_image_0000002571172689.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=7B00FD567EA011BD99CEB548B23A2E9DF91FAC06E8192D1A30E1F03C89CA4EC3) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qPVEfhvuSnaaTWDg4yRLIQ/zh-cn_image_0000002540772348.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=13A0A363149975094A5EA03EC3204FF0EB459A8F988C057C9C4569B7E40BB6C0) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Jq3n6M6tRjaBskcTHfIFRA/zh-cn_image_0000002571292643.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=8CCCD32FC325035F4D233E98C256B4EB2CF6F4AB392747684E1ACEB5F8A380F5) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DuwR9acOTueEcVhxxF_ziQ/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=6C537CF458D830C6A2A66A4EA686C2EF9B01CD0C5D991E3D6FCDF6A1F783C855) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/guGGODViSn25ENiWZmUA-g/zh-cn_image_0000002571172691.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=FB0BFA1DEDE57650666BA5A42E816484D8E66B102DB51039CDD879F5F9BFE5A7) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/qrpiLlflS_2L2o-PaHS1HQ/zh-cn_image_0000002540772350.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E00DB730C9481BC338219E5968926A566DF68C71735BCEBF1AD676EF78F6AEA1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/81KfNtzDRjqF3kLEAVOnQg/zh-cn_image_0000002571292645.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=B5A26381D876BF7681C6DEF90B2280A5F5A982CCB03338EB95BB83866DB2E359) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/06h-K4k_RnyQN3X6-j8t7w/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=B160BA7B21BA23EC3F77210BF589621BB31B1B582C2E5397FA07DCF116F2937C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4vk3NxIZT-WnN9YKkBYw0A/zh-cn_image_0000002540612698.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=1ED5E452A3269B888F1F01F436D8A4DC036EEAEDA04A3B0C7187E6057440E006) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/fqRfwr1GSkew7iFt8WClqQ/zh-cn_image_0000002571172693.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=50B6BAAF89B6A37C4E5E9E0A94726D0DEDF416BB5C332418C94A142C2D407DD1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kkc44PFGSa-f7T_H53onag/zh-cn_image_0000002540772352.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=BEF5EBC57C2BAB72E4B37EC5768C8E26ACA190519C2BD37909FC431CE2DB8F11) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Oe_QKCMdQ7yrOGjKlse3Eg/zh-cn_image_0000002571292647.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=F017D7D6C9AAC439E2C38E6AF52F9FCABF8C9A855E1B0317244BA04774FBE888) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Z1PvARE5QiSEKM8gsYci_A/zh-cn_image_0000002540612700.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=FA4C96BB0E65A03CEAECFF5B12FACF01C98F77FF368FB272C20D53C9BD1AE9BF) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KgyjkPvfRlu0mSHgmHPOFA/zh-cn_image_0000002571172695.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=0572DBE172C5C7898F718D6D3B442D34600FD4DE766EE140C18700868EE61FC5) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/BkyEsLNPRPatmOGME-qvHg/zh-cn_image_0000002540772354.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=D68DDF515388B8334F5F86478966C9C792C4026972FF1EF88741DB713CB47119) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qR8I1qnmTdWA425VDSf0yQ/zh-cn_image_0000002571292649.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=47830F5FDC7B8AF6D0FAF625CD05D1D98083BCDECE222FD692838D8735CDBEAE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/abqTtW7KQJW_zQfSOTBACg/zh-cn_image_0000002540612702.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=7BF922B587BE11953825F59F93275A001A1481357F175CA895E0539202B7F6EF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ngJ0GS45Q8mmueG1FCrwEg/zh-cn_image_0000002571172697.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=156CBA2A867E30E5655AD17353FB80784680D636BDCF9F6F5FFDE40A4F71ED0F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/m0C1aivHQ2uQGEMfQ1T1YA/zh-cn_image_0000002540772356.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=6885C51D3D59F697140D39A4C97E63C12AFE99DE9BC04CC3F8227D1D76568FB3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CKnmngrjQrWuBjS9kDDt5A/zh-cn_image_0000002571292651.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=5F8FF5915591CC373BB6B9B2C1D47D11DD2CCFD94E1A0140AFA3B4222DC78001) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mOiuCNfxSXuM8jx1IqztFw/zh-cn_image_0000002540612704.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=23CCB41673391CB971CD52825B3072D32F3C461C1857FAA9BE329F05D4518661) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SZDRz3coTnyh1J5ERBaDFg/zh-cn_image_0000002571172699.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=EE05EE226C3383EC10C682FBF96FCC3284C74308F410880478A3322EB21F8259) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/j9KH97hnRwOxhsjJhJ41lw/zh-cn_image_0000002540772358.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=2F1FA43B9AE8A13875B2B1EC87DF23AD075E1A3E777700488028DB3D9F02B891) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/yyWOa-GURm-tg8YP5SkVmA/zh-cn_image_0000002571292653.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=F60FEF45BE8675DD60B35A10E9DDC60050BF7553F59D819F6517FBF5342A561D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HASZHNqxQiiJgs_Ukpjzxw/zh-cn_image_0000002540612706.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=F49E9280F9DA6A960280377A1269570265B0043323CF3BB35726A51E82CD141E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6SStVNJlSVGMzL9RF-wqCA/zh-cn_image_0000002571172701.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=BC58D99D9E80B1CD7A10BF66E8C776129C05E6A61ED9EBFDB91E39606E3C3367) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vw3AU5MpR6qVg3ch6PYNLg/zh-cn_image_0000002540772360.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=C04EE275CA10F950E2C6AAC0B6D2706DFEFDFEEB9174B1B94E850FFAEDDC8304) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lu574Ju7S22VkL6Iy-Nzpw/zh-cn_image_0000002571292655.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=57530870D10E0414E5F4E1EDF5DEF54BE6394A70F1B94EEA3437836D8C77F584) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/2Z7kzhUGRYWI4v1vhoc06g/zh-cn_image_0000002540612708.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=487B038C16F9C529E857CECA1322DDD32D3A6FCDF8F588B80E7220ED3EF70213) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dNSHuWxRTyqQ8zz-YCr_ig/zh-cn_image_0000002571172703.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=3CC2259FE55AE1F779DC6797CAEB58ADDC6D86CDE541696440634A130E11728D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YeRcPYHYSPqk100uvsnKAw/zh-cn_image_0000002540772362.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=E5B47D665BCD9EC98754DEC02576D21A294FB5EEF2B309D10A053F8E1473977C) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ovhyb3anRRy8yrUyABS_fA/zh-cn_image_0000002571292657.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=818B445D71E7EBD9CCC8CCEA9E8CA90035F74481BE25011A7AAEA4C3C770ECBD) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/P1e4sORmRe6u7rbOULI0-g/zh-cn_image_0000002540612710.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=80128F0FE508BCB86EFA26D07891DF641FE2F8802AC17FF9D582734F2AD79A11) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qL5qpPM6Twef5I_bXkejPw/zh-cn_image_0000002571172705.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=7822315469E516BC78D5237873C606FCA813D40180896A2910C777A387572355) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IBo0e_0ZQKC3OnONVbwhQw/zh-cn_image_0000002540772364.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=BB353161C2D470FB8940045C6EF4D5C2D98CF8627B8337F81A50111B943BF0E4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4i5uRg2lQYi5CcZN-CnBmg/zh-cn_image_0000002571292659.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=0E6106F954D1BD1146454312BEA2FC7EE11CDE390D9F87E372AB9717781D85DF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/S1h65Hb6QL-pZSAW1wAACg/zh-cn_image_0000002540612712.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=54F839DAA88DAE46D24B834A058D6CC4B7AB5BE58165C2BC05DBFE6B11548FDA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iRbHrC1TTzeKmnrow1g7zQ/zh-cn_image_0000002571172707.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=D45664D661C0D8FBD91FA50E46ACBAD9957AE145AD85ED1E82D3939F5186C2C2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/I6h4fSlCTn6GelkIqDvNQQ/zh-cn_image_0000002540772366.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=42113F3328793DF1F6AE57A261E6B10D021965AA00955BD444810FD105D24E7B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JAEJb5unToiK6oMjKfRlzQ/zh-cn_image_0000002571292661.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=8499B814D4FAF22BB4BA084AE7957A75D73904F544BFCE3FA2597DAE1BE62F07) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zkmjSzDATXymIWPvxdmlbw/zh-cn_image_0000002540612714.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=FFB15C0A4343155280AA8B0E84027BCE99DB3F49B518954B5858BCF815E766B1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XMwfj9i0QIeFUDmMCQUGLg/zh-cn_image_0000002571172709.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=4C94F738C41DB6704DE74C92C697D451FD2D1BDBF0FC8430C427637131C7F9A0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/XgA5OTnGRH-pGtrCdShmDA/zh-cn_image_0000002540772368.png?HW-CC-KV=V1&HW-CC-Date=20260416T025816Z&HW-CC-Expire=86400&HW-CC-Sign=BD115B0FEFB70BFD6CD4C7A707A1397FBAC31D7624DA8D1F4D86C3DF931865E5) |
