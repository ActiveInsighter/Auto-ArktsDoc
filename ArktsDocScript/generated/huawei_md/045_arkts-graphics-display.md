# 显示图片 (Image)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display

开发者经常需要在应用中显示一些图片，例如：按钮中的icon、网络图片、本地图片等。在应用中显示图片需要使用Image组件实现，Image支持多种图片格式，包括png、jpg、jpeg等格式，不支持apng和svga格式，具体支持格式和用法请参考[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)组件。

Image通过调用接口来创建，接口调用形式如下：

```typescript
Image(src: PixelMap | ResourceStr | DrawableDescriptor)
```

该接口通过图片数据源获取图片，支持本地图片和网络图片的渲染展示。其中，src是图片的数据源，加载方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。

如果图片加载过程中出现白色块，请参考[Image白块解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution)。如果图片加载时间过长，请参考[预置图片资源加载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance)。

## 加载图片资源

Image支持加载存档图、多媒体像素图和可绘制描述符三种类型。

### 存档图类型数据源

存档图类型的数据源可以分为本地资源、网络资源、Resource资源、媒体库资源和base64。

- 本地资源 创建文件夹，将本地图片放入ets文件夹下的任意位置。 Image组件引入本地图片路径，即可显示图片（根目录为ets文件夹）。不支持跨包、跨模块调用该Image组件。 > **说明** > 从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使相关模块：build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356)相关介绍。 ```typescript Image('images/view.jpg')  .width(200) ``` 加载本地图片过程中，如果对图片进行修改或者替换，可能会引起应用崩溃。因此需要覆盖图片文件时，应该先删除该文件再重新创建一个同名文件。
- 网络资源 引入网络图片需申请权限ohos.permission.INTERNET，具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。此时，Image组件的src参数为网络图片的链接。 当前Image组件仅支持加载简单网络图片。 首次加载网络图片时，Image组件需要请求网络资源；非首次加载时，默认从缓存中直接读取图片。 更多图片缓存设置请参考[setImageCacheCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app#setimagecachecount7)、[setImageRawDataCacheSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app#setimagerawdatacachesize7)和[setImageFileCacheSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app#setimagefilecachesize7)。这三个图片缓存接口主要用于支持简单、通用的场景，后续不再继续演进，且在灵活和扩展性方面存在一定限制，例如： - 无法获取当前缓存占用信息。Image组件目前不支持查询磁盘缓存的实时状态，包括文件总大小和文件数量。 - 缓存策略不可定制，缺乏缓存状态观测能力。开发者无法通过接口感知缓存命中率、淘汰次数等运行时的指标，难以基于实际缓存效果进行动态调优。 对于复杂情况，推荐使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)，该图像库提供了更灵活、可扩展的缓存策略以及完善的生命周期管理能力，更适合复杂业务需求。 网络图片必须支持RFC 9113标准，否则会导致加载失败。如果下载的网络图片大于10MB或一次下载的网络图片数量较多，建议使用[HTTP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request)工具提前下载，提高图片加载性能，方便应用侧管理数据。 在显示网络图片时，Image组件在机制上会依赖[缓存下载模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request-cachedownload)，开发者可参考[示例3（下载与显示网络gif图片）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例3下载与显示网络gif图片)了解具体用法。 缓存下载模块提供独立的预下载接口，允许应用开发者在创建Image组件前预下载所需图片。组件创建后，Image组件可直接从缓存下载模块中获取已下载的图片数据，从而加快图片的显示速度，优化加载体验，并有效避免网络图片加载延迟。网络缓存的位置位于应用根目录下的cache目录中。 ```typescript Image($r('app.string.LoadingResources')) ```
- Resource资源 使用资源格式可以跨包/跨模块引入图片，resources文件夹下的图片都可以通过$r资源接口读取到并转换到Resource格式。 **图1** resources ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kU6nfIrVR1iFUxVlUsaFdw/zh-cn_image_0000002565290269.jpg?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=0E881541264DF000703CDC46E3FE825B270B262BF018A0036257F8319F156D3D) 调用方式： ```typescript Image($r('app.media.icon')) ``` 还可以将图片放在rawfile文件夹下。 **图2** rawfile ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/79mo_OrFTJCpQ3HKnmhvrg/zh-cn_image_0000002565210249.jpg?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=3E42FD031DEDE78479B3AEF9DF9B2E7FA02F38C0FE7A17B0FD513FF2FDCF33B4) 调用方式： ```typescript Image($rawfile('example1.png')) ```
- 媒体库file://data/storage 支持file://路径前缀的字符串，用于访问通过[选择器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker)提供的图片路径。 1. 调用接口获取图库的照片url。 ```typescript import { photoAccessHelper } from '@kit.MediaLibraryKit'; import { BusinessError } from '@kit.BasicServicesKit'; import { hilog } from '@kit.PerformanceAnalysisKit'; const DOMAIN = 0x0001; const TAG = 'Sample_imagecomponent'; @Entry @Component struct MediaLibraryFile { @State imgDatas: string[] = []; getAllImg() { try { let photoSelectOptions:photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions(); photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; photoSelectOptions.maxSelectNumber = 5; let photoPicker:photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker(); photoPicker.select(photoSelectOptions).then((photoSelectResult:photoAccessHelper.PhotoSelectResult) => { this.imgDatas = photoSelectResult.photoUris; hilog.info(DOMAIN, TAG,'PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult)); }).catch((err:Error) => { let message = (err as BusinessError).message; let code = (err as BusinessError).code; hilog.info(DOMAIN, TAG,`PhotoViewPicker.select failed with. Code: ${code}, message: ${message}`); }); } catch (err) { let message = (err as BusinessError).message; let code = (err as BusinessError).code; hilog.info(DOMAIN, TAG,`PhotoViewPicker failed with. Code: ${code}, message: ${message}`); }; }; async aboutToAppear() { this.getAllImg(); }; build() { Column() { Grid() { ForEach(this.imgDatas, (item:string) => { GridItem() { Image(item) .width(200) } }, (item:string):string => JSON.stringify(item)) } }.width('100%').height('100%') } } ``` 2. 从媒体库获取的url格式通常如下。 ```typescript Image('file://media/Photos/5') .width(200) ```
- base64 路径格式为data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。 Base64格式字符串可用于存储图片的像素数据，在网页上使用较为广泛。

### 多媒体像素图

PixelMap是图片解码后的像素图，具体用法请参考[Image Kit简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview)。以下示例将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上。

```typescript
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'Sample_imagecomponent';

@Entry
@Component
struct HttpExample {
  outData: http.HttpResponse | undefined = undefined;
  code: http.ResponseCode | number | undefined = undefined;
  @State image: PixelMap | undefined = undefined;

  aboutToAppear(): void {
    http.createHttp().request('xxx://xxx.xxx.xxx/example.png',
      (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          hilog.error(DOMAIN, TAG, `hello http request failed. Code: ${error.code}, message: ${error.message}`);
          return;
        };
        this.outData = data;

        if (http.ResponseCode.OK === this.outData.responseCode) {
          let imageData: ArrayBuffer = this.outData.result as ArrayBuffer;
          let imageSource: image.ImageSource = image.createImageSource(imageData);
          let options: image.DecodingOptions = {
            'desiredPixelFormat': image.PixelMapFormat.RGBA_8888,
          };
          imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
            this.image = pixelMap;
          });
        };
      });
  };

  build() {
    Column() {

      Image(this.image)
        .height(100)
        .width(100)
    }
  }
}
```

### 可绘制描述符

DrawableDescriptor是ArkUI提供的一种高级图片抽象机制，它通过将图片资源封装为可编程对象，实现了传统Image组件难以实现的动态组合与运行时控制功能。开发者可利用它实现图片的分层叠加（如徽章图标）、动态属性调整（如颜色滤镜）、复杂动画序列等高级效果，适用于需要灵活控制图片展现或实现复杂视觉交互的场景。详细使用方法，请参考[DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor)。

通过DrawableDescriptor显示图片及动画的示例如下所示：

```typescript
import {
  DrawableDescriptor,
  PixelMapDrawableDescriptor,
  LayeredDrawableDescriptor,
  AnimatedDrawableDescriptor,
  AnimationOptions
} from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct DrawableDescriptorType {

  @State pixmapDesc: DrawableDescriptor | null = null;
  @State pixelMapDesc: PixelMapDrawableDescriptor | null = null;
  @State layeredDesc: LayeredDrawableDescriptor | null = null;
  @State animatedDesc: AnimatedDrawableDescriptor | null = null;

  private animationOptions: AnimationOptions = {
    duration: 3000,
    iterations: -1
  };

  async aboutToAppear() {
    const resManager = this.getUIContext().getHostContext()?.resourceManager;
    if (!resManager) {
      return;
    };

    let pixmapDescResult = resManager.getDrawableDescriptor($r('app.media.landscape').id);
    if (pixmapDescResult) {
      this.pixmapDesc = pixmapDescResult as DrawableDescriptor;
    };

    const pixelMap = await this.getPixmapFromMedia($r('app.media.landscape'));
    this.pixelMapDesc = new PixelMapDrawableDescriptor(pixelMap);

    const foreground = await this.getDrawableDescriptor($r('app.media.foreground'));

    const background = await this.getDrawableDescriptor($r('app.media.landscape'));
    this.layeredDesc = new LayeredDrawableDescriptor(foreground, background);

    const frame1 = await this.getPixmapFromMedia($r('app.media.sky'));

    const frame2 = await this.getPixmapFromMedia($r('app.media.landscape'));

    const frame3 = await this.getPixmapFromMedia($r('app.media.clouds'));
    if (frame1 && frame2 && frame3) {
      this.animatedDesc = new AnimatedDrawableDescriptor([frame1, frame2, frame3], this.animationOptions);
    };
  };

  private async getPixmapFromMedia(resource: Resource): Promise<image.PixelMap | undefined> {
    const unit8Array = await this.getUIContext().getHostContext()?.resourceManager.getMediaContent(resource.id);
    if (!unit8Array) {
      return undefined;
    };
    const imageSource = image.createImageSource(unit8Array.buffer.slice(0, unit8Array.buffer.byteLength));
    const pixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return pixelMap;
  };

  private async getDrawableDescriptor(resource: Resource): Promise<DrawableDescriptor | undefined> {
    const resManager = this.getUIContext().getHostContext()?.resourceManager;
    if (!resManager) {
      return undefined;
    };
    return (resManager.getDrawableDescriptor(resource.id)) as DrawableDescriptor;
  };

  build() {
    RelativeContainer() {
      Column() {

        Image(this.pixmapDesc)
          .width(100)
          .height(100)
          .border({ width: 1, color: Color.Black })

        Image(this.pixelMapDesc)
          .width(100)
          .height(100)
          .border({ width: 1, color: Color.Red })

        if (this.layeredDesc) {
          Image(this.layeredDesc)
            .width(100)
            .height(100)
            .border({ width: 1, color: Color.Blue })
        }

        if (this.animatedDesc) {
          Image(this.animatedDesc)
            .width(200)
            .height(200)
            .margin({ top: 20 })
        }
      }
    }
    .height('100%')
    .width('100%')
    .margin(50)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ltTdHQC9TTOnnHFWsLAX7w/zh-cn_image_0000002534250426.gif?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=ED862EB0E250DFB09D77DDC5720AB0F50537B446870060909F16154AA0AC1772)

## 显示矢量图

Image组件可显示矢量图（SVG格式的图片），SVG标签文档请参考[SVG标签说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg)。

如果SVG图片没有原始大小，需要给Image组件设置宽高，否则不显示。SVG图片不支持通过image标签引用SVG格式和gif格式的本地其他图片。

SVG格式的图片可以使用fillColor属性改变图片的绘制颜色。

```typescript
Image($r('app.media.cloud'))
  .width(50)
  .fillColor(Color.Blue)
```

**图3** 原始图片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/rJof3puaS26NGGYRLupAQA/zh-cn_image_0000002534410372.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=4CD81437847E8F909B39FD76B590C4EC2B02D2DA8FCD9379CA0242D44B5E0017)

**图4** 设置绘制颜色后的SVG图片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/La-VC0hMSYe5o7gK934l7w/zh-cn_image_0000002565290271.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=69E84D1E0D35AB5E96879AE2F99BF3DDD44734178570E2487DDBFBAA15E07A3F)

### 矢量图引用位图

如果Image加载的SVG图源中包含对本地位图的引用，则SVG图源的路径应当设置为以ets为根目录的工程路径，同时，本地位图的路径应设置为与SVG图源同级的相对路径。

Image加载的SVG图源路径设置方法如下所示：

```typescript
Image('/images/icon.svg')
  .width(50)
  .height(50)
```

SVG图源通过<image>标签的xlink:href属性指定本地位图路径，本地位图路径设置为跟SVG图源同级的相对路径：

```typescript
<svg width="200" height="200">
  <image width="200" height="200" xlink:href="sky.png"></image>
</svg>
```

文件工程路径示例如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/mgbP443-RDG1eAx2Ai9GmA/zh-cn_image_0000002565210251.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=4C4FF5903083B10276592AC4E74CB9C231466D9AA4F363C5E78A8B34120F8CE6)

## 添加属性

给Image组件设置属性可以使图片显示更灵活，达到一些自定义的效果。以下是几个常用属性的使用示例，完整属性信息详见[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)。

### 设置图片缩放类型

通过设置[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#objectfit)属性，可以使图片在高度和宽度确定的框内进行缩放。

```typescript
@Entry
@Component
struct ImageScalingType {
  scroller: Scroller = new Scroller();

  build() {
    Scroll(this.scroller) {
      Row() {
        Column() {

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.Contain)
            .margin({bottom:25,left:10})

            .overlay('Contain', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.Cover)
            .margin({bottom:25,left:10})

            .overlay('Cover', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.Auto)
            .margin({bottom:25,left:10})

            .overlay('Auto', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }

        Column() {

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.Fill)
            .margin({bottom:25,left:10})

            .overlay('Fill', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.ScaleDown)
            .margin({bottom:25,left:10})

            .overlay('ScaleDown', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.img_2'))
            .width(200)
            .height(150)
            .border({ width: 1 })

            .objectFit(ImageFit.None)
            .margin({bottom:25,left:10})

            .overlay('None', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/KRymlvrRSB2LkflxMNrhAg/zh-cn_image_0000002534250428.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=379C526ABC99DC47A3E008CB1723BAA5CC9F05176D724605192B55370931C40D)

### 图片插值

当原图分辨率较低并放大显示时，图片会变得模糊并出现锯齿。这时可以使用[interpolation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#interpolation)属性对图片进行插值，以提高显示清晰度。

```typescript
@Entry
@Component
struct ImageInterpolationType {
  build() {
    Column() {
      Row() {

        Image($r('app.media.grass'))
          .width('40%')

          .interpolation(ImageInterpolation.None)
          .borderWidth(1)

          .overlay('Interpolation.None', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)

        Image($r('app.media.grass'))
          .width('40%')

          .interpolation(ImageInterpolation.Low)
          .borderWidth(1)

          .overlay('Interpolation.Low', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)

      Row() {

        Image($r('app.media.grass'))
          .width('40%')

          .interpolation(ImageInterpolation.Medium)
          .borderWidth(1)

          .overlay('Interpolation.Medium', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)

        Image($r('app.media.grass'))
          .width('40%')

          .interpolation(ImageInterpolation.High)
          .borderWidth(1)

          .overlay('Interpolation.High', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/S1jvm9TdTH2A9l-Alv_kfQ/zh-cn_image_0000002534410374.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=FC2011FCC89BD88DBF7EC94CBC9B3779C3BCA5DAC2CA23254600FC191119BD6D)

### 设置图片重复样式

通过objectRepeat属性设置图片的重复样式方式，重复样式请参考[ImageRepeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagerepeat)枚举说明。

```typescript
@Entry
@Component
struct ImageRepetitionStyle {
  build() {
    Column({ space: 10 }) {
      Column({ space: 25 }) {

        Image($r('app.media.ic_public_favor_filled_1'))
          .width(160)
          .height(160)
          .border({ width: 1 })

          .objectRepeat(ImageRepeat.XY)
          .objectFit(ImageFit.ScaleDown)

          .overlay('ImageRepeat.XY', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

        Image($r('app.media.ic_public_favor_filled_1'))
          .width(160)
          .height(160)
          .border({ width: 1 })

          .objectRepeat(ImageRepeat.Y)
          .objectFit(ImageFit.ScaleDown)

          .overlay('ImageRepeat.Y', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

        Image($r('app.media.ic_public_favor_filled_1'))
          .width(160)
          .height(160)
          .border({ width: 1 })

          .objectRepeat(ImageRepeat.X)
          .objectFit(ImageFit.ScaleDown)

          .overlay('ImageRepeat.X', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
    }.height(150).width('100%').padding(8)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/JV2yl0edRBWIUe3Kda_-gg/zh-cn_image_0000002565290273.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=6F97B325FB7ECE090CEAB0D98133D40E523DD1FF0AB7727A7B48037C9C3F1BDB)

### 设置图片渲染模式

通过renderMode属性设置图片的渲染模式为原色或黑白。

```typescript
@Entry
@Component
struct SetImageRenderingMode {
  build() {
    Column({ space: 10 }) {
      Row({ space: 50 }) {

        Image($r('app.media.example'))

          .renderMode(ImageRenderMode.Original)
          .width(100)
          .height(100)
          .border({ width: 1 })

          .overlay('Original', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

        Image($r('app.media.example'))

          .renderMode(ImageRenderMode.Template)
          .width(100)
          .height(100)
          .border({ width: 1 })

          .overlay('Template', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
    }.height(150).width('100%').padding({ top: 20,right: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/0MdsgbphROycgqMxhOat1g/zh-cn_image_0000002565210253.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=DF4F2B066119F69E4F155F4B22DB1BC0482ADC8B2D8403B7C1E4CF2A439C34C0)

### 设置图片解码尺寸

通过sourceSize属性设置图片解码尺寸，降低图片的分辨率。

原图尺寸为1280×960，该示例将图片解码为40×40和90×90两个尺寸。

```typescript
@Entry
@Component
struct SetImageDecodingSize {
  build() {
    Column() {
      Row({ space: 50 }) {

        Image($r('app.media.example'))

          .sourceSize({
            width: 40,
            height: 40
          })
          .objectFit(ImageFit.ScaleDown)
          .aspectRatio(1)
          .width('25%')
          .border({ width: 1 })

          .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })

        Image($r('app.media.example'))

          .sourceSize({
            width: 90,
            height: 90
          })
          .objectFit(ImageFit.ScaleDown)
          .width(100)
          .height(100)
          .aspectRatio(1)
          .border({ width: 1 })

          .overlay('width:90 height:90', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
      }.height(150).width('100%').padding(20)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jKJg_ZH7QTS6tRkmFEEFGg/zh-cn_image_0000002534250430.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=C3CF79560E691672154EA31718579DB236D60AA1CE4B9638D2887EDCE2B6586E)

### 为图片添加滤镜效果

通过colorFilter调整图片的像素颜色，为图片添加滤镜。

```typescript
@Entry
@Component
struct AddFilterEffectsToImages {
  build() {
    Column() {
      Row() {

        Image($r('app.media.example'))
          .width('40%')
          .margin(10)

        Image($r('app.media.example'))
          .width('40%')

          .colorFilter(
             [1, 1, 0, 0, 0,
              0, 1, 0, 0, 0,
              0, 0, 1, 0, 0,
              0, 0, 0, 1, 0])
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/lwQDu7rRReC7sKlMMjBgKA/zh-cn_image_0000002534410376.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=2CB62EB05CD1E5033BC67E0DE3A9C2CD8529F6DE7CB37C3D4AF35BC99167BDA5)

### 同步加载图片

一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。但是特定情况下，图片刷新时会出现闪烁，这时可以使用syncLoad属性，使图片同步加载，从而避免出现闪烁。不建议图片加载较长时间时使用，会导致页面无法响应。

```typescript
Image($r('app.media.icon'))
  .syncLoad(true)
```

## 事件调用

通过在Image组件上绑定onComplete事件，图片加载成功后可以获取图片的必要信息。如果图片加载失败，也可以通过绑定onError回调来获得结果。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'Sample_imagecomponent';

@Entry
@Component
struct EventCall {
  @State widthValue: number = 0;
  @State heightValue: number = 0;
  @State componentWidth: number = 0;
  @State componentHeight: number = 0;

  build() {
    Column() {
      Row() {

        Image($r('app.media.ic_img_2'))
          .width(200)
          .height(150)
          .margin(15)

          .onComplete(msg => {
            if(msg){
              this.widthValue = msg.width;
              this.heightValue = msg.height;
              this.componentWidth = msg.componentWidth;
              this.componentHeight = msg.componentHeight;
            };
            hilog.info(DOMAIN, TAG, `${msg}`);
          })

          .onError(() => {
            hilog.info(DOMAIN, TAG, 'load image fail');
          })

          .overlay('\nwidth: ' + String(this.widthValue) + ', height: ' + String(this.heightValue) + '\ncomponentWidth: ' + String(this.componentWidth) + '\ncomponentHeight: ' + String(this.componentHeight), {
            align: Alignment.Bottom,
            offset: { x: 0, y: 60 }
          })
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/_BqZipBPSRWXbo28VVr17Q/zh-cn_image_0000002565290275.png?HW-CC-KV=V1&HW-CC-Date=20260331T024048Z&HW-CC-Expire=86400&HW-CC-Sign=C2AF82709CAFDA60FE7B33309A34CF02526F7C60873FB73D9D7318903491DEF6)
