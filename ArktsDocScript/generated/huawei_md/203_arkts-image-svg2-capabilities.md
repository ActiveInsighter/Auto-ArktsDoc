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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/TuO38AtFSrK2kmWcF9Knzg/zh-cn_image_0000002535300540.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=950926E876578AD45230C8F00BEF07FD216612788A3DAD2E2DE5D5F1F90B082E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/4QwOpTJ8QiqltkENaY_ZDw/zh-cn_image_0000002566020403.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=9A0757DB7DE02A8D5D1266CB0FC533D74737AB1BE3AEF85EE7CB0D32321CA69C) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/hd8wdui3Qs62NrfdM8axdA/zh-cn_image_0000002566100415.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=FB7EDC7CF3375B19BE88EC78D432542203E5C32F2C84BB4BC4781B62BEC40C01) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/R_0kHYguQ5qmcNElZRFU-Q/zh-cn_image_0000002535140604.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=FF09AD2E2A0207A15BCF120A3BE7FA5AE844E4A526E03940671A30564D7BA394) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/WSkkNys-R-KYHyr5_miL8Q/zh-cn_image_0000002535300542.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C37BED1303294C816BC2ABE3AA34555D63F79AA0AA781E0D6A5A653FB80775CD) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/HlZAeNUdRya7dyk4dsoANw/zh-cn_image_0000002566020405.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C60EA139D35743CF3A9D8BA984A0FC53BC4C8BC1A620212795330034A6738B1C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/4E64lmKaQdiMeXSu_N5uTQ/zh-cn_image_0000002566100417.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3954E70A9073F615C5B6FD3DEFBD4C544AFE95F6D7A7CD0B62729F81AA99DAA3) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/C6dizlQbRBm4pmbzYiFwUg/zh-cn_image_0000002535140606.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=5FED53FAEB5976C551A2C0741A9235189EB5968C49CE2C386903B283809CE851) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2Ay-fR38S-6c31-DcYYMEQ/zh-cn_image_0000002535300544.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=67FAD877331259D14DA3DC130CC57E961A1195A8814B6524BCCD3A757C29C0DF) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/g-W1-PqERK2mp0WDRr1-tg/zh-cn_image_0000002566020407.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=6ABA023C04AC9FE34EDD342751A31388EDB996020CAFA1F6A4D96684E0247D1A) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/580Doj5bSdOLmAq0BytWLg/zh-cn_image_0000002566100419.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=E4AE6B9D436B15FB45371E6623D501B969C62A90FA3FB56C4E22136E5239F62E) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/_KxG_sINTfawPc76-rEsmw/zh-cn_image_0000002535140608.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=D973CF3C1F610F3E12FE6C7095D93BC6AC4CCFEAB7A9BB9A8CB9F06ADBD6529B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/539QaFVUQU2eGT0s_9mqcw/zh-cn_image_0000002535300546.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3B331100C9E408B32DDBD87667276630675DE1D2ECF4648B6D3CCAFD07B56367) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/SHtE_YjWSZOm7yIApgUWaQ/zh-cn_image_0000002566020409.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=ABDE438B0265FC875696987F2559F3C74B1B1467BD7201426F8E64DDADE85CC7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/BgO90-J2Tl-OIcYCCJh_zQ/zh-cn_image_0000002566100421.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=93301EC9374165CAFA0F69A74D5ACA4FF65EF49706298C922A1E869A2FCABBA7) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/7Ay-0sO3RCW5fRtxtNUhfw/zh-cn_image_0000002535140610.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=D8198055C5886157F1884D57F5C5693E773985CCED0231B4BB7A1BFBE669D2BF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Gm4zddBVSGikq6heZzm2Jw/zh-cn_image_0000002535300548.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=B547B4BB8FF59EDF6D40265E8D0B281D2F3303526D3E54B1E87E2507D85A24F7) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/aWMex01qQvyxR7ck__BhkA/zh-cn_image_0000002566020411.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=F22C505EFDD6A745EF1EA2D0AFB3FBC7A43832FFB8CA5BA52F28F43A2B64180E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/PEHxlnbOQL6pvoki56wiGA/zh-cn_image_0000002566100423.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=DE431758E3EBF706D7F39633BFB89D8C67D7CDE4D79A68846D4877858BA36C9E) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/YUI5rrqGQBaIqJbisQSOag/zh-cn_image_0000002535140612.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=D1BCCFAB11FCD6F985DB771B2BFBCDD67D68DCD243AD934DEC93AC9B46809430) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/iW5GdVeMSyK5oV5RqtBWHQ/zh-cn_image_0000002535300550.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=37C282742A4130843BB0F92D69F634C8D42B36005D23444FFF025A81867CF05E) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/xuwjm1_YTCuqhQQy-vTqdg/zh-cn_image_0000002566020413.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=2C1CE0D96661A74A016EE59039E21AA0702FB3DCC190031A8F93B22B9DB392AA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/d_ijzy_xS2OfCM9qStZLnQ/zh-cn_image_0000002566100425.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=571DFB86627E459411A5BC341A840899216D3180AB400F29F66C6006353F48D2) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/vY_-kGxkSJWeEuv0OGBaWA/zh-cn_image_0000002535140614.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C23530E25D8CFC7D0CC466B806D11673164077B60BBDD0F55BB46A6C2A30D750) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/NU0I-GqgRBW7Q7BNyN6wqg/zh-cn_image_0000002535300552.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=E35F4BAA9A41B28A6AD9DCFDC5516E1FF0AFC7DA787D5621DA5B848EC07A8C64) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aTXm8v3VSU6GVlCoHNuhCQ/zh-cn_image_0000002566020415.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3ECB3528CCA1C83E1C7CA50E51038358DDFD638538FF67C46801868909F7463B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/--B1qs6qQWy4s8bLidIpcg/zh-cn_image_0000002566100427.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=DB503871E0427DD329FB3CE8D105F8DC52979D2BC4A44DB2007B6C80AD25906C) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Bg8XxYzqQNKmldYnRZHe6Q/zh-cn_image_0000002535140616.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=F953CB2B47E21776B5E2E2898B8348260F01E355A60560AAF968A4750EF08D6C) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/v6QhlVsTTt-PDmXKdYaNYg/zh-cn_image_0000002535300554.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=31D722BA652230961848258BCFC735644A09FCFDDA4F046D8F878284DBEEC263) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/vqytfLbvSKGfU3XhzKl27g/zh-cn_image_0000002566020417.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3645B9415A9AD422D857370E1D5574E68F75775564C6ECF8AB9F0060575C35D0) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/HVqzSWHoSUWmJv2DukVCdA/zh-cn_image_0000002566100429.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=D9628238793FF7A1DC438739BA6EC0E28879BA31EAECAAC28E9D1D20FB4470A1) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/-IhKEB3zQrmnqNCilin4ag/zh-cn_image_0000002535140618.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=B49C50B55BF3EDBE8C6ED70B2FDD77C4AF01A3D92949BB0E306FF2233BC567DD) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/BnRDZwrgTBOeMxBfQ4iwZA/zh-cn_image_0000002535300556.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=CD2ECDD6EB9611E2490C70D32A5E4EC6FAC88AF3EF5DCC980EA8A0E5785A7DE5) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/YwfWlyhLT_qRHPa208lSWg/zh-cn_image_0000002566020419.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=4F9F50F0654B4D8118083E892A9960ED8EFE4F1C0783FCFAA20004B45976BC36) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/MlLByiu9SPSO93WT_mHe8A/zh-cn_image_0000002566100431.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=6A44E899E5881A48081B822A7EE743822E7CBD4FBE1763666BDBFFD3A80CFC34) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/te1EBln8QDC4meQZsJsZuQ/zh-cn_image_0000002535140620.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=786A3679464ECD001D09637C8A8B382279D967A2B63E82BD7EBB206B34CFDFFE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2UAMPVhSQ_SLc-WlAa9Kgw/zh-cn_image_0000002535300558.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=49833231ED21515D1528E5165BEE9883BABB8C5991DC635A547E4A803608DCC0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/FT72EHSHTD2o8_Cn4vmCRQ/zh-cn_image_0000002566020421.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=1F8E3DEF47DB68D214E97D3E53CD920621A6C106EB8A1F406F55048B1044D18A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/RVWR5KvaQR235Z3mLWcE6g/zh-cn_image_0000002566100433.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=B3B1588606798F9285739611FB6C65C59B7D33DB8C5DF64AA3E39DF593CB8101) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/xGX22YJRRJKfZumL2Iam1g/zh-cn_image_0000002535140622.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=2590F151EE579E8BEBE35C336EF4C88ACD633436970BD190CA6605B67230A6B3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/DBrUOeF9TMix882O41Druw/zh-cn_image_0000002535300560.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=53C023918DDC4F2E812AF8CFBDECAAFD19AD5110C19898E728FBFBC0B2978407) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/Kx5FBPHYQsyGkp-vFs6iXg/zh-cn_image_0000002566020423.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=76DB50C3BE825D46CFCDAD6D7781B1B7F11B46289151F4AC8FCB5607D6DBF957) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ujZtZV4WRjK0tURAJ5iB0Q/zh-cn_image_0000002566100435.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=D357C3DA3FD70F59C81EFA6E5266566D9F49F3D0659C67FF34B933525BFEA0BD) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/91_V8xLsTQ--bA76rbChLQ/zh-cn_image_0000002535140624.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=284A52CC2FB96C148BF3007CAC4D7B40EB3BADA6A846216C7B29C14DEEBD1C3E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/dXuWIOkyQcSc4S1IWTc5rw/zh-cn_image_0000002535300562.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=96FAABC56789446A90648E673479D776D6C14A72647CF1E6AA9BF94F49E2FB67) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/VkHLQD6oSBu4K1kK6sPePw/zh-cn_image_0000002566020425.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=0E3B992BDFBC9D261C28ABB5E3B9F5F443B18F8B4E191F879CA1FE591BA83BB3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/MSBrzHzGTU-ZSpOoDpMS6g/zh-cn_image_0000002566100437.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=86F4A1BB2C8E099A7DC8CA69AA5449147BD2554C1D906178333C5C2295BCF23C) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/FKUk_DMzT2ej6uUPMbTg4A/zh-cn_image_0000002535140626.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=02E8BA4314C41C57E556740C925F381DD5847B5B380FFFBAD8F37D3D55D4EF2F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/WII85NKDTwmvCIyNy_yYnw/zh-cn_image_0000002535300564.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=DB2A6837F9FB9F00F8AD6FEB1679979AA766419DA08692BC8EDCED383A36C216) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/pcqn_xbFTI-k_qI9kBl8nQ/zh-cn_image_0000002566020427.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=949B6A10687EB39D6CC1FBDB80AEB0AFC1D6FEBEF38D30ACF652CEEFD0D27487) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/5MZlRVOLSeSnWAbhZSOjQA/zh-cn_image_0000002566100439.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=EF5684DF14AA5B1444D94B2DE0BC7FC2C013C0C8A87FF4EE03B968F05B881C12) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/--wpoH_wRqq_qxf9EBYr9g/zh-cn_image_0000002535140628.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=85F3C7901D9EE720EEBA08C1EAE945B97151A9469C10342DD090D232EB660BE4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/V4boGs9_Rg-nWxPaIcE1pw/zh-cn_image_0000002535300566.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C28B5234D8364C964AA224AC32CAF6D71A5B3C4D2DCFDC307754FB946FA869CA) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/i8dFfk75T8-u28AEGZ50Lw/zh-cn_image_0000002566020429.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=65A936771A59BF62DAE24032144270A7B83C90A2C8AE155009BD97D8FDCF24F7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/oSZl_vnhTqap4ym1INTvUQ/zh-cn_image_0000002566100441.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=44253996AE5076945928B24A10689A4EE1BDFF3680FFE71F17CCB2DFA09D54A8) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/S3yd0nkTTxuuRZwHnkYaYA/zh-cn_image_0000002535140630.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=1BB37BA9506BD91A3D6EC4D7B3CD1ADD32814E9586B2B21F5379FE49A9FD4C74) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/cdntUrnqRxmu6LNI3lAMJg/zh-cn_image_0000002535300568.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3844C4EA7FE07C44E92ACCC53005E139AADA678D776FC6CD96B918284AEC864B) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/kbzSDpIQTeKhX3M1o_d__g/zh-cn_image_0000002566020431.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=660797B66EA3E8F04611E3119F1EDFEEF75715172D692F14217115A288C4D5A7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Ca1lZveOQsaqSeEDO_HJvw/zh-cn_image_0000002566100443.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=AF71285CE010F1F26CD2B537A330883FD1B8D08D3825E7B83198E4A46EC7B9B0) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/9E-2B9eTSg2Uff1lhEEOaA/zh-cn_image_0000002535140632.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=228BE9242B65B4A4E4F4C01B4E9CE8772749CE3B346AD4DBDB97C497B725BDB8) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/zj1uWRA3T_WeqcY8Qq2BSg/zh-cn_image_0000002535300570.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=0A7B8EEC365B622A60994E84A1C762975345D706346599F8F88FF413B929392F) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/EOqrzhP9T5OwmGePODIyig/zh-cn_image_0000002566020433.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=020B70112D907F4C62BD30E9295855468D4908611D416DA6EE3A631408EEBB28) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/0l70BKhKR5a_Fb5WvttIHA/zh-cn_image_0000002566100445.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=154851DDE31DA098A9BE325564CC8F64A944BAC279AAAEA0CF4A5B6425AA8112) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/T_I2fZRARGiqawHO1cR35A/zh-cn_image_0000002535140634.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=5AF14086B3B60E300CB3AF6BD3D047CF553DC6061896AE0314635A3228AAD797) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/n6csh6OvStGyxsoPFzIffg/zh-cn_image_0000002535300572.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=A36536EC4D27A085F13B10BDEB142EBEC33FBE730CE162F8AEA53945E9722306) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/bsstLjOrRHusrqsZzlN_nw/zh-cn_image_0000002566020433.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=F53112B90451F85D524377F9ABF84ADA28CF49E9AAE377D3377651CADB0FB3C4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Cj0hy2hmTwO_sae5Efnq5A/zh-cn_image_0000002566020435.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=304FD16FC657CD7CC06353A2E6A11EE3B7C170F35A718D4385DB78B02FD12FF5) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/7DRFs0-SSVCKqg3wWJBQMg/zh-cn_image_0000002566100447.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=F70E7BE3982CA82E3AB533D7626DE89BBE4C67183031D247C825EEE5D9A58611) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/EezU4tM2QzerI2WSdZ053Q/zh-cn_image_0000002535140636.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=A4E5AD97FA2F1EE8E832A1DD5D098075C372E659FD5DAAD927BE93482FDDE5A8) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/oxex_aL5RJWi-C2JVqD56Q/zh-cn_image_0000002535300574.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=FD9437A045464B0393EC5ADF96BE0A6B18DA2ED08C4D64080A1EBF1BED27C904) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/xXIqARJGQTK0K3f1BSv8zg/zh-cn_image_0000002566020437.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=31A52CBD7BF2D421100ADC2BFEB82092199B00F1C1433072509860918EBA6C6A) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/yx8EfEMAS4-XLBaRd592gA/zh-cn_image_0000002566100449.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=219299657E1391F8B00C24F78C34DEB425C11C533DC8AC0D1E0AE4767755B455) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/wti8Y4iFTp6YRSooUW9_PQ/zh-cn_image_0000002535140638.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=69FC1A3490C3ABFE76B3932B273CDF565ADFC15E8560921C185652AB64F73ABF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/MnZcPtJLRfmFlCJ5TjdoUQ/zh-cn_image_0000002535300576.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=B317759E845CEAE8FADAAA1F856DDEEF0DCDA04E8D74A478D13842A92EE16FE2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/_kZlUD-uQlqvUOt1mSVFrw/zh-cn_image_0000002566020439.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=69954B0845C4B6F69E6DEC0F06828B1437F9976F840E531D178C0EBD32F04D7E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/HxMw_SJUSYOciLtJgPqHiQ/zh-cn_image_0000002566100451.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3D84848879216EDC39EBA394E80500E6442824122DD9647BF7FAA831EFD01ECC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/LivKygX7Qkayj5YvpCvY8w/zh-cn_image_0000002535140640.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=7181DE456B591888C35A6F32C840E04489D643ED44CEE1C35FF02CA4C8C41044) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NO4PF7FwQHSIGsnAAy9vhg/zh-cn_image_0000002535300578.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=232383867E37E2F2F7FA3E669E3AB8D79A5F800B00847B2558170F5E115F9B78) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/qNyhymjqQnKy2SNuQQE3EA/zh-cn_image_0000002566020441.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=948A749D543CF0FD622755979C0E0047247DFAE7D4432AF6BB2C81B9FC5BA539) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/D6SMy-WCRU6qFr5spnZnYQ/zh-cn_image_0000002566100453.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=5D4826A13455E049C4F667F0BC38100860F274A3655AF386366006D4FB23810B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/NG6p9nBZSRWXWOMABsUW1g/zh-cn_image_0000002535140642.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=97D8253A3F62724145B6A96A65573AF0EB1F058D004C307740F9946CBE0A62C8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/d3_uOTzjTwa3PTTHzGs5UQ/zh-cn_image_0000002535300580.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=446A9D65D1536D840674560EB17EC07757F753D1852D2B28108AE4C5FE26DA32) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/BuyE_PTUTxSmGaEpn69oCg/zh-cn_image_0000002566020443.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=9C57E1C1FF1493D8D611A9D579866276AAE0F3BB5EC9C87C3DABA494D4959183) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/BQJrCPLNQwCm923hmbUhEA/zh-cn_image_0000002566100455.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=16B3AFA5081032FB2C566F9D4D809FE7E8DE14D9923FF29A1C90E50B1A0D59E2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/9khSNo8TQtuOJRYiVkkRIQ/zh-cn_image_0000002535140644.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=8B1DF7BB76E814D84AEBDA863010A1E92E982FB154CC4AB50098B6E587559A43) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/qcUNCkQiSFOYD-dS0cSXZg/zh-cn_image_0000002535300582.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=65094A2EF6484F28978F1183B853132DAA70E4ED31784D51D3F3E3D140A071CB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/DaziXOmuR12ozhA9oWxPOg/zh-cn_image_0000002566020445.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3D286AE5C860B3906890C78341DD01295D919B9EB082DFD43446ADDA2A9B17EE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/EauB3yYwSl-UCE9k9ctPZg/zh-cn_image_0000002566100457.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=7351AFE4DA3C4600795FAC21A4D6C3DF76E87E88E4E4F205342279B790AE56A6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D9f5ZSoaTKCTK4YExmu6pw/zh-cn_image_0000002535140646.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=0C2B5B031D9D46A17BD1EBB32D0587F0C6ACE56CA7136E852628A4741E19E8D5) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/vDyVkKPMTy6wkjcyrOIXZQ/zh-cn_image_0000002535300584.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=19B36DAA379ACA35106E8DD6893CBA2107C96CFE93BE86EAC0F734ADFB3CBAF0) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/-fmLQ1esTT2guRJR-Udgkw/zh-cn_image_0000002566020447.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C4C0CDAB7B95B073888645FF3D8605E459025C9C8612EA2FA692AF366D67997D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/KRTwQ_fVQCCnpqBkTiYH8g/zh-cn_image_0000002566100459.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=DB7AFEE99BE4487846492B1A920DB0ED6BA4EA3E38F5918C4E2BF0EF863B949C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/-5EfEHdqT3WgdLSHtHhhVg/zh-cn_image_0000002535140648.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=7F37593E76BD908678C9B9FE33F636B119D35AF7B7B90B0D746B69371EC4CA89) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Fz1Q_swfQMmZxhi8HmsBIg/zh-cn_image_0000002535300586.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=3A91C1A28B94706CB954C1C04DDB1511F06B6E8AB2A526F835E10F38F1239CB0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/F4qBazUJTqCD_tLZrHwOhw/zh-cn_image_0000002566020449.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=26332CAECE797DA9323FC7343BE97AB28073C795C023398F5DCE56252BDB3EB5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/rh41VB1CTuiTJxnjNKuC0A/zh-cn_image_0000002566100461.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=12E3F081200ACCF238000D832663CC9EF48E5F233202F2E9A88AF670C196FCC0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/IGfL5mTCQ-axaY9Eh52Nsg/zh-cn_image_0000002535140650.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=C29C9B346EA9A4282E3F46CEAAE15026727623FBF71C0114CA16DACB0135BFAC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/dF8JFDD9TEyH9zmbj-xu_g/zh-cn_image_0000002535300588.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=A1C867C9779232A280CB59A3D0555F547492B71793E9CEC86C48241E561CC329) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/vi8QS3ThTbmCaBCZ7qhJog/zh-cn_image_0000002566020451.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=BAECCF99BD3471058E7DC6C0DBFEFE6CF1D9DAEFD9EB1DE1412FB2417E7ADF0B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/-RSw55UOTEaoymeQimiSIA/zh-cn_image_0000002566100463.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=2E57DF268CA42AF0A9F1E97DE3E0AC233A71D813106A5827A926A4C1C31401AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Fb4P9g-VQ7iiRH1sEvE1tg/zh-cn_image_0000002535140652.png?HW-CC-KV=V1&HW-CC-Date=20260403T024235Z&HW-CC-Expire=86400&HW-CC-Sign=570C08F07D5860D161FC0B323CF0EFB4618E8463C9B5BA08DF02C6122E44A0A2) |
