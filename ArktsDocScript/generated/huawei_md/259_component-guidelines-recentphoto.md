# 使用RecentPhoto组件获取最近一张图片
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-recentphoto

应用可以在布局中嵌入最近图片组件，通过此组件，应用无需申请权限，即可指定配置访问公共目录中最近的一个图片或视频文件。授予的权限仅包含只读权限。

界面效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/jkxJnpJ_RByiD6bHpzWavw/zh-cn_image_0000002535948970.png?HW-CC-KV=V1&HW-CC-Date=20260405T025137Z&HW-CC-Expire=86400&HW-CC-Sign=A2F051FAF41F3428ABF982E4BF35E24C5DF3639AA85E75EBB01A9C72D2FDC416)

## 开发步骤

1. 导入最近图片组件模块文件。 ```typescript import { BaseItemInfo } from '@ohos.file.PhotoPickerComponent'; import {  PhotoSource,  RecentPhotoComponent,  RecentPhotoOptions,  photoAccessHelper } from '@kit.MediaLibraryKit'; ```
2. 创建最近图片组件选择选项实例（RecentPhotoOptions）。 通过RecentPhotoOptions，开发者可配置显示多长时间段内的图片、文件类型、文件内容来源，详见[RecentPhotoOptions API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-recentphotocomponent#recentphotooptions)。 ```typescript recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions(); ```
3. 初始化最近图片组件选择选项实例（RecentPhotoOptions）。 ```typescript this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE; this.recentPhotoOptions.period = 0; this.recentPhotoOptions.photoSource = PhotoSource.ALL; ```
4. 创建[RecentPhotoComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-recentphotocomponent#recentphotocomponent)组件。 ```typescript RecentPhotoComponent({  recentPhotoOptions: this.recentPhotoOptions,  onRecentPhotoClick: (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo),  onRecentPhotoCheckResult: (recentPhotoExists: boolean) => this.onReceiveCheckResult(recentPhotoExists), }) ```
5. 实现相关回调。 实现onReceiveCheckResult回调，可查询是否存在最近图片，仅返回true时才可进一步实现控制是否显示最近图片。 实现onRecentPhotoClick回调，将上报返回图片/视频相关信息[BaseItemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent#baseiteminfo)。 ```typescript private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {  if (!recentPhotoInfo) {  return false;  }  return true; } private onReceiveCheckResult(recentPhotoExists: boolean): void {  if (!recentPhotoExists) {  console.info('not exist recent photo');  } } ```

## 完整示例

完整示例请查阅[示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-recentphotocomponent#示例)。
