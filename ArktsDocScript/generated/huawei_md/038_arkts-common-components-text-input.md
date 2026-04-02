# 文本输入 (TextInput/TextArea/Search)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)、[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)。

> **说明**
> 仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件。

## 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```typescript
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```typescript
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```typescript
Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

- 单行输入框。 ```typescript TextInput() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2n2JzCxAT5i0aaLeH7JZQg/zh-cn_image_0000002534250376.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=234701F55E835A55096835A6A498BDD35B636FC9CAFA7794A7DD7911FC6B6F95)
- 多行输入框。 ```typescript TextArea() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/cl65H_4PQXSgPeZu0JYUjA/zh-cn_image_0000002534410322.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=C727686584B48A512C00147A3696143D767DE5BEAF3593AC31426AC075738CC0)
- 多行输入框文字超出一行时会自动折行。 ```typescript TextArea({ text: $r('app.string.CreatTextInput_textContent') })  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/aASfHa8dSNWiGofej9N-EQ/zh-cn_image_0000002565290221.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=8714664E918480B83E4B178E31310706DEE8625A6CB9D3ED4C43972A40231FFA)
- 搜索框。 ```typescript Search()  .searchButton($r('app.string.Creat_TextInput_Content')) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/pcqvHFBmRqGSHTlOfk67Sw/zh-cn_image_0000002565210201.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=23772F9532F4E938E5CC4CB4979563374E06B853D1B413865288C5DC2B31D756)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

### 基本输入模式（默认类型）

```typescript
TextInput()
  .type(InputType.Normal)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Oi9ZNZwNRFiNeVqTKWguiQ/zh-cn_image_0000002534250378.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=A33859C0997CA7FB8568AC4CEBE0AF37537F2F1D2840F5D9438838A49911D191)

### 密码模式

包括Password密码输入模式、NUMBER_PASSWORD纯数字密码模式、NEW_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```typescript
TextInput()
  .type(InputType.Password)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/FPFHJea_TROowUodb0YeAQ/zh-cn_image_0000002534410324.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=F7911286B8998E78B87BE7C9F456BB5D99F333FB26F51ABFD9B44F8ADABB20E0)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```typescript
TextInput()
  .type(InputType.Email)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/BHp5XpbZSYuzmHEVrrHD8A/zh-cn_image_0000002565290223.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=517F49F3E25ED01DE2BF1F79916F242F909EAABA57B4C1480E918E65BA7551E6)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```typescript
TextInput()
  .type(InputType.Number)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/VSzMkPa_SQGvHsb30Yw06g/zh-cn_image_0000002565210203.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=C9CC73B02BD6EB74260C4DE9DB771BFD1F148A92A3F2E857D160037F43680407)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

```typescript
TextInput()
  .type(InputType.PhoneNumber)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/pGGJHs8DTgeIJyL4Rgc1GQ/zh-cn_image_0000002534250380.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=256E8DA3EA959E52BC6DE34D7D3C8687746F9300BA8009E1E545C42A5773A683)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```typescript
TextInput()
  .type(InputType.NUMBER_DECIMAL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/DpiB5-HZTxyzwjSoF3uy9A/zh-cn_image_0000002534410326.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=01DD08B028D00CA5425E51FA379929290DE6EE48B5E14DBD8938F5AB0B89DD85)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```typescript
TextInput()
  .type(InputType.URL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/woNux_l0TFCj76hflSjGAw/zh-cn_image_0000002565290225.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=F79E675759D3A6D4B3937E7B3034B72C3BD9AAB78D18167B0E14F35DC713DAD0)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```typescript
TextArea()
  .style(TextContentStyle.DEFAULT)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ElM9TUamS8aDSyzgXwUHgA/zh-cn_image_0000002565210205.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=E5867804B5F3925BB766CD6A05204326448EF1AB069A81C5E789A779BE1DA4E2)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```typescript
TextArea()
  .style(TextContentStyle.INLINE)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/hIdAuyxXRlGKSs3GL7Vj_Q/zh-cn_image_0000002534250382.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=62B0F922A7134FDB9946A16F8F8B9F8E6A1653CB2107AB8892E3855CE1ACCA90)

## 自定义样式

- 设置无输入时的提示文本。 ```typescript TextInput({ placeholder: $r('app.string.i_am_placeholder') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/YFzUFysWSfyRRgh9Ikg7wQ/zh-cn_image_0000002534410328.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=EB94020EC467D8605DEB7AECBA93E64C538B6E68AA9A718D5B198A2EA861408B)
- 设置输入框当前的文本内容。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/H2QD1A84TKeDKAK6ASt6YA/zh-cn_image_0000002565290227.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=97C1D0E9465C6D6227DDC96F56B1CC220E9254992D7F52D1EF275256B0277757)
- 添加backgroundColor改变输入框的背景颜色。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') })  .backgroundColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/6ZiASJwgSzuNHrxzkleIUg/zh-cn_image_0000002565210207.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=139DDE4BB6F6D22968A1669BB5FFFD7704393C37A2B27EA60AFF7AC465DF4EAD) 更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。

## 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

> **说明**
> 在密码模式下，设置[showPassword](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpassword12)属性时，在[onSecurityStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。
>
> [onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)回调仅支持系统输入法的场景。
>
> [onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)的回调时序晚于[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)，早于[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';

@Entry
@Component
struct TextInputEventAdd {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr2: string = '';
  @State textStr3: string = '';
  @State textStr4: string = '';
  @State textStr5: string = '';
  @State textStr6: string = '';
  @State textStr7: string = '';
  @State textStr8: string = '';
  @State textStr9: string = '';
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
          \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
          \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
          .fontSize(20)
          .width('70%')
        TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .type(InputType.Password)
          .showPassword(this.passwordState)
          .onChange((value: string) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
            this.textStr1 = `onChange is triggering: ${value}`;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
            this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
          })
          .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
            this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
          })
          .onSecurityStateChange((isShowPassword: boolean) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
            this.passwordState = isShowPassword;
            this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
          })
          .onWillInsert((info: InsertValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
            return true;
          })
          .onDidInsert((info: InsertValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
          })
          .onWillDelete((info: DeleteValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
          })
          .onFocus(() => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
            this.textStr9 = `onFocus is triggering`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vFoOpz5LTxilCh7k-3wZUQ/zh-cn_image_0000002534250384.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=166A06135ED84BADC0138D11F88D432E9B50D9F2A4F8A25AA7A37112E60CA508)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、搜索的菜单。

TextInput:

```typescript
TextInput({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/1vKvmFPSQiqMqcx2fQu-UA/zh-cn_image_0000002534410330.jpg?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=F1D28D1522B34D12AB062E4CE7CCA75CA689FAEF781FAA4DC9779F16E2A21CE9)

TextArea:

```typescript
TextArea({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/m15hydO2SX6eI7iSyMZubQ/zh-cn_image_0000002565290229.jpg?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=BF8F24A90EC00BE24D35869804BDD5ADFA4281DB39D9BBFA46ABF16C10FD5A9B)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableSystemServiceMenuItem {
  aboutToAppear(): void {

    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {

    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {

        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/O51aYxm0R2yqvdvW64bzgw/zh-cn_image_0000002565210209.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=1B1ADC6850F717958CA38BD37931171762A95E202B08EFCA1E11BB3D586AFB33)

从API version 20开始，支持使用[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableMenuItem {
  aboutToAppear(): void {

    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
  }

  aboutToDisappear(): void {

    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {

        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/w6L-DxS-QGu36ZPka0kx2A/zh-cn_image_0000002534250386.png?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=6264AAD9C88C32C748F7D33B7F05D4E1CAF1C05610CC53A2971FE879300E06E4)

## 自动填充

输入框可以通过[contentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12枚举说明)。

```typescript
TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
  .width('95%')
  .height(40)
  .margin(20)
  .contentType(ContentType.EMAIL_ADDRESS)
```

## 设置属性

- 设置省略属性。 输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。 ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。 ```typescript TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })  .textOverflow(TextOverflow.Ellipsis)  .ellipsisMode(EllipsisMode.END)  .style(TextInputStyle.Inline)  .fontSize(30)  .margin(30) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/43N7L8PaQ7m2UWYWgendQg/zh-cn_image_0000002534410332.jpg?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=921926D14D332DC346446F001A4412189E4A7D6B3F633BE981A8490C8300E44B)
- 设置文本描边属性。 从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。 ```typescript TextInput({ text: 'Text with stroke' })  .width('100%')  .height(60)  .borderWidth(1)  .fontSize(40)  .strokeWidth(LengthMetrics.px(3.0))  .strokeColor(Color.Red) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/XRJXi6Z9S2acUdqve-JfoA/zh-cn_image_0000002565290231.jpg?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=99B005A8D612F667CF0E6B69C0C34BB2B2CCB924EAE61093A67A26B74A878833)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```typescript
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/lT9wefRGTJOvoWDZWCeVog/zh-cn_image_0000002565210211.jpg?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=5674F372C3DBA56A265B22D6D3D5F2E95B5FE460437EB19484788D27A61E3D4B)

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)。

```typescript
@Entry
@Component
struct KeyboardAvoid {
  placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

  build() {
    Scroll() {
      Column() {
        ForEach(this.placeHolderArr, (placeholder: string) => {
          TextInput({ placeholder: 'TextInput ' + placeholder })
            .margin(30)

        })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_52lJdPJT5OHo1si2qnK0w/zh-cn_image_0000002534250388.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=263F66E6DD012E116E623060F305F41ED6621275589855E8D7C28DFA6310F4C8)

## 光标避让

[keyBoardAvoidMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET_WITH_CARET和RESIZE_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE_WITH_CARET，非滚动容器应该使用OFFSET_WITH_CARET。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { KeyboardAvoidMode } from '@kit.ArkUI';
```

```typescript
onWindowStageCreate(windowStage: window.WindowStage): void {

  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err, data) => {
    let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
    windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  });
}
```

```typescript
@Entry
@Component
struct CursorAvoid {
  @State caretPosition: number = 600;
  areaController: TextAreaController = new TextAreaController();
  text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
    ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy,' +
    ' totally forgetting that there is something happy in our own life.\
    So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
    'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
    If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
    'Happiness is just what you think will make you happy.' +
    'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
    'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
  ';

  build() {
    Scroll() {
      Column() {
        Row() {
          Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
            this.caretPosition += 1;
          }).fontSize(10)
          Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
            this.caretPosition -= 1;
          }).fontSize(10)
          Button('SetCaretPosition: ').onClick(() => {
            this.areaController.caretPosition(this.caretPosition);
          }).fontSize(10)
        }

        TextArea({ text: this.text, controller: this.areaController })
          .width('100%')
          .fontSize('20fp')
      }
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/S9Qy-ZbOSFu4El19XEabOw/zh-cn_image_0000002534410334.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=35834CC10AECAE601E8365D9787D9A922127DBE5A58B02078E2125D8B3BBF75D)

## 常见问题

### 如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)自行计算高度。

```typescript
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextExample {
  private textAreaPadding = 12;
  private setMaxLines = 3;
  private resourceManager = this.getUIContext().getHostContext()?.resourceManager;

  private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
  @State fullText: string = this.changeText;
  @State originText: string = this.changeText;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.originText,
    fontSize: 18
  });

  build() {
    Column() {
      TextArea({ text: 'minLines: ' + this.fullText })
        .fontSize(18)
        .width(300)
        .minLines(3)

      Blank(50)

      TextArea({ text: 'constraintSize: ' + this.fullText })
        .fontSize(18)
        .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
        .width(300)
        .height('auto')
        .constraintSize({

          minHeight: this.textAreaPadding * 2 +
            this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
        })

      Blank(50)

      Button($r('app.string.NormalQuestion_AddInput'))
        .onClick(() => {
          this.fullText += this.changeText;
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .padding({ top: 30 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/am4S71qARLWrFu1BhTQ6fQ/zh-cn_image_0000002565290233.gif?HW-CC-KV=V1&HW-CC-Date=20260402T023445Z&HW-CC-Expire=86400&HW-CC-Sign=6FAA208EFC5D418849D49CC91C774F809AFC5E59F1A0B270895A05B2C57411E5)
