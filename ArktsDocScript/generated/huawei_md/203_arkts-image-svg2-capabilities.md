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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VGyU99-aReaayU5YM8brKg/zh-cn_image_0000002571292613.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=86103FB8D1EB24035C1B1D581FE10812802EC5491F513B19EA125122D3F9B11E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ewnyj0dtQYGTWVKRIw4vwQ/zh-cn_image_0000002540612666.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=1312AF82E2E24EC03E4357E94746B968D770C1F24A520743F474D6F216454CE5) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/2YOu03J7TDm_fJ6ttO0_Tw/zh-cn_image_0000002571172661.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=C2DA91EFBA8AD1147EF93A1AD706FC59AC939F6CCF0979700B55186B0C8AF716) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-mc8ICV7TnaqzTdZQlQPDA/zh-cn_image_0000002540772320.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B28B7F7E9AF2C53FBFCB7F4890F6140373016D2E128ABF7613C963E48689E5F9) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ctK8rj8WSN67Ueene__nfg/zh-cn_image_0000002571292615.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=137E4C80F7D1DB75EC838AAFCDB774883E48D9405A2248E16DD27C71CFE4F1E8) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Edl0TWBVSRmBAvT-fGX2Og/zh-cn_image_0000002540612668.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=008226F38E006A434E210D1552608EAC6846279CFD684FD08A3500C2C5FF884A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Hcsfa448TnS8M35xi2Kx-Q/zh-cn_image_0000002571172663.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=DEA2406C2B7F3B3B97113E3ED47C856C43317C4DDC72C08FE834EBC87AFB9AC1) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/MRWCUrtpSOij--9CPfIPFQ/zh-cn_image_0000002540772322.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=282596C52494C20CA1B63AD0418B1EB303A1E18822565C9D036FA360961D9E3E) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/rz3Jisj9TqarN3MJSA0sEw/zh-cn_image_0000002571292617.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5055BC1C0927EF3B5C74BCE29C5273DEABC53D2485328702C3954AA300E0ABCF) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/cuYOd7mlSDOsLzRPs2ceSw/zh-cn_image_0000002540612670.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5DB01CE1303AAA46550BF2D4D59F8B6D1FC8C33C7B4FBDD3534A0D085DB755E0) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/b6Qt-3qcREihcvIK7O7CAw/zh-cn_image_0000002571172665.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=FAD5A573ECDEE1AEA0DACC6BAF03EA106A7EAFD0E98FF187A95D970D3BEEE53D) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/6Pj4OrQqTxSAsztPUgS6dg/zh-cn_image_0000002540772324.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=41B516C1767183B7A075337580D6CA1C21C7B63E863FF24372ECFFC0717B9D61) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/PCWy_RlvQ8-b9Qgl7X383A/zh-cn_image_0000002571292619.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=FB57E8F781C1FCA61E760C86EF89FE0A3CB0C0B0A9D8B8D254DA7F0FBAF5F25C) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/DyTB_y46TAGTaCWpdWhsiw/zh-cn_image_0000002540612672.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=F44A4FE0F2F2E15AF2478A0D033085A3CEFDBDE0394F52962D77883FAFED1E69) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZsM_nVMXRuiVXa6iHI9buw/zh-cn_image_0000002571172667.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=FF35002615CE72F30A99B630DBFFD5F020BE86755C6C30979B8AB4C1DC1758B9) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9oo8WUI5QOCpCSyohW7RhQ/zh-cn_image_0000002540772326.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B29C64BD71CB87FA7BD1CA267CCFF81E1FA9584265433435DA3168FC2059D4BB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DX-JtqZCSkyp5ht1sjlcLw/zh-cn_image_0000002571292621.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=32B53EA44DBA39C4AFA59C9167CA0791901C95771171495F4AA31A4045BA4788) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/GKvq92jAS5GCmZNHoEmX3g/zh-cn_image_0000002540612674.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=98B0A7B58BC70AE97C036D42563F76823F811CF56A741C2D313AEF399C0C9A80) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Z2QFxtZtQl-TprIeuvOuBQ/zh-cn_image_0000002571172669.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=172BE85E22D56C1A663616EA7CF0C3940A2392C0216DCD22C45B15FCAFF63A4F) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Q8aMOB9xTNaOvJ3Z-A1J4g/zh-cn_image_0000002540772328.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=8511459EC7B067F58791BFB11419010D9349B77667AD91F9D952EDA398669705) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9OF9HW1vTlWoiJDzWFrcEg/zh-cn_image_0000002571292623.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=C4067B2DED3BA101083139816ABB817330988D95C81B73D82F4535D028947100) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jd0HZv1gSbu-xaVfEf8prw/zh-cn_image_0000002540612676.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=8CEA4C1F21EC2A4EC327D92487499292F9D77554E602FB4BAC4D35E45FE60326) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/VT90f6ASSpu63FREZROChQ/zh-cn_image_0000002571172671.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=EBD644D1F9F541AAA229F3F8441CBC89708203B0071DBF043EC8E8AFB790A119) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0pNYWIEFSUG1YnUgX1Tdig/zh-cn_image_0000002540772330.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=553C27FEDD45613F2B792E22933E14ADECA50CF0DFE6E5F887EFB6885C88CC17) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zr7870VKRjKMbCdIqarOkQ/zh-cn_image_0000002571292625.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=3A986FFE02B6BED8E31AD356B7EC928D13358F41588DEEE7A0B0B06E61A482F7) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qKzO2jDyQveLJoOTe4Zorw/zh-cn_image_0000002540612678.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=922B109E169E3E10AAD64BEC7DE0B7FCA7A8554BCC66629118DBF68196C3FF36) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e6OfWO1CSE20KoZac_8JGg/zh-cn_image_0000002571172673.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=81A823E0019BE582E880F74C0026115EC07CDE9758B4F45892E79F0544FABAD8) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SFw0UjfMSzSkqtySCgj54Q/zh-cn_image_0000002540772332.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=BE6F77FB346799E6D52BDBF75E8CF998D3FEDC4CA172B1C25D954B9BD0C5F1CE) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/a7nlLz3LRieAcsBW_V7hgw/zh-cn_image_0000002571292627.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=79DFFD17D6B6DD50BCFEF11765B46CA2F6B4398D7870537C372FEC3BC02C3D83) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/qEVKxjD-RomYTG5APeamBw/zh-cn_image_0000002540612680.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=F4413B41FB8CACB221D73CAC2C1510F7637690A595F52A762D97719345CA811E) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/VUNY7qLCRcqPaGAETAyOZA/zh-cn_image_0000002571172675.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=4C71229A627DA0506C4C4203EA6927FD52C6A6610F24904ADB5D13DCE63E3A2B) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DShelAQiT5a5UnXBgI2Hhg/zh-cn_image_0000002540772334.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B7A9735037F158B470FDBB99CEE1D68E5D1425C6EF06DCB21DA3D4C87926435B) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WlpILEALQr2i4NBUKjBI0w/zh-cn_image_0000002571292629.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=72E50CD934E0AD4DF4E520F1AE4691DB1DA2A3C7614C976453AF859C1BE8FD72) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ezIxJGBPRxWkFF3LOOfTRw/zh-cn_image_0000002540612682.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5BD9AA47EE0983FBC83752253B9AE14E72ADD6726741240D1485068343FDF8E4) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/13eQS_P9QjKVAzLbmv3N9w/zh-cn_image_0000002571172677.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=F95F832BF05227FDF09E0153DD3B528A27D375B6629B0D96634AB1211A578D5B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Y11OXsh1Q7-ZEEXOyFfEzw/zh-cn_image_0000002540772336.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=BD6018EFD0619FA262B2A53F1560AE0B1BBB8F143B7C4BD8CDCE244951373C94) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZZqjDZ0GQrKEIED5LWfJZA/zh-cn_image_0000002571292631.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=ECBB0F2512263A8A9B2566BE1B5845DDBB6FE43E2EE9A9AB788B795C1B5AE273) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mgIILhUhTEO7DYUuKnKVhA/zh-cn_image_0000002540612684.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=021AB4401A3DC7E43024C4B894FBE98376CBF13F796BF74E64FA5F050A6A9BCD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/EccIjkjVTte2I_tQph_JuQ/zh-cn_image_0000002571172679.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=7895BF6ED4AAAE8C5852D0E3BF6543B7593D9CC6E623E02604225490AD4B348D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GfwmSol9Stajk4KvIjE7rA/zh-cn_image_0000002540772338.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6D6169909FB0C71E3D10818DB2343BD7C3CECE90F98A3E3AAAA32834FD12FA3C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/E3NCxB_6TfaqlGCe3nFEHg/zh-cn_image_0000002571292633.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=3B7F0B6E71A7DD192613CA086ADDD07FE1AB53C70A9BD33821CE1052CC83F0A2) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Ka2M1b9FQp-cr8QlevYLRw/zh-cn_image_0000002540612686.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=02DE180D8C1C247F3C72F4AB3B823AA8243D9DF710B7A4AB46A07C3A317F1D7C) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/F7jXgGu_Reuz4mu5ZCXR5Q/zh-cn_image_0000002571172681.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=07CA351D37D9EA6D16F1DEBA5BE934FD06AF383AB588790C8732DCDFAAFA4144) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_LN902QQQOWu4i6FUp7kSA/zh-cn_image_0000002540772340.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=8CF814E7D5A5616ADCC2385216AC681848F15B4BB8252B30F064EE6271AF856F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/9yvs2lrDT4ynqjH-Rci6Ag/zh-cn_image_0000002571292635.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=9F9D6BA6F1D03C457DE644C3CEDF104748502775C00E6BAD2AE35C3720B569BC) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jpgAO2exTOiJBY0MFpqC0A/zh-cn_image_0000002540612688.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=564A05E963EBD51C42ED8697C07963552A88E365D653D8AD59B5645CE2D36E1D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tAS0iJgmQM-Wci5_nkn8-w/zh-cn_image_0000002571172683.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=EE8E740931E3D46551220B724AF11A5D261BC987B0B746B4B0F599E66C367EC1) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Cr_zBaQzSCq2oxvDBdGG6A/zh-cn_image_0000002540772342.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=1A36D44663E9C3137B82E3845922D1EB29A401B0F8B5F621210BADE9A1E496B6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/c-Gmv0PST9yqhYoUomwZwQ/zh-cn_image_0000002571292637.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6A1BE01F273FA45E68A278157682B6E22A5FE989C297FE2A94D605871AF2E647) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/d8qIfw9vRDyYNHK5XCB4Lw/zh-cn_image_0000002540612690.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=3A4FC9C33FDD9EE01D296283680DA6E1443E9BC8AE3405183F3976A1B6C66BB7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/GUvUxRwpSiKwqOYRTbx2Sg/zh-cn_image_0000002571172685.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6761CEE30EDCDFBC8FC2F42ACF873733F68D05B4ADDE5E619C34FFE96A759316) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/aOH_rZZ4StaA7CQ-HPPzrQ/zh-cn_image_0000002540772344.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=CC4D927E30F24F4C9C8C9C84F7186A3D46422CBEDF19E6567716716032817FDF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/zsVwXPysQ9GTZKvgseLF7Q/zh-cn_image_0000002571292639.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=04E90E507E1D67584181B91833ED42C836BAB57A5F14019B801BD54AA6856002) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Y_ycWxFpQIiLEoQa-_aPmQ/zh-cn_image_0000002540612692.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=D3C273DDBB67A2DF58BD477AD3C42AEC69ECDDCE2ABFE48E6B04B3F5F13613B1) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AWYlgGLEShuaWPgTGcX8NQ/zh-cn_image_0000002571172687.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=ADC359DF202902C55F9C4981DF0F5811B10D15401B88153626D5F84F9DE4D1AB) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Oginu0vbQ6OJx_4JTPBMGw/zh-cn_image_0000002540772346.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=4C03F623B4F98CAAD3AAB808F224DAF6AA7881DEB55D5BB9A6A7B0B02D4CE9D1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kyuU1ZF3RzSZwHd8rb_gXg/zh-cn_image_0000002571292641.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=8269CB51243F6E4A28AF6E0E0BEC9D34229475DFED7A9F309EFDE7DAAA65210C) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uv3kmEHoTwy6HVIz35WEoA/zh-cn_image_0000002540612694.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=068DCEAB02026FB0EC5173154EF028DC535572BBFFF65C9F1FFE56F62847C0ED) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/tQAvezM3SAy-zyMql8P5BA/zh-cn_image_0000002571172689.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=3175D7BF45B543258125C89288DA6D5F23913BBBAC621369D22BEB24CFA0C913) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qPVEfhvuSnaaTWDg4yRLIQ/zh-cn_image_0000002540772348.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=071031B9DCD07AA4D9CDB73764E14DF823B17D4F86A7271310143291B3E86BE1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Jq3n6M6tRjaBskcTHfIFRA/zh-cn_image_0000002571292643.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=1E46F67C9106BC982EB671E7428833A25BAD38A45EC9388B7D537DF0F9DCEB0D) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DuwR9acOTueEcVhxxF_ziQ/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=9873FBB77946190D675B6F5E3414B6B7B05920E8F7C6CF618DC32C2F1BC1C7B1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/guGGODViSn25ENiWZmUA-g/zh-cn_image_0000002571172691.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=A125928E7F49C7FE7987B49A7D4A6E6B71662854433A53CC7458FFE2B899E892) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/qrpiLlflS_2L2o-PaHS1HQ/zh-cn_image_0000002540772350.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=CFDABD044C7A4FFB3C16B9C193B669AE40C52E27A522D88CFC6BADBE9E7F6603) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/81KfNtzDRjqF3kLEAVOnQg/zh-cn_image_0000002571292645.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6CFFB994F35A6952AC446152FAA39212B797C19B734A453A716F7173299AB44A) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/06h-K4k_RnyQN3X6-j8t7w/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=71FF9C713B1340E6FBAC463483FE44734FA9021065830D9B9837FFCB2E3FF5AC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4vk3NxIZT-WnN9YKkBYw0A/zh-cn_image_0000002540612698.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=A04E7AAD3B8AE6E9FDDBD5EF6E56AE176F2CA50DEDA831F0A740D80E0A61C8C8) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/fqRfwr1GSkew7iFt8WClqQ/zh-cn_image_0000002571172693.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=341CCC5EA283CF73BBA4095677C017FC94A425E97FE6CD94DA53C4968FAB7557) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kkc44PFGSa-f7T_H53onag/zh-cn_image_0000002540772352.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=2D64A281786E653E7D16B41D5FAD8A6D2D4942166BBF2CE939915645E99141F3) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Oe_QKCMdQ7yrOGjKlse3Eg/zh-cn_image_0000002571292647.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B8ACD44907EBF6676D788BBCC194AC6B74A15B89E2B2F3CE016FD1A0C863EB50) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Z1PvARE5QiSEKM8gsYci_A/zh-cn_image_0000002540612700.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B26F456F2D7DE9C1AD9ED1885D9F6CEE335B3042E51520B3BC5CD0227C0B8E5B) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KgyjkPvfRlu0mSHgmHPOFA/zh-cn_image_0000002571172695.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=09EDFE84DBE139EE63F308A5629622CC93BF62498B019E473A4CA6D37993A89A) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/BkyEsLNPRPatmOGME-qvHg/zh-cn_image_0000002540772354.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=EE2D23B95B8A87A9B42439C93940E30B98B9BA48916E157EDA7FC30BF8FED3B6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qR8I1qnmTdWA425VDSf0yQ/zh-cn_image_0000002571292649.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=AC54CE2A63C3DD2ACCD2B6704C70C79825725D4AE1B72FA71DE6732DCD64F5BE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/abqTtW7KQJW_zQfSOTBACg/zh-cn_image_0000002540612702.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=D8BBC4464D68498227F58DA8C4E40BF987FE17264ED8599A4C13D4E1226ABB03) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ngJ0GS45Q8mmueG1FCrwEg/zh-cn_image_0000002571172697.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=92FD53E9D098329C0F572EEA84B3CEFD7E814A38FC4A866DC728ECC4004075B7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/m0C1aivHQ2uQGEMfQ1T1YA/zh-cn_image_0000002540772356.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=FEA08E5257FBC6B12CF7B953A87953073F737E082BD8B028A5064B19EA9D9DC0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CKnmngrjQrWuBjS9kDDt5A/zh-cn_image_0000002571292651.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=CE58030F8ABA97B9578D7E034ADE9C1901EE1A55D25FF653E498DEE84CECE2B3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mOiuCNfxSXuM8jx1IqztFw/zh-cn_image_0000002540612704.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=938F8BC1670537BF6390E3F5BF92249870DC0E777A76A7703678BE1BB4EF22B1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SZDRz3coTnyh1J5ERBaDFg/zh-cn_image_0000002571172699.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5349C2C32F020D2DBBA7FC57BA6A9E5B448477A36C2167234D23DFD9FDDDE814) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/j9KH97hnRwOxhsjJhJ41lw/zh-cn_image_0000002540772358.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5421CA39E56AF6CAC5B39B189A3CAD871ABED4D29769AB90E8BB7565DC2EEE30) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/yyWOa-GURm-tg8YP5SkVmA/zh-cn_image_0000002571292653.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=C86F580E56E872E0211A50372C045AD8209FC034D5450FF8822D786A1A1F2B86) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HASZHNqxQiiJgs_Ukpjzxw/zh-cn_image_0000002540612706.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=FDDF530BFFCE386D1E4957C4A6E58F956BF75C01B5B1B6EB0635183E99F4264B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6SStVNJlSVGMzL9RF-wqCA/zh-cn_image_0000002571172701.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6563E60D1EA236978D3EA98906CFE4AA860C3E051CD699F38D4B182C985FB0A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vw3AU5MpR6qVg3ch6PYNLg/zh-cn_image_0000002540772360.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=A04FBB9B97C34DEDD2809A8C4F02B0E56981CAAE37A11AC118A6CCF9196EF561) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lu574Ju7S22VkL6Iy-Nzpw/zh-cn_image_0000002571292655.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=6A55CA7AEE937ABFCFBB61D2707E736C34D644EB0FC8529183CA7CC059252C8B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/2Z7kzhUGRYWI4v1vhoc06g/zh-cn_image_0000002540612708.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=2B3A01C598EC3C376388B98F31F45D3E052FCCFD6F5C132C0E3EA17E1D09872B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dNSHuWxRTyqQ8zz-YCr_ig/zh-cn_image_0000002571172703.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=3B0077F25043A9A5FB7E538D7582809DC8B6E1E80203A1615DD565460930FEAC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YeRcPYHYSPqk100uvsnKAw/zh-cn_image_0000002540772362.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=4CFEBC1C5D64E2119E1AA7E611BCF9D77A457EC7D71CD7AA75E4EFED0E32370F) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ovhyb3anRRy8yrUyABS_fA/zh-cn_image_0000002571292657.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=2EC28C2A0D9644F33CB50F6A85260E6306872BAEFABAA014A7454C865DBFBA89) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/P1e4sORmRe6u7rbOULI0-g/zh-cn_image_0000002540612710.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=AC03054A2AFE88173F7DD6287E5C84E7A59520897702D880600E9241F2DC49E2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qL5qpPM6Twef5I_bXkejPw/zh-cn_image_0000002571172705.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=683FD7C0B8126C62331E4F2858BE03B8591AA7D532115F6F06209CC524FF58B5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IBo0e_0ZQKC3OnONVbwhQw/zh-cn_image_0000002540772364.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=5F4579075D32251CB977F6CA9B9DC441A631D1DB32EB0AF4B9A44A446C920886) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4i5uRg2lQYi5CcZN-CnBmg/zh-cn_image_0000002571292659.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=D217879EC31F356C00978525CCF0844B0D2CC4525A7DA9865495881BC40DF403) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/S1h65Hb6QL-pZSAW1wAACg/zh-cn_image_0000002540612712.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=E25D28301A3D403D7C1D2F8D18084941CA8099079A19752858A4EB8695B09BD9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iRbHrC1TTzeKmnrow1g7zQ/zh-cn_image_0000002571172707.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=B4BC6F46044A535B3D3AB2293CD557249594983519590727871075699D6C9714) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/I6h4fSlCTn6GelkIqDvNQQ/zh-cn_image_0000002540772366.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=97FFFFC8BEC9E59A2E109686FBC9951BADEFCF42A69CE0714EE54C7BE9EFB28F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JAEJb5unToiK6oMjKfRlzQ/zh-cn_image_0000002571292661.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=00A6ACACAE63D0084BD782ACCE10D5C65FEA1344CE8FBCA3249376C33D046A16) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zkmjSzDATXymIWPvxdmlbw/zh-cn_image_0000002540612714.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=1E2139BF91F593752FF9FE21EE912F9AD8DF24581429697489E1445863B8EEF9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XMwfj9i0QIeFUDmMCQUGLg/zh-cn_image_0000002571172709.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=32B53A61D756482F9E14E689F624FDBC0BC01871830063CCB7D8397DC80AF575) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/XgA5OTnGRH-pGtrCdShmDA/zh-cn_image_0000002540772368.png?HW-CC-KV=V1&HW-CC-Date=20260414T025348Z&HW-CC-Expire=86400&HW-CC-Sign=2304FB07E13D046A68E101F4CE0F446F361C4313B5D84FA7088D3E52A6445EFD) |
