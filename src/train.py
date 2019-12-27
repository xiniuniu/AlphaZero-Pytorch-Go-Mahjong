"""General-purpose training script of AlphaZero for different games
This script works for various games (with option '--game': e.g., go, mahjong) and
different networks (with option '--model': e.g., resnet, vgg).
You need to specify the experiment name ('--name'), and game ('--game').

<todo>
It first creates model, dataset, and visualizer given the option.
It then does standard network training. During the training, it also visualize/save the images, print/save the loss plot, and save models.
The script supports continue/resume training. Use '--continue_train' to resume your previous training.
Example:
    Train a model for the game of Go:
        python train.py --game go --name alphazero_go --model resnet

See options/base_options.py and options/train_options.py for more training options.
"""

from options.train_options import TrainOptions
from game import create_game
from model import create_model
from coach import Coacher

if __name__ == '__main__':
    opt = TrainOptions().parse()   # get training options
    game = create_game(opt)
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    total_iters = 0                # the total number of training iterations
    coacher = Coacher(game, model, opt)

    coacher.learn()

