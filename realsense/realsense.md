# realsense 

## mac install 
1. 依赖于xcode(xcode-select) cmake libusb pkg-config https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_osx.md
2. 似乎只支持node 10 https://github.com/IntelRealSense/librealsense/tree/master/wrappers/nodejs
3. rso 格式的说明 http://wiki.ros.org/rosbag
4. bag 格式 http://wiki.ros.org/rqt_bag

## note 
- 2021/01/19 已经可以从bag里读取 通过node wrapper 操作了， 不过目前只能在node_modules里测试和看文档