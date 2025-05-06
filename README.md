**Network Latency Optimisation**

Delayed control signals and camera streams can critically undermine robotic operations in disaster response scenarios. When communication lags occur, the operator’s commands reach the robot with significant delay, resulting in inaccurate maneuvering and poor situational responsiveness. Similarly, outdated camera feeds impair the operator’s ability to accurately assess the environment, leading to misinterpretations of hazards and obstacles. The combined effect of these delays can inadvertently exacerbate collateral damage in an already volatile disaster zone and may also place victims at additional risk by delaying or misdirecting rescue efforts. Immediate steps to reduce network latency and implement predictive control algorithms are essential to mitigate these risks and enhance operational safety in high-stakes environments.

**Generalised Workflow**

– MJPEG latency is calculated using timestamps on each frame.
– HLS latency is estimated based on segment buffering.
– Tracks bandwidth usage of both in real-time.

**MODES**

**Single Protocol Streaming**

Observations: Optimal latency is measured at ~33ms, while the stream’s latency including normal jitters, shows periodic spikes to 42ms.
Analysis: Variations could be caused by the length of the video stream buffer, or docker container limitations. Further testing required to understand this with protocol/framerate switching included.

**Switched Protocol Streaming**

Observations: Optimal latency is measured at ~38ms. Prior to protocol switch, there is an increasing delay up to 49 ms. Post-detection and protocol-switch, mean latency is reduced to ~46 ms, an improvement of 6.1%.
Analysis: Protocol switch from MJPG to HLS shows a stable but reduced performance during periods of increasing network activity.
Reduction of frame rate rather than streaming protocol may be necessary to improve the operators visual experience by a substantial amount. Revised target was set at 20%, to ensure that the change was more visually obvious to the operator. This would set the delay at ~39 ms.
