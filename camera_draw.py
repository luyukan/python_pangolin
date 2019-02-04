import OpenGL.GL as gl
import pangolin

import numpy as np


pangolin.CreateWindowAndBind('window', 6540, 480)
gl.glEnable(gl.GL_DEPTH_TEST)