# 使用AlbumPicker组件访问相册列表
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-albumpicker

开发者可以在布局中嵌入AlbumPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的相册列表。

需配合[使用PhotoPicker组件访问图片/视频](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-photoviewpicker)一起使用，用户通过AlbumPickerComponent组件选择对应相册并通知PhotoPickerComponent组件刷新成对应相册的图片和视频。

界面效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/2j4e3VhCTUCEH14bJ9GuRQ/zh-cn_image_0000002537333468.png?HW-CC-KV=V1&HW-CC-Date=20260409T024132Z&HW-CC-Expire=86400&HW-CC-Sign=F0D478EF18C8F9F13B833B93C2A1137B9390B747CE91028A931C7F476876DA7D)

## 开发步骤

1. 导入相册组件模块文件。 ```typescript import {  AlbumPickerComponent,  AlbumPickerOptions,  AlbumInfo,  PickerColorMode,  PickerController,  DataType } from '@kit.MediaLibraryKit'; ```
2. 创建相册组件配置选项实例（AlbumPickerOptions）。 通过AlbumPickerOptions，开发者可配置相册页主题颜色，详见[AlbumPickerOptions API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-albumpickercomponent#albumpickeroptions)。 ```typescript albumOptions: AlbumPickerOptions = new AlbumPickerOptions(); pickerController: PickerController = new PickerController(); ```
3. 初始化组件配置选项实例（AlbumPickerOptions）。 ```typescript this.albumOptions.themeColorMode = PickerColorMode.AUTO; ```
4. 创建[AlbumPickerComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-albumpickercomponent#albumpickercomponent)组件。 ```typescript AlbumPickerComponent({  albumPickerOptions: this.albumOptions,  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo), }) ```
5. 与PhotoPicker组件联动，将相册URI给到应用，根据相册URI更新PhotoPicker组件宫格页内容。 ```typescript private onAlbumClick(albumInfo: AlbumInfo): boolean {  if (albumInfo?.uri) {  this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);  }  return true; } ```

## 完整示例

```typescript
import {
  PhotoPickerComponent,
  AlbumPickerComponent,
  AlbumPickerOptions,
  AlbumInfo,
  PickerColorMode,
  PickerController,
  DataType
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct AlbumPage {
  @State pickerController: PickerController = new PickerController();
  @State Width: string = '100%';
  @State Height: string = '100%';
  @State isShowAlbum: boolean = false;
  @State fontColor: string = '#182431222'
  @State selectedFontColor: string = '#007DFF'
  @State currentIndex: number = 0
  private controller: TabsController = new TabsController();
  albumOptions = new AlbumPickerOptions();
  albumOptions1 = new AlbumPickerOptions();
  albumOptions2 = new AlbumPickerOptions();

  private onAlbumClick(albumInfo: AlbumInfo): boolean {
    this.isShowAlbum = false;
    if (albumInfo?.uri) {

      this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);
    }
    return true;
  }

  aboutToAppear() {

    this.albumOptions.themeColorMode = PickerColorMode.AUTO;
    this.albumOptions1.themeColorMode = PickerColorMode.LIGHT;
    this.albumOptions2.themeColorMode = PickerColorMode.DARK;
  }

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('100%')
  }

  build() {
    Stack() {
      Column() {
        Row() {
          Button("全部相册").width('95%').height('5%').onClick(() => {
            this.isShowAlbum = true;
          })
        }.margin({ top: 40 })
        Column() {
          PhotoPickerComponent({
            pickerController: this.pickerController,
          }).height(this.Height).width(this.Width)
        }.width('100%').height('100%').alignItems(HorizontalAlign.Center).visibility(this.isShowAlbum ? Visibility.None: Visibility.Visible)
      }

      if (this.isShowAlbum) {
        Row() {
          Column() {

            Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(0, '系统'))
              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions1,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(1, '浅色'))

              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions2,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(2, '深色'))
            }
            .vertical(false)
            .barMode(BarMode.Fixed)
            .barWidth('100%')
            .barHeight(56)
            .animationDuration(100)
            .onChange((index: number) => {
              this.currentIndex = index;
            })
            .width('100%')
            .height('100%')
            .backgroundColor('#F1F3F5')
          }.width('100%').height('100%').justifyContent(FlexAlign.Center).alignItems(HorizontalAlign.Center)
        }
        .margin({ top: 40 })
      }
    }
  }
}
```
