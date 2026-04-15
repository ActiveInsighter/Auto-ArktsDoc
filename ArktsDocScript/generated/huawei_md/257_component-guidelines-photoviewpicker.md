# 使用PhotoPicker组件访问图片/视频
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-photoviewpicker

当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。

界面效果如图所示。

| 宫格页 | 大图页 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/PqCvjLMuRn-l8MBq9nejgA/zh-cn_image_0000002571292045.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T025150Z&HW-CC-Expire=86400&HW-CC-Sign=7A19CB7A7A2AE079CF2AA4DE068BD03B99D3961A4DE17FF42F5261EAA0D70325) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/JW-4tjQIQjaFeXA5ZxRN-w/zh-cn_image_0000002540612098.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T025150Z&HW-CC-Expire=86400&HW-CC-Sign=2675BD9296D765CC60F4F371C2187FDD32B45E759E85CF7F1336F4EE573DA8E0) |

## 开发步骤

1. 导入PhotoPicker模块文件。 ```typescript import {  PhotoPickerComponent,  PickerController,  PickerOptions,  DataType,  BaseItemInfo,  ItemInfo,  PhotoBrowserInfo,  ItemType,  ClickType,  MaxCountType,  PhotoBrowserRange,  ReminderMode,  photoAccessHelper } from '@kit.MediaLibraryKit'; ```
2. 创建Picker组件配置选项实例（PickerOptions）和控制实例（PickerController）。 通过PickerOptions，开发者可配置Picker宫格的样式（如勾选框背景色、文本颜色等）、滑动预览方向、最大选择数量等参数，详见[PickerOptions API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#pickeroptions)。 通过PickerController，应用可向Picker组件发送数据。 ```typescript pickerOptions: PickerOptions = new PickerOptions(); @State pickerController: PickerController = new PickerController(); @State selectUris: Array<string> = new Array<string>(); @State currentUri: string = ''; @State isBrowserShow: boolean = false; ```
3. 应用界面出现时，初始化组件配置选项实例（PickerOptions）。 此处仅列举实例用到的参数，当前支持的配置项及其取值范围详见[PickerOptions API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#pickeroptions)。 ```typescript this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE; this.pickerOptions.maxSelectNumber = 5; this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST; this.pickerOptions.isSearchSupported = true; this.pickerOptions.isPhotoTakingSupported = true; ```
4. 实现回调函数。 通过实现以下回调事件，可在用户在界面操作时，将相关信息报给应用进行处理。 - 进退大图、切换大图回调，上报的大图相关信息详见[PhotoBrowserInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#photobrowserinfo)。 - 勾选图片/视频，将上报图片URI供应用使用。 > **说明** > - 回调返回的所有URI均为只读URI，开发者可以根据结果集中的URI读取文件数据。但不能在Picker的回调中直接使用此URI打开文档，需要定义一个全局变量保存URI，样例可参考[指定URI读取文件数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri读取文件数据)、[指定URI获取图片或视频资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)。 > - 如需获取元数据，可通过[文件管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)和[文件URI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri)接口，根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。 - 点击图片（缩略图item），将上报图片/视频信息[ItemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#iteminfo)； - 点击相机item，可默认拉起系统相机或应用自行处理。如何自行拉起相机请参考[cameraPicker.pick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camerapicker#camerapickerpick)。 支持的回调事件及其参数请参考[PhotoPickerComponent API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#photopickercomponent)。 ```typescript private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {  if (!itemInfo) {  return false;  }  let type: ItemType | undefined = itemInfo.itemType;  let uri: string | undefined = itemInfo.uri;  if (type === ItemType.CAMERA) {  return true;  } else {  if (clickType === ClickType.SELECTED) {  if (uri) {  this.selectUris.push(uri);  this.pickerOptions.preselectedUris = [...this.selectUris];  }  return true;  } else {  if (uri) {  this.selectUris = this.selectUris.filter((item: string) => {  return item != uri;  });  this.pickerOptions.preselectedUris = [...this.selectUris];  }  return true;  }  } } private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {  this.isBrowserShow = true;  return true; } private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {  this.isBrowserShow = false;  return true; } private onPickerControllerReady(): void {  let elements: number[] = [PhotoBrowserUIElement.BACK_BUTTON];  this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); } private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {  this.currentUri = browserItemInfo.uri ?? '';  return true; } private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void { } private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void { } private onCurrentAlbumDeleted(): void { } ```
5. 创建[PhotoPickerComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#photopickercomponent)组件。 ```typescript PhotoPickerComponent({  pickerOptions: this.pickerOptions,  onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),  onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),  onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),  onPickerControllerReady: (): void => this.onPickerControllerReady(),  onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),  onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),  onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),  onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),  pickerController: this.pickerController, }) ```
6. 通过PickerController向Picker组件发送数据，实现控制PhotoPickerComponent组件行为。 存在多种用法，详见[PickerController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#pickercontroller)API文档。

## 完整示例

```typescript
import {
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  DataType,
  BaseItemInfo,
  ItemInfo,
  PhotoBrowserInfo,
  ItemType,
  ClickType,
  MaxCountType,
  PhotoBrowserRange,
  ReminderMode,
  photoAccessHelper
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct PhotoPickerComponentDemo {

  pickerOptions: PickerOptions = new PickerOptions();

  @State pickerController: PickerController = new PickerController();

  @State selectUris: Array<string> = new Array<string>();

  @State currentUri: string = '';

  @State isBrowserShow: boolean = false;

  aboutToAppear() {

    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;

    this.pickerOptions.maxSelectNumber = 5;

    this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;

    this.pickerOptions.isSearchSupported = true;

    this.pickerOptions.isPhotoTakingSupported = true;
  }

  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {

      return true;
    } else {

      if (clickType === ClickType.SELECTED) {

        if (uri) {
          this.selectUris.push(uri);
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }

        return true;
      } else {

        if (uri) {
          this.selectUris = this.selectUris.filter((item: string) => {
            return item != uri;
          });
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }

        return true;
      }
    }
  }

  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = true;
    return true;
  }

  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = false;
    return true;
  }

  private onPickerControllerReady(): void {
  }

  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }

  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
  }

  private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
  }

  private onCurrentAlbumDeleted(): void {
  }

  build() {
    Flex({
      direction: FlexDirection.Column,
      alignItems: ItemAlign.Start
    }) {
      PhotoPickerComponent({
        pickerOptions: this.pickerOptions,
        onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
        onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
        onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
        onPickerControllerReady: (): void => this.onPickerControllerReady(),
        onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
        onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
        onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
        onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
        pickerController: this.pickerController,
      })

      if (this.isBrowserShow) {

        Row() {
          ForEach(this.selectUris, (uri: string) => {
            if (uri === this.currentUri) {
              Image(uri).height(50).width(50)
                .onClick(() => {
                })
                .borderWidth(1)
                .borderColor('red')
            } else {
              Image(uri).height(50).width(50).onClick(() => {
                this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);

                this.pickerController.setPhotoBrowserItem(uri, PhotoBrowserRange.ALL);
              })
            }
          }, (uri: string) => JSON.stringify(uri))
        }.alignSelf(ItemAlign.Center).margin(this.selectUris.length ? 10 : 0)
      } else {

        Button('预览').width('33%').alignSelf(ItemAlign.Start).height('5%').margin(10).onClick(() => {
          if (this.selectUris.length > 0) {

            this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
          }
        })
      }
    }
  }
}
```
