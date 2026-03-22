# SVG标签解析能力增强-图片与视频-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/MsGubtXLQAqnT-XqCdH1RA/zh-cn_image_0000002531226016.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=06EDA25C9BBCA4351DF33DB8041E0D50FE11AC0F4CECECD6D1F0292DEE8B75A0) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/hoY8r7ysQSSTZZULQD2SEQ/zh-cn_image_0000002562025999.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=CCB463656D37C33A03B9370F55DE54A070D683DF6411979B62A1B63F30B7E3EF) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mct86Xz-TCWGliRmSFUIIQ/zh-cn_image_0000002562145985.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=04ABE770B7276AC7BE0B43EBFAE68200E72C10D18D3565153176CE686F92CF4E) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zCulBZSMQYSG76AwACd6JA/zh-cn_image_0000002531106084.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=01E318B6C9E8320EDCC36156F27BA43D101EA45CDA9597C941DC7001A9E21865) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/S5Bym8PZT6ulIQqqraZkeA/zh-cn_image_0000002531226018.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=5DC4EF5906CE902FBC89E095E22003086F2867F7FB9CDE067DB64693947C57F1) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/IbEU8DcJQqyJc_jk4419SQ/zh-cn_image_0000002562026001.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=E7BDA6368E9EA8B7A667F2FEB0FB6C324230AA81AE80F77C86CBF88A0C8152E7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eK8rWI09Teu6wCQr5nJPMw/zh-cn_image_0000002562145987.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=E032EC6161F83FEC1B569AAADEFAD3B008CF1B1A9C7D34B23C454A2BA75601DE) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hDb7ycCaQae2i8EYs60ulw/zh-cn_image_0000002531106086.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D2854AC48F1FF5BD8400C0968CC549C925F9328D4C0F09A52482FC329C12DC4A) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/2y43ulkURVC0VEYhefESkA/zh-cn_image_0000002531226020.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D4C183A1ACC2A36BC7D91DFBE8A0AF159AAC8815B201D0FFB4EB125DD619C284) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/193mMcO-S0KUZk0DgvIpDw/zh-cn_image_0000002562026003.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=9FF05EDF2F90485AFDCB87910319AEDE07272C095BED6F202B2747EF99487256) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/JpwqOTFISlm2gQmpBRS3vw/zh-cn_image_0000002562145989.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D2C99817A4BEBCC5CAFC09523EB2A4CF86BB654D8B4EE2CAFDE8333B76F36422) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Gc1O_NdLS2GUdifGCdLB7A/zh-cn_image_0000002531106088.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B9F492E0628A2878111CE0F086AC0C2A66F0B32B5F8A21DD05B47B1620AB9CF8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_At9qU-eRE-KRKfoWzpuQg/zh-cn_image_0000002531226022.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D7B5E3B7824E5AF25E0B284BEDC1E4B1A49322DA5AA87064C5806CB5DD82E6F1) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XMSf5UlzSby6QPdQC5aipg/zh-cn_image_0000002562026005.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D8BC029AA0CD5B4670410C03C02036D2514828C49AB500C0AD8DB39CF7F9F3F2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/-Y_PP3ulTaqz7w3GQ6cMQA/zh-cn_image_0000002562145991.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=7AD8821ABE1E719C23F017C1D19EC0F5FAC32E98A99CAD4AAF486B0EBEDFED88) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/g95t-8LaQoeEiFO4MZvcWA/zh-cn_image_0000002531106090.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=DA1E8D612AD475D0C306F948F19601395D2C2B3D6798B5792B152624A62176F9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/a1PNeI0sQdGbHPkFV_unMQ/zh-cn_image_0000002531226024.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=3E44F02DB9740183FA97FBA9DC67641D5BB3873DFFD6FF2FD35AEB286A5EF954) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/rjffx4ftQIC97m0ASoOxeA/zh-cn_image_0000002562026007.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=371B5A246350281904EE159621199CCA0B49594CDDD6D96DB402A4AF444D0FEE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/IPo1iBkvS6uLCEGV_LNB_Q/zh-cn_image_0000002562145993.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=7EB8893576826C8A37D3B6AED26FD2639D6FADCBCD49754128199FF867A6FFB7) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ooxHBqleQzWNGjKkF2FVDw/zh-cn_image_0000002531106092.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B66CA09BE6B6889B90E10B19F3A14D7BA59F033CB9B068FDC78A63BC2CDAA5F5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KGhqJo_3QAS_Oh-wenTI5g/zh-cn_image_0000002531226026.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=98A3572799FCE6EB8CDBD927B13D926A2489BFBE6B032A064ECDB0096FB1121F) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_XSzxZabSN-YmDmdi1hCrg/zh-cn_image_0000002562026009.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F5009F10FED2E1C3022A70BADBBB186577D08F58A39259D90595706B8D978B71) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WB-9znnzSlm64Gu2eFjkrA/zh-cn_image_0000002562145995.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=EB551DC2B06F1691BE2F2DFFD648414A414EE18E0F2B8C1F04B5DF3F833A7666) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/WBMjY2ihQg-MEOrMMy6g6w/zh-cn_image_0000002531106094.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=AAEFCD0A1D63DA354B9499A9638AB34E4FA0ABF87B458773EE2D92525EBC05DA) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/nsZIAqlGT96dM19SAzkqNw/zh-cn_image_0000002531226028.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F97F59A510D02EC0D9EFFFB8E56709E06A980CFDC96331DC19671532F2C181DB) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nOqsIxreR9KnpLVLgnhKGQ/zh-cn_image_0000002562026011.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=9A6479F8124A069A97BFBA9051FF2C22EDD97B3D5B7410004178BBB5FE809E5A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5FYNVTbHQrq6frtXlBf2Bg/zh-cn_image_0000002562145997.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=6A9697D24CB11779E84F7F4BF5039D05D51161A54865716E6B563CA66FC66F23) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/J28u8BgESKKUJy5IEn2l6w/zh-cn_image_0000002531106096.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=86FF903B5E52C9593521D166B30BD41670CB78699F2369CDD9521FB47D719C85) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/EcVtPbH9R0C3g1ThaKC8lg/zh-cn_image_0000002531226030.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=CDFC5393CF03926C7C5320C92A1010EA021ED8CD99721C364F26E2C83BF8886C) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/nEo1ZcJqQFaDTjBbLKjmOw/zh-cn_image_0000002562026013.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=23F2DD2B2256D262010E474F356BD69B0E81B5DED6A067E9EB67AB49E23457AA) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KpNxHNSPRgaXImGaK65GdA/zh-cn_image_0000002562145999.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=26B71F42DB7C6115ED0873E808049D6A9D4F1C23FFCF3CB6D848C860E7E38EB2) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/GoTzTwV9RGWIhvkunMoHlg/zh-cn_image_0000002531106098.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=237401026EBBCCB15D3EEF3F6F049D6FA2FC28752435649A65E86901A9913D83) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/sHyhQyXzQAifR_TyrI4Vfw/zh-cn_image_0000002531226032.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=0E9CD358ED17419D67671AE4A23C3D873E627A17AB440DDF5FAB2F8F875E95EF) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MNhTmHqRT9KXatitgn76Zg/zh-cn_image_0000002562026015.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=3348EBBC443BE2D4E5D2C471C042281F98040BA7A2E463D8858ED9547167E139) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/DkcCpR9oRmu5BiVFeXFS0w/zh-cn_image_0000002562146001.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=DF91850C0BCCF3ABBAFE33B0214E6061CB35CF3D378143CE8E733B64EC2DDEFF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/krxJcgkkRYiAphnKEQ_CZw/zh-cn_image_0000002531106100.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=E46111C70F914AE74220AA32584AA97C34C99CA8AEF1CCFE169AF79C0A473457) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/FL8gcSEnSf-s_OviHqLR_g/zh-cn_image_0000002531226034.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=EBA22396AD66003251883A96E4EBCE67726CDA652582C82536FF0F2D497AFD82) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8XUI3hD0RpiYqEYyjF_Sxw/zh-cn_image_0000002562026017.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B1C0B9A8DBFA062CF20E6E4F506A604EFB2CE23D08F154C2972E2F05551C825A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/XgdWgq_mTbKbE_xSsSC4dg/zh-cn_image_0000002562146003.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=ED76370CE52896C8169E9E0B0EC80E77AC68422854D93BB53EC0C5F90C08B493) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/6sEhEPrbTKiGFAzHel5lcg/zh-cn_image_0000002531106102.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D463C64C6545DDCE8787C52B0863F088C56EDFDDB6B3985F59ECC36688D9C9A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/frkhgIhMQaqv15-RjDFFZw/zh-cn_image_0000002531226036.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=17BA2C36C715A8FB5CA3E77AA96DA0957CEA8572B1780BDC974F1FDB861906C7) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HikxhtJsQsGFat-LngwjKA/zh-cn_image_0000002562026019.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B5E2DA3372FAA0654D2EC0B20BDA350E75A7FEE01C9F0E5945EDC67502CE1666) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zUvT6SjQRpiyjZ3IQqEiuA/zh-cn_image_0000002562146005.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=2F65EEAB8F84B1CFE51CB07AD5225A066D7F2B181B4F0DCB130D623BC3751288) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CeUm7lnuQpSO-smMXisXBQ/zh-cn_image_0000002531106104.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=C6FABE44837351A426860DAB410BD4834B1B544D08334DFCD6CD7FDD69BF788C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QeaoqrtwTI6igmpj9uyT0A/zh-cn_image_0000002531226038.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=94A15484394A7DA8B3FEC73239C6FDC43FAB2AB3D4762B1EF1EF4637EBC305BB) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kPpcvB9sRwabtVzlYpm5Mg/zh-cn_image_0000002562026021.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=9C306874D87179C6E6B31D123C756F23349BC4F4615AD1431DE80B48FD3D5AEA) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ivZ7iPxYQPWAxIWifJ1KFg/zh-cn_image_0000002562146007.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=0A70E8212122018512C471A635AC99B04E823CD9E284C7BC4DDFDABEFCBD3AE8) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wZQkntFcTiuiHjiFYCTTZw/zh-cn_image_0000002531106106.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=8A1665CF31D616DBAB8CB1AE3CAD358C5552B5E951B34AE1CBDE109DA64B50DC) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/h6t6EC9pR5mQ5qTPslcfqg/zh-cn_image_0000002531226040.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=DA145039FECE3A8F758EF2A80525D278B96C4B960462FC814042471FFDFE0A87) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MahNlqwbQHShWSkIueJLyg/zh-cn_image_0000002562026023.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=C88A292C199525DC73AB583254CE8E36A85A10AE2A32C7C6F7492DFB66BD1B1C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VAJaGi20TV2padLk7E_GKw/zh-cn_image_0000002562146009.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=2F613A585D4024F445EEB4E4536725B67501EE19A6AF2638DB8832895947866B) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/P15cbpUUQMaVkJNUumgzcA/zh-cn_image_0000002531106108.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=43E9E673F7366038673A1950F058127A32657AD64624E8587E47CA38A24A361B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/stYmfh7MTCSotVPU3b0SKw/zh-cn_image_0000002531226042.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=8D2F3678254762762A31523B4884C9A4EB4AA6D4819699CC32A061349894A958) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dgMA5i3JQauH20lYjohUJQ/zh-cn_image_0000002562026025.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=853F2A64F04FBF1EBC4D4EDAF3B649508AD1F0E2E231373BF772E06C873002CB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_pjHAW9-TgS-ZydTOuXv8A/zh-cn_image_0000002562146011.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=42600F5F4106C2860FDA4BA5099656E4C75A9C9762A0F3BAB487994D6FF79D67) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bfhAKlkWQM6laLnWgGTeuA/zh-cn_image_0000002531106110.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=772983B3B6C7954D61378DD00F0D9A42DCE333171521B61ED899490E5CB17E30) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yag93OgrSHa9z7whde7fMw/zh-cn_image_0000002531226044.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=7EC8B0A550163BD71A6F1D2B8CD3E8860353E456015227CE754238AEC1A02E4E) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/KohZoDqrS7OdvWpHQ07tpA/zh-cn_image_0000002562026027.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=0C0965C1ED14FF286D5050036EAD06B786BE9203261732110B3181B1B45A9ED2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MDiYMd-7TFSeIUskarK0Mw/zh-cn_image_0000002562146013.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=7E316E4A93BC44D60D9535D59E3162265A398454B0780BEF14B944208ED948C9) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/abZ7fuRHSDqfc4LbSqHkzg/zh-cn_image_0000002531106112.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=5F2E6431E7417A2AF5A6455D2B8B517C86B5BDAB9B561AD17B5F2AA2EEDDDFCC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ptAOhSadQ7yoDs1gVRgfuA/zh-cn_image_0000002531226046.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=CEA0E4854076946021FFFC10092AF3EEE02195E109D28BEC143B1C92F641BEF7) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JSfagPGsS6S_8zhTgVwsKQ/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=A19C515906690859204DE4C5CF9615A388587A47607B20A078464463BB6689EC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Y6CUxnEzQSK7kCZ-zklEmA/zh-cn_image_0000002562146015.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=34D77944E14838BD81F32E619192E5D39A66416E36C7D21BD8A46F9F52C4CC05) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Oq77nB48Rn-rwgaLlA4hnw/zh-cn_image_0000002531106114.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=23540900135452E116724254F887317469D99843AAB9B26F1014CF9340F11236) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/DclcQtdqQmaVCIt9HpJZsw/zh-cn_image_0000002531226048.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=85BFE679A716806B23A7BBA01570EA3DBA911A1250DD3ADA79D406728F226740) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GpzaKbncT16jtF_OeJx7_A/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=A5F11B0CBAA935AEFCB91A0F989BF3FC23BA28D769884ACAC659B45AF4CD75B1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QxzfjgwFRa62Z1pq5qpdmQ/zh-cn_image_0000002562026031.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=4981687D80F64C31E9E6DADCA5B4F6E9F234464E542E76EC6FD0E5E317588464) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/a1xtMoSrSM-L3ujpOBgSQQ/zh-cn_image_0000002562146017.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=FE651E019A15DC3A19D98B3F5471B7B44819A4068D85C940E3F86BEB90D503F5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/br2qJVMYQWatQXb6bqYzhQ/zh-cn_image_0000002531106116.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=E9D6D3CC051260C6F745933B864CA25B6DAC2836B614EA4F4C41C6C65A96CE3A) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/pu0gQteMTwSov_uHsxjz4A/zh-cn_image_0000002531226050.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B837A8E7D613517586F52EB73B053B892B7BA4030E1BB0D01BE1D7147D04A915) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jqO9UvEbS22tFGsO6tVZ-Q/zh-cn_image_0000002562026033.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B7A671DB2ABD4F801CEA8464F4A1A2F6926288A4EB34823F23479D0C20DC330E) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/T6SRypwRScmkghsqNkJkDg/zh-cn_image_0000002562146019.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=5CCEF2A105245C2FE5E4EDC061BFCE497DCCA72834C095F1C4DB1812A60BC6E2) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/F3Xd70RpQlG1Jce7stvITg/zh-cn_image_0000002531106118.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F077D345B7B80D222669575C9AC002EE72DBCDB9978F218C8CB0CD12A2089A1D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Gy0FtAOFSFWcxls05FN0iw/zh-cn_image_0000002531226052.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=877F085AD4CFB724B78F4307D1A66EC6CD2F25D38908F4F024103C5297A2B0A8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/jvvU7NrYRxaLc9yNBexMsw/zh-cn_image_0000002562026035.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=EB7726272664863738A27C5306610A4C8408FD197E0F80D8C4309BB5B4DDAE4E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/r32_5jtpTua4n65TVKS7Cg/zh-cn_image_0000002562146021.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=AF778D27919B557CDF5421FE5352484A2D230AD73772E0B47CFDDD1C58F21962) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/blbsWIQsT_iu9OGIXDZALA/zh-cn_image_0000002531106120.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=0798233341FDB2218270459CFB929434635A4BC902B68BB235CF63F69DE4C25B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fRlmlHaKRLSh1nuZnALoDg/zh-cn_image_0000002531226054.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=1123D8062D324D87F495D5772AA4008AEACC1F2EFDDB1E259226B9E687AF3318) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V1mjjTDzQRSsnEbOPpnYCg/zh-cn_image_0000002562026037.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=6C9E34265BB19A519EEE01CAB66F28F71A686ED545D206D4619ACBF0626C649D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jxcPM5R7SCmNSusonCc0aQ/zh-cn_image_0000002562146023.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=70C7D7F09B1B8E3E7E787B2EC68E287C24942EAC392AF7462BA329E78C875F3F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ASfGTvrLSM2FUgj_QVWLyw/zh-cn_image_0000002531106122.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=6854B23513F205CF2A8F5F2D244594CD39C186D992752E5E1E918E0E6E4B9AB7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wZrjWUDcS-6CHwiYaqccTQ/zh-cn_image_0000002531226056.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=2A63FD0A3D27D40633231124ECFFCECCAF5F9C07065443C603F6F1DC2201BB17) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/oASIdz_dQW-hs8rTRL7Tww/zh-cn_image_0000002562026039.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F244102338C7F049B56C792F531DECDC160D42C7206E5FF0FD776CF7CA6DD875) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/a4oALb_BThaymLQFVTVHaA/zh-cn_image_0000002562146025.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=C57C962800FCFFDC2257D6AE7B200BB98EF572B924D394D5D98FF501052A33A7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Jqx8ArIWRX-y9eSLmeVi0w/zh-cn_image_0000002531106124.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=7FDE039A7BFC5D67EEB310844711A7D8F489047A41BAA71E88EBDF5FC75DDBD5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/dBLJHSVeR4avgT_OYAHYEQ/zh-cn_image_0000002531226058.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=98A7192C3ED04CF94ACC839199FCA60E358C43991FD086AC519FC9129CD6BF3C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/8pqRn1cYRVyqwr2newqOFg/zh-cn_image_0000002562026041.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=816DEE9E1990CE95957AB9E6A2D898ECEB73F709922F76A868FE962897425300) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4GvJyUxOR2ecmv_IPFCAaQ/zh-cn_image_0000002562146027.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=310BCD0F3BEEB13886F4F948B810F3840AFE97149FB59BAEBB86963568EC5F56) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/0f2hKesHSJ-Ob3qcaY1CUQ/zh-cn_image_0000002531106126.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=CB52594887AB6C9948468DE339899A39719C55EB137FBF277441C266FC403A09) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eV69HhchSOaz4n_yF74GVQ/zh-cn_image_0000002531226060.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=D9CCA51F9E3927F3399ECF159ADE22DC0A43EFAD803ECCA32C7E9B498F9137BD) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/O19y5y2CSI2UGWaXxFS9zQ/zh-cn_image_0000002562026043.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F8398547890C7A32C94CE7284256C05C9996EB968C305A441BE55B43D7318DC7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xfQdLA5ZT76oVrC8yvrkpg/zh-cn_image_0000002562146029.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=E76F5411066DE78CB0A002EEA0953BAA55E8504AAF27F0FF2E5C13783288F55A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/JfxWl8mOTOyiD1mQfm-OVA/zh-cn_image_0000002531106128.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=DB5872A0D18A4CE1CABFFAC153EB0C5D2B7FD000E1FA8DF7435E9D760B7D24F7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IhJHv8ByQuyVSmMGbGKp-g/zh-cn_image_0000002531226062.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B26337D31FB74C46C7FC9B0FA54272FFF1736C7ABC7893F9C06EEFABBA4E4A15) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yasC9FFJSmCIM0IWuB4eBw/zh-cn_image_0000002562026045.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=B18598ECEDE78ED8932708C5092A8C0163FFAFAEC9C4F168FEC4401781BBD708) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-voVzRYRSEiL5g3NmgL9Qw/zh-cn_image_0000002562146031.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=284B07DA1D19EF4B670C1FE1C41532B16CA9D1EA730E42F25D387D2B8D9CCE92) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CLBScMeeR5ucLe8kiPIUNg/zh-cn_image_0000002531106130.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=F62FF9B0B75F8A9EED825417FFACB914CD59E6981CB55F1F89EDC07526FE76AD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/gQmcqygQQ3ClntqIWGsWWA/zh-cn_image_0000002531226064.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=87E50D5C91C21842CDD23BE9E582B19A5F34B5A9143F2678A4B68BB7B274E427) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dxkx0DPKTwaohUnKFJSoXw/zh-cn_image_0000002562026047.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=62D722CDB1AE9B71DC27929B47AE5D2A75B9173BF18770CD3F5F1DB16A6417B1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/IGQREW9FQ4e00wZH6kACWA/zh-cn_image_0000002562146033.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=47C43816D785A9BB150254235EFC7FD3AE6C95F791E718873C57CEC93ABB8F75) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nbFet5N3RripaMfi9K9IoA/zh-cn_image_0000002531106132.png?HW-CC-KV=V1&HW-CC-Date=20260322T023550Z&HW-CC-Expire=86400&HW-CC-Sign=BF9C9583E650B544AC9B2EC855EF2C4DBA2E1C1A084C48B8DF59CE2D6931C293) |
