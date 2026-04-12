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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WA7BldDTRwuWwnQ9o5fsyQ/zh-cn_image_0000002569169621.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9179A313C4741EA93C61B5AFA41ECB867BAFB192408A4D8789A097BF4527A8ED) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/wFu60U6ERS2FRYi_y7QsXA/zh-cn_image_0000002569129647.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=5B30662B371874179003F1A24FCDA42F233E3A093B06CD38494000B46C8486BC) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/P4GVjIWnRXO14JStSX2TGg/zh-cn_image_0000002538129926.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=37FA5DE8DB8904804075BDFAA208F9FF1B3EA27A5F93B36494626452F98D00B4) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/gC3OsaDDTuaHk3Y_xXuovA/zh-cn_image_0000002538289860.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=C716813FE658D25A67B065C30BF5F9A17B0F2DDD841E6D1137695CB66C9ADF6B) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qU6EAAysR0yO2ruP3swxcw/zh-cn_image_0000002569169623.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=138DC3BE77198AF25BA97596573DAC1AA4B551587364CCD5D204C4EDD14338E9) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/knsxJXv0RvGyGD_nwLgvIw/zh-cn_image_0000002569129649.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=256A29A3597B4BFAD9ACF3ABB2941FAA1F4D0F79ACC7F351F0E5DA46690AF408) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/V912thuQTum9vNXWNnSoMA/zh-cn_image_0000002538129928.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2BE5A8D62A93FD4F246DFCDF700A9D705E6C16213FC1FCD77E3F35A059652B60) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wPtQWSAZTVWEbuxsslmESA/zh-cn_image_0000002538289862.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2E2E53E12A75A76CC4AF03BC29B64853092418453533276F5F2F0305AD89BFC2) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/7KZrugncQfO9vq8XE3EsCg/zh-cn_image_0000002569169625.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=382DD3B6F471A84AE5DDD81BBBBBF84090EDA993312DED39F246A4FE2B5A24E9) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/DEkQvnCPSmmmDg-VgJ0bEA/zh-cn_image_0000002569129651.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=339FE33A8D8F92A9DDE92E28D46934372E1D2B9FAA0AE3E740D398AD793D45B5) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/P5Vw43eIRmSor8l5UxsgOQ/zh-cn_image_0000002538129930.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=05AA06D91D98B74386E7F59AF7F21345B92E20A95D34B3C7172AADEA3D85FB2E) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Se0xlVHrTt2rJ3-M1Pi8Sw/zh-cn_image_0000002538289864.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=FE7C404AE757143BE037EF9566F31A54F60A088DCC000015F0940E08F3D7000D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/rXtEWpWeSYi8JG0zqmwTtA/zh-cn_image_0000002569169627.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=DDE172A5484AB3CD2355AB244502CA27EAFC8085F16C0F882DCD70848644852B) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/odjX-RCiQRuASYHrtYuqOg/zh-cn_image_0000002569129653.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=05BAC3B06AE4EC5BC85976735F2E129B8EDECDBBAD77EB57F6E7B2F7A56C6189) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Xab1F-pCSZCwcJqy1bcXxg/zh-cn_image_0000002538129932.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=047ACD5BF0814BEFC55B1D720CE375DD6E935A6C43170C2C2C39E1CB8C8528E9) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/1FNPcjpHQqmeXjsR6WJQ2w/zh-cn_image_0000002538289866.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=5844AB03E1CBEBADFF05EC2E454796AFC20A0809BD5085C308B3638CDC36B338) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/a5z8lWXNRZiUMLhh-XkFyw/zh-cn_image_0000002569169629.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=6041EDFDB3626D3561697E3E997F5C1E0AA68AE7D432FA4AAF83DBAFFB20542A) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k2hVM9xlS4ieoHHRArSnsQ/zh-cn_image_0000002569129655.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=12B4765DE60EF43DB2C2FA4EC94E4FD35BE06A166C669FBC970F3C93EB3F28D0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/pAGp6Z0TRxCGRI0Q29dqjw/zh-cn_image_0000002538129934.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=11B20BF8CD35DC2822045423108CF356F03FFA664B073769D31ABB2B3E745313) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ITUKINqtQF6ErPcmI5tnEA/zh-cn_image_0000002538289868.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=F388C5CC90DE51167220C9EF40033DB21F672BF2DFCEF9F855E04EC7360A5C26) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/H-8zfDGJTjefOEwUb3uZXQ/zh-cn_image_0000002569169631.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=87070471783E02B829C963E2CAF46E4DFA2F4C06CE968B0F2AC4C2666B55A6A5) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UopHQIonTeyIzZTWkfM0hg/zh-cn_image_0000002569129657.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9F5BB84BCCDE9715FE578362A3D281F32DBB9FA0ABEBB3DD27F39602C34B3CC7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/drWaBlTORdelcn7A719SAg/zh-cn_image_0000002538129936.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=1FD8CB24E948671D08313A6DAD5F5D0A470F880CA9541225DEED8723D8150D7A) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/iggABZlxSvyPgXH5mYe3Pw/zh-cn_image_0000002538289870.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=23523533755AC856ECA77122A9E6CED426AAD5097BEBCC896743107A2A418CCB) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/cJh7ILdmQgy3oHSUFSsIRw/zh-cn_image_0000002569169633.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=0BBA84B5CC8F4028AE52A3FE7BEC592D7D9F0AE290B2698C26FEFD4A428FA2CE) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wxneaY78SmmvUVJ2vWxOEg/zh-cn_image_0000002569129659.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=1306DDF2EA9AD8C3207275540072EE90095B7FCAB3C6C398D6A25A81EC4641C4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/kCZHi5JYR4WQmKg7V1zIjA/zh-cn_image_0000002538129938.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=0522885A8E7F8454346C79283F754CCDCA14B383E1F8006B39489D97E59E515E) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/9N3l79yIQgalCLg-XdTHww/zh-cn_image_0000002538289872.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=C31AD1382AC3F5CBB8EDF51EF32C6D1E2DD133D548092F92AB4BDEB7C63FF36B) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/PlUCN6qCSy6wEi4AQhpDwg/zh-cn_image_0000002569169635.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2523F9CA317C0AACF769464290DF18D8F141016C13F77E77E15411B3D183A905) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/5I7MHlVgTNOTYZRQl7M2-g/zh-cn_image_0000002569129661.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2E86B9D5B435FFAD3E74342EE35418D5AEA87DD4EE6A82A3051A58DF0AEF7E0D) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iSCpOMtHSpuAEyWVH104mQ/zh-cn_image_0000002538129940.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=420C21336200A222AD96E9B664C052D123C5E8193FA70D6DF767C4E933AF5662) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Ctz23_WpSPqJzHrncUpsQg/zh-cn_image_0000002538289874.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=B8F867A3E20106712C380F347680D2942A6F3CDB3350A513CBA31D756E2514F3) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NozJl6fnSfGca5qMmTUByQ/zh-cn_image_0000002569169637.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2BF3397874949B07BB583CC9FD1F59A2F92038ECCF6D7C212EC7F5212B84D28E) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/RxHI0F3vRYGRSjIYjGCS2A/zh-cn_image_0000002569129663.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=7C4797B6F81E3944D2E6FAFFBDC8E3363D2234465F13B3EA8AF0929799C8322B) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/otcgLRW3RgqHN-ARwHruLw/zh-cn_image_0000002538129942.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=87A9C2D3A166BB3D61BAF6DE8C1348FA6D5211531451BA1AD630BF6115D4D6EA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/3lWak_ZQTb62WrcBY3jVpA/zh-cn_image_0000002538289876.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=F17D40F238D0563E6ECCCB8C56A232FD36F37B5AF59FF0C8ECFE8F9F69C6621D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/K4Kp3cPsQ-m3aDtPTGV8fQ/zh-cn_image_0000002569169639.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9A6E8F85B78B0370CC041B042255779213B1DB8022B4AC3C86B9170DB67A5109) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/MhqRW4hPQRqxYBDiQIU58Q/zh-cn_image_0000002569129665.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9AA3F17119FC88288DB01A80851E0659005382C970C95368AA0C592AAD4BBFDB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/fIRb1xZ3QEixJ-Pvmerc9Q/zh-cn_image_0000002538129944.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=45E82DFCFC47E31C8C436CF930353912E2F1B4CBC96A65DB74F4BC074328099B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JAZ-SguVQiitfbF7sL8hEA/zh-cn_image_0000002538289878.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=BD6800B52F596F6A350577BD9ACE2175AAAC34855D47353BCB32BC6A2D259F72) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/rPpylfC_SUyW7Z-cPQPDNQ/zh-cn_image_0000002569169641.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=DFB7F492FEB4F73E5D061DDF537C76BD3712E2D81A7966ABB59E74BCEA3B3D0E) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/C1SlGxBVTKqErf7ytRHrkw/zh-cn_image_0000002569129667.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=76831D701A24704359601A2CDF49FE4B2A91C7DCF29F4A6EB1DF3AEA68D64C32) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/l28bICioQNCGGdZxnD6_6g/zh-cn_image_0000002538129946.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=1FB94FB605109295FE94BAB6627FAEEEB2A52E649716CACF6C0ED0064458013C) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/5HZVY3vkQlWdihTUYZSkFw/zh-cn_image_0000002538289880.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=120D6815E9B9B8476534A3897DBD8D3CC087B5F7E21003DC1CBD7E59BFF06598) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/pS6YKmB4Qe-8ebwVPI_Mjw/zh-cn_image_0000002569169643.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=28D9092CB8765B6382D15C0D0BAF465A993C7E9DB0207E4CA0DB154CB46EC131) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/I8DEpRaTSrGurQYY_iLGlQ/zh-cn_image_0000002569129669.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=8E834E68A670AC835BD3D2109DE43A27C211DAEA4ED710402B49D6BC51B58AE3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/_ScuHyYkSmeRTVayw4WGfg/zh-cn_image_0000002538129948.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=42E95259D28A71AC0AA7ADB49A3ABD5732F4EAD356ABEADDA0F08188A889BBBA) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/CjRH8FUGQTWhCNQXg8_xHw/zh-cn_image_0000002538289882.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=BDB1F801B832BCF0ED8E8E27C9BAE367A326367ABB4F788317ECFAAD6DF15C60) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/wvQj85SDRaadsv9GtszzSw/zh-cn_image_0000002569169645.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=DC63E707EFCCEF7410035ADC2F9B1A2F60A69589DACA5BC04F6CC0F1AE78F27C) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/lo8bjWlwSre2MEbMTk0utA/zh-cn_image_0000002569129671.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=06F5C09B40B999E2C59FAFEA90991E7A270EE5C06FDF8D8F4AF9F4F6F66F4222) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bkLV89w3RHKjnTMZMd_98A/zh-cn_image_0000002538129950.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=6404D978D4E90A6AA0CD07598DB485CA30D0D54E41BDCCF3A767D23CE74D8841) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/dICKzYPtTbOrBQou7ZpxIQ/zh-cn_image_0000002538289884.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=A44C532A005E273BC8DCB390A4B584F243596A11FFF80A6E47E150899E9BA383) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q8jkDJi7TWepJc-5PayLtw/zh-cn_image_0000002569169647.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=27BFBA4CB410FF637DAF2DC04862C7E872DCB2DA5B21BB64750E9211CB51444D) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zSPPmRjUSJ6U1Qrgh27fBg/zh-cn_image_0000002569129673.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=7158BA4CE6D1640F280CF763AC528F63D17B9AD25BAE62D812C1D021654C63BB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/BU49f7P-SPCrhHCN1gMOnA/zh-cn_image_0000002538129952.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=F0E34B08A500E1A15997237845BD2C05471D41339AE96E03E468F2463C35239B) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/hT9i0WLFToq2-_VzSyck-A/zh-cn_image_0000002538289886.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=FA38433E5AEB3CBC01FFA2ABBA62B8332E5AA782C65CEAACE147CF030DA354B7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/kLFyu2rgSdiz14rPDzJd1g/zh-cn_image_0000002569169649.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=178B9D29577C91234A8E8F99E30BD2F446F1481E9E105945A92B8A137B7494B5) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/xtTXzOfsQPS2fizxukD1lg/zh-cn_image_0000002569129675.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=8D0B9718C73F8EC84FE8ED8AF17C2B292846E5AF40DD35520E3913F212B5EB38) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/j8V8pSV2R36EYelSK5HqXg/zh-cn_image_0000002538129954.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=188FCE7CDD97727D0FE3ED011F48299F40D1C740352CDC4FCC35B7B945D895CB) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/gRdVeSUpRNamya71LIVGgA/zh-cn_image_0000002538289888.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=F2C9E068F5E122A29FDA5AE1A7FF2FA2271C1CDF732C4A663314403D22AAF88D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/SOq7Y8CWQPOH8tmIyqK57Q/zh-cn_image_0000002569169651.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2E6F08809BE7B5E6ECF66CA85D71DD4219BBF25544559B90B4A2E5E8E9A089F3) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/qkASV5rCQ9iWZJF8Ejvcqg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=3112A27EC7BC01F83EBE9F997C3504CDCC2C849E5D78D738732D42BCB603DD06) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7R_p7m7uSzKbn8qO0sIKQg/zh-cn_image_0000002538129956.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2071CBBBBB389905C7ACB7FD38363C80A4313213B5C4CC2D13F749BD87DA8809) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/MKXf5mg0SDm4dqbk00fXGw/zh-cn_image_0000002538289890.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9451678AE96139A2A5EE2326A40233A61CB2E209E2AD326B938EB7D1FA9B9B89) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XRH3qKHTQqCntguZKTvtlw/zh-cn_image_0000002569169653.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=CC96F1C0BBD63730C6F9CB7138F92E30CB69A0AED84E72B98782C319F08907BD) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WcIHDSESSuyW8JjU0mXxHg/zh-cn_image_0000002569129677.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=4B46F6CD351F4E6074FD15B3365BF3AED9F9F201D29719CD356DDD5C6C3BD2E7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/6yjZBXjKT8aih5jG-eF2DQ/zh-cn_image_0000002569129679.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=AAC833466D2449DB47453205DCB085E8A9FD47A09B3C8F7A710756317D8DA8F7) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ow88rYlEQZGWvoVu0E5afA/zh-cn_image_0000002538129958.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=8BE1B85CE7C50C7C7DCB510E977E61D504F1B41DF551AFB3F3E9F97C19F76B10) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zxYjrsTHQfq50H3CvOvlLQ/zh-cn_image_0000002538289892.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=73919D56102B905B61EBBCF9D5820D0B890991B99F74A0E9BEBE5CFE7CAE7B97) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/q0F5Bco5Q0OKTzmRM8YnWQ/zh-cn_image_0000002569169655.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=6B693F41C706366DF9D472120B2655C00F3D4FD95069A54249E2115DBE959079) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Iqj_E5yaTPOPucDVvTe2_g/zh-cn_image_0000002569129681.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=58AA3D940E25F2037BC547B475137F64480A87A40C7BAFFD35A6812D267B36EF) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GWplHjzfT3iqyZNtxKb9rQ/zh-cn_image_0000002538129960.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=3C20CFC1822BD2CAF39158F52E5E3E4BA9772E87C8FEA96C866977F01E70A607) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/6Nlvc7jPQtOrDVxIpjgyeQ/zh-cn_image_0000002538289894.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=014F5FDDB5B674C7BD355258CE0035F5C7FE3C6D2D65532108C6286890CF52FA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/rqwFtlz9TM2WGVI809ZP7g/zh-cn_image_0000002569169657.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=946DFFD7C76244FA1074E7BC67220C119B28F1F9FC9F40A72D1AE8C9E05D722B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Mn6lah5gTG-kqrAZqLYZhg/zh-cn_image_0000002569129683.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=8A103B01CAC6B7CE4CC559C44FF437C65E236D2ECF272E5324519277F317D2D5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zF9vbxIhSi618dQnStAQqA/zh-cn_image_0000002538129962.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=DA0F3E7559C19789AAABE276207A7A50F1ED168116D004032046FB36BEADA398) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/E4haMeE8RtWuGVYbetJL1A/zh-cn_image_0000002538289896.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=46133B49E5FD69736ED9313CFE1FBEB783902B7B144041ABF28FC29B9CECCE8E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/L_7LW9cCSsSlDDlcDlVTpw/zh-cn_image_0000002569169659.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=D2F342DDDD01BCE3143B75446C6F9B9AE3EE6E4D897A4E9837C030CB6AC14DE9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8gJ3xnW2QJWV9baL7NGfhg/zh-cn_image_0000002569129685.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=03D1AA954FC2AD945C3DE26271F8848AD89837CB1F397D168D47E63EF1F5EC5C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/yWMapRNBSYyTz21_rngQ5A/zh-cn_image_0000002538129964.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=FED608190E80F2B64FA047F5FFEA039978A031659D2A01BEE04D8C760B01D962) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/zeqdY0ILTMKktBF5v8rrxg/zh-cn_image_0000002538289898.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=C576BF0CE90DB90964801492E4B9FAED83B7D45CF9761754AAB775EB62D7FB0C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Hd1piXuOTRWMqWbkP9sQZg/zh-cn_image_0000002569169661.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=AABB0B703B03348C88808CA56A5E7B6E40AF2315E3224EFF1532A2154CCF3785) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/MPvt2bEgTUSgXTegFYVoIw/zh-cn_image_0000002569129687.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=13F14465E1E097408650D0346F4A791245B50D6E325003B8EAFD32F780967899) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/4Nlp2ZYyTxmLrgR0SR9UtA/zh-cn_image_0000002538129966.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=0B1778A21B139BBCF85F17CED2EEABCF548EBBFB47A731795AE83F16FF58A54E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/nZKJx7zPSKa7erBj-LwHkg/zh-cn_image_0000002538289900.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=F61C14E2E26B24E3DAB4D317A3B877A1DFD90A9EDD801DD17590CC5AF878B6E8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1fUwORl5TkCNixdG44ShkA/zh-cn_image_0000002569169663.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=D6B86A33CDFA7CB5DD63CF3CB7BA1655DCAB4042FE90DF5EC2996A13A7A92545) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/2gxdcq9MTBSc_Ajo4Na0dA/zh-cn_image_0000002569129689.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=90EC01F85E0204C4B6A10BD5A8347CAAD64562449D066DBCECF2A5FA83EBD8D7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/OXc7fTELR4urBx32L54VSQ/zh-cn_image_0000002538129968.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=BDAE1547255E62563469BB4A04EDC79EBFF67FFC2D3459399BB3ACA52892562B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UWCM5_F4RzaDfLr42sUA0w/zh-cn_image_0000002538289902.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=AC0900D6981938CD48EA74F7AA533C89D42FCD5DB22F79F45619179EFD367578) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AlGvj17HQJiMyeO6O6m74Q/zh-cn_image_0000002569169665.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=9DD762B71677F8F8B5485FCED5E05882E6D745D2F348FC0A38B57E514BE213AE) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/FBxBSBghTGGJiJDIGqYR6Q/zh-cn_image_0000002569129691.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2875A942DE9E5B7CDA21D88F8D8A1480ADF27B7B58BFDBF39FFCCEEAE1939E71) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/twaYB_bFQCiGaaVcDHQ-og/zh-cn_image_0000002538129970.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=6BE11AC04A1F0223A29745D5B9A823FE2F388177923C16F86B6072708812FA62) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lzZaKrs3Rk-qQrAZr9AB7g/zh-cn_image_0000002538289904.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=85617731CB3C1686E7AF59DD1D127094D7DB6CA688E1B2028D16B3EBDA880D1D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KelqlMJSRVm8lVEAk3IKpg/zh-cn_image_0000002569169667.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=2285F51EC372C3CEE7501CDB1E8F4F44D90E701A7C092D37B60F7C4BAF8B0B59) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/FiMfgQkJT1qNwoWxTlsL3A/zh-cn_image_0000002569129693.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=4FEE2C987053E7C645E25F3F27CA7256A8CBABDBCC976CB38D8676CBE959A1AD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Wu-PjMW-Rw-jGAC9YQoQlA/zh-cn_image_0000002538129972.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=BD276AEC61228360FB7D424164E5E615BBDEA33499848C2F9CFAFA10913178E6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/YUxBEHhQRzWPkg1AaTOowQ/zh-cn_image_0000002538289906.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=28439149C3CA0C58D3FE6F686458358D5F350E7058C9A795C925F82ADA773481) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/xms_HpfSSzylyJYQcjA4vQ/zh-cn_image_0000002569169669.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=8120882E694C0535F2D833F0953A9974718C2CA7B77F73A12E5B4619453946A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ChDDm1t_Te6mY0YFfcuung/zh-cn_image_0000002569129695.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=3A434F08213B24B26C2F572D6F7DEC0C32CD71407D6317D0C9A53122A6092295) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/R7vmi6zjRuOt-cdxQFv2yw/zh-cn_image_0000002538129974.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=DD49E1C1CD25EBBB2C3D31388256A9357457C5140A0917F0334DF0F251CE5254) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Ub_fSxThQFK-ZxbLJxSMFw/zh-cn_image_0000002538289908.png?HW-CC-KV=V1&HW-CC-Date=20260412T025615Z&HW-CC-Expire=86400&HW-CC-Sign=D33B1C88D2B8A152B77DFC435742738407E4E3CC7422E6A042512438F5F13739) |
