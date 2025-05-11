# PtraceIl2cppDumper
一个用于在安卓平台上通过主动调用对unity游戏进行dump的so模块。

# 如何使用
~~先在目标手游的/data/data/packageName/files目录下创建test.txt文件，test.txt文件中的**每一行**均为要进行dump的程序集名称如Assembly-CSharp.dll,**注意这里创建以及写入test.txt文件务必在手机设备的环境上进行，否则可能会出现bug**。在创建/data/data/packageName/files/test.txt文件并写入要进行dump的程序集名称后即可~~
通过任意ptrace注入器将该so模块注入至要dump的unity游戏进程中，主动调用dump将自动执行。**最好是在游戏的相应逻辑触发后再进行注入，因为如果需要的类还未加载就不会被dump**。可在logcat中使用Perfare进行过滤查看结果。如dump成功会在/data/data/packageName/files目录下生成test.cs以及test_method_info.txt文件。

~~目标unity手游的所有程序集名称均可在其apk包的assets\bin\Data\ScriptingAssemblies.json中找到。~~
推荐使用的ptrace注入器为[Android-Ptrace-Injector](https://github.com/reveny/Android-Ptrace-Injector)或[AndKittyInjector](https://github.com/MJx0/AndKittyInjector)。

## 新增ida.py脚本
使用ida加载libil2cpp.so后导入并执行ida.py脚本，再根据引导选择dump生成的test_method_info.txt文件即可重命名大部分函数。


# 如何构建
克隆本项目后，使用androidStudio打开，然后等待项目配置自动完成，之后在本项目目录下使用**gradlew :app:externalNativeBuildRelease**命令进行编译，编译完成后会在<项目目录>\app\build\intermediates\cmake\release\obj\arm64-v8a下生成libtest.so文件。



# 致谢
本项目基于[Zygisk-Il2CppDumper](https://github.com/Perfare/Zygisk-Il2CppDumper)