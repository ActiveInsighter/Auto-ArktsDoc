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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WA7BldDTRwuWwnQ9o5fsyQ/zh-cn_image_0000002569169621.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=DC0D597D7929A80036D71B5666AF63135C1689BFD3CB447FE1E4EE43D94C54CF) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/wFu60U6ERS2FRYi_y7QsXA/zh-cn_image_0000002569129647.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=4A70E848D2CEC06BC780D84BA25D3DD02F73812AD62930E679DFCB8C13009317) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/P4GVjIWnRXO14JStSX2TGg/zh-cn_image_0000002538129926.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=AA16BD7120F908666996727209C45B14177D73B6B9BEA24123027A139C9A2ED2) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/gC3OsaDDTuaHk3Y_xXuovA/zh-cn_image_0000002538289860.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6B585FE571E5E288DCB545B799CF1945543B68C8518CCEC4AF3AAF8070FCCA15) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qU6EAAysR0yO2ruP3swxcw/zh-cn_image_0000002569169623.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=D92420DB83DA40B1A99497B38528F7552606BDDC7E66D1DFD079CC5DFA4E844D) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/knsxJXv0RvGyGD_nwLgvIw/zh-cn_image_0000002569129649.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=39E7ADB43E947589BD9C6497E360DE3D812E9FB8C7325C47609A25A4BCD41EC6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/V912thuQTum9vNXWNnSoMA/zh-cn_image_0000002538129928.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=DCC2F93AE8C60136C0D98A8A579A878CB9766B1ED180B32677767D146683E99D) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wPtQWSAZTVWEbuxsslmESA/zh-cn_image_0000002538289862.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=E6BA8EC3BDE2A4BEB4D7192CD34FC4374EDF4CD2A7CF23B7C00EBAA0E2BFA4BD) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/7KZrugncQfO9vq8XE3EsCg/zh-cn_image_0000002569169625.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=D9F5F3A7682C3AC9AC91E9E7E04C3A98481FB5572778440501BE3855E38FA957) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/DEkQvnCPSmmmDg-VgJ0bEA/zh-cn_image_0000002569129651.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=F42B7D2E30C68628512725D6CCDDA929877EC945E77FF0352C0C69DB6EDFAC3E) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/P5Vw43eIRmSor8l5UxsgOQ/zh-cn_image_0000002538129930.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=1F6226F871DA27A2BD542D9B53F5DC63AD346B0B4E24FDCC16E9292B93996722) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Se0xlVHrTt2rJ3-M1Pi8Sw/zh-cn_image_0000002538289864.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=270F6CE62236A4508D3DC40AB4F318204DE5042611E68997C51784BD27195EBD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/rXtEWpWeSYi8JG0zqmwTtA/zh-cn_image_0000002569169627.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6FEF94905F7A3A5A0D6516F4BA9ED65854CBE33E2B249B2225F68110B3399864) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/odjX-RCiQRuASYHrtYuqOg/zh-cn_image_0000002569129653.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=F4192970F1929234661414AFC6BEB8873BDC34A4B4FF0D309597210153D3A679) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Xab1F-pCSZCwcJqy1bcXxg/zh-cn_image_0000002538129932.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=B3AD1C34D1C7B149FB7A7D15445090D09FC9378203F62F8CDBCBC22D9311A5A1) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/1FNPcjpHQqmeXjsR6WJQ2w/zh-cn_image_0000002538289866.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=1D60A98A9DB5092E76CBD78C891D008F38578FA5DF785C84AC33D66679EB007C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/a5z8lWXNRZiUMLhh-XkFyw/zh-cn_image_0000002569169629.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=98149F65D0068E587A1FB7343B3CDD0EB2FFC10A9C8FAB7495F931045C1EC815) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k2hVM9xlS4ieoHHRArSnsQ/zh-cn_image_0000002569129655.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=E1065681965C0FCB11A4D5898C5D44B5693D9D8F1D705F73217B57E20C046167) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/pAGp6Z0TRxCGRI0Q29dqjw/zh-cn_image_0000002538129934.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=0FDC5C94AD67B0EC9C56859271755993E0E67EE77EC6DB29F17D130C379A764F) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ITUKINqtQF6ErPcmI5tnEA/zh-cn_image_0000002538289868.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=13E66ED56B8BF0AFDEF0BB967A6F69B13555680EC2EB7EF4E2A2F6AD85F5C0C6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/H-8zfDGJTjefOEwUb3uZXQ/zh-cn_image_0000002569169631.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=C7930C0A2CD596A2CF23019444424BB2B60028BBE2C0B5EB92D0D0D79F6658F9) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UopHQIonTeyIzZTWkfM0hg/zh-cn_image_0000002569129657.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=710C8BC9099F0B2BBE2DC436C605AAB0FE63BC75AB4D42F8D1AFA23189F125D9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/drWaBlTORdelcn7A719SAg/zh-cn_image_0000002538129936.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=CD2A7D9B672302ADF12A376E4013431700DB1F085259F021A37228B5BFFAC9A5) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/iggABZlxSvyPgXH5mYe3Pw/zh-cn_image_0000002538289870.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=7187CBD88FBC1F6D76234E5D7FCE122065D78099D6D410951AF51167DB296204) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cJh7ILdmQgy3oHSUFSsIRw/zh-cn_image_0000002569169633.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=70F8133695D34C41D47C172FF9833624678EACFE467DF4326164C5EE620806EC) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wxneaY78SmmvUVJ2vWxOEg/zh-cn_image_0000002569129659.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=A7DB48598CB1A438A4DF1774852405FF6EC5212BF183454825989159883AD22C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/kCZHi5JYR4WQmKg7V1zIjA/zh-cn_image_0000002538129938.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=B718B0194DFC4150556A8C9FF9093AE7BCB05245C333AF391D83C6ABBB705535) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9N3l79yIQgalCLg-XdTHww/zh-cn_image_0000002538289872.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=32B9A494DBFD453EADAC3B4EC641D70FE70918D2693A3913B46A38F65EE535E8) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/PlUCN6qCSy6wEi4AQhpDwg/zh-cn_image_0000002569169635.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=A6FB74B55807910F1891CADCA7B22C30188B2BDF416BDB8B84F5F6DC2C112372) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/5I7MHlVgTNOTYZRQl7M2-g/zh-cn_image_0000002569129661.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=845D7B0F5FE9A484C503322D2A11D95A4A9EB0E3A5007C5E851DC6E83FF68AB5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iSCpOMtHSpuAEyWVH104mQ/zh-cn_image_0000002538129940.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=5880CE7970848406DFBEB0F167D2A42E66032DDB3B2FD88B52B0B91F1524DBD8) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Ctz23_WpSPqJzHrncUpsQg/zh-cn_image_0000002538289874.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=426AA77AAA95CA5F7D1270E6D931896440C9D1CCC9701E33102D6E4B682DE9C8) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NozJl6fnSfGca5qMmTUByQ/zh-cn_image_0000002569169637.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=63855A1137F523F59B07BAC5CA0C3112ABE3A1C22E6ABA67C02E97A93C5F2BB9) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/RxHI0F3vRYGRSjIYjGCS2A/zh-cn_image_0000002569129663.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=789D9202AF17AD2224471FD70598ECC280D164259C86BB141AFE00610BA435E3) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/otcgLRW3RgqHN-ARwHruLw/zh-cn_image_0000002538129942.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=EA3DB6BE0FD818C80ECE82E3EAAD350BE7AFA680E5AD8FC6E0473E1DECC3559B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/3lWak_ZQTb62WrcBY3jVpA/zh-cn_image_0000002538289876.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=D84F2B4ABE679122BD424C9CE076DDD9E07F30A71DFE8D0C95874FBDD46BC347) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/K4Kp3cPsQ-m3aDtPTGV8fQ/zh-cn_image_0000002569169639.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=DE0716D24B59357DAAAAA4F0BBB0BDD11008288CB8B634659E21A5D76C0CDE79) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/MhqRW4hPQRqxYBDiQIU58Q/zh-cn_image_0000002569129665.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=FFFF89F695F0434C273C02B6A80F3428EA2D6B9A2F419BD9591B6D357E3A7520) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/fIRb1xZ3QEixJ-Pvmerc9Q/zh-cn_image_0000002538129944.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=44B965792D523B5AD576008FA8B4821551CE14ACCF10262FDCD897EE1006A45F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JAZ-SguVQiitfbF7sL8hEA/zh-cn_image_0000002538289878.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=A71BB8DD19EE84F4348A6543271711CA9CD6C6AA5EBECE639B3D4F735399EDB6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/rPpylfC_SUyW7Z-cPQPDNQ/zh-cn_image_0000002569169641.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=72911DDB1FF55E4E6CB2CA37A2CA4C26D67676EC2A41EA0A5E0F4F77BE281C64) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/C1SlGxBVTKqErf7ytRHrkw/zh-cn_image_0000002569129667.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=44C75B38114667A57EC7A4CBBDB3191B6FC372D4C38507764951D4D60C9398E4) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/l28bICioQNCGGdZxnD6_6g/zh-cn_image_0000002538129946.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=41667649AA0B354FE76C040F09534A41BA448126A715741B662BE48E5F54668C) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/5HZVY3vkQlWdihTUYZSkFw/zh-cn_image_0000002538289880.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=F572BA86E3BA75778C0E4E75BB6C6E7B7A2F187B5FB4248193DE5D2CACA0513C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pS6YKmB4Qe-8ebwVPI_Mjw/zh-cn_image_0000002569169643.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=7B15189071DB0C4940E0FF651E951BB73B935119DF5C9F4DCA3D496F9D5A45E4) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/I8DEpRaTSrGurQYY_iLGlQ/zh-cn_image_0000002569129669.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=A455E9F1382845F6DA75A286D53878FE3CD09E26693D023DE597D7249AF43772) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/_ScuHyYkSmeRTVayw4WGfg/zh-cn_image_0000002538129948.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6B4BE12987021D07E7A3200E23C45CB1AC6E91E123C0DCC9A56C478E6A60E2CA) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/CjRH8FUGQTWhCNQXg8_xHw/zh-cn_image_0000002538289882.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=2A9736A8689D4A8563F628C5CF704E3E87909AB698AC7ADD4626D030DA932AA2) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/wvQj85SDRaadsv9GtszzSw/zh-cn_image_0000002569169645.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=55F5B6F5C938ADBDB9AF09A2C05DCA0D8F1C104AD978EC28167F41C3041FB8BE) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/lo8bjWlwSre2MEbMTk0utA/zh-cn_image_0000002569129671.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=AC91A79C421FB699AF9508DCF5DD8DDE756AD4DECD559D1DEBBE74ED89D052FC) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bkLV89w3RHKjnTMZMd_98A/zh-cn_image_0000002538129950.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=0AE2033274466F9522EA3A378E6B22CCE2C3DB4A26BA8BE182299E60F2D0BB55) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/dICKzYPtTbOrBQou7ZpxIQ/zh-cn_image_0000002538289884.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=F521E4535CC4D0786659481FF62055F0EEC05A6F1A0022889CA13EFA47204D64) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q8jkDJi7TWepJc-5PayLtw/zh-cn_image_0000002569169647.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=F42BC1F02B0FA9379F1B00D91ED0FB34CBCE58A5559EB7CF5E97D8EC10191AEB) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zSPPmRjUSJ6U1Qrgh27fBg/zh-cn_image_0000002569129673.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=078E55063C2DD96CB9A34D8D35B35A5EF4D5036E195E44921AC6C02480599690) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/BU49f7P-SPCrhHCN1gMOnA/zh-cn_image_0000002538129952.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=71BF857EF2A5289FE5D231FA4A8677431CF62A386BB96CA779B55644FCBE3083) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/hT9i0WLFToq2-_VzSyck-A/zh-cn_image_0000002538289886.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=DEBCCC2D05D49F94A54C7CEAC580C3CB9E1E6AB4B14162A8E158DEA71C6D5101) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/kLFyu2rgSdiz14rPDzJd1g/zh-cn_image_0000002569169649.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=87D45AC822AAC373BC7A8EE38F2EF168037F2E2D6CBDD60E0920B28788529262) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/xtTXzOfsQPS2fizxukD1lg/zh-cn_image_0000002569129675.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=8D8A83B94AFFE9A7318A368D36522D708A79C76CC84F98FF8ADD34E631D6F96C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/j8V8pSV2R36EYelSK5HqXg/zh-cn_image_0000002538129954.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=23BB15BC19FE93630453C830A0B157B2CAD6E9F204F058EFE041D21393CB7167) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/gRdVeSUpRNamya71LIVGgA/zh-cn_image_0000002538289888.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=DCD3183F2C1FD766A4CA3F072FB1CC8E4D6D7E007B80566105A2A45C4B3FB4BD) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/SOq7Y8CWQPOH8tmIyqK57Q/zh-cn_image_0000002569169651.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=8B920239EE3C4610029C0DD50F69078FE1793FE0547A383BACDD3484E2B205CC) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/qkASV5rCQ9iWZJF8Ejvcqg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=AC7E5CA93230656F314D0B6A2F458C957F52A70990C36B4A018B65E7787E5BB1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7R_p7m7uSzKbn8qO0sIKQg/zh-cn_image_0000002538129956.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=5B80B883A855D5F886BD9FC4235057C4A8A55D81E02867940FE8E5DC137D1B82) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/MKXf5mg0SDm4dqbk00fXGw/zh-cn_image_0000002538289890.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=7331ED0D3B5DE3AEF7F2CA2F6C513A5314CC635FCBF358FAA827D467561137DC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XRH3qKHTQqCntguZKTvtlw/zh-cn_image_0000002569169653.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=CC672356004A1B958C1F54ED2B8A82787C521B23B59B1FDD6CABBFEBE6FDE167) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WcIHDSESSuyW8JjU0mXxHg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=ADC19F068B74F2FAF01CC9CF33570EDD51BD34E8DF964D8B8AD29E5A5F3EB341) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/6yjZBXjKT8aih5jG-eF2DQ/zh-cn_image_0000002569129679.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=09A173E6C19AC5D969D6B7C7899DA6E95AB57DBBB2B910C7D5FE5554E43291B8) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ow88rYlEQZGWvoVu0E5afA/zh-cn_image_0000002538129958.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=397200C190FA600FBF498D2C2298F6FFC830633807C48C84F21D4CE0180B3F42) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zxYjrsTHQfq50H3CvOvlLQ/zh-cn_image_0000002538289892.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=422F2CA5150E7E44089C0821EAB57CE993E7DFEFBF86E48E319E2BA0CB9D65D7) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/q0F5Bco5Q0OKTzmRM8YnWQ/zh-cn_image_0000002569169655.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=9925486BB81E6431DB99FB7D953CAC8430C4C5724A0C799432785E6F68D35944) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Iqj_E5yaTPOPucDVvTe2_g/zh-cn_image_0000002569129681.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=46647824D5A5E19412CD5E88B6894AF5B64ABD9ECD7835FC86A0CAD59889EFAA) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GWplHjzfT3iqyZNtxKb9rQ/zh-cn_image_0000002538129960.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=34A5B3545A3BC3DD538BC39A4719DF8E6A8D23E0A68015C1829B6E06A0EA2700) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6Nlvc7jPQtOrDVxIpjgyeQ/zh-cn_image_0000002538289894.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=8550DDCE08829D4961878185B51349E0903EC3249F946FF5F40248FBE179FD08) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/rqwFtlz9TM2WGVI809ZP7g/zh-cn_image_0000002569169657.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=D683B45106F2E5265A2A9F1BCDFFFC9525CAC1DB0C6463A44635783E64ACD89A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Mn6lah5gTG-kqrAZqLYZhg/zh-cn_image_0000002569129683.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6F71EB3D91BFA7755EE398F91BB9C53C2DD8448145B85913F25D9012637F0A53) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zF9vbxIhSi618dQnStAQqA/zh-cn_image_0000002538129962.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=40616D73841D52D9EEF322F9A32D9E29A51A70A160DEBBDA6AC9A958FC4B40A5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/E4haMeE8RtWuGVYbetJL1A/zh-cn_image_0000002538289896.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=8193960918BC5C8E99138AA2803D88A7D2297E4FA956A035FE4BFCFE4877A794) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/L_7LW9cCSsSlDDlcDlVTpw/zh-cn_image_0000002569169659.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=C2C77695A9B617E43964939BB486428EBFE11EFAACEE03640213AD97E0A2F3F3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8gJ3xnW2QJWV9baL7NGfhg/zh-cn_image_0000002569129685.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=9A915B1C29ADDEADB2595EBCFACA1450B4851BCD553A20A3D5103E00EB5DB3DD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/yWMapRNBSYyTz21_rngQ5A/zh-cn_image_0000002538129964.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=BE908E16E4A385A70C23ABF6282B8A359F1CEACABD686C53782D9C1FFAE80C48) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/zeqdY0ILTMKktBF5v8rrxg/zh-cn_image_0000002538289898.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6665994640DC6999180A8EF8D281100CBC544DF17F5ED3E60AE5C391036AB34B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Hd1piXuOTRWMqWbkP9sQZg/zh-cn_image_0000002569169661.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=AEBDA514BFE235B16FB1DC3AC65F1128F5145D021820ADEA45854A671731A2FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/MPvt2bEgTUSgXTegFYVoIw/zh-cn_image_0000002569129687.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=32C6F29D908406F4A55568BFBD900C393EAFE05D89A0154CED92268C8CB608ED) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/4Nlp2ZYyTxmLrgR0SR9UtA/zh-cn_image_0000002538129966.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6ACD53E39A8080E36FB1D41A6C0570AFB31F83AC40FAE468036F0071CB7984DE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/nZKJx7zPSKa7erBj-LwHkg/zh-cn_image_0000002538289900.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=C3834B7460BBA18BF01CFBD4BDD34D2C558724CA885F18E772167437528829ED) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1fUwORl5TkCNixdG44ShkA/zh-cn_image_0000002569169663.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=C992A11541CFF0B9113BF81DE98E4C1E2426C12BAED6FE7FAE795CC41DD920F1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/2gxdcq9MTBSc_Ajo4Na0dA/zh-cn_image_0000002569129689.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=657535E33C36D512B7079FF2DF1B3A5C782BB4037A18C6BCE737A531B030E407) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/OXc7fTELR4urBx32L54VSQ/zh-cn_image_0000002538129968.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=657AF180B8ECC3309109369CD55C025E27C4AE7A7005AD72E7116333E94FD8E3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UWCM5_F4RzaDfLr42sUA0w/zh-cn_image_0000002538289902.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=677D7814A1D1D72506719AEF306B235B9896FF83FD8BE55884FA18C883779BAD) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AlGvj17HQJiMyeO6O6m74Q/zh-cn_image_0000002569169665.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=AB2D5FFC3081A68B8D284F16E299EAB522E6A46BE8AA47D87817C2D557AEFB6E) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/FBxBSBghTGGJiJDIGqYR6Q/zh-cn_image_0000002569129691.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=4B18DEA3F15AB4A75576E3C8ABA5CCE8A4E915D062F0B3386892AE203A8CF035) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/twaYB_bFQCiGaaVcDHQ-og/zh-cn_image_0000002538129970.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=22A44070ECC95BD989B7E074E220F38C9B17E5CB2AE0460907DFBBA9EC3F7381) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lzZaKrs3Rk-qQrAZr9AB7g/zh-cn_image_0000002538289904.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=0F29E48EE3BE5C3404F1E876EB15070A751E98FAED7B2C6A0919D16EA4FDF4FD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KelqlMJSRVm8lVEAk3IKpg/zh-cn_image_0000002569169667.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=0DC35B44059A1052DAA8E44E397733495D0E93AF44939C32EC5B4D0368F60D19) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/FiMfgQkJT1qNwoWxTlsL3A/zh-cn_image_0000002569129693.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=98F6F7F8C390A283060D61DBDC6ADC50F5054C64E0BD215745D05F610ABEEBC3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Wu-PjMW-Rw-jGAC9YQoQlA/zh-cn_image_0000002538129972.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=7A26546EB6C7363EFE9D3D5750636C5B48D57A01821F1792C08EFCBAA227B2F3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/YUxBEHhQRzWPkg1AaTOowQ/zh-cn_image_0000002538289906.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=4AA6E1B02481288DD7D3B7C0A0250BE4327D0A2513371F280C36D73B589B0CF1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/xms_HpfSSzylyJYQcjA4vQ/zh-cn_image_0000002569169669.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=0FDF29219F0CE6EB05149DE2EE0515BA42E1C9C941584BCD56E187C080928F3A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ChDDm1t_Te6mY0YFfcuung/zh-cn_image_0000002569129695.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=6DD35E344D9654CE11D19683779AC8B2F3074B105EDB0DE93C4572EC15213134) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/R7vmi6zjRuOt-cdxQFv2yw/zh-cn_image_0000002538129974.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=968E4316B2264DA6C7C0415F6DA5240031363B2B56BECE5E1C045A856DEE0B98) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Ub_fSxThQFK-ZxbLJxSMFw/zh-cn_image_0000002538289908.png?HW-CC-KV=V1&HW-CC-Date=20260413T030031Z&HW-CC-Expire=86400&HW-CC-Sign=BE57AE74B426F8173F4790FEE31AED277679DFDEC09BEA64ADB45AEA212E9C70) |
