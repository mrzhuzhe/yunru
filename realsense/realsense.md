# realsense 

## mac install 
1. 依赖于xcode(xcode-select) cmake libusb pkg-config https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_osx.md
2. 似乎只支持node 10 https://github.com/IntelRealSense/librealsense/tree/master/wrappers/nodejs
3. rso 格式的说明 http://wiki.ros.org/rosbag
4. bag 格式 http://wiki.ros.org/rqt_bag
5. cmake .. -DBUILD_NODEJS_BINDINGS=1 -DBUILD_EXAMPLES=true -DBUILD_WITH_OPENMP=false -DHWM_OVER_XU=false
6. brew install homebrew/versions/glfw3 这个失效了 没用
7. 还是得建一个release文件夹在build下 把编译结果的dylib放进去 才能正确编译addon
8. 似乎是这个的问题 https://www.codenong.com/33991581/

## note 
- 2021/01/19 已经可以从bag里读取 通过node wrapper 操作了， 不过目前只能在node_modules里测试和看文档