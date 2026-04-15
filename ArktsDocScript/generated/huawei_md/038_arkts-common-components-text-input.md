# 文本输入 (TextInput/TextArea/Search)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)和[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)组件的API文档。

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

- 单行输入框。 ```typescript TextInput() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Nz-kGxvIQoar1ACQ8tLAfg/zh-cn_image_0000002540611444.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=7BF7A4D211C847D6FB2C25EC82057449B4E9946A0204AAE498F5C9AE9F456492)
- 多行输入框。 ```typescript TextArea() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/_WUO-7oyQSeFvetgUGf-JA/zh-cn_image_0000002571171439.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=2093B1DF6DC9F8AF0A565AA95F1696F7F94B112859E79E633269CAEDB45921CD)
- 多行输入框文字超出一行时会自动折行。 ```typescript TextArea({ text: $r('app.string.CreatTextInput_textContent') })  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/TswLmx44TEqBlL-IaGUasw/zh-cn_image_0000002540771096.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=9B716425540654872508E409CC883C8967E5279D3AD813573749197429172804)
- 搜索框。 ```typescript Search()  .searchButton($r('app.string.Creat_TextInput_Content')) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/7R_m8eoPRgOfQFsCdocHRQ/zh-cn_image_0000002571291395.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=DD2A331109FD0395CEC310F47E259002719FB33AEB5CCAB5030A14D3D45D7D77)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

### 基本输入模式（默认类型）

```typescript
TextInput()
  .type(InputType.Normal)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/q11R2WznRDGwnTWWJt-8qA/zh-cn_image_0000002540611446.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=6DF973EFA32588DD5B03EAA1C606C170F3A42040E2EF7D569C66FA66E1ADA8F9)

### 密码模式

包括Password密码输入模式、NUMBER_PASSWORD纯数字密码模式、NEW_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```typescript
TextInput()
  .type(InputType.Password)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/uO3NaZp3QMyJMDVx9SCbOw/zh-cn_image_0000002571171441.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=D5AD3278B4253E8768EB427B6F703E5CEAC95B687EFD82A685B1404F2D9783A3)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```typescript
TextInput()
  .type(InputType.Email)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Hyoc2rQFSxmO2CNWDTN0UA/zh-cn_image_0000002540771098.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=E81D2E0546881B02A99341A52B23B1F1FEA59BFBCE3056FB861720A5FD87BA7A)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```typescript
TextInput()
  .type(InputType.Number)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/EJ_kHuTiRUuZLj0A88qrCQ/zh-cn_image_0000002571291397.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=9626BF88BFFB9984BDD74E7E885B774A5A05BF98608BECD52A40A6A64F3701EA)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

```typescript
TextInput()
  .type(InputType.PhoneNumber)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/WLES8R_iQHmA7l7i1ald5w/zh-cn_image_0000002540611448.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=B67C7A17F6298EEC053C12AB5E8669CCE467400986B6F0B08522FF0F131DAB90)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```typescript
TextInput()
  .type(InputType.NUMBER_DECIMAL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/gK1orhyLRSGL-oErZlrEmg/zh-cn_image_0000002571171443.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=E8EF66374FA4313B9C50C868E55E2D5863171C9F43B37EEA24F5EF2235DB786E)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```typescript
TextInput()
  .type(InputType.URL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/0UDSkrrGS_qLDlbspY0cDQ/zh-cn_image_0000002540771100.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=E9DAC93564ABB41596657BA4D141EEF9E3BBF931F83E85CD64B5F62E09E83672)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```typescript
TextArea()
  .style(TextContentStyle.DEFAULT)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/l7w4-M7CTWCZrQt_MURBmw/zh-cn_image_0000002571291399.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=A60EB0CE72CFCAD7619113396FD589E3111515E173B2C3CED981CF979E2D870A)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```typescript
TextArea()
  .style(TextContentStyle.INLINE)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/v6FIg5ZbSPGfA3SiIzBmHQ/zh-cn_image_0000002540611450.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=72B5DEC2A843EAB0054A1011C0922C6BAE4A1366E39CED4B49ABAFB1147C74A9)

## 自定义样式

- 设置无输入时的提示文本。 ```typescript TextInput({ placeholder: $r('app.string.i_am_placeholder') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/RR0GGYQyT328p-tQuRqTqg/zh-cn_image_0000002571171445.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=88FFFBF105C27D33B3536F4E2BBD865E8521AEBFF7D056B37D02A441F6F213CA)
- 设置输入框当前的文本内容。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/1d6glu-NTcahDeHM6Hz3sw/zh-cn_image_0000002540771102.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=F791C87BFD14DAD6F9111187C4B47473F8D890A76A28E7A789C08D93A51E8C8F)
- 添加backgroundColor改变输入框的背景颜色。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') })  .backgroundColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/ISv5i6fnQYm_sZ7XJzSWNA/zh-cn_image_0000002571291401.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=784E081F76F3FF843FA5B318242BB09DF69565F713E8F560CDCEDF00E9597831) 更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/SUyOfL6wRVCToB2WT8jMDg/zh-cn_image_0000002540611452.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=AFBD6F78A5503FBA13F6AFA901818BDBAF0451013E99C42DEFF3D5A9B8F86A02)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、搜索的菜单。

TextInput:

```typescript
TextInput({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UrbrV-q7SNiLVEJSwdznNw/zh-cn_image_0000002571171447.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=2F938B7B63E37B6B2A0FB1B51A6DEC73CF55EA65B6B40D4D76A69CDA0C30B8B1)

TextArea:

```typescript
TextArea({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/pTHc_-CGSVmthlJPUrUXmw/zh-cn_image_0000002540771104.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=E293357E74AEDB639A6FD13AC9934EB620B00CF9873324092D5EDE45DB9025B9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ZFYvOfF4R2yw168j6XVxWg/zh-cn_image_0000002571291403.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=9FB984C6183DA9B07F4B59F978050A5C35E405CA2F34AA9027B4E879328CF353)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/avWF0TZZQMOMlq9-tKYqug/zh-cn_image_0000002540611454.png?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=2F47950A4B62426A6CC894346217D2246DC462BF8EBE354D54949F04ED3A0BEE)

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

- 设置省略属性。 输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。 ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。 ```typescript TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })  .textOverflow(TextOverflow.Ellipsis)  .ellipsisMode(EllipsisMode.END)  .style(TextInputStyle.Inline)  .fontSize(30)  .margin(30) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/w-RodM1sQD2JB2bHbEZAxw/zh-cn_image_0000002571171449.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=1128A6EE1E5A670851D5DD8FABEDBEADF1D5DA58E34DAF9BE65CC8032C41773B)
- 设置文本描边属性。 从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。 ```typescript TextInput({ text: 'Text with stroke' })  .width('100%')  .height(60)  .borderWidth(1)  .fontSize(40)  .strokeWidth(LengthMetrics.px(3.0))  .strokeColor(Color.Red) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/883_pi9oSmml3Tx_HsvcYg/zh-cn_image_0000002540771108.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=5E01E94C9562D9745BA671D17FB203F98C71AB83435C7E9680A82C207754FFDD)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```typescript
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/H67tkWvuQ5iMPG_jZldz5w/zh-cn_image_0000002571291405.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=ECB68040C6DB9C9003ABBF0F3950822A08AFC5DB93926D0BA75F8AB83BDED306)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/RdSsugvRTJabKoHius89lA/zh-cn_image_0000002540611456.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=B615ADBDC7D8B2445DBFF7B7A72CCA38A46E201D6108AD0FF17DFA279B9B6AC8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/OZeIDBycQM2eofXDz_4Ibg/zh-cn_image_0000002571171451.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=0527FA15D40B73A5497C3A91AF3A66171B29D48FD174FD503ED3D82B167BC28E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/F--0ZLSgTNqMeTabKhizNA/zh-cn_image_0000002540771110.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024820Z&HW-CC-Expire=86400&HW-CC-Sign=35F7ED9D10093076A65D3E29B67BA9FA175DF748236DAF0EE17A28076549DFF8)
