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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VGyU99-aReaayU5YM8brKg/zh-cn_image_0000002571292613.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=CA7B6029700B3328AAA06BAF2D4097E975F6DC840ED57279428AC6C159166102) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ewnyj0dtQYGTWVKRIw4vwQ/zh-cn_image_0000002540612666.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=2360CE85B2862FE62C126976CC0B2E9B91F02A34798409A639A49CEDE40641EA) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/2YOu03J7TDm_fJ6ttO0_Tw/zh-cn_image_0000002571172661.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=28FC85AE09E960B912F4C022A0490965ED44CDDB23D73BE820DC9879A3D6C3F9) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-mc8ICV7TnaqzTdZQlQPDA/zh-cn_image_0000002540772320.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=151AA73572CEC73C326BA0E8AB8BC8FF663BE1C125BFFD92475672EBBEE1E1BB) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ctK8rj8WSN67Ueene__nfg/zh-cn_image_0000002571292615.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E08DC1DC159B2A38FE1068331A37A582060366F6CC6EF55077736D66F51A2C29) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Edl0TWBVSRmBAvT-fGX2Og/zh-cn_image_0000002540612668.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=3F4248C5F428A5BCFD11FD0DFCB354DC54CB41B07E394E52B53CC4E39EEEA2D5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Hcsfa448TnS8M35xi2Kx-Q/zh-cn_image_0000002571172663.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E55177594A25BB7E8EE4C2249BB00A2FD8B424DA2CDC26460F3542493A6DB67F) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/MRWCUrtpSOij--9CPfIPFQ/zh-cn_image_0000002540772322.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=B00573619344678526FE856E5137B18379EAC65F4829573C0AB0A754007164EE) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/rz3Jisj9TqarN3MJSA0sEw/zh-cn_image_0000002571292617.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E70B232E63789CE308473473D483DC45097909460426425E6A233DAACC9FBC6C) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/cuYOd7mlSDOsLzRPs2ceSw/zh-cn_image_0000002540612670.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=01259900EA22839784E76A9FCBE0C8473E2A191A141538242EA4FDBE9699337B) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/b6Qt-3qcREihcvIK7O7CAw/zh-cn_image_0000002571172665.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=0FAECFB46E445F85AAF1D62BCC6A9355BB7DC23EA9C35784915FFA3C99B41544) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/6Pj4OrQqTxSAsztPUgS6dg/zh-cn_image_0000002540772324.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=B936387D98007D0E1FF83F1F4F0450AC4304BFC608EB92B297057FCCC0580D9B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/PCWy_RlvQ8-b9Qgl7X383A/zh-cn_image_0000002571292619.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C7BEB913D3C374F310FD5BA6BA5BACCFF6089DCC5475988EC1AB79B8B39DAD8F) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/DyTB_y46TAGTaCWpdWhsiw/zh-cn_image_0000002540612672.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=8E3FB89BE5AF7D31B9889F4DAD188FFB83B8E66C681694B2F28E09CC12487024) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZsM_nVMXRuiVXa6iHI9buw/zh-cn_image_0000002571172667.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=5CF90AB928A956C406F8EEC76F51B53072A0BC2BCBDAB8EFC831AA8316B529A9) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9oo8WUI5QOCpCSyohW7RhQ/zh-cn_image_0000002540772326.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=6C38FC1C713AECD5D5FAC3540F2696511F0A7B5D4C975EA630FB41DAF250EB01) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DX-JtqZCSkyp5ht1sjlcLw/zh-cn_image_0000002571292621.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C949C7C0CA62864D486F62DE05040B8468260E6AA20526EF524B6E58621A744C) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/GKvq92jAS5GCmZNHoEmX3g/zh-cn_image_0000002540612674.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C1722F69B4E49511C50697BB0DAADE807F3D5120DE56B653DE4EF60D9CA3203D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Z2QFxtZtQl-TprIeuvOuBQ/zh-cn_image_0000002571172669.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=EE03C4E7628469BD8D6C15942AFB8EDC56A6AB9968BF27BDB67B77D16A3BD3DA) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Q8aMOB9xTNaOvJ3Z-A1J4g/zh-cn_image_0000002540772328.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=AD7778BFBD44796FD02AF381DD59A5EC51E24A9452DD620422C1FD581F5E2FA5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9OF9HW1vTlWoiJDzWFrcEg/zh-cn_image_0000002571292623.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E417778F7F3ABB6933E0A265FE10361669E2B98E86B3DD40A1218A162BDC4F8D) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jd0HZv1gSbu-xaVfEf8prw/zh-cn_image_0000002540612676.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=2A6D08262C4E42C364DC9EE127A19B327DF154239E0000A837297EC63C3C13EC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/VT90f6ASSpu63FREZROChQ/zh-cn_image_0000002571172671.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=CE0375E7037CD999B2A925602B3ED1A61D7A70C495DE1D0A698F716574A94F17) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0pNYWIEFSUG1YnUgX1Tdig/zh-cn_image_0000002540772330.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C0268471A6351A8BE2639DC6BA87F243CF8A724F6E7D3EE2F7AA3A21FDEC4A29) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zr7870VKRjKMbCdIqarOkQ/zh-cn_image_0000002571292625.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1F046F182F776748A53C9FCD9CBC28CEDD7499D44E93A5C34D5E2D630D692E1E) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qKzO2jDyQveLJoOTe4Zorw/zh-cn_image_0000002540612678.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=EC38B7A79338D2ED7B9E78A51EB19AE6E1526B008B98DB62F40613EE3F091B8C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e6OfWO1CSE20KoZac_8JGg/zh-cn_image_0000002571172673.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1AE77BCF341BE12D3CD34DE6DF63004DFB13FE80A513D1715447D28489332983) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SFw0UjfMSzSkqtySCgj54Q/zh-cn_image_0000002540772332.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=90414E1E4A6C617C350ED61506C9D40A97634ADFCEB434340BC8BA281C8C91BE) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/a7nlLz3LRieAcsBW_V7hgw/zh-cn_image_0000002571292627.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=CEAF117BFE3A25C30AA2F1A3F0C26256C55014F329BF12412C5F80A1707C3F92) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/qEVKxjD-RomYTG5APeamBw/zh-cn_image_0000002540612680.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C1F53C92C4B30F42CF140CDA8FADEE582885F8B9E2D444496506E59F965F7EB3) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/VUNY7qLCRcqPaGAETAyOZA/zh-cn_image_0000002571172675.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=EBCB885B210C892E31F37EC18F4007EC96884BED6A6356D13B16434CA5772C68) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DShelAQiT5a5UnXBgI2Hhg/zh-cn_image_0000002540772334.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=2E253BE11FA9946A0EDE3EC528231A22C7D0F76C84F886AA2DA8E94AD78B5765) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WlpILEALQr2i4NBUKjBI0w/zh-cn_image_0000002571292629.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=19DF4B1A943AAA2CC8029C55C0E44E49FEF43CB240FCDB3D217EF32776C20EB0) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ezIxJGBPRxWkFF3LOOfTRw/zh-cn_image_0000002540612682.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=BD3CF56CEB692212EBA315680FA1362CA54213E3BCFD07C1F682ABC37936B50C) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/13eQS_P9QjKVAzLbmv3N9w/zh-cn_image_0000002571172677.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=817E4603CDD8ACE91D61DE35148136162A65CA4ECFE54A8FB6971CF60EBADF30) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Y11OXsh1Q7-ZEEXOyFfEzw/zh-cn_image_0000002540772336.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=7985BA683D6D3A60074A06AC6EB332EE936447609AE9750FC22AB9FFA544D434) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZZqjDZ0GQrKEIED5LWfJZA/zh-cn_image_0000002571292631.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=B3B660E01E1F1CD6FB49F55E496329BCF5A5A51BBF763A33A5ED7BEF62E46A83) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mgIILhUhTEO7DYUuKnKVhA/zh-cn_image_0000002540612684.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=D0DED6C8F71CEB042755EF04ED033FBBF128F264A8541878E9F9DAAFF37D413E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/EccIjkjVTte2I_tQph_JuQ/zh-cn_image_0000002571172679.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E41539320559C9165892377BAA33FECE303E0D206D7252142B87B47A1C7E3053) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GfwmSol9Stajk4KvIjE7rA/zh-cn_image_0000002540772338.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=3FC33D8D05B5826F86871058B89CFF3D3D604D2975CD85C9649D4106892F4D17) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/E3NCxB_6TfaqlGCe3nFEHg/zh-cn_image_0000002571292633.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=2D65D4BBA7F6661269C89BC529C06E512C550E4F7F07442ED33DEA0265393AE6) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Ka2M1b9FQp-cr8QlevYLRw/zh-cn_image_0000002540612686.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=83A9D8DBBA1115AD1AFBB096702EC093806E8C22A742C8E8F62614A94AEB27A5) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/F7jXgGu_Reuz4mu5ZCXR5Q/zh-cn_image_0000002571172681.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=6D184E9A9C3078503C8396158B796D2623F246173DA81C6185B2ACC536FF97DD) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_LN902QQQOWu4i6FUp7kSA/zh-cn_image_0000002540772340.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=5953F4C3C1224D5364A4D279E336A6FC573425E7544C1CB9FB9EDEC6ECAD9D76) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/9yvs2lrDT4ynqjH-Rci6Ag/zh-cn_image_0000002571292635.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=26F978123D66A042C1B6E56B739DD3CFF9D34AE72FDA153CF51773963A13355C) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/jpgAO2exTOiJBY0MFpqC0A/zh-cn_image_0000002540612688.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=D3381BE179837B39DA147DE3C86DE14A8052F932526A1C2B35BC2F842C88CDB6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tAS0iJgmQM-Wci5_nkn8-w/zh-cn_image_0000002571172683.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=20A26572B9F692D0F769F08A3C87AFF4184AEEC892B2EC72BEB0E7AF1FC97649) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Cr_zBaQzSCq2oxvDBdGG6A/zh-cn_image_0000002540772342.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=933B3C588140893A963AD94B86C7CE69CE96BA54EF60E963FF60DEDA332D9070) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/c-Gmv0PST9yqhYoUomwZwQ/zh-cn_image_0000002571292637.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1A4465428AC0EC0D35588FD4AA1F510CC2B01AF613E500B044881F08390005E0) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/d8qIfw9vRDyYNHK5XCB4Lw/zh-cn_image_0000002540612690.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=89D1F711AEC98D70FD2BAC61310D640688333AF1DC97B425C03D0120C67B0F66) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/GUvUxRwpSiKwqOYRTbx2Sg/zh-cn_image_0000002571172685.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=77404A252DC2ABAC879821662C44739006675227E47BDE24BF57245CC4B4F073) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/aOH_rZZ4StaA7CQ-HPPzrQ/zh-cn_image_0000002540772344.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E78C4A3206E9A40778D27617FFF0F42ED9E71189F3171B33102719441DFF1F9B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/zsVwXPysQ9GTZKvgseLF7Q/zh-cn_image_0000002571292639.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=C23C7C153C96161E3D2E0FB5061B49B482173D838028F2B25D513565050D3D63) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Y_ycWxFpQIiLEoQa-_aPmQ/zh-cn_image_0000002540612692.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=81012CE5974D2BE6D24260E24F3287326DBCC90335CED7904BB1F892E16C20B3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AWYlgGLEShuaWPgTGcX8NQ/zh-cn_image_0000002571172687.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=52DC704F63CC1CCFC420378A3A58797F49EDE960EA9A9312E877CA875F94D488) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Oginu0vbQ6OJx_4JTPBMGw/zh-cn_image_0000002540772346.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=BE74A231ED528271B6E826A0B7E26B35D0EC9A0509145220B6FDF8028561BB3E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kyuU1ZF3RzSZwHd8rb_gXg/zh-cn_image_0000002571292641.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=A0E3A38A74CA7AA2DD51C689773F10C517642BB295E89CCD81D436712309169A) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/uv3kmEHoTwy6HVIz35WEoA/zh-cn_image_0000002540612694.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=9C2F1F00BB3FC062B1F19665B042E5B25C7DB14A36CA4BEE4DAB40F2292E283C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/tQAvezM3SAy-zyMql8P5BA/zh-cn_image_0000002571172689.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=FB75091D875CAED8F4356A3D04B008E3628F0A343B618E58980A0B9BF98B52B4) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qPVEfhvuSnaaTWDg4yRLIQ/zh-cn_image_0000002540772348.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=11D42DC4B9FFF9E3CEDD52C45E9CB16EF3C97A42EF40A9AAC1CE1FF1B8CBF326) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Jq3n6M6tRjaBskcTHfIFRA/zh-cn_image_0000002571292643.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1B1CB44FFF5AE21FAA7109A217E1EA595A514CE0C8B892204FC2C9850AE6BD7C) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/DuwR9acOTueEcVhxxF_ziQ/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=F51EDAA2D804802E2210DF1CFDF9CEF34FF035263CCDDF1596B6E7E796433F3B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/guGGODViSn25ENiWZmUA-g/zh-cn_image_0000002571172691.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=CFA9EB413C042F654C3332BB53B7B008F1E3B57EC10074FCE1BBF282C8387CD8) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/qrpiLlflS_2L2o-PaHS1HQ/zh-cn_image_0000002540772350.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=8BE967DE434DDEE5D0B9C7EAACA31B868A9609FD1ADB013CF6B71C4B16B90742) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/81KfNtzDRjqF3kLEAVOnQg/zh-cn_image_0000002571292645.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=EE514A0980ABD5ECA75BF9874AFFD5FBD0188CF3215B619F7CC2A1045EDC8595) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/06h-K4k_RnyQN3X6-j8t7w/zh-cn_image_0000002540612696.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=8BE6B8B14EE082705BB11D30ED3F9E54BB1898CABCBDCB8DC86951707CB6E3E2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4vk3NxIZT-WnN9YKkBYw0A/zh-cn_image_0000002540612698.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=488403932E46E9C53B0075B0EFF70507783BC7A4A6CD177076F6F1A0CCA55B3C) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/fqRfwr1GSkew7iFt8WClqQ/zh-cn_image_0000002571172693.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=2992922B4C324FDC95CAAF9ABC7E45A0A4D0AC3B2FB3D4637BF6E4690190C4A5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kkc44PFGSa-f7T_H53onag/zh-cn_image_0000002540772352.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=952C07D1D4DFF92FDB6B72BD8AF0668833E1CE0DF23CCDC77995AFDD7F2D5837) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Oe_QKCMdQ7yrOGjKlse3Eg/zh-cn_image_0000002571292647.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=9023FC18EF19B41FD148244025BC51CF1BDDF3BDB464BDA44964E5908002738B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Z1PvARE5QiSEKM8gsYci_A/zh-cn_image_0000002540612700.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E3C276C50A0CB1ACB2FBBE52E49B4B1C53136778D27A62E6806C1C971DF8B614) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KgyjkPvfRlu0mSHgmHPOFA/zh-cn_image_0000002571172695.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=53B96C66C1C866A2C771A02FD870DD6DC87EC614D63F9BCE80BB9BE671547CDC) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/BkyEsLNPRPatmOGME-qvHg/zh-cn_image_0000002540772354.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=602D1FF201F47D33414D1D1FBEA3AD4744112E85B7FD93BFC63688633851B723) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qR8I1qnmTdWA425VDSf0yQ/zh-cn_image_0000002571292649.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=7A39F365BF802A98E918FD839A68FE14DEA51B3CA218037063A60FE7C327B1DA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/abqTtW7KQJW_zQfSOTBACg/zh-cn_image_0000002540612702.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=53935563D63575E2BF8CBC1872B8C06595B9127521FB5EF08C4BD171AF9FC2CC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ngJ0GS45Q8mmueG1FCrwEg/zh-cn_image_0000002571172697.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=9B4C93EADF23AA90255ECF8B1F4E11F6B8823A7C2022357D0BFD0CBC95E80B0B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/m0C1aivHQ2uQGEMfQ1T1YA/zh-cn_image_0000002540772356.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=9319E85144DA3174B71A9C99D702289BE4B82F6DBF235D420A1AB58B067543B8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CKnmngrjQrWuBjS9kDDt5A/zh-cn_image_0000002571292651.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=192AC7F8E5CC06406406FD51FD2588626CC7898F64DEE77FA4D42B5E11DD43AF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mOiuCNfxSXuM8jx1IqztFw/zh-cn_image_0000002540612704.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=DF744A20322204BB2EB2412E790590CA2C30F05D8C479D6A99B861F986438CC3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SZDRz3coTnyh1J5ERBaDFg/zh-cn_image_0000002571172699.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=4486D392BE4625526D8982EE464A9B985AAE9DA476D5985697FA9B501D03BE4E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/j9KH97hnRwOxhsjJhJ41lw/zh-cn_image_0000002540772358.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=4348E99B4E56131FA8D4494668BA479DE5444694D2D5648C5958E67B80E5E129) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/yyWOa-GURm-tg8YP5SkVmA/zh-cn_image_0000002571292653.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1389EDA7AA667D390F2A6A38F63B2922C8EC71848D0CA4879A59CDD738342BB1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/HASZHNqxQiiJgs_Ukpjzxw/zh-cn_image_0000002540612706.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=F5E86F9E96BC605E2664532F58CE843E477C8A2E46F1B6F4D725B97CF9632E38) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6SStVNJlSVGMzL9RF-wqCA/zh-cn_image_0000002571172701.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=551F4D0356C533D2CB7E14402BF7D384377354C4D259A315B9822A4A28AE9916) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vw3AU5MpR6qVg3ch6PYNLg/zh-cn_image_0000002540772360.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=354FD6BCEC2E79AF66BE6381E7A6DF1628536A712AF2DAF572B376C09C2FBD8E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Lu574Ju7S22VkL6Iy-Nzpw/zh-cn_image_0000002571292655.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E92071F646B2AD78AF1034028B0B8A989F9705762FA991670568983B0903C3EF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/2Z7kzhUGRYWI4v1vhoc06g/zh-cn_image_0000002540612708.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=EBE2006E5FD0EF1CD9DB47BF304A5C10035439AF840D770EE70C11DA69D0956A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dNSHuWxRTyqQ8zz-YCr_ig/zh-cn_image_0000002571172703.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=F5BB213AA0E63AD1C7914525967352DB2ECA6FB15DFF8A2C022CFF35BC5E9F17) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YeRcPYHYSPqk100uvsnKAw/zh-cn_image_0000002540772362.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=8C1BBCAB11648B7B33845B9EE9D697D406FA46D92DD75007C632E2F5B613B813) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ovhyb3anRRy8yrUyABS_fA/zh-cn_image_0000002571292657.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=106B92E7BB3ABB210FE0AA44B645F5D2FDE806B12789216886BA2CE557DDECDF) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/P1e4sORmRe6u7rbOULI0-g/zh-cn_image_0000002540612710.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1851E64A7C6A43A2CBF4D7E8E64BEEC6775C644D68E554C1F33A16E403AEB703) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qL5qpPM6Twef5I_bXkejPw/zh-cn_image_0000002571172705.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=1BFFD883C260450CC5B6DC2693DD2017C1B10F4AE1979CC932CDD9F8C25F60FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IBo0e_0ZQKC3OnONVbwhQw/zh-cn_image_0000002540772364.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=ACDAFCEE7AADFC66884251E072D285AA9A2C74598C9E5EF1BC372062FB202F9D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/4i5uRg2lQYi5CcZN-CnBmg/zh-cn_image_0000002571292659.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=8925439FD058DD4E754CD9E037C669EBF824AE107D26D9A9F1414938C1B39E18) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/S1h65Hb6QL-pZSAW1wAACg/zh-cn_image_0000002540612712.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=E1E9B62B8EE61CE4F8074BE7FF3D8495E0DCA55119D53448ED6986E954482079) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/iRbHrC1TTzeKmnrow1g7zQ/zh-cn_image_0000002571172707.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=D918763ED9FD1D494546D5634A927DC74A3EA80B426CC4505AC1ACD576F2A4C9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/I6h4fSlCTn6GelkIqDvNQQ/zh-cn_image_0000002540772366.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=0B60CD5134E4AC244148B9B47174E89B1C6052284882CB53710791764D83F3D9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JAEJb5unToiK6oMjKfRlzQ/zh-cn_image_0000002571292661.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=046B08307FA2860F654942ADCE05CEF355E941EA436F9C8977912B4E06FDC7BB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/zkmjSzDATXymIWPvxdmlbw/zh-cn_image_0000002540612714.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=006D37FBAE6199D256A4A6AA2CC151A47B634D04D5830A6E2C3662023E132A3F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XMwfj9i0QIeFUDmMCQUGLg/zh-cn_image_0000002571172709.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=F07D3109CF878D5B1CBBCC9DA2D62878E0CD281C1334E6337E245517D1AFBF0D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/XgA5OTnGRH-pGtrCdShmDA/zh-cn_image_0000002540772368.png?HW-CC-KV=V1&HW-CC-Date=20260417T025408Z&HW-CC-Expire=86400&HW-CC-Sign=B56B83490E8BCA5C790C52F20FE100B483B2CAA7903CFBBD70B7E8A9EA85E48C) |
