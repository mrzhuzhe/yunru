const rs2 = require('node-librealsense');



const colorizer = new rs2.Colorizer();  // This will make depth image pretty
const pipeline = new rs2.Pipeline();  // Main work pipeline of RealSense camera

const cfg = new rs2.Config()
cfg.enableDeviceFromFile("depth_under_water.bag")

pipeline.start(cfg);  // Start camera

/*
const frameset = pipeline.waitForFrames();  // Get a set of frames
const depth = frameset.depthFrame;  // Get depth data
const depthRGB = colorizer.colorize(depth);  // Make depth image pretty
const color = frameset.colorFrame;  // Get RGB image
*/

let device = pipe.getActiveProfile().getDevice();
let playback = rs2.PlaybackDevice.from(device);

for (let i = 0; i < 10; i++) {
    let frames = ppipelineipe.waitForFrames();
}

pipe.stop();
rs2.cleanup();