from manim import *
from PIL import Image

from manim_ml.neural_network.layers.convolutional_2d import Convolutional2DLayer
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer
from manim_ml.neural_network.layers.image import ImageLayer
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
        nn = NeuralNetwork(
            [
                ImageLayer(numpy_image, height=1.5),
                Convolutional2DLayer(1, 7, 7, 3, 3, filter_spacing=0.32),
                Convolutional2DLayer(3, 5, 5, 3, 3, filter_spacing=0.32),
                FeedForwardLayer(3),
            ],
            layer_spacing=0.25,
        )
        # Center the nn
        nn.move_to(ORIGIN)
        nn.scale(1.3)
        self.add(nn)
        """
        self.play(
            FadeIn(nn)
        )
        """
        # Play animation
        forward_pass = nn.make_forward_pass_animation(
            corner_pulses=False, all_filters_at_once=False, highlight_filters=True
        )
        self.wait(1)
        self.play(forward_pass)
