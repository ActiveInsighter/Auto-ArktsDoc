# 粒子动画
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-particle-animation

[粒子动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation)是通过在限定区域内随机生成大量粒子的运动，进而组合成的动画效果，通过Particle组件来实现。动画的基本构成元素为单个粒子，这些粒子可以表现为圆点或图片等形式。开发者能够通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等多个维度上的动态变化做动画，以营造特定的氛围，例如模拟下雪场景时，飘舞的雪花实际上是由一个个雪花粒子的动画效果所构成。

粒子动画的简单实现如下所示。

```typescript
@Entry
@Component
struct ParticleExample {
  build() {
    Stack() {
      Text()
        .width(300).height(300).backgroundColor('rgb(240, 250, 255)')
      Particle({ particles: [
        {
          emitter: {
            particle: {
              type: ParticleType.POINT,
              config: {
                radius: 5
              },
              count: 100,
            },
          },
          color:{
            range:['rgb(39, 135, 217)','rgb(0, 74, 175)'],
          },
        },
      ]
      }).width(250).height(250)
    }.width('100%').height('100%').align(Alignment.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ntx2GR7KSX-RvRsUWDX6oQ/zh-cn_image_0000002572679987.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024226Z&HW-CC-Expire=86400&HW-CC-Sign=A7CB1E6E8BA48EB700FC540925F2C7CA3114D0E3F63738339EBC9096B85A9738)

## 实现粒子发射器

粒子发射器（Particle Emitter）主要定义粒子的初始属性（如类型和位置），控制粒子的生成速率，以及管理粒子的生命周期。可通过[emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation#emitter12)方法调整粒子发射器的位置、发射速率和发射窗口的大小，实现发射器位置的动态更新。

```typescript
@State emitterProperties: Array<EmitterProperty> = [
  {
    index: 0,
    emitRate: 100,
    position: { x: 60, y: 80 },
    size: { width: 200, height: 200 }
  }
]

Particle(...).width(300).height(300).emitter(this.emitterProperties)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/2YERP5WQSRehiHaYEr1CbQ/zh-cn_image_0000002541960080.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024226Z&HW-CC-Expire=86400&HW-CC-Sign=EFD3D3B1E799CCBA28CD90E44D2F68E6BDAA532604047CC6EA7302073162268F)

## 设置粒子颜色

可以通过[range](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation#particlecolorpropertyoptions)来确定粒子的初始颜色范围，而[distributionType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation#particlecolorpropertyoptions)则用于指定粒子初始颜色随机值的分布方式，具体可选择均匀分布或者高斯（正态）分布。

```typescript
color: {
  range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'],
  distributionType: DistributionType.GAUSSIAN
},
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/l6qmQojxRNWrJW1u27QcxQ/zh-cn_image_0000002572640025.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024226Z&HW-CC-Expire=86400&HW-CC-Sign=85B25973B92BEA380258B433C6B838966A1515CBE0FFD8E9E7A0942E30CEC111)

## 粒子的生命周期

粒子的生命周期（Lifecycle）是粒子从生成至消亡的整个过程，用于确定粒子的存活时间长度。粒子的生命周期可通过设置[EmitterParticleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation#emitterparticleoptions18)的lifetime和lifetimeRange属性来指定。

```typescript
emitter: {
  particle: {

    lifetime: 300,
    lifetimeRange: 100
  },
  emitRate: 10,
  position: [0, 0],
  shape: ParticleEmitterShape.RECTANGLE
},
color: {
  range: ['rgb(39, 135, 217)','rgb(0, 74, 175)'],
},
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/rgp04IU5Rb6ftlU3Zt-V8A/zh-cn_image_0000002542119718.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024226Z&HW-CC-Expire=86400&HW-CC-Sign=B81B3F5E281AEDF72260ECFE531CBDB0910DD9E2DC773B475FD57A51DF338662)

## 设置粒子扰动场

扰动场（Disturbance Field）是一种影响粒子运动的机制。通过在粒子所在的空间区域内施加特定的力，扰动场能够改变粒子的轨迹和行为，进而实现更为复杂和自然的动画效果。扰动场的配置可以通过[disturbanceFields](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation#disturbancefields12)方法来完成。

```typescript
Particle({ particles: [
  {
    emitter:
    color:
    scale: {
      range: [0.0, 0.0],
      updater: {
        type: ParticleUpdater.CURVE,
        config: [
          {
            from: 0.0,
            to: 0.5,
            startMillis: 0,
            endMillis: 3000,
            curve: Curve.EaseIn
          }
        ]
      }
    },
    acceleration: {
      speed: {
        range: [3, 9],
        updater: {
          type: ParticleUpdater.RANDOM,
          config: [1, 20]
        }
      },
      angle: {
        range: [90, 90]
      }
    }

  }
]
}).width(300).height(300).disturbanceFields([{
  strength: 10,
  shape: DisturbanceFieldShape.RECT,
  size: { width: 100, height: 100 },
  position: { x: 100, y: 100 },
  feather: 15,
  noiseScale: 10,
  noiseFrequency: 15,
  noiseAmplitude: 5
}])
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/9XepPYzGTnWjz3cPRX3Rrw/zh-cn_image_0000002572679989.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024226Z&HW-CC-Expire=86400&HW-CC-Sign=3A5CB9E59EE98E7AD27E24E0D0365C76AC094604B5D5395C9D3516F52D99C39C)
