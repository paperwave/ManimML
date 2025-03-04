from manim import *
from PIL import Image
import numpy as np

from manim_ml.neural_network.layers.convolutional_2d import Convolutional2DLayer
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer
from manim_ml.neural_network.layers.image import ImageLayer
from manim_ml.neural_network.layers.max_pooling_2d import MaxPooling2DLayer
from manim_ml.neural_network.neural_network import NeuralNetwork

# Make the specific scene
config.pixel_height = 1200
config.pixel_width = 1900
config.frame_height = 6.0
config.frame_width = 6.0

class CombinedScene(ThreeDScene):
    def construct(self):
        image = Image.open("../assets/mnist/digit.jpeg")
        numpy_image = np.asarray(image)
        # Make nn
        nn = NeuralNetwork([
                ImageLayer(numpy_image, height=1.5),
                Convolutional2DLayer(1, 8, filter_spacing=0.32),
                Convolutional2DLayer(3, 6, 3, filter_spacing=0.32),
                MaxPooling2DLayer(kernel_size=2),
                Convolutional2DLayer(5, 2, 2, filter_spacing=0.32),
            ],
            layer_spacing=0.25,
        )
        # Center the nn
        nn.move_to(ORIGIN)
        self.add(nn)
        self.wait(5)
        # Play animation
        forward_pass = nn.make_forward_pass_animation(
            corner_pulses=False, all_filters_at_once=False
        )
        print(forward_pass)
        print(forward_pass.animations)
        self.wait(1)
        self.play(forward_pass)

class SmallNetwork(ThreeDScene):
    def construct(self):
        image = Image.open("../assets/mnist/digit.jpeg")
        numpy_image = np.asarray(image)
        # Make nn
        nn = NeuralNetwork([
                ImageLayer(numpy_image, height=1.5),
                Convolutional2DLayer(1, 8, filter_spacing=0.32),
                MaxPooling2DLayer(kernel_size=2),
            ],
            layer_spacing=0.25,
        )
        # Center the nn
        nn.move_to(ORIGIN)
        self.add(nn)
        # Play animation
        forward_pass = nn.make_forward_pass_animation(
            corner_pulses=False, all_filters_at_once=False
        )
        self.wait(1)
        self.play(forward_pass)