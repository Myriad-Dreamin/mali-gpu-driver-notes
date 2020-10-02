## KBase Device Main File

KBase Driver作为一个kernel module/driver，核心文件位于`drivers\gpu\arm\midgard\mali_kbase_core_linux.c`

## Module Initialization/Exit

#### kbase_driver_init

+ 创建名为`mali`的platform_device，注册kbase的platform_driver，定义在[`kbase_platform_driver`](#Bifrost%20KBase%20Platform%20Driver)中。

+ 获取预定义在`versatile_platform_config`中的io资源并注册到`mali` device上

+ 任何失败都会回收和删除已经注册的资源

#### kbase_driver_exit

回收`kbase_platform_driver`和platform_device资源。
