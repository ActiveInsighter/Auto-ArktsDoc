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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/45xyL-rsQI6AOzbrMee5Nw/zh-cn_image_0000002568253825.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=6A14E41C6379AC6727568B3376D151ED941678E9BD34B9C93FA42C3B58E0A308) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/7FvzF9BkTNuKIdKUmSHkKw/zh-cn_image_0000002537174116.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7861C65ED61AAAACD1CE50A4807E701D0B49D48B0642BDCAD9342515CFA8ADE3) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/42tSgV35RPKcd5m0lmAkRQ/zh-cn_image_0000002537334036.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=FF56ECA42D21BE8E9D937F42AC866DF17A4EC2C239B96A1B4E27A06FD132BD5A) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/77UEboWMQAChwyeHzvUwiQ/zh-cn_image_0000002568173831.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=AC7CF95AF07E8252E81EF0ED18DDAFFC42ABC06D8246C756F16D12999FDBF52C) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/aSsW3slBQCSCmh8exE2xbg/zh-cn_image_0000002568253827.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7366CD8DEC0EA9C40900C0CE02925DF61F28A8A2FE518A5D0425A1437F690878) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Nd-o7YLxTp2WwVyCq6C8yQ/zh-cn_image_0000002537174118.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F10A59EB171D296E4E2BCC0E7A8CB8869010C9B582C73ACEBE866AC304BECCF9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/CAn_uCAwQ76f5bLBjY3a0w/zh-cn_image_0000002537334038.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=951EA3FA421551D926268AFF0D86302C2E3464FB393DDE674B530729707F1872) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/otQWout1Qb2Daf068iDnEw/zh-cn_image_0000002568173833.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=5B1AEA278C057833CF8A920A51D7122F62C587FC68A1818773FEA1676FE90D5F) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/aAb_OuRqQBy7YFniWynN3w/zh-cn_image_0000002568253829.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=AED64CECB560FD651124A0AD426654A3DBAA43C24FB41CE4FFCF1F7F3AB8BF9F) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VYQ96kwFTuC8zSLdK9BkhQ/zh-cn_image_0000002537174120.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=17EBEC745737CDDAEA8A876789EAE4319690F0958AC9AE2923A2596669178C2C) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/12kbammoSC-7NXCgtCKf0g/zh-cn_image_0000002537334040.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=B89AF2DE6DF051EAFA4ED86109F3372219A45AD924D75BC21C9D7E1347FB9368) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/2WE-_0uST9OtmFUx1IygeQ/zh-cn_image_0000002568173835.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=3545F38245775E96629885B32F88E409C437E335149E852AA01B015D73494A99) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/YSe307DLSXC4JzJKV6eLWw/zh-cn_image_0000002568253831.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=AD82A9EDC48379DE78D43BBCF12F5DF13C8331A6B0AE28B444F7C3AA4936D96B) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/pAeefupETkufOKbhOMme3g/zh-cn_image_0000002537174122.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=4CB2B6627D06373DDF6B860D8E60CD8E0320B3AE224986A35498369F858B656F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uvocXxb0SL-17lpaM0y5Rg/zh-cn_image_0000002537334042.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=CB0BCE5474B6167E7144AA9681D6944BAB7D508AB04796BF65C380C48D4BA3B7) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/08YrSa2dQl2sBHkBDHUNfQ/zh-cn_image_0000002568173837.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=22549380A7B9EA9C722A7B81A231A6E10073CA21162D7C3C0149AD5D47349E85) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ICzzwrMmRL6d7l2YHgB8PQ/zh-cn_image_0000002568253833.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7CD12ACD58ECC1E3B8C048B007482493FCB2EB7CC74C3B031DE5DCF9DE8E4E4B) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/g_q8khm-QdaJ351XeOHo9g/zh-cn_image_0000002537174124.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=91F7FD99411CCF9D9DABDD4C1A7467B52EED6B41AD3EC9F375822BF4C2063378) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/--8uK_3RQry0HjvWxpXqIg/zh-cn_image_0000002537334044.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=9791BFDD1D798AD094021EC7F0CFE63A87434BDCD802C98B43AE7E6AF3BDD994) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ocL9M-suQmChE1r_pZM6Iw/zh-cn_image_0000002568173839.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=36D73C4694010769408A94E0DBE4F27DEA73559B8B457A3CE83561D26C5CDE1D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8U1jVOSWTdKEShTiRpUhzA/zh-cn_image_0000002568253835.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=2BC06CC681742465271C3E730AB08EFC508B41179F59598BFB365CE26158053F) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/vn6im5O9SQWxqKo_eE4uqw/zh-cn_image_0000002537174126.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=35394899B021B4AC1F6A75E473498A99485E503340E23D2B126A79926FF17AA5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/M_F5hzY1SHeRSUUZC2ITDw/zh-cn_image_0000002537334046.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=C31B2AFFCADC413E8F9CA9B73E2AB54F73847871742803043269D74CE9A5C4FB) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/krYvY2UuSKiWEswtdsMS1g/zh-cn_image_0000002568173841.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=BF70D4E8B291F0159893979A2E3C5A18C681C620051B21F49D877FC332EFC952) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/xHMHF4dsT0qdRcHZfW9FuA/zh-cn_image_0000002568253837.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=011CA18AC1F3E586CB9E6E421DA722F6B78B9B956367BE42432E2B16799F0F27) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/lvKWyZbVRjaedYnIiNfSTw/zh-cn_image_0000002537174128.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=63FF23B7827D54FCFC9D1F181A3E5C3D4356B325C2624229935D40D780B151CD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/umyDKDlxR7-wEPpdOCJdAw/zh-cn_image_0000002537334048.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=9145DDA93B6D25AE4278EE212E28364E3D67B89FC606A77D1BC2ED106E8E274D) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/c6nM60LISVCFrLSao64HfQ/zh-cn_image_0000002568173843.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=CFDA89B43920A7D7D219384E3AB00A25872DF12FBE3BCF2FF3E459E9309CC5B5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/iUPeLv0KTXak8uxl4cCgGQ/zh-cn_image_0000002568253839.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=94755F5080888D6567EFB5832D1861F3DBEB321AB43E6BCAC96F7A0BC0D96669) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/oX5aZxAgS3SM3pBrj-436w/zh-cn_image_0000002537174130.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=8079491598275DE6232A352E1E8D4C38B7BC994304AF204DB9AC9335B0E198FA) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/sOKbkqk_SDG6AvhMb0M0Ww/zh-cn_image_0000002537334050.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=74BB9E3EB444B36B413E77EA4F380E00ECA9E2AEF7852DD766236C7272B0CDC7) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CjGhX0Z2TPGJK-MFTnwDxQ/zh-cn_image_0000002568173845.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=ACA06289A5B3B75712370525E883521E58A1B0103B791FABDD18B2CAE8A0F43D) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/cTdz-z--QiaDIpSqYgIECA/zh-cn_image_0000002568253841.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F6B7AEBB82AAC3807952D4ED7619FF62D4BB60BCC73D362054FD33C6BEAF4653) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/6ZgZhJ6rRHOUtOoWVWqRxA/zh-cn_image_0000002537174132.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=E0149CE2051B7265323BF4A706F92E06F9F288B44A7106F444F6C91825B95A7E) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/87ebU61DQhO8QD3S355Wuw/zh-cn_image_0000002537334052.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=5CC22536C02054EFE8CB2F6484BAD4B8F037CE43849070B97B4D2179470C8B1E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/szPZXMufThGZpVoNNZAafA/zh-cn_image_0000002568173847.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=44F0B1A137D41B444DF19A63B65AFC826CCAF344F558373E8B7C3F57A1D1F3B3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/G6OHzGXNSdKSnurJ2r6duQ/zh-cn_image_0000002568253843.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=32E5C637A07597EB63AE42F7007AFC851EC94CF68FEFE36D5DA7F71EA527046F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/s3jgoLiiT-2kqqJUDMPEZQ/zh-cn_image_0000002537174134.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=1F2C1CE1204A3A21DE7C1E61556C4A130DC274D458AAB495FA34D6C95FDA61B8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ErgZ1ZW_S9CbgfVo13-Q0w/zh-cn_image_0000002537334054.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=B8B202C913B43BC425AB30E9426F1A8D822EC46049455E24233114FEE01FC531) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/p9c53UCHQjWTsVrfHISHzw/zh-cn_image_0000002568173849.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=02D54109EA3533D3FEDC66F7CABD786EE91A9BA8F7FB261636E27A2842974C9A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/378UtI3yQdGQxN8x7XbJtA/zh-cn_image_0000002568253845.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=753A3083FAE8701FB1E3C7312E60622528E2B2B31D9BE3E041591DE35A771F9B) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GHzxFYYDSsaBGPrE80zLjQ/zh-cn_image_0000002537174136.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=8F95DAD33B34DC3BBA94C6E759D6513657A32A5E9806E0E15F2A7C48776C3AE4) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/lSoI1uQCTCqIO9u3PQlO9Q/zh-cn_image_0000002537334056.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=881FCA86D85AA4FB5F617B356AA9FA25DC8A08B170B6C82EA6F9AC64F1AABFA2) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Sf5Z7TrMTaa30lSMJ_sHmg/zh-cn_image_0000002568173851.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=BAB1AF814A5AD36153176EF1B94425D91DB0271173EADA82268C639C70E90F5B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lC6b7kSKSGWlD35LMHN-nA/zh-cn_image_0000002568253847.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=29DA83CA9616B09BFF62668748B8622DFEEF42824BAE621B5F359A6C5AE811CD) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ohk0RNybTieg4KPBt4CSJA/zh-cn_image_0000002537174138.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=21BD340F969879686037F6F7FDB9DDEC7A3C4B428A09BB448858985CBC8C9185) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/kg3oOD9lRxWfju_bXiJeeA/zh-cn_image_0000002537334058.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=07D9844BB4A5F8722ADF8FFD258432C12CCC1F6A0157D110BF3B72AB38514723) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/f519LwHqTwWyAggnOhz0mg/zh-cn_image_0000002568173853.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7F57A72B967A8CE6A47E2A383BABCAD63E36CAA68042A7539B7AAE7A9BF04B01) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/weALKAymRl2xFhPZRR1Smg/zh-cn_image_0000002568253849.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=7FC9881DDD721E699466D265163B786244C2ADBDD412335043DE549421367AD8) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/0pWfnZ-bSnOtu567Lvjj1Q/zh-cn_image_0000002537174140.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=ABD05FAA0775D9691D0F89B01F0DCC4745571B238154A34604DE06F47EA2D9C6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Mdyxq3-_SFiCnYKFnXj39A/zh-cn_image_0000002537334060.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=6A91FDC862A5D1FE9FCBB54DB095220FC6F2F02CBC8E807692EA6A440D33D79D) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XoYBXwamSl-1OtcBbYDX0w/zh-cn_image_0000002568173855.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=15303F586C48498C6732F766141EFF18D1B6420C085CEBE6FB9B41EED2906372) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YuS2smwPSeu6ULtnc20rVQ/zh-cn_image_0000002568253851.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=C2BDE44107CDE70B9C65AAD822FFD6AD55227AA34E9BE2A99331F47BD792701A) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/GCeqeMACTniVWS3M_yaL1A/zh-cn_image_0000002537174142.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=74218A421897697CD883000D7DF4B9543C522EBD3EF537AE3030A06200EFEBF4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/K7u44wRhThy5BddpAZrJsA/zh-cn_image_0000002537334062.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F9CB45B4261A6B5C9C1BD35C6B306989FF5A7C42690DCBC53D81463157AE53D0) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/3u_L2yF4TVuaafiGkGVBeQ/zh-cn_image_0000002568173857.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=4A0369C1716FB8CB6C8795B523A118A129724E01A159C41289A9E00739ACF2A6) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/UjBvuym_QSOD6K3yuYz5xg/zh-cn_image_0000002568253853.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=AF3CF88E7125BA3D02E6A15A23694851E9F01EC9F7397D031A7F58880FA61F1E) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/IHX8yecHQh-M80olfD4muA/zh-cn_image_0000002537174144.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=C2238D363AF616BA50A9B55A74F3AB296547802FD85C9E0D97D1EAF08F16ADAF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4Nto1GUKRKa0QKaNf9pYvA/zh-cn_image_0000002537334064.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=504B67498539DF26700EB89FBEFAC3B7EB90C9641D229310F1F961CD8595346D) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wulssJLTRWCQz5XCt7Igbg/zh-cn_image_0000002568173859.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=DFE3B57D49A9EC3526C9D4AED641F97E63DC745B6B4B7B3CD48B382C7D22462D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MiDj_xHJR9aZXNf39nfZ0w/zh-cn_image_0000002568253855.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=C1CA6AC1A309AE7FAD478DA952DEA4ADA4B27597D7B0D8AB296F9199E7865F08) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/YSiQSiKJQgSxIBXQgWEPmA/zh-cn_image_0000002537174146.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=5602D07AF5E21B7C4939A7A91D5803594A5A7289CABCD97A79AB741D5DE95633) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/SaLR4yQZSB2i5X3wMOi-FQ/zh-cn_image_0000002537334066.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=2C733B8F860E3B2CA941153002185CB08F964630346EB953F124F94180C7A385) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/rfLletk4TaSmxPNeHxGg8A/zh-cn_image_0000002568173861.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=3EEBC9E44AA29798A4274D025194069C001056160022BDCED234126B9F9BE55F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/zKpDvbuiRTy-opcZqs7J4w/zh-cn_image_0000002568253857.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=79A1D49B8E55216339409F88FD396E9C1712733BC8BCD852AE0155C19429C8F6) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fpvXg8pZQImSRsandRq-1Q/zh-cn_image_0000002537174146.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=4F30442A5EC4CDC6DC7F01CC8E6FDC9355F57992A84433C799CE7E1BE91BC513) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/0PX9-IT5Tye4shnzBfrpdA/zh-cn_image_0000002537174148.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=89916D1181BCB114B226AAAF7F9F6E354FB3CE0D5B0AF3304AFAD5E497198C6A) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/DMTISzflSMSFyI481Nl9Aw/zh-cn_image_0000002537334068.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=8ACC5510843D64BE9C229949F9C8E611C6524958D19BDB566F5ED85F134136DE) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-C7TPOiORK2qTpPEv2J8rg/zh-cn_image_0000002568173863.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=137543CDF785CFDA0AB0BE8212A08A335C61C5F9CF3FABB8516F6C1EB979FFF2) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iJ5UE-DnTwCVf6fynURluA/zh-cn_image_0000002568253859.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=EF305B65AC6880518DF16DCDDC1486FD358F09EF7FA2688E64F517BBD15510D7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/N9j5sQy4Q52kQHLfjseAlg/zh-cn_image_0000002537174150.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=03EA38052CD23018B466ECA75C2D4E158E3867A5E5D465079BC5767C14AB7764) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/MoI0YsrlSx2qvxjdqMii3w/zh-cn_image_0000002537334070.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=5786661BCD6E5911A3E95952272FF9083BE04B27B381B9168B64BCF8665971AB) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/NQ2LupoeSYe7u7qyY4tCPg/zh-cn_image_0000002568173865.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=D94CE3363A27737A4830A311827E4882378A98FA6CF7A442A9CFDF5D36F6331A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/FwRxXvRBQuqs9qGGKpkAhQ/zh-cn_image_0000002568253861.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=E8C5CD1370BAFF1F846D480A69F943FE34DCCC1DCBCD884C419A7444CA8AA9B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Ytkg95U7RoyubkDVr7xcDA/zh-cn_image_0000002537174152.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=4C6D82DDC7EF2B206779189F9DF12CE4CBE3C2CA12A405BA6B2BDEC21B668EBB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fR7VItmATc-qd71_hY3Ohw/zh-cn_image_0000002537334072.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=ABD6E89ED90C95B9F9A2E77C0ED900D5E55746BE95CAC24ED00D8D75D23F1ED6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/G0emO6IIS3mfaxQ6rekBUw/zh-cn_image_0000002568173867.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=0F3013856BDACCF7ED3E47F802E6BCF0C7D152EDA5963A920D54F6D449E3A209) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/g73u4fShTJavr5-F5NBIUw/zh-cn_image_0000002568253863.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=45078EA358BEF0844C76794C3015FE5E9A5DD210621C0FD037882476A207292E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/56_ZqSPbTfqi0uEF3KmrrA/zh-cn_image_0000002537174154.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F03A5DF53E83A8A9902C5C8D937CD0EFC098E9C159343E51499D1A34A8C9F547) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/737zJF9cStG8kkTUbJfe_A/zh-cn_image_0000002537334074.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=E8DF8FDEBD9C65B178314CBF88BF90313392989C766D2DA1599F48397742AE77) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/O5itD47KQwuX7L8C7nN4DA/zh-cn_image_0000002568173869.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F9F5131CF411FA5D65CDE7E1244D57270427B2DDF998221A25A95699A8E58D21) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fZP982pIRW-VEVRWC7kaxw/zh-cn_image_0000002568253865.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=41DD726492E20972C65A879F70ACE003B6414E851963DB33D98E3CF9FBD39C94) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/voJ6Yc-xQ6WddXfpcXOVSA/zh-cn_image_0000002537174156.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=0D600DDA0367DFA8D277695B18AEC4DCD9EC69C6963DBDA4EDFC8D794AA2275A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2sx--GfXTIW2ufYOsqhaNw/zh-cn_image_0000002537334076.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=D46067D279A5585F73419B95575D4D07F34354CA498B3AA130471876637F34D8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/XXVkFdnDT5aPk-G4TGHu4w/zh-cn_image_0000002568173871.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=EE37AE55AA816F1381E89851EB0B7A79FAF84E3A42AC8EA0407EA189B212ECAD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/bEzT4kdnQHKyr5apz9vNOA/zh-cn_image_0000002568253867.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=3D3D8A66D78C96558FE1B7930CDBC3E186E998DB15E30116C8725B14BC543BE5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1vE-8e1yRWCH0uh27DATSw/zh-cn_image_0000002537174158.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=153299337A125973BD200C4D226C761D70967D456D6C38C7327D5B51348BD09C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/dKum298pQ1aDnowty4eftw/zh-cn_image_0000002537334078.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=8C24ADC82C2AE609DEB2CF10AF54B7ED7C1FADE3B423E02A0E98F225DA4F1C6F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/pNoJQo4-QKmLSe5dQhNarw/zh-cn_image_0000002568173873.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=B961B8F7C03D1FED01DFBD7D85C032B443B3401C6A0F06D4513CB1AA0B334971) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/BpsE6ro4RpGAlWA5a7VvJA/zh-cn_image_0000002568253869.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=02F7F00B8B1ED59DE5A971101A3BF64F570EA52608FA1B162F942A8E55DC506B) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/vxPajUIER6iM6VhD0z3mIw/zh-cn_image_0000002537174160.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=F4CDBDBE7004CF665BAD9E815F04D390AF5319A1C9E2CF484C878976EE50FB73) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/PDu_Eg9XT4KeiD0q8g0Lcg/zh-cn_image_0000002537334080.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=ACB13B2507C87D94ACB3091F0B99D3668FD8885004AAF344358BE45C348D6D59) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Nqg22YE0QP-DR0VZ9Euz2Q/zh-cn_image_0000002568173875.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=AD86D2AFA8FCDE5715A6BA4A078E829B4D4B3EA719D702E5E1C8D02DF989EA3E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/g6jssnTeTZ27v_viCVI2GA/zh-cn_image_0000002568253871.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=77E8B7FFF06878BE47FE3F608554C3F1EF0A0203BEBCD9EF89310417C3FA9122) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/vOQgazStSSu1iwGr7C55fw/zh-cn_image_0000002537174162.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=EFAF75210EF899FE053F196EDB5C8720AB152E7C91D72928473963ABC9FB2BCD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/v3LFpuSTQjCfTYBSJ_lXbA/zh-cn_image_0000002537334082.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=4F7CF0196D71BFE925E1DD2D125837F2484EBC31C4022FC24B034B3239A49DD7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Xb-YjBxBTvmbw8I932BeAQ/zh-cn_image_0000002568173877.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=1F606C3A699DA4F8CF8F7E05D90C2D81D28785644770A814B37DB1436BD20236) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/AL8ClguYTbaUvnc03WRI7Q/zh-cn_image_0000002568253873.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=51AB038C1E6D564AF3C726D196662A231E7FB753B6C1F7DCF69EEDCBA9C637BB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/FjPF_3tFRo2TavwqNGMKmQ/zh-cn_image_0000002537174164.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=2D5F092D910B3335A2BAD8E2F4DBFCA18C51D426270A815004562706EFC56585) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/hBncQdqfSEaawgGj97l4tw/zh-cn_image_0000002537334084.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=2B8985275F2F5FF4F26D15D35B4E8CD4E1CB75691DC83CED56975A4B79EEBF01) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/fZoVOIs3T0CUlXset27PgQ/zh-cn_image_0000002568173879.png?HW-CC-KV=V1&HW-CC-Date=20260409T024030Z&HW-CC-Expire=86400&HW-CC-Sign=93712012EB1C325484D32408D2E143E9A23145721292555A20B6E8E56102FBB3) |
